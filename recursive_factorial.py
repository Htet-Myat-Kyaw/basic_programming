# SET PATH=C:\Users\k\opt\Python27
# pushd  C:\Users\kyaw_kyaw_nnaing\Desktop

# "Think like a programmer" by . Page 150-155


NUM = 5 

def factorial(n):
    if n == 1:  return 1
    
    # ORIG prodd= n * iif(n-1)
    product= n * factorial(n-1)
    
    return product

facto5 = factorial(NUM)
print(facto5)



