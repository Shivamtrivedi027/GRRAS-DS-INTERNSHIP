# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1,2,3,4])
# y1 = [10,20,20,40]
# y2 = [20,30,25,30]
# y3 = [15,25,35,45]
# # calculation -> width
# w = 0.25
# plt.bar(x - w,y1 , label="boys",width=w) # hide second
# plt.bar(x + w,y2, label="girls",width=w) # show
# plt.bar(x ,y3, label="mens",width=w)
 
# plt.xlabel("groups")
# plt.ylabel("number of students")
# plt.title("Number of Students in Each group")
# plt.legend()
# plt.show()



# # 5. Histogram chart

# import matplotlib.pyplot as plt
# marks = [40,55,60,70,75,90,33,50]
# plt.hist(marks,bins=8,color='green')
# plt.show()



# # 6. Pie chart

# import matplotlib.pyplot as plt
# fruits = ['apple','banana','orange','watermelon']
# count = [40,30,15,70]
# colors = ['red','yellow','orange','green']
# plt.pie(count, labels = fruits,colors=colors,startangle=90,autopct="%1.1f%%")
# plt.show()


# # 7. subplots
# import matplotlib.pyplot as plt
# # first chart 
# x = [1,2,3,4,5]
# y = [10,20,30,40,55]

# plt.subplot(1,2,1)  # rows,column,position
# plt.plot(x,y)
# plt.xlabel("x axis")
# plt.ylabel("y axis")

# # second chart
# x1 = ['apple','banana','orange','watermelon']
# y1 = [40,30,15,70]

# plt.subplot(1,2,2)
# plt.pie(y1,labels=x1,startangle=90)
# plt.xlabel("x1 axis")
# plt.ylabel("y1 axis")
# plt.tight_layout()
# plt.show()

# example
import matplotlib.pyplot as plt
import numpy as np
 
plt.figure(figsize=(10,8))
 
# 1. Line Chart
plt.subplot(2,2,1)
 
x = [1,2,3,4,5]
y = [10,20,30,40,50]
 
plt.plot(x,y,marker='o')
plt.title("Line Chart")
plt.xlabel("X")
plt.ylabel("Y")
 
# 2. Bar Chart
plt.subplot(2,2,2)
 
fruits = ["Apple","Banana","Orange","Mango"]
sales = [50,30,40,60]
 
plt.bar(fruits,sales)
plt.title("Bar Chart")
plt.xlabel("Fruits")
plt.ylabel("Sales")
 
# 3. Pie Chart
plt.subplot(2,2,3)
 
languages = ["Python","Java","C++","SQL"]
students = [40,30,20,10]
 
plt.pie(
    students,
    labels=languages,
    autopct="%1.1f%%",
    explode= [0.1,0,0,0],
    shadow= True
)
 
plt.title("Pie Chart")
 
# 4. Histogram
plt.subplot(2,2,4)
 
data = np.random.normal(50,10,1000)
 
plt.hist(
    data,
    bins=20,
    edgecolor="black"
)
 
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
 
plt.tight_layout()
plt.show()