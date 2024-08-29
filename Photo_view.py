from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_image():
   global counter
   img_label.config(image=img_array[counter%len(img_array)])
   counter=counter+1

counter=1
root=Tk()
root.title('Photo View')
root.iconbitmap('favicon-ico.ico')
root.geometry('800x700')
root.config(background='black')

files=os.listdir('Photos')

img_array=[]
for file in files:
   img=Image.open(os.path.join('Photos',file))
   resized_img=img.resize((750,500))
   img_array.append(ImageTk.PhotoImage(resized_img))


img_label=Label(root,image=img_array[0])
img_label.pack(pady=(15,10))


next_btn=Button(root,text='Next',bg='white',fg='black',width=28,height=2,command=rotate_image)
next_btn.pack()
root.mainloop()
