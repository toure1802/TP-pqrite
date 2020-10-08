#!/usr/bin/env python3


def somme_de_controle(string):
	words = string.split(' ')
	res = {}
	for word in words:
		currentSum = sum(map(ord,word))
		res[word] =currentSum


	totalSum = 0


	sumAscii = [res[word] for word in words]
	print("Checksum: ")
	print(' '.join(map(str,sumAscii)))
	print("Somme des Cheksum -> ",sum(sumAscii))


if __name__ == "__main__":
	string = input("entrer un string(s): ")
	somme_de_controle(string)

