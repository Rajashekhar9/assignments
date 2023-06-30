#Write a program that takes a positive integer from the user 
#and prints the sum of its digits through recursion

def final(a):
    if a<=9:
        return a
    else:
        b=a%10
        c=a//10
        return b+final(c)

a=int(input())
b=final(a)
print(b)