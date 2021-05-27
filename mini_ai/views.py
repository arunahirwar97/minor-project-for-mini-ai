from django.shortcuts import render
from django.shortcuts import render, redirect 
from .models import ocr_model   
from .forms import *
from pytube import YouTube
from PIL import Image
import pytesseract 
import glob
import getpass
import moviepy.editor as mp
import shutil
# Create your views here.
def index(request):
    alert_message = False
    if request.method == 'POST': 
        
        submitted_form = ocr_forms(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()   
            pytesseract.pytesseract.tesseract_cmd = r'.\\tesseract\\tesseract.exe'
            path = glob.glob('.\\media\\images\\*')
            img = path[0]
            tt = pytesseract.image_to_string(img)
            z = print(tt)
            print(len(tt))
            shutil.rmtree("./media/images")
            alert_message = {
                'status': True,
                'message': 'Successfully saved the image'
            }
            return render(request, 'index.html',{'number':tt})

        else:
            print("<<<<<<<<<<<<<<1111111111111111111111111111111111111111111<<<>>>>>>>>>>")
    
            alert_message = {
                'status': False,
                'message': 'Form data is invalid. Please check if your image / title is repeated'
            }
    

    return render(request, 'index.html')



def mp4_video(request):
    if request.method == 'POST':
        url = request.POST.get('url',None)
        print(url)
        username = getpass.getuser()
        print(username)
        title = YouTube(url).title
        z = YouTube(url).streams.first().download("C:/Users/{}/Downloads".format(username))
        print(z)
        return render(request,'youtubetomp4.html',{"title":title})
        
    return render(request,'youtubetomp4.html')
    

def mp3_video(request):
    
    if request.method == 'POST':
        url = request.POST.get('url',None)
        print(url)
        username = getpass.getuser()
        aa = YouTube(url).streams.first().download("C:/Users/{}/AppData/Local/Temp/".format(username))
        title = YouTube(url).title
        print(aa)
        print(title)
        VIDEO_FILE = "C:/Users/{}/AppData/Local/Temp/".format(username)+title+".mp4" # Video File Location
        OUTPUT_AUDIO_FILE = "C:/Users/{}/Downloads/".format(username)+title+".mp3"  # Audio File Location Where are you store audio file 
        v_c = mp.VideoFileClip(VIDEO_FILE)
        v_c.audio.write_audiofile(OUTPUT_AUDIO_FILE)
        return render(request,'youtubevideomp3.html',{'title':title})

    return render(request,'youtubevideomp3.html')




