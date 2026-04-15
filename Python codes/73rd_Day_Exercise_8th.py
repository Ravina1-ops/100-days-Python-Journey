'''
Exercise 8: PDF Merger
Write a program to manipulate pdf files using pyPDF2. 
Your programs should be able to merge multiple pdf files into a single pdf. 
You are welcome to add more functionalities.

pypdf is a free and open-source pure-python PDF library capable of splitting, 
merging, cropping, and transforming the pages of PDF files.
'''
# Note: You will need to pip install pypdf

#  - Exercise 8 Solution
# from pypdf import PdfWriter
# import os

# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith(".pdf")]

# for pdf in files:
    # merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()