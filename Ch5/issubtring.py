# Given two strings s and t, check if t is a rotation of s
# Assume that we have a function isSubtring that can check if
# one string is a substring of the other

def isrotation(s, t):

	# Idea: t is a rotation of s iff
	#       t[:i] and t[i:] are both substrings of s
	#       for some i

	for i in range(len(t)):

		sub1 = t[:i]
		sub2 = t[i:]

		if issubstring(s, sub1) and issubstring(s, sub2):
			return True

	return False


def issubstring(s, sub):
	return (sub in s)


s = "chocolate"
t = "chaklat"

print(isrotation(s, t))