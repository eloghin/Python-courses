"""
Problem 1: Match a decimal number
https://regexone.com/problem/matching_decimal_numbers

	match 	3.14529 	
	match 	-255.34 	
	match 	128 	
	match 	1.9e10 	
	match 	123,340.00
	Skip    720p
"""
pattern1 = r"(-|\+)?\d{1,},?\d{0,3}\.?\d*e?\d*$"

"""
Problem 2: Matching phone numbers 

capture 	415-555-1234 	415 	To be completed
capture 	650-555-2345 	650 	To be completed
capture 	(416)555-3456 	416 	To be completed
capture 	202 555 4567 	202 	To be completed
capture 	4035555678 	    403 	To be completed
capture 	1 416 555 9292 	416
"""

pattern2 = r"(\d )?\(?(\d{3})(-| )?\)?(\d{1,3}(-| )?)+"


"""
Problem 3: Matching emails 

capture 	tom@hogwarts.com 	tom 	To be completed
capture 	tom.riddle@hogwarts.com 	tom.riddle 	To be completed
capture 	tom.riddle+regexone@hogwarts.com 	tom.riddle 	To be completed
capture 	tom@hogwarts.eu.com 	tom 	To be completed
capture 	potter@hogwarts.com 	potter 	To be completed
capture 	harry@hogwarts.com 	harry 	To be completed
capture 	hermione+regexone@hogwarts.com 	hermione
"""

pattern3 = r"([a-z]+\.?[a-z]+)([+][a-z]+)?@hogwarts.(com|eu.com)"


"""
Problem 4: Matching HTML
capture 	<a>This is a link</a> 	a 	To be completed
capture 	<a href='https://regexone.com'>Link</a> 	a 	To be completed
capture 	<div class='test_style'>Test</div> 	div 	To be completed
capture 	<div>Hello <span>world</span></div> 	div 	To be completed

"""

pattern4 = r"(^<(a|div)(>| )[a-zA-Z='://. _<>]+)"


"""
Problem 5: Matching specific filenames 
https://regexone.com/problem/matching_filenames

skip 	    .bash_profile 		
skip 	    workspace.doc 		
capture 	img0912.jpg 	        img0912 jpg 	
capture 	updated_img0912.png 	updated_img0912 png 	
skip 	    documentation.html 		
capture 	favicon.gif 			favicon gif 	
skip 	    img0912.jpg.tmp 		
skip 	    access.lock

"""

pattern5 = r"(\w+)\.(jpg|png|gif)"



"""
Problem 6: Trimming whitespace from start and end of line 
https://regexone.com/problem/trimming_whitespace?

capture 		The quick brown fox... 		The quick brown fox... 	To be completed
capture 	   jumps over the lazy dog. 	jumps over the lazy dog.

"""

pattern6 = r"^\s+(.+)"


"""
Problem 7: Extracting information from a log file 
https://regexone.com/problem/extracting_log_data?

Task 		Text 														Capture Groups 	 
skip 		W/dalvikvm( 1553): threadid=1: uncaught exception 		
skip 		E/( 1553): FATAL EXCEPTION: main 		
skip 		E/( 1553): java.lang.StringIndexOutOfBoundsException 		
capture 	E/( 1553):   at widget.List.makeView(ListView.java:1727) 	makeView 
																		ListView.java 
																		1727 	
capture 	E/( 1553):   at widget.List.fillDown(ListView.java:652) 	fillDown 
																		ListView.java 
																		652 	
capture 	E/( 1553):   at widget.List.fillFrom(ListView.java:709) 	fillFrom 
																		ListView.java 
																		709
"""

pattern7 = r"E/\( 1553\):\s+at widget.List.([a-zA-Z]+)\(([a-zA-Z]+\.[a-z]+):(\d+)\)"



"""
Problem 8: Parsing and extracting data from a URL 
https://regexone.com/problem/extracting_url_data?

Task 		Text 															Capture Groups 	 
capture 	ftp://file_server.com:21/top_secret/life_changing_plans.pdf 	ftp 
																			file_server.com 
																			21 	
capture 	https://regexone.com/lesson/introduction#section 				https 
																			regexone.com 	
capture 	file://localhost:4040/zip_file 									file 
																		    localhost 
																		    4040 	
capture 	https://s3cur3-server.com:9999/ 								https 
																			s3cur3-server.com 
																			9999 	
capture 	market://search/angry%20birds 									market 
																			search 	
"""

pattern8 = r"^(\w+)://(\w+\-?\w+?\.?\w+?):?(\d+)?/(.*)"