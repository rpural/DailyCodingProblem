#! /usr/bin/env python3

from pypdf3 import PdfFileReader

def extract_information(pdf_path):
    with open( pdf_path, 'rb' ) as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}:

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


if __name__ == '__main__':
    import sys
    path = sys.argv[1]
    extract_information(path)
