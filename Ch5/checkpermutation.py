# Given two strings, check if one is a permutation of the other

def check_permutation(s, t):

	# Idea: String s is a permutation of string t if s contains the same chars as t with the 
	#       same count, but potentially in some different order. We can use a hashtable (dict)
	#       to count the occurences of chars in s and compare to them in t
	if len(s) != len(t):
		return False

	s_chars = {}
	for char in s:
		if char not in s_chars:
			s_chars[char] = 1
		else:
			s_chars[char] += 1

	t_chars = {}
	for char in t:
		if char not in t_chars:
			t_chars[char] = 1
		else:
			t_chars[char] += 1

	# Now loop through one of the dicts and compare to the other dict
	for key, val in s_chars.items():
		if key not in t_chars:
			return False
		else:
			if val != t_chars[key]:
				return False

	return True


print(check_permutation("high", "ih"))