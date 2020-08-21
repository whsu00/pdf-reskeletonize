import fpdf
import json

def get_color(i, solid=0):
    rgb = [solid for _ in range(3)]
    rgb[i % 3] = 255
    return rgb

def draw_block(pdf, position, color, text):
    x, y = position
    pdf.set_draw_color(*color)
    pdf.set_fill_color(*color)
    pdf.rect(x, y, 7.5, 3, "DF")
    pdf.text(x + 0.05, y + 0.2, text)

def generate_pdf(blocks, file, submission=True):
    pdf = fpdf.FPDF(orientation='P', unit='in', format='letter')
    pdf.set_margins(left=0.5, top=0.5)
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0)
    pdf.add_page()
    page = 1
    page_width, page_height = 8.5, 11
    x, y = 0.5, 0.5
    objs = []
    for i in blocks:
        if y + 3 > page_height:
            pdf.add_page()
            page += 1
            y = 0.5
        color = get_color(i) if submission else get_color(i, 192)
        text = "Box {}".format(i+1)
        if submission:
            text += ": Submission Data"
        draw_block(pdf, (x, y), color, text)
        objs.append({
            "id": "box{}".format(i+1),
            "page": page,
            "x": x,
            "y": page_height - y - 3
        })
        if not submission:
            objs[-1]["w"] = 7.5
            objs[-1]["h"] = 3
        y += 3
    pdf.output(file + ".pdf")

    with open(file + ".json", "w") as f:
        json.dump(objs, f)

if __name__ == '__main__':
    generate_pdf(range(6), "outline", submission=False)
    generate_pdf(range(6), "submission1", submission=True)
    generate_pdf([0, 2, 3, 5], "submission2", submission=True)
    generate_pdf([4, 1, 0], "submission3", submission=True)

