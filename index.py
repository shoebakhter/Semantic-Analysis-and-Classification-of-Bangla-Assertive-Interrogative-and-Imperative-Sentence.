# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 10:54:32 2018

@author: shoeb
""" 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# MACHINE LEARNING section ###########################################
dataset2 = pd.read_csv('two_word.csv')
dataset3 = pd.read_csv('three_word.csv')
dataset4 = pd.read_csv('four_word.csv')
dataset5 = pd.read_csv('five_word.csv')
X2 = dataset2.iloc[:, 0:2].values
y2 = dataset2.iloc[:, -1].values
X3 = dataset3.iloc[:, 0:3].values
y3 = dataset3.iloc[:, -1].values
X4 = dataset4.iloc[:, 0:4].values
y4 = dataset4.iloc[:, -1].values
X5 = dataset5.iloc[:, 0:5].values
y5 = dataset5.iloc[:, -1].values

from sklearn.linear_model import LinearRegression
regressor2 = LinearRegression()
regressor3 = LinearRegression()
regressor4 = LinearRegression()
regressor5 = LinearRegression()
regressor2.fit(X2, y2)
regressor3.fit(X3, y3)
regressor4.fit(X4, y4)
regressor5.fit(X5, y5)
def prediction(t,lenth):
    if lenth==2:
        y_pred = regressor2.predict(t)
        
    elif lenth==3:
        y_pred = regressor3.predict(t)
    elif lenth==4:
        y_pred = regressor4.predict(t)
    elif lenth==5:
        y_pred = regressor5.predict(t)
    print(y_pred)
    if y_pred>=19 and y_pred<=21.50:
        print("বিবৃতিমূলক বাক্য") 
    elif y_pred>=21.50 and y_pred<=22.50:
        print("প্রশ্নবোধক বাক্য") 
    elif y_pred>=22.50 and y_pred<=23.50:
        print("আদেশসুচক বাক্য") 
        
        
### parts of speech tagger
def tagger(splited):
    print(splited)
    lenth = len(splited)
    i=0;
    nlp_array=np.empty((0))
    for i in range(lenth):
        pos=string.find(splited[i])
        #print(len(splited[i]))
        if pos>=0:
            #for j in range(10):
                if string[pos+len(splited[i])]=='_':
                    t=string[pos+len(splited[i])+1:pos+len(splited[i])+4]
                    #print(t)
                    if t=='NNN':
                      #print(1)
                      print("NOUN")
                      nlp_array=np.append(nlp_array,1)
                    elif t=='PRN':
                      #print(2)
                      print("PRONOUN")
                      nlp_array=np.append(nlp_array,2)
                    elif t=='ADJ':
                      #print(3)
                      print("ADJECTIVE")
                      nlp_array=np.append(nlp_array,3)
                    elif t=='VRI':
                      #print(4)
                      print("VERB")
                      nlp_array=np.append(nlp_array,4)
                    elif t=='VRT':
                      #print(5)
                      print("VERB")
                      nlp_array=np.append(nlp_array,5)
                    elif t=='ADV':
                      #print(6)
                      print("ADVERB")
                      nlp_array=np.append(nlp_array,6)
                    elif t=='PRP':
                      #print(7)
                      print("PREPOSITION")
                      nlp_array=np.append(nlp_array,7)
                    elif t=='CNJ':
                      #print(8)
                      print("CONJUCTION")
                      nlp_array=np.append(nlp_array,8)
                    elif t=='INJ':
                      #print(9)
                      print("INTERJECTION")
                      nlp_array=np.append(nlp_array,9)
                    elif t=='WHW':
                      #print(10)
                      print("WH WORD")
                      nlp_array=np.append(nlp_array,10)
                    elif t=='EXM':
                      #print(11)
                      print("EXCLAMETORY WORD")
                      nlp_array=np.append(nlp_array,11)
                    elif t=='IMP':
                      #print(12)
                      print("IMPERATIVE WORD")
                      nlp_array=np.append(nlp_array,12)
                    else:
                      #print("ট্যাগের নামে ভুল আছে")
                      print("NOT FOUND")
                      nlp_array=np.append(nlp_array,0) 
                    #break;
                else:
                    #print("underscore নাই") 
                    print("NOT FOUND")
                    nlp_array=np.append(nlp_array,0)
                    #break;
                    
                    
        else:
         print(" খুইজা পাই নাই")
         nlp_array=np.append(nlp_array,0)  
         
         
    nlp_array=np.reshape(nlp_array,(1,lenth))
    return nlp_array

#### stemmer ################################################# 
def stemmer(string):
    string = string.replace("দের","")
    string = string.replace("রে","র")
    string = string.replace("রের","র")
    string = string.replace("নের","ন")
    string = string.replace("নে","ন") 
    string = string.replace("কে","") 
    string = string.replace("তের","ত") 
    string = string.replace("দের","") 
    string = string.replace("শের","শ")   

    return string
########### Main Executable

def main():
    inputText = input("Enter a bangla sentence ")
    stemmed_text=stemmer(inputText)
    splited =  stemmed_text.split();
    lenth = len(splited)
    j=0
    for j in range(lenth):
        if splited[j]=='?'or splited[j]=='কী'or splited[j]=='কে' or splited[j]=='কেমন' or splited[j]=='কোথায়' or splited[j]=='কখন' or splited[j]=='কীভাবে' or splited[j]=='কেন'  or splited[j]=='কবে' or splited[j]=='কাকে' or splited[j]=='নাকি':
            print("প্রশ্নবোধক বাক্য")
            main()
            break
        elif splited[j]=='যাও'or splited[j]=='খাও'or splited[j]=='কর' or splited[j]=='পড়' or splited[j]=='চল' or splited[j]=='উঠাও' or splited[j]=='নামাও' or splited[j]=='শোন'  or splited[j]=='নিভাও' or splited[j]=='দাও' or splited[j]=='উড়াও' or splited[j]=='ডাক' or splited[j]=='আন' or splited[j]=='দৌড়াও' :
            print("আদেশসুচক বাক্য")
            main()
            break
        elif  lenth>5:
            print("বিবৃতিমূলক বাক্য")
            main()
            break
    nlp_array=tagger(splited) 
    print(nlp_array) 
    prediction(nlp_array,lenth) 
    main()        


###########NLP Section      
file = open("dataset.txt","r+", encoding="utf8")
string =file.read()
string=stemmer(string)

#print(string)
 
#####Calling main function
main()



    


