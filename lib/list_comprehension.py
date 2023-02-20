#!/usr/bin/env python3

def return_evens(num_list):
    new_num_list = []
    for n in num_list:
        if n % 2 == 0:
            new_num_list.append(n)
    print(new_num_list)   
    return(new_num_list)
        

def make_exclamation(sentence_list):
    new_sentence_list = []
    for n in sentence_list:
        new_sentence_list.append(f'{n}!')
    print(f'{new_sentence_list}!')
    return(new_sentence_list)
    
    

return_evens([0,1,3,5,7,8,9])
make_exclamation(["Hello", "I'm doing great", "Python is fun"])