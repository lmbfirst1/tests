"""
https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
"""



def spin_words(sentence):
    spin_sentence = sentence.split()
    for word in range(len(spin_sentence)):
        if len(spin_sentence[word]) > 4:
            new_word = "".join(reversed(spin_sentence[word]))
            spin_sentence[word] = new_word
    sentence = " ".join(spin_sentence)
    return sentence
   
     
print(spin_words("Hey fellow warriors"))
