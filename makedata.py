#!/usr/bin/env python

from __future__ import print_function  
from random import randint
import numpy as np
import cv2

def TestData(mat):
	arr = np.sum(mat,axis = 1)
	if np.var(arr) < 2.82:
		return True
	else:
		return False
def random(mat):
	N = 30
	i = 0
	while i < N*7/2:
		tmp = randint(0,899)
		x = tmp//N
		y = tmp%N
		if x > y and mat[x][y] != 1:
			mat[x][y] = 1
			mat[y][x] = 1
			i += 1
def PrintData(mat,n):
	s = "tr"+str(n)+".in"
	f = open(s, 'w')
	N = 30
	for i in range(N):
		s = ""
		for j in range(N):
			s += str(mat[i][j])
			s += " "
		s += "\n"
		f.write(s)
def main():
	N = 30
	n = 0
	while n < 10:
		mat = [[0 for x in range(N)] for y in range(N)]
		random(mat)
		if TestData(mat):
			PrintData(mat,n)
			n += 1

if __name__ == "__main__":
    main()
