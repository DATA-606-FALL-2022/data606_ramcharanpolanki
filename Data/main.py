from flask import Flask, render_template, request, redirect, abort
from tensorflow import keras
from matplotlib import pyplot as plt
import random
import tensorflow as tf
import keras 
from keras import layers
import numpy as np
import matplotlib.pyplot as plt
import os
import re
import random
import cv2
import base64


app = Flask(__name__,static_folder = "templates")



# Home page
@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

# Home page
@app.route("/", methods = ['POST'])
def index_post():
    d = dict(request.form)
    message = ""
    files = os.listdir("data")
    path = "data/"+files[random.randint(0,len(files))]
    img1 = cv2.imread(path)
    generator = keras.models.load_model('./generator (2).h5')
    noise = np.random.normal(0,1,(1,100))
    img = np.array(generator(noise)[0])
    img1 = cv2.resize(img1, (img.shape[0],img.shape[1]))
    
    img = img + 255*img1
    
    cv2.imwrite('./templates/new_plot.png',img)    
    

    with open("./templates/new_plot.png", "rb") as imageFile:
        img = base64.b64encode(imageFile.read())
        img = "data:image/png;base64,"+str(img)[2:-1] 

    print(img[:50])
    
    return render_template('resp.html', name = 'Generated face', bytes = img)


# entering point for the program
if __name__ == "__main__":
    app.run(debug = True)