#Write a Python script using class to reverse a string word by word.

def rev_word(word):
  
    reverse_word = ' '.join(reversed(word.split(' ')))
  
    return reverse_word 
  
if __name__ == "__main__": 
    input = "I am a student"
    print (rev_word(input))