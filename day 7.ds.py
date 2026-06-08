# OOPS
# 1. class and objects
# 2. constructor
# 3. polymorphism
# 4. Encapsulation and anstraction


# # example
# class shivam:
#     def __init__(self, name):         # constructor
#         self.name = name
 
#     def show(self):
#         print(self.name)
 
# p = shivam("hello")
# p.show()


# # exmaple 1
# class shivam:
#     def __init__(self):
#         print("calling constructor")

#     def show(self):
#         print("show the name")

# s = shivam()
# s.show()



# # example 2
# class shivam:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def getAge(self):
#         print("My age is: ",self.age)

#     def getName(self):
#         print("My name is: ",self.name)

# # s = shivam("hello",20)
# # s.getAge()
# # s.getName()

# s = shivam(age=20,name="hello")
# s.getAge()
# s.getName()



# # example 3
# class student:
#     def __init__(self,args):
#         print(type(args))
#         print(args)
#         self.name = args

#     def getStu(self):
#         # print("the student is: ",self.name)
#         return self.name


# s = student({"name":"hello","age":20}) # arguments -> 1,2
# t = s.getStu()
# print(t["age"])



# # example 4
# class Student:
#     def __init__(self,*args):
#         self.data=args
#     def users(self):
#         for i in self.data[0]:
#             print(i)
#     def details(self):
#         for i in self.data[1]:
#             print(self.data[1][i])
# s=Student(["Dheeraj","kunal","harsh","praveen"],{"address":"kukas","college":"arya","loc":"jaipur"})
# s.users()
# s.details()



# Example 5 :
# class college:
#     def __init__(self, name):
#         self.name = name['name']
#         self.location = name["location"]
#     def getCollege(self):
#         print("The college name is: ", self.name)
#         print("The college location is: ", self.location)
# c = college({"name": "GRASS", "location": "Bangalore"})
# c.getCollege()

# Example 6 :
# class student:
#     def __init__(self, *args):
#         self.data = args 
#     def users(self):
#         return self.data[0]
#     def details(self):
#         return self.data[1]
# s = student (["dheeraj","kunal","harsh"],{"address":"kukas","college": "arya", "location": "jaipur"})
# u = s.users()
# for i in s.users():
#     print(i)
# d =s.details()
# for i in s.details():
#     print(i, ":", s.details()[i])

# Example 7 :
# class Student:
#     def __init__(self, **data):  # **data or **kwargs is used for collects keyword argument into a dictionary 
#         self.data = data
# s = Student(name="Harsh", age=20)
# print(s.data)
    
