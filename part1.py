the_count = 0

word = input("word: ").split()

if "the" in word or "The" in word:
	the_count += 1

print("Total count %s" % (the_count))
