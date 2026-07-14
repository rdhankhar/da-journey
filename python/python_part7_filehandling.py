# f = open("demo.txt","r")

# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")

# data = f.read(15)
# print(data)

# f.close()

# f = open("demo.txt","r")

# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

# f = open("sample.txt","a+")
# f.write("abc is a text file")

# data = f.read()

# print(data)
# f.close()

# with open("sample.txt","r")as f:
#     data = f.read()
#     print(data)
    
# with open("sample.txt","w")as f:
#     f.write("hi what's up")

# import os

# os.remove("samplee.txt")

# f = open("practice.txt","w")
# f.write("Hi everyone\nwe are learning File I\O\nusing Java.\nI like programming in Java.")

# with open("practice.txt","r")as f:
#     data = f.read()
    
#     new_data = data.replace("Java","Python")
#     print(new_data)
    
#     with open("practice.txt","w")as f:
#         f.write(new_data)
# word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found")

# def check_for_word():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#     # if(data.find(word) != -1):
#         if(word in data):
#             print("Found")
#         else:
#             print("Not found")
        
# check_for_word()

# def check_for_line():
#         word = "learning"
#         data = True
#         line_no = 1
#         with open("practice.txt","r") as f:
#             while data: 
#                 data = f.readline()
#                 if(word in data):
#                     return line_no
#                 line_no += 1
                
#         return -1

# print(check_for_line())  

# count = 0
# with open("practicee.txt","r") as f:
#     data = f.read()
    
#     nums = data.split(",")
#     for val in nums:
#         if(int(val) %2 == 0):
#             count += 1
        
# print(count)


with open("practicee.txt","r") as f:
    data = f.read()
    print(data)
    nums =""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(nums))
            nums = ""
        else :
            nums += data[i]