#4. Using matplotlib, plot: • a simple line graph of your choice • a bar graph of marks of 5 subjects

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
marks = [85, 90, 78, 92, 88]
plt.figure(figsize=(6,4))
plt.bar(subjects, marks, color='green')
plt.title("Marks of 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()