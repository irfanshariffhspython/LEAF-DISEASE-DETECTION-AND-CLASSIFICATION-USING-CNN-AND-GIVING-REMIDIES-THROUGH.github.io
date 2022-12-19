from gtts import gTTS
from playsound import  playsound

import pandas as pd

from cgitb import text
from flask import Flask, render_template, request, jsonify

import os

from predict import prediction, getDataFromCSV


#Translate Lnaguage
from googletrans import Translator
import googletrans
import textblob            #to import
from textblob import TextBlob
#import translator
from gtts import gTTS
from playsound import playsound

DEVELOPMENT_ENV = False
translator = Translator()

# create image folder if not exits
if not os.path.isdir(os.path.join(os.getcwd(), 'images')):
    os.mkdir(os.path.join(os.getcwd(), 'images'))
    



app=Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/Diaseae")
def Disease():
    return render_template('Disease1.html')

@app.route('/model1')
def model1():
    return render_template('')
@app.route("/Contact")
def Contact():
    return render_template('contact.html')

baseDir = os.path.join(os.getcwd(), 'detail_Leaf_Image_link')
file_name =(os.path.join(baseDir, 'tomato_project_details_with_usage.csv'))
@app.route('/result', methods=['GET', 'POST'])
#file =('C:\\Users\\User\\Desktop\\Flask_Projet_Phase3\\Flask_Projet\\Flask_Projet\\detail_Leaf_Image_link\\tomato_project_details_with_usage.xlsx')


#print(newData['usage'])
def result():
    product_id = request.args.get('id', default=-1, type=int)
    # update it for the default fields which will be null and redirect to the home page
    app_data = {
        'index':product_id,
        "disease_name": "undefined",
        "supplement name": "null",
        "supplement image": "null",
        "buy link": "null"
    }
    if product_id != -1:
        dataPredicted = getDataFromCSV(product_id)
        if any(dataPredicted):
            app_data = {
                'index':dataPredicted[0],
                "disease_name": dataPredicted[1],
                "supplement name": dataPredicted[2],
                "supplement image": dataPredicted[3],
                "buy link": dataPredicted[4]
                
            } 
    global translation_result_1 
    translation_result_1 =''
    global translation_result 
    translation_result =''
    global translation_result_2 
    translation_result_2=''
    global newData
    newData=''
    global xx
    xx=''
    global ind
    newData = pd.read_csv(file_name)
    ind=app_data['index']
    xx=newData.loc[ind,'usage']
    if request.method == 'POST':
        try:
            newData = pd.read_csv(file_name)
            ind=app_data['index']
            print('index =' ,ind)
            xx=newData.loc[ind,'usage']
            print(newData.loc[ind,'usage'])
            print(xx)#'ERROR: We are not able to handle your request right now'#newData['usage']
            m=[app_data['disease_name'],app_data['supplement name'],xx]
            #for i in range(len(m)):
            text_to_translate = m[0].lower()
            text_to_translate_1 = m[1].lower()
            text_to_translate_2= m[2].lower()
            selected_language = request.form["select-language"]
            translated_text = translator.translate(text_to_translate, dest=selected_language)
            translated_text_1 = translator.translate(text_to_translate_1, dest=selected_language)
            translated_text_2= translator.translate(text_to_translate_2, dest=selected_language)
        
            translation_result = translated_text.text
            translation_result_1 = translated_text_1.text
            translation_result_2= translated_text_2.text
        
            pronunciation_data = translated_text.pronunciation
            if (str(pronunciation_data) == "None"):
                pronunciation_data = "{Sorry, data not available}"
            confidence = round((translator.translate(text_to_translate, dest=selected_language).extra_data["confidence"])*100, 2)
        except:
            pronunciation_data = "-"
            #translation_result = "{ERROR: We are not able to handle your request right now}"
            confidence = "-"
        
        return render_template('result.html',app_data=app_data,ind=ind, translation_result=translation_result , translation_result_1=translation_result_1 ,translation_result_2=translation_result_2,newData=newData, xx=xx,pronunciation=pronunciation_data, confidence_level=str(confidence)+" %")
    
    return render_template('result.html',app_data=app_data,newData=newData,xx=xx,ind=ind)


@app.route('/analyze', methods=['POST'])
def analyze():
    image = request.files['file']
    print(image.filename)
    pathOfFile = os.path.join(os.getcwd(), 'images', image.filename)
    image.save(pathOfFile)
    data = {}

    # update the request
    data['product_id'] = prediction(pathOfFile)
    os.remove(pathOfFile)
    return jsonify(data)



@app.route('/translate',methods=['POST','GET'])
def translate():
    product_id = request.args.get('id', default=-1, type=int)
    #global text_0
    #global text_1
    #global text_2
    
    # update it for the default fields which will be null and redirect to the home page
    app_data = {
        "disease_name": "undefined",
        "supplement name": "null",
        "supplement image": "null",
        "buy link": "null"
    }
    if product_id != -1:
        dataPredicted = getDataFromCSV(product_id)
        if any(dataPredicted):
            app_data = {
                "disease_name": dataPredicted[1],
                "supplement name": dataPredicted[2],
                "supplement image": dataPredicted[3],
                "buy link": dataPredicted[4]
            }
    if request.method == 'POST':
        #try:
        xx="A line is a one-dimensional figure, which has length but no width. A line is made of a set of points which is extended in opposite directions infinitely. It is determined by two points in a two-dimensional plane. The two points which lie on the same line are said to be collinear points."
        m=[app_data['disease_name'],app_data['supplement name'],xx]
        #for i in range(len(m)):
        text_to_translate = m[0].lower()
        text_to_translate_1 = m[1].lower()
        text_to_translate_2= m[2].lower()
        selected_language = request.form["select-language"]
        translated_text = translator.translate(text_to_translate, dest=selected_language)
        translated_text_1 = translator.translate(text_to_translate_1, dest=selected_language)
        translated_text_2= translator.translate(text_to_translate_2, dest=selected_language)
        
        translation_result = translated_text.text
        translation_result_1 = translated_text_1.text
        translation_result_2= translated_text_2.text
        pronunciation_data = translated_text.pronunciation
        if (str(pronunciation_data) == "None"):
            pronunciation_data = "{Sorry, data not available}"
        #confidence = round((translator.translate(text_to_translate, dest=selected_language).extra_data["confidence"])*100, 2)
        #except:
        
        return render_template('result_ree.html',translation_result=translation_result , translation_result_1=translation_result_1,translation_result_2=translation_result_2)
    return render_template('result_ree.html')


if '__main__' ==__name__:
    app.run(use_reloader = True,debug=True)
    
    