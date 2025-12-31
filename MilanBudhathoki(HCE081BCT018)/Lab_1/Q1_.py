# 1. Write a Python program to input five numbers and print the largest number.

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
largest = max(numbers)
print(f"The largest number is: {largest}")