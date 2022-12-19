# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:58:36 2022

@author: Surface
"""
import sys
sys.path.insert(1, r"C:\Users\Surface\Desktop\Stuff\WordleProject\TheList")
import creating_list
words, t = creating_list.ordered_words(5, "C:\\Users\Surface\Desktop\Stuff\WordleProject\TheList\words.txt")

valid_letters = "abcdefghijklmnopqrstuvwxyz"
new = words[:]
remove_letters = ""
letters_in = ""


def letter_position(colour, input1_col, z):
    global words
    print(input1_col, end="")
    for i in z:
        letter = i[0]
        position = i[1]
        
        
        if colour == "ORANGE":
            for j in words:
                if (letter in j[position]) or (letter not in j):
                    new.remove(j)
            words = new[:]
            
        elif colour == "GREEN":
            for j in words:
                if letter not in j[position]:
                    new.remove(j)
            words = new[:]
                

def remove_grey(a):
    global words
    
    for i in words:                 
        for j in a:
            if j in i:
                new.remove(i)
                break
    words = new[:]    #Words is not shortened so searches through it are faster, and we don't need to keep checking if something in words is in new: it has to be






def a_return(a, c, p):
    global words
    remove_grey(a)
    letter_position("GREEN", "\x1b[1;32m", c)
    letter_position("ORANGE", "\x1b[1;33m", p)
   
    
    if len(new):
        return 
    else:
        return "Empty" 
    
    
    
