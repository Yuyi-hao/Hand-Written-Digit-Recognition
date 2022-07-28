from tkinter import *
from PIL import Image
import cv2 # computer vision 
from keras.models import load_model

class HandWrittenDigitRecognition:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Hand Written Digit Recognition ")
        self.radius = 5
        self.canvas = Canvas(self.window, height=280, width=280)
        self.canvas.pack()
        self.resultLabel = Label(self.window, text="Click on Show Digit...", font=("arial", 14, "bold") )
        self.resultLabel.pack()
        self.canvas.focus()
        self.canvas.bind("<B1-Motion>",self.draw)
        self.frame = Frame(self.window)
        self.frame.pack()
        Button(self.frame, text="Clear canvas", command=self.clear, justify="left").pack(padx=10, pady=5, side=LEFT)
        Button(self.frame, text="Show Digit", command=self.saveImage, justify="left").pack(padx=10, pady=5, side=RIGHT)
        self.window.mainloop()
    
    def draw(self,event):
        self.canvas.create_oval(event.x-self.radius, event.y-self.radius, event.x+self.radius, event.y+self.radius, fill="black")
    
    def clear(self):
        self.canvas.delete("all")

    def saveImage(self):
        self.canvas.postscript(file = "test.eps")
        img = Image.open("test.eps")
        img.save("test.png", "png")
        self.predictNumber()

    
    def predictNumber(self): 
        model = load_model('trained_model.h5')
        imgage=cv2.imread('test.png',0)
        imgage=cv2.bitwise_not(imgage)
        imgage=cv2.resize(imgage,(28,28))
        imgage=imgage.reshape(1,28,28,1)
        imgage=imgage.astype('float32')
        imgage=imgage/255.0
        pred= model.predict(imgage)
        pred_list = pred.tolist()[0]
        max_index = pred_list.index(max(pred_list))
        self.resultLabel["text"] = f"The Digit is : {max_index}"


HandWrittenDigitRecognition()