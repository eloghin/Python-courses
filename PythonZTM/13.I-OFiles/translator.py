"""
	Read a file and translate and print its content into another language.
	Available languages:
		https://en.wikipedia.org/wiki/ISO_639-1
		Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)
"""

from translate import Translator

try:
	with open('text.txt','r') as my_file:
		cont = my_file.read()
		translator = Translator(from_lang = 'it', to_lang = 'en')
		translation = translator.translate(cont)
		print(translation)

except FileNotFoundError:
	print("Check the file path!")

