from PIL import Image
from random import randint
import numpy, os
from helper import *

def inputImage():
	im = Image.open('input/selected_img.png')
	pix = im.load()
	return im, pix

#step no 4
def rgbMatrix(im, pix):
	# Obtaining the RGB matrices
	r = []
	g = []
	b = []
	for i in range(im.size[0]):
		r.append([])
		g.append([])
		b.append([])
		for j in range(im.size[1]):
			rgbPerPixel = pix[i, j]
			r[i].append(rgbPerPixel[0])
			g[i].append(rgbPerPixel[1])
			b[i].append(rgbPerPixel[2])
	return r, g, b

#step 4(b)
def keyGenarator(im):
	m = im.size[0]
	n = im.size[1]

	# Vectors Kr and Kc
	alpha = 8
	Kr = [randint(0, pow(2, alpha) - 1) for i in range(m)]
	Kc = [randint(0, pow(2, alpha) - 1) for i in range(n)]
	ITER_MAX = 1

	with open('Kr.txt', 'w+') as kr:
		for a in Kr:
			kr.write(str(a) + '\n')

	with open('Kc.txt', 'w+') as kc:
		for a in Kc:
			kc.write(str(a) + '\n')

	return m, n, Kr, Kc, ITER_MAX

def encryptImage(im, pix, m, n, r, g, b, Kr, Kc, ITER_MAX):
	for iterations in range(ITER_MAX):
		# For each row
		for i in range(m):
			rTotalSum = sum(r[i])
			gTotalSum = sum(g[i])
			bTotalSum = sum(b[i])
			rModulus = rTotalSum % 2
			gModulus = gTotalSum % 2
			bModulus = bTotalSum % 2
			if (rModulus == 0):
				r[i] = numpy.roll(r[i], Kr[i])
			else:
				r[i] = numpy.roll(r[i], -Kr[i])
			if (gModulus == 0):
				g[i] = numpy.roll(g[i], Kr[i])
			else:
				g[i] = numpy.roll(g[i], -Kr[i])
			if (bModulus == 0):
				b[i] = numpy.roll(b[i], Kr[i])
			else:
				b[i] = numpy.roll(b[i], -Kr[i])
		# For each column
		for i in range(n):
			rTotalSum = 0
			gTotalSum = 0
			bTotalSum = 0
			for j in range(m):
				rTotalSum += r[j][i]
				gTotalSum += g[j][i]
				bTotalSum += b[j][i]
			rModulus = rTotalSum % 2
			gModulus = gTotalSum % 2
			bModulus = bTotalSum % 2
			if (rModulus == 0):
				upshift(r, i, Kc[i])
			else:
				downshift(r, i, Kc[i])
			if (gModulus == 0):
				upshift(g, i, Kc[i])
			else:
				downshift(g, i, Kc[i])
			if (bModulus == 0):
				upshift(b, i, Kc[i])
			else:
				downshift(b, i, Kc[i])
		# For each row
		for i in range(m):
			for j in range(n):
				if (i % 2 == 1):
					r[i][j] = r[i][j] ^ Kc[j]
					g[i][j] = g[i][j] ^ Kc[j]
					b[i][j] = b[i][j] ^ Kc[j]
				else:
					r[i][j] = r[i][j] ^ rotate180(Kc[j])
					g[i][j] = g[i][j] ^ rotate180(Kc[j])
					b[i][j] = b[i][j] ^ rotate180(Kc[j])
		# For each column
		for j in range(n):
			for i in range(m):
				if (j % 2 == 0):
					r[i][j] = r[i][j] ^ Kr[i]
					g[i][j] = g[i][j] ^ Kr[i]
					b[i][j] = b[i][j] ^ Kr[i]
				else:
					r[i][j] = r[i][j] ^ rotate180(Kr[i])
					g[i][j] = g[i][j] ^ rotate180(Kr[i])
					b[i][j] = b[i][j] ^ rotate180(Kr[i])

	for i in range(m):
		for j in range(n):
			pix[i, j] = (r[i][j], g[i][j], b[i][j])
	im.save('encrypted_images/encrypted_result.png')
	print('Encrypted')

#main
'''filePath = 'encrypted_images/encrypted_result.png';
#As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(filePath):
	os.remove(filePath)
else:
	print("Can not delete the file as it doesn't exists")'''
im, pix = inputImage()
r, g, b = rgbMatrix(im, pix)
m, n, Kr, Kc, ITER_MAX = keyGenarator(im)
encryptImage(im, pix, m, n, r, g, b, Kr, Kc, ITER_MAX)






