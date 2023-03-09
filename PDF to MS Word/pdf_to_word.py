# Install pdf2docx package
# By making use of pdf2docx package to convert a pdf document into MS Word document
# By Samuel Ko

# Install pdf2docx package
from pdf2docx import parse
from typing import Tuple
import traceback as tb
import sys

def convert_pdf2docs(in_file : str, pages : Tuple = None):
    try:
        input_file = "pdf/"+in_file
        out_file = ""
        if pages:
            pages = [int(i) for i in list(pages) if i.isnumeric()]
        result = parse(pdf_file=input_file, docx_files=out_file, pages=pages)
        
        summary = {
                    "File" : input_file, "Pages" : str(pages), \
                    "Output File" : out_file
                }
        
        print("Converstion Processing....")
        print("\n".join("{}:{}".format(i,j) for i,j in summary.items()))
        print("Finished!")
        return result
    except:
        tb.print_exc()

if __name__ == "__main__":
    getPDF = input("Please enter your pdf file to convert : ")
    convert_pdf2docs(getPDF)