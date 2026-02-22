# 2. Write a program to print the multiplication table of any number (from 1 to 10).

num = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")