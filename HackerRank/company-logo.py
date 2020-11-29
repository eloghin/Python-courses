"""
A newly opened multinational brand has decided to base their company logo on the three most common characters 
in the company name. They are now trying out various combinations of company names and logos based on this condition. 
Given a string, which is the company name in lowercase letters, your task is to find the top three most common 
characters in the string.

    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count.
    If the occurrence count is the same, sort the characters in alphabetical order.
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools



if __name__ == '__main__':
    
    s = list(input())
    logo = []
    my_list = [[char, s.count(char)] for char in set(s)]
    my_list.sort(key = lambda x:x[1], reverse=True)
    
    final_list = itertools.groupby(my_list, key = lambda x:x[1])
    
    for k, group in final_list:     
        group_sorted = sorted(list(group), key = lambda x:x[0])
        for g in group_sorted:
            logo.append(g)
        if len(logo) > 3:    
            break
        
    for item in logo[:3]:
        print(*item)