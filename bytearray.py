#!/usr/bin/ python

import random
def bypair(x):

	b=x.decode('utf-8')
	s=0
	for i in range(len(b)):
		if b [i] == "1":
			s += 1
	if (s%2) != 0 :
		#le nombre de 1 est pair
		b= "0"+ b
	else:
		#le nombre de 0 est pair
		b="1"+ b
	print(b)
	x=bytearray(b, 'utf-8')

	return x

def by_impair(x):

        b=x.decode('utf-8')
        s=0
        for i in range(len(b)):
                if b [i] == "1":
                        s += 1
        if (s%2) == 0 :
		#le nombre de 1 est pair
                b= "1"+ b
        else:
		#le nombre de 1 est impair
                b="0"+ b
        print(b)
        x=bytearray(b, 'utf-8')

        return x


def rand_key(p):
	key1= ""
	for i in range(p):
		temp = str(random.randint(0,1))
		key1 +=temp
	return(key1)
n = 10
str1 = rand_key(n)
print (str1)
x = bytearray(str1,'utf-8')
print(bypair(x))
