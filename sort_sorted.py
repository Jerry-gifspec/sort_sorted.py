from functools import reduce

list_of_numbers = [34, 11, 23, 68, 98, 58473]
squared_numbers_list = [13, 5, 9, 12, 18, 23]

cubed_numbers_list = list(map(lambda x: x**3, squared_numbers_list))
print("Cubed numbers list:", cubed_numbers_list)

even_numbers_list = list(filter(lambda x: x % 2 == 0, list_of_numbers))
print("Even numbers list:", even_numbers_list)

largest_number = reduce(lambda a, b: a if a > b else b, list_of_numbers)
print("Largest number in the list:", largest_number)

is_largest_number_palindrome = lambda x: str(x) == str(x)[::-1]
print("Is the largest number a palindrome?", is_largest_number_palindrome(largest_number))

squared_numbers = list(map(lambda x: x**2, list_of_numbers))
print("Squared numbers list:", squared_numbers)

odd_numbers_list = list(filter(lambda x: x % 2 != 0, list_of_numbers))
print("Odd numbers list:", odd_numbers_list)

sum_of_numbers = reduce(lambda a, b: a + b, list_of_numbers)
print("Sum of all numbers:", sum_of_numbers)

count_specific_number = list_of_numbers.count(68)
print(f"Occurrences of number 68: {count_specific_number}")

product_of_numbers = reduce(lambda a, b: a * b, list_of_numbers)
print("Product of all numbers:", product_of_numbers)

sorted_ascending = sorted(list_of_numbers)
print("List sorted in ascending order:", sorted_ascending)

sorted_descending = sorted(list_of_numbers, reverse=True)
print("List sorted in descending order:", sorted_descending)

print("Original list of numbers:", list_of_numbers)
print("Original squared numbers list:", squared_numbers_list)