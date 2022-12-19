from fnmatch import translate
from tkinter import *
from tkinter import ttk #, messagebox
import googletrans 
from textblob import TextBlob
from gtts import gTTS
from pygame import mixer  
import os
from playsound import playsound 

root=Tk()
root.title('Translator Lanaguage')

root.geometry("1200x450")

def lable_change():
    c=combol.get()
    c1=combol2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,lable_change)


def translate_now():
    language=googletrans.LANGUAGES
    languageV=list(language.values())
    lang1=language.keys()
    #global language
    text_=text1.get(1.0,END)
    #c=combol.get()
    c1=combol2.get()
        
    for i,j in language.items():
        #print('key :',i,'value :',j)
    
        if c1==j:
            text_=TextBlob(text_)
            text_=text_.translate(to=i)
    text2.delete('1.0','end')
    text2.insert(END,text_)
    #x=text_
    #yield x



    

'''
    try:
        

    except :
        messagebox.showerror("Googletrams",'Please try agian')
    
    try:
        text_=text1.get(1.0,END)
        c=combol.get()
        c1=combol2.get()  
        if(text_):
            text_=text_.read()
            words=TextBlob(text_)
            lan=words.detect_language()
            
        for i,j in language.items():
             
            #   if (j==c1):
                    lan_=i
                    words=words.translate(from_lang=lan,to=(lan_))
                    print(words)
                    #text2.insert(END,words)
                    #text2.delete  (1,0,END)
    except Exception :
        messagebox.showerror("Googletrams",'Please try agian')
'''
def Speeach_select_ENG():
    text_=text1.get(1.0,END)
    print(text_)
    #c=combol.get()
    #c1=combol2.get()
    text_=TextBlob(text_)
    English = gTTS(text=str(text_),slow=False)
    English.save('English.mp3')
    #with open(str('C://Users//User//Desktop//Flask_Projet//English.mp3'), 'wb') as f:
    mixer.init()
    mixer.music.load('English.mp3')
    volume = 0.4
    playsound("English.mp3",volume)
    os.remove('English.mp3')

def Speeach_select():
    text_=text1.get(1.0,END)
    print(text_)
    #c=combol.get()
    c1=combol2.get()
    
        
    for i,j in language.items():
        #print('key :',i,'value :',j)
        #try:
            #os.remove("Hindi.mp3")
        #except :
            #pass
        if c1==j:
            text_=TextBlob(text_)
            text_=text_.translate(to=i)
            #x=str(text_)
            #print(x)
            #x="javaTpoint ಗೆ ಸುಸ್ವಾಗತ"
            
            Hindi = gTTS(text=str(text_),slow=False)
            
            Hindi.save('Hindi.mp3')
            #with open(str('C://Users//User//Desktop//Flask_Projet//Hindi.mp3'), 'wb') as f:
            mixer.init()
            mixer.music.load('Hindi.mp3')
            volume = 0.4
            playsound("Hindi.mp3",volume)
            os.remove('Hindi.mp3')
            #t1 = gtts.gTTS(x) 
            #t1.save("welcome.mp3")
            #playsound("welcome.mp3")
            #t1.close('welcome.mp3')
            #os.remove("welcome.mp3")
            #try:
                #mixer.music.unload()
                #os.remove("Hindi.mp3")
            #except Exception:
                #print("Error while deleting file ", "Hindi.mp3")
                        
            
       
    
    
    

    


#icon
#image_icon.PhotoImage(file='leaf.png')
#root.iconphoto(False,image_icon)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combol=ttk.Combobox(root,value=languageV,font='Roboto 14',state='r')
combol.place(x=110,y=20)
combol.set('ENGLISH')

label1=Label(root,text="ENGLISH",font='segoe 30 bold' ,bg='white',width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="black",bd=5)
f.place(x=10,y=118,width=540,height=210)

text1=Text(f,font='Robot 20' ,bg='white' ,relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=530,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side='right',fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Creating a photoimage object to use image
photo1 = PhotoImage(file = r"Speeach_i.png")
  
# Resizing image to fit on button
photoimage1 = photo1.subsample(3,8)
  
# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
Speeach=Button(root, text = 'Speeach',command=Speeach_select_ENG, image = photoimage1,compound = TOP).place(x=420,y=340)
#Speeach.place(x=630,y=480)


######################################################################
combol2=ttk.Combobox(root,value=languageV,font='Roboto 14',state='r')
combol2.place(x=730,y=20)
combol2.set('SELECT LANGUAGE')
label2=Label(root,text="SELECT LANGUAGE",font='segoe 30 bold' ,bg='white',width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(root,bg="black",bd=5)
f1.place(x=620,y=118,width=540,height=210)

text2=Text(f1,font='Robot 20' ,bg='white' ,relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=530,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side='right',fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Creating a photoimage object to use image
photo = PhotoImage(file = r"Speeach_i.png")
  
# Resizing image to fit on button
photoimage = photo.subsample(3,8)
  
# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
Speeach=Button(root, text = 'Speeach',command=Speeach_select,image = photoimage,compound = TOP).place(x=690,y=340)
#Speeach.place(x=630,y=480)

#translate Button
translate =Button(root,text='Translate',command=translate_now,activebackground='purple',cursor='hand2',fg='white',font='Roboto 15 bold italic',bd=5,bg='red')
translate.place(x=526,y=350)

#Let us create a dummy button and pass the image
photo = PhotoImage(file = "Speeach_i.png")
root.iconphoto(False, photo)



  



lable_change()
root.configure(bg='white')  
root.mainloop()
