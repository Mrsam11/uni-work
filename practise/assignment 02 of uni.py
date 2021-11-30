#Write a python program to take string phrase input from the user through keyboard
strng = input("Enter Any Phrase : ")
strng = strng.lower() # convert in lower case letters
vowel = 0 #to check Total Vowels .
con = 0 # to check Total Consonants.
space = 0 #to check total spaces
char = 0 # for character in string
word =0 
for i in strng: # running loop on items in string
    if (i >= 'a' and i <='z'):
        if (i == 'a' or i=='e' or i =='i' or i=='o' or i=='u'):
            vowel = vowel + 1
        else:
            con = con + 1
    if i ==" ":
        space += 1
    else:
        char += 1
strng1 = strng.split() # split the string to check total words 
for j in strng1:
    word +=1
print(f'Total vowel in given phrase are : {vowel}')
print(f'Total consonants in given phrase are : {con}')
print(f'Total spaces in given phrase are : {space}')
print(f'Total characters in given phrase are : {char}')
print(f'Total words in given phrase are : {word}')