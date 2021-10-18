"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

# test = [2, 3, 4, 7]
# print(output_all_items(test))


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if(num % 2 == 0):
            even_nums.append(num)
    return even_nums

# test = [2, 3, 4, 7]
# print(get_all_evens(test))

def get_odd_indices(items):
    # TODO: replace this line with your code
    result = []
    
    for idx in range(len(items)):
        if (idx % 2 != 0):
            result.append(items[idx])
    
    return result

# test = [2, 3, 4, 7]
# print(get_odd_indices(test))

def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i}. {item}")
        i+=1

# test = [2, 3, 4, 7]
# print(print_as_numbered_list(test))

def get_range(start, stop):
    # TODO: replace this line with your code
    nums = []
    start_here = start
    for i in range(stop):
        if i >= start_here: 
            nums.append(start)
            start += 1

    return nums
# print(get_range(2, 8))
        

def censor_vowels(word):
    pass  # TODO: replace this line with your code
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)  
    return "".join(chars)

# print(censor_vowels("Hello World"))
    
def snake_to_camel(string):
    
    camel_case = []
    
    for word in string.split("_"):
        camel_case.append(f"{word[0].upper()}{word[1:]}")

    return "".join(camel_case)

# print(snake_to_camel("hello_world"))

def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if (longest<len(word)):
            longest = len(word)
    return longest

    
# print(longest_word_length(["jellyfish", "zebra"]))


def truncate(string):
    # TODO: replace this line with your code
    result = []

    for char in string:
        if (len(result) == 0 or char != result[len(result)-1]):
            result.append(char)
    
    return "".join(result)

# print(truncate('aaaabbbbcccca'))

def has_balanced_parens(string):
    pass  # TODO: replace this line with your code
    parens = 0
    for char in string:
        if (char == "("):
            parens += 1
        elif (char == ")"):
            parens -= 1
            if(parens<0):
               return False
    return parens == 0
    
# print(has_balanced_parens('((This) (is) (good))'))
# print(has_balanced_parens(('(Oh no!)(')))

def compress(string):
    # TODO: replace this line with your code
    compressed = []

    curr_char = ""
    char_count = 0

    for char in string:
        if (char != curr_char):
            compressed.append(curr_char)
            if (char_count > 1):
                compressed.append(str(char_count))
            curr_char = char
            char_count = 0
        char_count += 1
    
    compressed.append(curr_char)
    if (char_count > 1):
        compressed.append(str(char_count))
    
    return "".join(compressed)

#print(compress('Hello, world! Cows go moooo...'))
print(compress('aabbaabb'))