"""
Task: 
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.

Format your results in the following way:
    Start : Tag1
    End   : Tag1
    Start : Tag2
    -> Attribute2[0] > Attribute_value2[0]
    -> Attribute2[1] > Attribute_value2[1]
    -> Attribute2[2] > Attribute_value2[2]
    Start : Tag3
    -> Attribute3[0] > None
    Empty : Tag4
    -> Attribute4[0] > Attribute_value4[0]
    End   : Tag3
    End   : Tag2
"""
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for a in attrs:
            print(f'-> {a[0]} > {a[1]}')
            
    def handle_endtag(self, tag):
        print ("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for a in attrs:
            print(f'-> {a[0]} > {a[1]}')



N = int(input())

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

for _ in range(N):
    
    line = input()

    parser.feed(line)