#!/usr/bin/python3

# take a list a return string separated by a comma and a space

spam = ['apples', 'bananas', 'tofu', 'cats']


def comma_code(some_list):
    final_string = ''
    for item in some_list:
        if item == some_list[-1]:
            final_string = final_string + item + '.'
        else:
            final_string = final_string + item  + ', '

    return final_string


print(comma_code(spam))

