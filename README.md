# PDF Reskeletonize
Proof of concept for re-skeletonizing PDFs.

## Requirements
+ PyPDF2 with (PR #240)[https://github.com/mstamy2/PyPDF2/pull/240] applied

## Usage
`python reskeletonize.py outline.pdf outline.json submission.pdf submission.json output.pdf`

`outline.json` specifies a list of template objects in the outline PDF, their x/y coordinates, and their width & height.

`submission.json` specifies a list of objects from the template that are present in the submission PDF, and their x/y coordinates.

Coordinates are all in inches, and the origin is at the bottom left of a page. 
PDF pages are 1-indexed (page 1 is the first page of a PDF).

## Examples
Examples are generated with PyFPDF. PyFPDF sets the origin at the top left of a page.

