#!/usr/bin/python3
import re

# Regex for dates (DD/MM/YYYY)
date_detection = re.compile(r'''(
        \b((0?[1-9])|[12][0-9]|3[01])\b     #day -> \b word boundary (match 123, not abc12)
        /                                   # separator
        \b(0?[1-9]|1[012])\b                # month
        /                                   # separator
        1[0-9]{3}|2[0-9]{3}                 # year
)''', re.VERBOSE)
# day - 01-31
# month 01 - 12
# year 1000 - 2999

# then detect only valid dates

mo = date_detection.findall('01/12/1999 and 2/10/2001')
