# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:15:46 2018

@author: luiscar
"""
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal,LTTextBox,LTTextLine

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import  PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice





def _process_layout(self, layout):
        """Process an LTPage layout and return a list of elements."""
        # Here we just group text into paragraphs
        elements = []
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                elements.append(Paragraph(lt_obj.get_text().strip()))
            elif isinstance(lt_obj, LTFigure):
                # Recursive...
                elements.extend(self._process_layout(lt_obj))
        return elements 


def extractTextWithFullLayout(analyzed_data):
    """
    Extraction of text from each page with layout support.
    Sample output object: (same as extractTextWithSimpleLayout)
    [
        [   # New Page
            {   # New Text Group
                "text": ["Extracted Text Line 1", "2nd line here"],
                "type": "text",
                "layout": { # This is the box that bounds the text group
                    'x0': group.x0,
                    'x1': group.x1,
                    'y0': group.y0,
                    'y1': group.y1
                }
            }
        ]
    ]    
    """

    data = []
    for page in analyzed_data:
        if not page:
            continue

        data.append([])
        for lt_obj in page:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                data[-1].append({
                        'type': 'text',                         # Might support more types (e.g. figures) in the future.
                        'text': lt_obj.get_text().split("\n"),
                        'layout': {
                            'x0': lt_obj.x0,
                            'x1': lt_obj.x1,
                            'y0': lt_obj.y0,
                            'y1': lt_obj.y1
                        }
                    })

    return data 

if __name__ == "__main__":
    
    
    document = open('sefip.pdf','rb')
    rscrmgr = PDFResourceManager()
    laparams = LAParams()
    
    device = PDFPageAggregator(rscrmgr,laparams = laparams)
    interpreter = PDFPageInterpreter(rscrmgr,device)
    pages = PDFPage.get_pages(document)
    extractTextWithFullLayout(pages)
    exit(1)
    #para cada PDFPage
    for page in PDFPage.get_pages(document):
        interpreter.process_page(page)
        #obtem o LTPage
        layout = device.get_result()
        extractTextWithFullLayout(layout)
        exit(1)