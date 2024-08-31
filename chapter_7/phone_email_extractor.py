#!/usr/bin/python3
'''
copy text and extract phone numbers and email adresses then put extracted items to clipboard
'''
import pyperclip, re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # area code (optional -> match 0 or 1)
        (\s|-|\.)?                      # separator
        (\d{3})                         # first 3 digits
        (\s|-|\.)                       # separator
        (\d{4})                         # last 4 dogits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
        )''', re.VERBOSE)


emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       # username (+ means 1 or more matches)
        @                       # @ symbol
        [a-zA-Z0-9.-]+          # domain name
        (\.[a-zA-Z]{2,4})       # dot-something
        )''', re.VERBOSE)



# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8] # reformat extension
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches)) # it takes only single string value, need to join()
    print('Copied to lipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email adresses found.')
