# Write a function that takes two lists (one of keys, one of values) and creates a dictionary

def create_dict(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    print(result)
create_dict(['a', 'b', 'c'], [1, 2, 3])

# Create a function that takes a list and returns two lists - one with even numbers and one
# with odd numbers. Use list methods where appropriate.

def even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd


# Create a function that takes a list of strings and returns a new list containing only strings
# with length greater than 5 Use a for loop to iterate through the lists.

def string_lengths(strings):
    results = []
    for s in strings:
        if len(s) > 5:
            results.append(s)

    return results

print(string_lengths(["hello", "world", "python", "programming", "is", "fun"]))



#Write a function that takes a list of numbers and returns a new list where each element is
# multiplied by 2 using a for loop.

def mul_two(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result
print(mul_two([1, 2, 3, 4, 5]))

# Write a function sum_numbers that only sums numeric arguments passed via *args,
# ignoring non-numeric types.
def sum_numbers(*args):
    total = 0
    for num in args:
        # if type(num) == int or type(num) == float:
        if isinstance(num, (int, float)):
            total += num
    return total
print(sum_numbers(1, 2, 'three', 4.0, [5], 6)) 

# Create a function called shopping_list that accepts items and quantities as keyword
# arguments, and prints a formatted shopping list
def shopping_list(**kwargs):
    for items ,quantity in kwargs.items():
        print(f"{items}:{quantity}")
    return shopping_list
shopping_list( apple=5, susan=25, karina=15, spinner = 1)

   