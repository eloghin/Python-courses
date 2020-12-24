"""
create funny texts by asking for input for a paragraph that misses words.
"""

adj = input("Adjective: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
animal = input("Animal: ")

madlib = f"Sometimes I go into the woods because it makes me feel sooo {adj}. Otherwise, I {verb} in a mall, \
where I like to {verb2} unnoticed with my {animal}."

print(madlib)