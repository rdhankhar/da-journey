# Loops 

# i = 1
# while i <= 5 :
#     print("hello rahul dhankhar",i)
#     i += 1
    
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
    
#     print("loop ended")

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# n = int(input("enter a number : "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {i * n}")
#     i += 1

# i = 1
# while i <= 10:
#     print(i*i)
#     i += 1

# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0 
# while idx < len(num):
#     print(num [idx])
#     idx += 1

# i = 1
# while i  <= 10:
#     print(i ** 2)
#     i += 1

# heroes = ["batman","spiderman","avengers","rahul"]
# idx = 0 
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1
    
# num = [1,4,9,16,25,36,49,64,81,100]
# x = 36
# idx = 0 
# while idx < len(num):
#     if(num[idx] == x):
#         print("num found at idx", idx)
#         break
#     else:
#         print("founding...")
#     idx += 1
    
# print("end of loop")

# i = 1 
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("end of loop")    


# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue

#     print(i)
#     i += 1


# i = 1
# while i <= 10:
#     if (i % 2 == 0):
#         i += 1
#         continue

#     print(i)
#     i += 1

# nums = [1,2,3,4,5,6,7,8,9]

# for value in nums:
#     print(value)

# tupples = (1,2,3,4,5,6,7,8,90)

# for value in tupples:
#     print(value)

# fruits = ["apple","orange","mango","banana"]

# for value in fruits:
#     print(value)

# str = ["apple","orange","mango","banana"]

# for value in str:
#     print(value)

# str = "apple"

# for char in str:
#     print(char)
# else:
#     print("end of the loop")

# str = "apple"

# for char in str:
#     if(char == 's'):
#         print(" l found")
#         break
#     print(char)
# else:
#     print("end of the loop")

# nums = [1,4,9,16,25,36,49,64,81,100]

# for elements in nums:
#     print(elements)

# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx = 0
# for elements in nums:
#     if(elements == x ):
#             print("elements found at index :", idx)
#             break
#     idx += 1
    
# start
# sequence = range(10)

# for el in sequence:
#     print(el)
    
# for el in range(50):
#     print(el)
    
    # start and stop 
    
# for el in range(20 , 50):
#     print(el)

# start , stop and step 


# for el in range(1 , 100 , 2):
#     print(el)

# for el in range(1 , 101):
#     print(el)

# for el in range(100 , 0 , -1):
#     print(el)

# n = int(input("enter a number : "))

# for el in range(1 , 11 ):
#     print(n*el)

# for el in range(20):
#     pass
    
# print("end of the code ")

# for el in range(20):
#     pass
#     if el > 5:
#         print("end of the code ",el)

# n = 10 

# sum = 0
# for el in range(1 , n+1):
#     sum += el
    
# print("sum is : ", sum)

# n = 10 

# sum = 0 
# i = 1
# while i <= n:
    
#     sum += i
#     i += 1
# print("total sum : ", sum)
    

# n = 5 

# fact = 1
# i = 1
# while i <= n:
    
#     fact *= i
#     i += 1
# print("factorial of",n ,"is =",fact)

n = 10 

fact = 1

for el in range( 1 , n+1):
    fact *= el
    
    print("factorial of",el,"is =",fact)