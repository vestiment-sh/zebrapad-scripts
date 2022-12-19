# importing required modules # importing required modules 
import PyPDF2 
import os

path = 'Address to folder with PDF(s)'
os.chdir(path)    

for pdf in os.listdir(path):
    pdfFileObj = open(pdf, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    pageObj = pdfReader.getPage(0) 
    text = pageObj.extractText() 
    pdfFileObj.close() 
    outfile = open("Address to folder you want to save TXT files" + f'{txt}'+".txt",'w', encoding= 'utf-8')
    outfile.writelines(text)
