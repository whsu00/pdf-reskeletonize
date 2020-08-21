import click
import json
from PyPDF2 import PdfFileWriter, PdfFileReader

UNITS_PER_INCH = 72
PAGE_SIZE = (8.5, 11)

@click.command()
@click.option('--outline-pdf', type=click.File(mode='rb'), default="outline.pdf", prompt=True, help="PDF file of the outline")
@click.option('--outline-json', type=click.File(), default="outline.json", prompt=True, help="JSON file describing components of the outline")
@click.option('--submission-pdf', type=click.File(mode='rb'), default="submission.pdf", prompt=True, help="PDF file of the submission")
@click.option('--submission-json', type=click.File(), default="submission.json", prompt=True, help="JSON file describing components of the submission")
@click.option('--output-pdf', type=click.File(mode='wb'), default="output.pdf", prompt=True, help="Output path of the reskeletonized PDF file")
def main(outline_pdf, outline_json, submission_pdf, submission_json, output_pdf):
    """Proof of concept for reskeletonizing PDFs."""
    outline_data = json.load(outline_json)
    submission_data = json.load(submission_json)
    outline = PdfFileReader(outline_pdf)
    submission = PdfFileReader(submission_pdf)
    outline_pages = [outline.getPage(i) for i in range(outline.getNumPages())]
    submission_pages = [submission.getPage(i) for i in range(submission.getNumPages())]
    for page in submission_pages:
        page.scaleTo(PAGE_SIZE[0] * UNITS_PER_INCH, PAGE_SIZE[1] * UNITS_PER_INCH)
    for outline_obj in outline_data:
        for submission_obj in submission_data:
            if outline_obj["id"] == submission_obj["id"]:
                w, h = outline_obj["w"], outline_obj["h"]
                page = submission_pages[submission_obj["page"] - 1]
                page.trimBox.lowerLeft = (submission_obj["x"] * UNITS_PER_INCH, submission_obj["y"] * UNITS_PER_INCH)
                page.trimBox.upperRight = ((submission_obj["x"] + w) * UNITS_PER_INCH, (submission_obj["y"] + h) * UNITS_PER_INCH)
                outline_pages[outline_obj["page"] - 1].mergeTranslatedPage(page, (outline_obj["x"] - submission_obj["x"]) * UNITS_PER_INCH, (outline_obj["y"] - submission_obj["y"]) * UNITS_PER_INCH)
    output = PdfFileWriter()
    for page in outline_pages:
        output.addPage(page)
    output.write(output_pdf)

if __name__ == '__main__':
    main()
