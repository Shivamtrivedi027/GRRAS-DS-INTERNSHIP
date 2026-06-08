#conditional statements

# if
# num1 = 10
# num2 = 20
# if num1 < num2 :
#     print(num2)

# #if-else
# num1= int(input("Enter the first number: "))
# if num1 :
#     print("number :-", num1)
# else :
#     print("zero",num1)

# #if-elif-else
# age = int(input("Enter the first number: "))
# if age == 18:
#     print("your age is :" , age)
# elif age > 18:
#     print("your age is above then ", age)
# else:
#     print("your age is less than:", age)

# marks= int(input("Enter the marks: "))
# if marks >= 60 and marks <= 75:
#     print("C grade")
# elif marks > 75 and marks >= 90:
#     print("B grade")
# elif marks >90:
#     print("A grade")
# else:
#     print("Fail")


# Loops

# for loop
# for i  in range(5):
#     print("i = ",  i)

# for i in range(1, 11):
#     print("i = ", i)

#list
# l = [11,12,13,14]
# print(len(l))
# for i in range(4):
#     print(l[i])

#while loop
num1 = int(input("Enter the first number: "))
i = 0
while i< num1:
    print(i)
    i += 1
 # list 
l = [10,11,12,13,14,15]
i=0
while i< len(l):
    print(l[i])
    i += 1