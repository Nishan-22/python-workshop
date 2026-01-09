# Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and
# converts the remaining strings to uppercase.

result = [s.upper() for s in strings if len(s) >= 4]






# Write a function that merges two dictionaries. If a key exists
# in both dictionaries, sum their values. If a key exists in only
# one, include it as is.


def merge_dicts(d1, d2):
    result = {}

    for key in d1.keys() | d2.keys():
        result[key] = d1.get(key, 0) + d2.get(key, 0)

    return result



# Write a function that determines if two strings are anagrams
# (contain the exact same characters in a different order).

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)



# Write a function that identifies all duplicate elements in a
# list. The solution must run in linear time, meaning you
# should only traverse the list once.


def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)
