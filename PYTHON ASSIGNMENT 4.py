#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# 
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[2]:


#oops method
class poly:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))

class triangle(poly):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def get_area(self):
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5        

t = triangle(a,b,c)
print("area : {}".format(t.get_area()))


# In[6]:


#normal function method
a=float(input("enter 1st side: "))
b=float(input("enter 2nd side: "))
c=float(input("enter 3rd side: "))

s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("area of triangle is %0.2f" %area)


# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.

# In[1]:


lst1=[]

def filterlongword (x,n):
    for i in x:
        if len(i) > int(n):
            lst1.append(i)
        
    return lst1

lst=["boy","girl","watch"]
filterlongword(lst,3)


# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# 
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[6]:



def wordtoint(l):
        return len(l)
    
lst=["word","integer","print","for"]   
     
lst1=list(map(wordtoint,lst))
lst1


# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.

# In[41]:


def vowelornot(t):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if t not in vowels:
        return False
    return True
t="p"
k=list(map(vowelornot,t))
k


# In[ ]:




