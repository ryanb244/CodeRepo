
def master_yoda(text):


	textlist = text.split()
	print(textlist)
	reverse_word_list = textlist[::-1]
	print(reverse_word_list)

	return " ".join(reverse_word_list)
	


print(master_yoda("Poopy dick face"))