"""
A valid postal code P have to fullfil both below requirements:
    - must be a number in the range from 100000 to 999999 inclusive.
    - must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Your task is to provide two regular expressions:
    regex_integer_in_range and 
    regex_alternating_repetitive_digit_pair. 
Where:
    regex_integer_in_range should match only integers range from 100000 to 999999 inclusive
    regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
"""

# **********
# ** SOL 1**
# **********

regex_integer_in_range = r"^([1-9]\d{5})$"   # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)(?:\d)(\1)+)"    # Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# ***********
# ** SOL 2 **
# ***********

regex_integer_in_range = r"^([1-9]\d{5})$"   # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"    # Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# ***********
# ** SOL 2 **
# ***********

regex_integer_in_range = r"^([1-9]\d{5})$"   # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"    # Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)



# ***********
# ** SOL 3 **
# ***********

regex_integer_in_range = r"^([1-9]\d{5})$"   # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"    # Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
"""
The (\d) captures any digit. The (?=) is a positive look-ahead. Positive look-aheads see if 
there is a match without actually matching them (so that they can be used to find additional 
matches instead of being registered as already being "checked"). The period (?=.) matches anything 
that follows the first digit. The \1 is a reference back to the original capturing group (\d). 
So basically "match a digit, then check to see if there is anything next (.) followed by the same 
original digit (\1)".
"""