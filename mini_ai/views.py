from django.shortcuts import render
import numpy as np
from PIL import Image
# import cv2
import matplotlib.pyplot as plt
import pytesseract 


# Create your views here.
def index(request):
    pytesseract.pytesseract.tesseract_cmd = r'G:\tesseract\tesseract.exe'

    img = Image.open("H:/project/IMG_20201224_220643.jpg")
    plt.figure(figsize = (20,10))
    plt.imshow(img)

    tt = pytesseract.image_to_string(img)
    z = print(tt)

    return render(request,'index.html',{'number': tt})




# from PIL import Image

# im = Image.open('Foto.jpg')
# im.save('Foto.png')



# from PIL import Image

# image1 = Image.open(r'path where the image is stored\file name.png')
# im1 = image1.convert('RGB')
# im1.save(r'path where the pdf will be stored\new file name.pdf')



# Python program to create
# a pdf file


# from fpdf import FPDF


# # save FPDF() class into a
# # variable pdf
# pdf = FPDF()

# # Add a page
# pdf.add_page()

# # set style and size of font
# # that you want in the pdf
# pdf.set_font("Arial", size = 15)

# # create a cell
# pdf.cell(200, 10, txt = "GeeksforGeeks",
# 		ln = 1, align = 'C')

# # add another cell
# pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
# 		ln = 2, align = 'C')

# # save the pdf with name .pdf
# pdf.output("GFG.pdf")






        # <div class="Neon Neon-theme-dragdropbox">
        # <input style="z-index: 999; opacity: 0; width: 320px; height: 200px; position: absolute; right: 0px; left: 0px; margin-right: auto; margin-left: auto;" name="files[]" id="filer_input2" multiple="multiple" type="file">
        # <div class="Neon-input-dragDrop"><div class="Neon-input-inner"><div class="Neon-input-icon"><i class="fa fa-file-image-o"></i></div><div class="Neon-input-text"><h3>Drag&amp;Drop files here</h3> <span style="display:inline-block; margin: 15px 0">or</span></div><a class="Neon-input-choose-btn blue">Browse Files</a></div></div>
        # </div>


#                 .Neon {
#     font-family: sans-serif;
#     font-size: 14px;
#     color: #494949;
#     position: relative;
    

# }
# .Neon * {
#     -webkit-box-sizing: border-box;
#     -moz-box-sizing: border-box;
#     box-sizing: border-box;
# }
# .Neon-input-dragDrop {
#     display: block;
#     width: 343px;
#     margin: 0 auto 25px auto;
#     padding: 25px;
#     color: #8d9499;
#     color: #97A1A8;
#     background: #fff;
#     border: 2px dashed #C8CBCE;
#     text-align: center;
#     -webkit-transition: box-shadow 0.3s, border-color 0.3s;
#     -moz-transition: box-shadow 0.3s, border-color 0.3s;
#     transition: box-shadow 0.3s, border-color 0.3s;
# }
# .Neon-input-dragDrop .Neon-input-icon {
#     font-size: 48px;
#     margin-top: -10px;
#     -webkit-transition: all 0.3s ease;
#     -moz-transition: all 0.3s ease;
#     transition: all 0.3s ease;
# }
# .Neon-input-text h3 {
#     margin: 0;
#     font-size: 18px;
# }
# .Neon-input-text span {
#     font-size: 12px;
# }
# .Neon-input-choose-btn.blue {
#     color: #008BFF;
#     border: 1px solid #008BFF;
# }
# .Neon-input-choose-btn {
#     display: inline-block;
#     padding: 8px 14px;
#     outline: none;
#     cursor: pointer;
#     text-decoration: none;
#     text-align: center;
#     white-space: nowrap;
#     font-size: 12px;
#     font-weight: bold;
#     color: #8d9496;
#     border-radius: 3px;
#     border: 1px solid #c6c6c6;
#     vertical-align: middle;
#     background-color: #fff;
#     box-shadow: 0px 1px 5px rgba(0,0,0,0.05);
#     -webkit-transition: all 0.2s;
#     -moz-transition: all 0.2s;
#     transition: all 0.2s;
# }