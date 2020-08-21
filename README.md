# PDF Reskeletonize
Proof of concept for re-skeletonizing PDFs.

## Requirements
+ PyPDF2 with [PR #240](https://github.com/mstamy2/PyPDF2/pull/240) applied

## Usage
`python reskeletonize.py`

+ `outline.json` specifies a list of template objects in the outline PDF, their x/y coordinates, and their width & height.
+ `submission.json` specifies a list of objects from the template that are present in the submission PDF, and their x/y coordinates.

Coordinates are all in inches, and the origin is at the bottom left of a page. 
PDF page numbers are 1-indexed (page 1 is the first page of a PDF).

## Examples
Examples are generated with PyFPDF. PyFPDF sets the origin at the top left of a page.

**Outline**

![Image of Outline](https://raw.githubusercontent.com/whsu00/pdf-reskeletonize/master/examples/thumbnails/outline.jpg)
```
[
    {
        "id": "box1",
        "page": 1,
        "x": 0.5,
        "y": 7.5,
        "w": 7.5,
        "h": 3
    },
    {
        "id": "box2",
        "page": 1,
        "x": 0.5,
        "y": 4.5,
        "w": 7.5,
        "h": 3
    },
    {
        "id": "box3",
        "page": 1,
        "x": 0.5,
        "y": 1.5,
        "w": 7.5,
        "h": 3
    }
]
```

**Submission**

![Image of Submission](https://raw.githubusercontent.com/whsu00/pdf-reskeletonize/master/examples/thumbnails/submission.jpg)
```
[
    {
        "id": "box3",
        "page": 1,
        "x": 0.5,
        "y": 7.5
    },
    {
        "id": "box2",
        "page": 1,
        "x": 0.5,
        "y": 4.5
    }
]
```

**Output (Reskeletonized)**

![Image of Output (Reskeletonized)](https://raw.githubusercontent.com/whsu00/pdf-reskeletonize/master/examples/thumbnails/output.jpg)


