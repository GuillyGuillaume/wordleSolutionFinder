# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:49:48 2022

@author: willi
"""
import numpy as np

path = 'ALLWORDS.txt'
dic = np.genfromtxt(path, dtype=str)

def wordL(length):
    global dic
    filter_dic = np.full(len(dic), False)
    for i in range(0, len(dic)):
        if(len(dic[i]) == length):
            filter_dic[i] = True
    dic = dic[filter_dic]
    print(dic)
    
def hasLetter(letters):
    global dic
    filter_dic = np.full(len(dic), False)
    for i in range(0, len(dic)):
        containsAll = 0
        for char in letters:
            if(char in dic[i].lower()):
                containsAll += 1
        if(containsAll == len(letters)):
            filter_dic[i] = True
    dic = dic[filter_dic]
    print(dic)

def notHasLetter(letters):
    global dic
    filter_dic = np.full(len(dic), True)
    for i in range(0, len(dic)):
        for char in letters:
            if(char in dic[i].lower()):
                filter_dic[i] = False
    dic = dic[filter_dic]
    print(dic)
    
def setLetter(letter, spot):
    global dic
    filter_dic = np.full(len(dic), False)
    for i in range(0, len(dic)):
        if(dic[i][spot].lower() == letter):
            filter_dic[i] = True
    dic = dic[filter_dic]
    print(dic)
    
def notSetLetter(letter, spot):
    global dic
    filter_dic = np.full(len(dic), True)
    for i in range(0, len(dic)):
        if(dic[i][spot].lower() == letter):
            filter_dic[i] = False
    dic = dic[filter_dic]
    print(dic)
    
def knowIs(word):
    wordL(len(word))
    for i in range(0,len(word)):
        if (word[i]!="?"):
            setLetter(word[i],i)
            
def knowIsNot(word):
    wordL(len(word))
    for i in range(0,len(word)):
        if (word[i]!="?"):
            notSetLetter(word[i],i)