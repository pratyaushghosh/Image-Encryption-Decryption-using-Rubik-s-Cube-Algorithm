# Image-Encryption-Decryption-using-Rubik-s-Cube-Algorithm

This is a novel image encryption algorithm based on Rubik's cube principle. The original image is scrambled using the principle of Rubik's cube. Then, XOR operator is applied to rows and columns of the scrambled image using two secret keys. Finally, the experimental results and security analysis show that the proposed image encryption scheme not only can achieve good encryption and perfect hiding ability but also can resist exhaustive attack, statistical attack, and differential attack.

**Algorithm Description**

****Rubik’s Cube Image Encryption Algorithm****

  1. I0: α bit grayscale image. Image size is M x N.
  2. Generate random vectors KR & KC of length M & N respectively.
  3. KR(i) & KC(j) elements take a random value of set A = {0,1,2,3,…….2α -1}.
  4. Determine no. of iteration ITER MAX & initialize the counter ITER at 0.
  5. Increment counter by 1, ITER = ITER+1.
  6. For each row of i of image I0.
      i. Compute the sum of all elements in row of i
      ii. Compute modulo of 2 summation of each row of i
      iii. If mod_row = 0 then apply right circular shift on i th row
      iv. Else apply left circular shift on i th row
  7. For each column of j of image I0.
      i. Compute sum of all elements in column of j
      ii. Compute modulo of 2 sum of each column of j
      iii. If mod_col = 0 then apply up circular shift on j th column
      iv. Else apply down circular shift on j th column
  8. Step 6 and 7 will create a scrambled image denoted by ISCR
  9. Using vector KC – Bitwise XOR operator is applied to each row of scrambled image ISCR
  10.Using vector KR – Bitwise XOR operator is applied to each column of scrambled image ISCR
  11.If ITER = ITER MAX then, Encrypted image IENC is created and Encryption is successfully done.
  12.Otherwise it goes back to step 5.

  KR and KC: SECRET KEY But here, ITER MAX = 1 : fast encryption.
  
**Rubik’s Cube Image Decryption Algorithm**

  1. Initialise ITER = 0.
  2. Increment the counter by 1, ITER = ITER + 1.
  3. Bitwise XOR operation on vector KR of the encrypted image IENC.
  4. Bitwise XOR operation on vector KC of the encrypted image IENC.
  5. For each column j of scrambled image ISCR
      i. Compute sum of all elements in the column j
      ii. Compute modulo of 2 sum of each column of j
      iii. If mod_col = 0 then apply up circular shift on j th column
      iv. Else apply down circular shift on j th column
  6. For each row i of scrambled image ISCR
      i. Column sum of all elements summation of all elements in the row of i
      ii. Compute modulo of 2 sum of each row i
      iii. If mod_row = 0 then apply right circular shift on i th row
      iv. Else apply left circular shift on i th row
  7. If ITER = ITER MAX then, Image is decrypted.
  8. Otherwise it goes back to step 2.
