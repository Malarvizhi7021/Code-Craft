def separate(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel = []
    consonant = []
    for ch in text:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):  
            if ch in vowels:
                vowel.append(ch)
            else:
                consonant.append(ch)   
    return vowel, consonant 

text = input("Enter a word: ")
print(separate(text))
