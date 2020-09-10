counter = 0
run = True
while run:
	try:
		string_in = input("Please input a statement: ").split()
		continue_on = True
	except EOFError:
		print("See ya!")
		break	
	except: 
		print("please enter something valid")
		continue_on = False
		
	if continue_on:

		for i in string_in:
			if i == "the" or i == "The":
				counter += 1
			elif i == "exit":
				run = False
	print("count: %s" % (counter))
