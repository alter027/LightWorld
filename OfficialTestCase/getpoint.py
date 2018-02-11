#!/usr/bin/env python

from __future__ import print_function  
import numpy as np
import cv2
# cv2.imshow('gray', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print cv2.findChessboardCorners(gray,(10,10))

def Solve(mat,di,dj,base_i,base_j):
	gray = cv2.imread('point.png', cv2.IMREAD_GRAYSCALE)
	for i in range(718):
		for j in range(719):
			if gray[i][j] <= 21:
				tmp_i = int((i-base_i)/di)
				tmp_j = int((j-base_j)/dj)
				mat[tmp_i][tmp_j] += 1
def PrintAndTest(mat):
	for i in range(100):
		for j in range(100):
			if mat[i][j] > 10:
				print("1 ",end="")
				mat[i][j] = 1
			else:
				print("0 ",end="")
				mat[i][j] = 0
		print("")
	for i in range(100):
		for j in range(100):
			if i<j:
				if mat[i][j] != mat[j][i]:
					print("%d %d"%(i,j))

def main():
	mat = [[0 for x in range(750)] for y in range(750)] 
	base_i = 1
	base_j = 13
	di = float(706-1)/100
	dj = float(717-13)/100
	Solve(mat,di,dj,base_i,base_j)
	PrintAndTest(mat)
if __name__ == "__main__":
    main()
