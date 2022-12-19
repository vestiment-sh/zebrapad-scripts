import nltk
from nltk.tokenize import sent_tokenize
import os

nltk.download('punkt')
txt_num = 1
path = 'E:/steven/kellylessons/Relationship Astrology Intro Course/txt'
os.chdir(path)

for txt in os.listdir(path):
    with open(txt, 'r') as file:
        data = file.read().replace('\n', '')
    result = str(sent_tokenize(data))
    token_lst = result
    outfile = open(r"E:/steven/kellylessons/Relationship Astrology Intro Course/token/test_"+ str(txt_num)+ ".txt",'w')
    outfile.writelines(token_lst)
    txt_num += 1