# Image-Encryption-Decryption-using-Rubik-s-Cube-Algorithm

This is a novel image encryption algorithm based on Rubik's cube principle. The original image is scrambled using the principle of Rubik's cube. Then, XOR operator is applied to rows and columns of the scrambled image using two secret keys. Finally, the experimental results and security analysis show that the proposed image encryption scheme not only can achieve good encryption and perfect hiding ability but also can resist exhaustive attack, statistical attack, and differential attack.

Algorithm Overview
Given an input image having the three R,G,B matrices of size M X N Hyperparameters include α - used for vector creation ITER_MAX - maximum number of times to carry out operations

A. Encyption
Create two vectors Kr and Kc with |Kr|=M & |Kc|=N. The values of these vectors are randomly picked from 0 to 2α -1

Repeat below steps ITER_MAX number of times

i. Rolling Rows:

The sum of all pixel values of every row of the image RGB matrices are calculated one by one.

If the sum of a given row rowNumber is even, Roll the row to the right Kr[rowNumber] times Otherwise roll to the left Kr[rowNumber] times.

ii. Rolling Columns:

The sum of all pixel values of every column of the image RGB matrices are calculated one by one.

If the sum of a given row columnNumber is even, roll the column up Kc[columnNumber] times. Otherwise roll the column down Kc[columnNumber] times.

iii. XORing Pixels:

For every pixel(i,j), XOR the pixel with the below two values

Value #1 - Kc[columnNumber] if i is odd else 180 rotated bit version of Kc[columnNumber]

Value #2 - Kr[rowNumber] if j is even else 180 rotated bit version of Kr[rowNumber]

B. Decryption
Given an encrypted image, vectors Kr and Kc & ITER_MAX , decryption can be done by following the reverse procedure - XORing pixels → Rolling Columns → Rolling Rows ITER_MAX number of times
