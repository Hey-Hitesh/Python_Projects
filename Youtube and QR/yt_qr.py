import urllib.request
import re
import pyqrcode 
from pyqrcode import QRCode 
import tkinter as tk

window = tk.Tk()
window.title("Youtube Link and QR")
window.geometry("400x400")

txt1 = tk.Label(text="Enter the name of the youtube video ")
txt1.place(x=100,y=50)

in1=tk.Entry(window)
in1.place(x=100,y=80)


def proceed():

 search_key = (in1.get())
 # search_keyword = input("Enter the title of the video:\n")
 html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_key)

 video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
 #print(video_ids) All the video ids for the video

 temp = "https://www.youtube.com/watch?v=" + video_ids[0]
 #print("https://www.youtube.com/watch?v=" + video_ids[0])

 disp = tk.Label(text=temp,fg="blue")
 disp.place(x=100,y=110)

 #url = pyqrcode.create(temp)
 #url.svg("QR.svg", scale = 10) 
 


gen=tk.Button(window,text="OK",command=proceed)
gen.place(x=120,y=150)


window.mainloop()
