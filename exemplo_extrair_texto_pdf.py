# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import  PDFDocument,PDFNoOutlines
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal,LTPage,LTTextBox,\
            LTTextLine,LTChar,LTAnno,LTImage,LTFigure
            
def get_toc(pdf_doc, pdf_pwd=''):
    """ Return the table of contents (toc), if any, for this pdf file"""
    
    return with_pdf(pdf_doc, pdf_pwd, __parser_toc)
    

def get_pages(pdf_file,pdf_pwd='',images_folder='/tmp'):
    """Process each of the pages in this pdf files and print the entire text
    to stdout"""
    print('\n\n'.join(with_pdf(pdf_file, __parser_pages, \
                               *tuple([images_folder,pdf_pwd]))))

    #(1_versao)with_pdf(pdf_doc, pdf_pwd, __parse_pages)    
    

def __parser_pages(pdf_file,images_folder,pdf_pwd=''):
    """with an open PDFDocument object, get the pages and parse each one
    [this is a highter-order function to be parsed to with_pdf()] """
    
    rscrmgr = PDFResourceManager()
     
    laparams = LAParams()
     
    device = PDFPageAggregator(rscrmgr,laparams=laparams)
     
    interpreter= PDFPageInterpreter(rscrmgr, device)
    
    #a list of strings, each representing text collected from each page of 
    #the doc 
    text_content = [] 
    
    for i, page in enumerate(PDFPage.get_pages(pdf_file,password=pdf_pwd)):
        
        interpreter.process_page(page)
    
        #receive the LTPage object for this page

        layout =  device.get_result()
 
        #layout is a LTPage object which may contain child objects like
        #LTTextBox, LTFigure, LTImage, etc.
        text_content.append(parse_lt_objs(layout,(i+1),images_folder))
    
    return text_content
         

def parse_lt_objs(lt_objs, page_number, images_folder,text=[]):
    """Itarate through the lista of LT* objects and capture the text or image
    data contained in each """
    text_content = []
    
    for lt_obj in lt_objs:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            #text
            text_content.append(lt_obj.get_text())
        elif isinstance(lt_obj, LTImage):
            #an image, so save it to the designed folder, and note it's place
            #in the text saved_file = save_image(lt_obj, page_number, 
            #images_folder)
            if saved_file:
                #use html style <img/> tag  to mark the position of the image
                #within the text 
                text_content.append('<img src="'+ os.path.join(images_folder, \
                                                               saved_file) + \
                                                                '"/>')
            else:
                print("Error saving image on page", page_number, \
                                                      lt_obj.__repr__,\
                                                      file=sys.stderr)
        elif isinstance(lt_obj,LTFigure):
            #LTFigure object are containers for other LT* objects, so 
            #recurse through the children 
            text_content.append(parse_lt_objs(lt_obj.objs,page_number,\
                                                  images_folder,\
                                                  text_content))
    return '\n'.join(text_content)

def __parser_toc(doc):
    """With an open PDFDocument object, get the table of contents (toc) data
    [this is a highter-order function to be passed to with_pdf()] """
    
    toc = []
    try:
        outlines = doc.get_outlines()
        for (level, title, dest, a, se) in outlines:
            toc.append((level,title))
    except PDFNoOutlines:
        pass
    return toc

def with_pdf(pdf_doc, fn, *args):
    """Open the pdf document, and apply the function, returning the results"""
    
    result = None
    
    try:
        #open the pdf file
        fp = open(pdf_doc, 'rb')
        
        #apply the function and return the result
        result = fn(fp,*args)
            
        #close file
        fp.close()
        
    except IOError:
        #the file doesn't exist or similar problem
        pass
    return result

def executar(arq = r'C:\Users\\luiscar\\Documents\\livros\\programacao\\p_teste\\beginning-django-e-commerce.pdf'):
    
    print(get_toc(arq))
    
if __name__ == '__main__':
    #executar()
    get_pages(r'C:\projetos\sefip.pdf','')
