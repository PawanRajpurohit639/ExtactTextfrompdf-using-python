from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import csv
import os
from translate import Translator

# set pdf file path
try:
    pdf_file = "kishanraj.pdf"
    # store all pages of pdf valarible

    pages = convert_from_path(pdf_file, 500)
    image_counter = 1

    for page in pages:
        # pdf will store one by one page into filename variable as image format
        filename = "pages_" + str(image_counter) + ".jpg"

        # save the image of the page in system

        page.save(filename, 'JPEG')
        image_counter = image_counter + 1

    filelimit = image_counter - 1
    outfile = "output.txt"
    f = open(outfile, "w+",encoding='utf8')

    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'

    for i in range(1, filelimit + 1):
        filename = "pages_" + str(i) + ".jpg"
        text = pytesseract.image_to_string(Image.open(filename), lang='eng', config=tessdata_dir_config)
        #text = pytesseract.image_to_osd(Image.open(filename), lang='ara', config=tessdata_dir_config)
        print(text)
        text = text.replace('-\n', '')
        f.write(text)
    
    #translator= Translator(from_lang="ara",to_lang="en")
    #translation = translator.translate(text)
    #translation=translation.replace('\\r','r')
    #print(translation)
    #f.write(text)
    f.close()
   # csvf.close()
except Exception as ex:
    print("Exception: ", ex)

    # fileData = csv.reader(f, delimiter=';')
    # fileData = f.read()
    # CSVFILE="Example.csv"
    # csvf = open(CSVFILE, "w")
    # csvf.writelines(text)
    # out_csv = csv.writer(csvf)
    # file3 = out_csv.writerows(fileData)
    # print(file3)
