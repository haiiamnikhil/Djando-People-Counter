from django.shortcuts import render
import cv2 as cv
import pandas as pd
from PIL import Image
from django.http import StreamingHttpResponse
from .Run import run

def index_view(request):
    return render(request,'home.html')


# def extract_frames():
#     cam = cv.VideoCapture(0)
#     __ret__,__frames__ = cam.read()
#     return __frames__


def get_frames():
    cam = cv.VideoCapture(0)
    __ret__,__frames__ = cam.read()
    if __frames__ is not None:
        count = run(__frames__)
        ret,out = cv.imencode('.jpg',count)
        return out.tobytes()
    else:
        pass


def video_streaming(extractframes):
    while True:
        frame = get_frames()
        yield(b'--frame\r\n' b'Content-Type:image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')
        

def video_streaming_view(request):
    return StreamingHttpResponse(video_streaming(get_frames()),content_type='multipart/x-mixed-replace; boundary=frame')