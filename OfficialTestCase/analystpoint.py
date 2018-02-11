#!/usr/bin/env python

# from __future__ import print_function  
import numpy as np
import cv2

def DataInput(mat,N):
	for i in range(N):
		a = raw_input()
		l = a.split(" ")
		j = 0
		for tmp in l:
			mat[i][j] = int(tmp)
			if i == j:
				mat[i][j] = 1
			j += 1
			if j == 100:
				break
def GetData(mat):
	arr = np.sum(mat,axis = 1)
	print "mean =",np.mean(arr)
	print "var =",np.var(arr)
	print "std =",np.std(arr)

def main():
	N = 100
	mat = [[0 for x in range(N)] for y in range(N)]
	DataInput(mat,N)
	GetData(mat)
if __name__ == "__main__":
    main()
