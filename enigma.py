import string

def main(inp,d):
	alpha = list(string.ascii_uppercase)
	alpha.append(' ')
	roter_1 = [4, 1, 20, 25, 7, 2, 23, 10, 3, 11, 17, 21, 15, 6, 0, 26, 19, 12, 13, 18, 9, 5, 8, 16, 24, 22, 14]
	roter_2 = [25, 8, 0, 26, 24, 7, 16, 9, 15, 1, 20, 17, 10, 18, 4, 13, 5, 3, 12, 23, 22, 6, 11, 21, 19, 14, 2]
	roter_3 = [18, 9, 6, 22, 25, 5, 20, 24, 1, 0, 26, 12, 4, 7, 8, 3, 2, 13, 15, 23, 11, 16, 21, 19, 17, 10, 14]
	out = []
	for x in inp:
		if d == 'e': out.append(alpha[roter_1[roter_2[roter_3[roter_3[roter_2[roter_1[alpha.index(x)]]]]]]])
		elif d == 'd': out.append(alpha[roter_1.index(roter_2.index(roter_3.index(roter_3.index(roter_2.index(roter_1.index(alpha.index(x)))))))])
		if roter_1[1] != 4:
			roter_1 = roter_1[1:] + roter_1[:1]
		else:
			if roter_2[1] != 25:
				roter_2 = roter_2[1:] + roter_2[:1]
				roter_1 = roter_1[1:] + roter_1[:1]
			else:
				roter_3 = roter_3[1:] + roter_3[:1]
				roter_2 = roter_2[1:] + roter_2[:1]
				roter_1 = roter_1[1:] + roter_1[:1]
	return out

if __name__ == "__main__":
	d = raw_input("e or d ->")
	inp = raw_input("Enter the message ->")
	inp = inp.upper()
	out = main(inp,d)
	out = ''.join(out)
	print out