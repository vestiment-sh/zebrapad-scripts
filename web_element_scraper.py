import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
global txt_num

txt_num = 1
df = pd.read_csv(r'PATH to CSV file')

options = Options()
options.binary_location = r'PATH to browser.exe'
driver = webdriver.Firefox(executable_path=r'PATH to geckodriver.exe (exclusively for Firefox)', options=options)

for row in df['column name'].values: 
    driver.get(row)
    element = driver.find_element_by_class_name(" distinct class name")
    outfile = open("PATH to folder you want to save text/file"+str(txt_num)+".txt",'w', encoding= 'utf-8')
    outfile.writelines(element.text)
    txt_num += 1