
"""
Write a program which accepts a string as input to print "Yes" 
if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""

def string_op(s):
  print("Yes") if s in ['yes', 'YES', 'Yes'] else print("No")

string_op("yer")
