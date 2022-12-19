# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:57:13 2022

@author: Surface
"""



def load_words(file_name):
    #print("Loading word list from file...")
    in_file = open(file_name, "r")
    line = in_file.read() # Creates string of words from the file
    words = line.split() # Creates a list of all words by splitting at spaces
    #print(len(words), "words loded.")
    in_file.close()
    return words



def ordered_words(size, our_file):
    word_list = load_words(our_file)
    
    #Create a list of words of a specified length with no repeating letters--------------------------
    words_size = []
    words_size_unique = []
    for i in word_list:     #Make a list of words of a certain length
        if len(i) == size:
            words_size.append(i)
            
            
    for i in range(len(words_size)):    #Make the list refer words with no repeating letters
        
        if len(set(words_size[i])) == len(words_size[i]):
            words_size_unique.append(words_size[i])
    
    #print("We will be using", len(words_size_unique), "words for this game.", end = "\n\n")
    
    #Create a way to score all the letters. ------------------------------------------------
    common_letters = {}
    for j in "abcdefghijklmnopqrstuvwxyz":
        total = 0
        for i in range(len(words_size)):    #Go through each word in the list
            if j in words_size[i]:          #If the letter is in the word, the counter increases by one
                total = total + 1
        common_letters[j] = total          #Put the letter in a dictionary with its number of appearances
    

    #print(common_letters, end="\n\n") 
    
    
    #Give each word a score in a dictionary----------------------------------------------------
    words_size_rank = {}
    
    for i in range(len(words_size_unique)):
        count = 0
        for j in words_size_unique[i]:
            count = count + common_letters[j]
        words_size_rank[words_size_unique[i]] = count
    
    #Create an ordered list with all the words beginning with the highest valued
    words_size_ordered = []
    
    i = max(words_size_rank.values())
    while i >= 0:
        for j in words_size_rank:
            if words_size_rank[j] == i:
                words_size_ordered.append(j)
        i = i -1
    
    #Returns the List of words in order of value from highest to lowest-----------------------
    return words_size_ordered, common_letters
