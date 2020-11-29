"""
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
If there are two or more words that are the same length, return the first word from the string with that length. 
gnore punctuation and assume sen will not be empty.

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""

def LongestWord(sen):

  import re

  # code goes here
  word_length = 0
  pattern = r"[\w]*"

  for match in re.finditer(pattern, sen):
    match_length = match.span()[1] - match.span()[0]
   
    if match_length > word_length:
      word_length = match_length
      word = match.group()
    
  return word



def LongestWord(sen): 
    pattern = re.compile(r'\W+')
    x = pattern.split(sen)
    return max(x, key=len)

# keep this function call here 
print(LongestWord(input()))