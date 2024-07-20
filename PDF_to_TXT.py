from ironpdf import *
import os
import base64
from PIL import Image 
from pytesseract import pytesseract 
# from openai import OpenAI

# input PDF path
# pdfPath = r"pythonai\T2.pdf" 

# will make gptstrats/pdfName/pdfName.txt
# def pdf_to_txt(pdfPath, outDir = ""):
#     pdfName = os.path.basename(pdfPath).removesuffix(".pdf")
#     newDirName = os.path.join(outDir, pdfName)   
#     if not os.path.exists(newDirName):
#         os.mkdir(newDirName)
#     else:
#         files = os.listdir(newDirName)
#         for file in files:
#             file_path = os.path.join(newDirName, file)
#             os.remove(file_path)
#     financesText = open(os.path.join(newDirName, pdfName + ".txt"), "a")


def pdf_to_txt(pdfPath, outDir = ""):
    # VARIABLES
    pdf = PdfDocument.FromFile(pdfPath) # type: ignore #PDF Object
    pdfName = os.path.basename(pdfPath).removesuffix(".pdf")
    newDirName = os.path.join(outDir, pdfName)   

    # path where tesseract executable was installed https://github.com/UB-Mannheim/tesseract/wiki
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # creating a new directory to store the images, or clearing existing directory
    if not os.path.exists(newDirName):
        os.mkdir(newDirName)
    else:
        files = os.listdir(newDirName)
        for file in files:
            file_path = os.path.join(newDirName, file)
            os.remove(file_path)
    
    # # CONVERTS PDF TO IMAGE
    pdf.RasterizeToImageFiles(newDirName+"\*.png")

    # READS TEXT, WRITING TO TXT
    # Providing the tesseract executable 
    # location to pytesseract library 
    pytesseract.tesseract_cmd = path_to_tesseract 

    # output txt file
    financesText = open(os.path.join(newDirName, pdfName + ".txt"), "w")
    
    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    files = os.listdir(newDirName)
    for i in range(1, len(files)):
        img = str(i)+".png"
        img_path = os.path.join(newDirName, img)
        text = pytesseract.image_to_string(img_path) 
        financesText.write("\n"+img + "\n")
        financesText.write(text[:-1])
        os.remove(img_path)

    financesText.close()



