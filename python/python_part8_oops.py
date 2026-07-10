# class Student:
#     name = "Rahul"
#     rollno = 8
    
# s1 = Student()
# print(s1.name)
# print(s1.rollno)

# s2 = Student 

# print(s2.name)
# print(s2.rollno)


# class Car :
#     colour = "Blue"
#     brand = "Mercedes"
    
# c1 = Car()
# print(c1.colour , c1.brand)

# class Student:
    
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
        
# s1 = Student("Rahul",7)

# print(s1.name,s1.rollno)

# class Student:
#     name = "Rahul"
#     def __init__(self):
#         print("Addding a new student in  database")
    
# s1 = Student()
# print (s1.name)

# class Student:
#     #Default Constructor
#     # def __init__(self):
#     #     pass
    
#     # Parameterized Constructor
#     college_name = "L.P.U"
#     name = "default" # class attribute
#     def __init__(self,name,marks):
#         self.name = name # object attribute > class attribute
#         self.marks = marks
#         print("Addding a new student in  database")
    
# s1 = Student("Rahul",[97,96,95])
# print (s1.name,s1.marks)
# print (s1.college_name)

# print(s1.name)

# s2 = Student("Gourav",[97,98,99])
# print (s2.name,s2.marks)
# print (s2.college_name)

# class Student:
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def welcome(self):
#         print("welcome",self.name)
        
#     def get_marks(self):
#         return self.marks
        
# s1 = Student("Rahul",98)
# s1.welcome()
# print (s1.get_marks())

# practice question

# class Student:
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     @staticmethod   
#     def hello():
#         print("hello")
        
#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum += val 
#         print("Hi",self.name,"your average is :",sum/3)

# s1 = Student("Rahul",[97,98,99])     
# s1.get_avg()
# s1.hello()

# s1.name = "Tony stark"
# s1.get_avg()

# class car:
    
#     def __init__(self):
#         self.acc = False
#         self.cluth = False
#         self.brake = False
    
#     def start(self):
#         self.acc = True
#         self.cluth = True
#     print("Car started..")

# c1 = car()
# c1.start()

# class account:
    
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc
        
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount ,"was credited")
#         print("total balnace = ", acc1.balance)
        
#     def debit(self,amount):
#         self.balance  -= amount
#         print("Rs.",amount ,"was debited")
#         print("total balnace = ", acc1.balance)
    
    
# acc1 = account(10000,12345)
# print(acc1.balance,acc1.account_no)
# acc1.debit(9000)
# acc1.credit(40000)
# acc1.debit(5000)

# Oops Part 2

# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
#     def acess(self):
#         print(self.__acc_pass)
        
# acc1 = account(123478,"rahul")

# print(acc1.acc_no)
# acc1.acess()

# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass
            
# acc1 = account(123478,"rahul")
# del acc1.acc_no
# print(acc1.acc_no)


# class person:
#     def __hello(self):
#         print("hi user")
        
#     def helllo(self):
#         print(self.__hello)
        
# p1 = person

# p1.__hello()

# Single inheritence

# class Car:
    
#     colour = "black"
#     @staticmethod
#     def start():
#         print("Car started..")
        
#     @staticmethod
#     def stop():
#         print("Car stopped.")
        
# class ToyotaCar(Car):
    
#     def __init__(self,name):
#         self.name = name
        
# car1 = ToyotaCar("Fortuner")
# print(car1.name)
# car1.start()
# car1.stop()
# print(car1.colour)

# Multilevel Inheritence

# class Car:
    
#     def __init__(self,colour):
#         self.colour = colour

# class Brand(Car):

#     def __init__(self,brand,colour):
#         super().__init__(colour)
#         self.brand = brand

# class Price(Brand):
    
#     def __init__(self,colour,brand,price):
#         super().__init__(colour,brand)
#         self.price = price

# c1 = Price("Black","Toyota",6000000)

# print(c1.colour)
# print(c1.brand)
# print(c1.price)

# Multiple inheritance

# class A:
    
#     A = "This is class A"

# class B:
    
#     B = "This is class B"
    
# class C(A,B):
    
#     C = "This is class C"

# c1 = C()

# print(c1.A)
# print(c1.B)
# print(c1.C)

# Super Method 

# class Car:
    
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped")


# class ToyotaCar(Car):
    
#     def __init__(self, brand ,type):
#         super().__init__(type)
#         self.brand = brand
#         super().start()

# c1 = ToyotaCar("fortuner","Diesel")

# print (c1.type)


# class Person:
    
#     name = "anonymous"
    
    # def __init__(self,name):
    #     self.name = name 
        # self.__class__.name = name 
        # Person.name = name 
        
#     @classmethod
#     def changeName(cls,name):
#         cls.name = name 

# p1 = Person()
# p1.changeName("Rahul Kumar")

# print(p1.name)
# print(Person.name)

# class Student:
    
#     def __init__(self,phy,chem,maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
        
    
    # def calpercentage(self):
    #     self.percentage =  str((self.phy + self.chem + self.maths)/3) + "%"
    
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.maths)/3) + "%"
    
    
# s1 = Student(97,98,95)
# s1.phy = 86

# print(s1.phy)
# print(s1.percentage)

# s1.calpercentage()
# print(s1.percentage)

# Polymorphism

# print(1+3)
# print(type(1))

# print("apna" + "college")
# print(type("apna"))

# print([1,2,3] + [4,5,6])
# print(type([1,2,3]))

# class Complex:
    
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real , "i + ", self.img ,"j")
        
#     def __add__(self,num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return  Complex(newreal , newimg)
    
#     def __sub__(self,num2):
#         newreal = self.real - num2.real
#         newimg = self.img - num2.img
#         return  Complex(newreal , newimg)
    
# num1 = Complex(1,2)
# num2 = Complex(3,7)

# num1.showNumber()
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# num1.showNumber()
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()

# Practice Question

# class Circle:
    
#     def __init__(self,radius):
#         self.radius = radius
    
    # def Area(self):
    #     area = 3.1417 * self.radius * self.radius
    #     print(area)
    
#     def area(self):
#         return 3.1417 * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * 3.1417 * self.radius
    
# c1 = Circle(21)

# print(c1.radius)
# c1.Area()

# print(c1.area())
# print(c1.perimeter())

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")

# e1 = Employee("accountant", "Finance", "60,000")
# e1.showDetails()

# engg1 = Engineer("Elon Musk", 40)
# engg1.showDetails()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = Order("chips", 10)
odr2 = Order("tea", 15)

print(odr1 > odr2)  # True