my_list = list(map(int, input('Enter a list of numbers separated by spaces: ').split()))
print("Original list:", my_list)

even_list = []
odd_list = []

def classify_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

classify_numbers(my_list)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
