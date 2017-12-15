# Given a string (represented as an array of chars) and the "true" length of the string (length of the array),
# replace all occurences of a space with '20%'

def urlify(chars, l):

	for i in range(l):
		if chars[i] == ' ':
			chars[i] = '2'

			# Now we need to shift all chars in the subarray chars[(i+1):] the right by two
			for j in range(l-1, i, -1):
				chars[j] = chars[j - 2]
			chars[i+1] = '0'
			chars[i+2] = '%'

	return chars


c = ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' ']
l = 17
print(urlify(c, l))