n = int(input())
a = ['***', '* *','***']


def star(n,list):
	total = []
	if n == 3:
		return list
	else:
		for i in list:

			total.append(i*3)
		for i in list:
			total.append(i+' '*len(list)+i)
		for i in list:
			total.append(i*3)
		return star(n/3,total)

for i in star(n,a):
	print(i)

