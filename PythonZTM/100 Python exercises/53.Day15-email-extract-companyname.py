"""
    Assuming that we have some email addresses in the "username@companyname.com" format, 
    please write program to print the company name of a given email address. 
    Both user names and company names are composed of letters only.

    Example: If the following email address is given as input to the program:

    john@google.com

    Then, the output of the program should be:

    google
"""

import re

email = 'john@google.com'

# SOLUTION 1
pattern = re.compile(r"\w+@(\w+)\.\w+")

print(pattern.match(email).group(1))

# SOLUTION 2
email = "john@google.com elise@python.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern,email)
print(ans)