# 3. Create a list of 10 integers and print: • all even numbers • all odd numbers

numbers = [12, 7, 9, 14, 22, 5, 8, 11, 18, 3]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)