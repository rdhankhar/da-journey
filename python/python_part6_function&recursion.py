# function

# def sum(a, b):
#     s = a + b
#     return s

# print(sum(1 , 2))

# def sum(a, b):
#     return a + b

# print( "sum is : " ,sum(1 , 2))

# def avg(a, b):
#     return (a + b)/2

# print( "Average is : " ,avg(10 , 20))

# def hello():
#     print("hello rahul ")

# hello()
# hello()
# hello()
# hello()
# hello()

# def prod(a= 10 , b= 20):
#         print(a*b)
#         return a * b
# prod()

# num = [ 1,2,3,4,5,6,7]

# def leng():
#     print("length of a list is :",len(num))

# leng()

# cities = ["delhi","bombay","kolkata","pune","banglore","hyderabad"]
# heroes = ["shaktiman","captain america","batman","spiderman","ironman"]

# def leng(list):
#     print(list)

# leng(len(cities))
# leng(len(heroes))

# def print_list(list):
#     for item in list:
#         print(item , end = " ")
        
# print_list(heroes)
# print_list(cities)
# print()

# def facto(n):
#         fact = 1
#         for i in range(1 , n+1):
#             fact *= i
#         print("factorial is :", fact )
    
# facto(5)

# def conversion(n):
#     usd = 83
#     print("conversion is dollar is :",usd *n)
    
# conversion(6)

# def conversion(n):
#     usd = 83
#     print( n,"USD =",usd *n,"INR")
    
# conversion(43567748)

# def ans(n):
#     if(n %2 == 0):
#         print("Even number")
#     else:
#         print("Odd number")

# ans(6)

# recursion

# def show(n):
#     if (n == 0):
#         return 
#     print(n)
#     show(n-1)
#     print("end")

# show(5)
# def fact(n):
#     if(n == 0 or n ==1):
#         return 1
#     else:
#         return n * fact(n-1)

# print("Factorial of n is :",fact(5))

# def number(n):
#     sum = 0
#     for i in range(1 , n-1):
#             sum += i
#     if(n == 0):
#             return 0
#     else:
#         return sum
# print(number(5))

# def fact(n):
        
#         if(n == 0 or  n == 1 ):
#                 return 1 
#         else:
#                 return fact(n-1)*n

# print("Factorial of is :",fact(5))     

# def cal_sum(n):
        
#         if(n == 0 ):
#                 return 0 
#         else:
#                 return cal_sum(n-1) + n
# sum = cal_sum(155)  
# print(sum)        

def print_list(list , idx = 0):
        if(idx== len(list)):
                return 0
        print(list [idx])
        print_list(list, idx+1)  

fruits = ("mango","orange","apple","banana")

print_list(fruits)