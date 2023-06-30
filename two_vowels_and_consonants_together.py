#Write a program that takes a string from the user and prints
#the number of times two vowels and two consonants occur together in the string.

def count_vowels_and_consonants(a):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    v_count = 0
    c_count = 0
    b=len(a)
    for i in range(b- 3):
        if a[i] in vowels and a[i+1] in vowels and a[i+2] in consonants and a[i+3] in consonants:
            v_count += 1
            c_count += 1
    return v_count, c_count
    
user_input = input()
vowels, consonants = count_vowels_and_consonants(user_input)
print("Consonants -", consonants)
print("Vowels -", vowels)
