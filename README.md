# basic_programming
Basic Programming

Credits to https://nostarch.com/thinklikeaprogrammer by V. Anton Spraul
I used material from the 1st half of Chapter 6 
Wonderful explaination and examples illustrating how recursion works


How You Would Write a Recursive Function

NUM = 5 

def factorial(n):
    if n == 1:  return 1
    
    # ORIG prodd= n * iif(n-1)
    product= n * factorial(n-1)
    
    return product

facto5 = factorial(NUM)
print(facto5)


Line 14 : Handle the base case, the most trivial case
Line 16 : Imagine there is an imaginary iterative function(called "IIF"), and pass the smaller version of the problem to it
Line 17 : Instead of calling IIF, the function calls itself recursively
DONE




https://github.com/Htet-Myat-Kyaw/basic_programming/blob/master/ap_cs_2018_2019_books.jpg
I will cover lessons from these books in ap_cs_2018_2019_books.jpg in future.
