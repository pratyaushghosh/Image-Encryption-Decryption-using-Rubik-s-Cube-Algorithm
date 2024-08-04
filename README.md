# 📸 Rubik’s Cube Image Encryption

Welcome to the **Rubik’s Cube Image Encryption** project! This project showcases a unique image encryption algorithm based on the principles of the classic Rubik's Cube. Here's a quick overview of the project's components and how they work together.

## 🚀 Methodology

**Methodology** refers to the theoretical analysis or guidelines of methods applied during research or study. It typically includes a theoretical model, phases, paradigm, and qualitative techniques. Here, our algorithm serves as a constructive theoretical framework to structure, plan, and control the image encryption process.

## 🔄 Rubik’s Cube Algorithm

### Image Encryption
1. **Initialization**:
   - Start with a grayscale image of size M x N.
   - Generate random vectors KR and KC for rows and columns respectively.
   - Determine the number of iterations (ITER MAX).

2. **Scrambling**:
   - For each row, compute the sum and apply a circular shift based on the modulo result.
   - Repeat for columns.

3. **Bitwise XOR**:
   - Apply the bitwise XOR operation using KR and KC vectors to scramble the image further.

4. **Iterations**:
   - Repeat the above steps until ITER MAX is reached, resulting in the encrypted image.

### Image Decryption
1. **Initialization**:
   - Start with the encrypted image and initialize the iteration counter.

2. **Bitwise XOR**:
   - Reverse the XOR operation using KR and KC vectors.

3. **Unscrambling**:
   - For each column and row, compute the sums and apply circular shifts to restore the original image.

4. **Iterations**:
   - Repeat the steps until the original image is successfully decrypted.

## 🔥 Firebase Realtime Database

**Firebase** is a Google product that helps developers build, manage, and grow their apps easily. The Firebase Realtime Database is a cloud-based NoSQL database that manages data at lightning speed. It functions as a large JSON file, providing efficient data management and synchronization.

![image](https://github.com/user-attachments/assets/e142672a-1ecc-4163-9bea-d5432a93544c)

Traditional Database vs. Firebase






![image](https://github.com/user-attachments/assets/c55db933-a796-457d-b475-1082c0bb732b)

Firebase JSON File
## 📧 Sending Mail with Python

Using Python’s **SMTPlib** module, we can send emails with attachments. The process involves:
- Creating SMTP client session objects.
- Providing valid source and destination email IDs and port numbers.
- Using the MIME module for flexibility.





![image](https://github.com/user-attachments/assets/93da83ff-7beb-4e5e-a717-4ad59d98f428)

SMTP Server

## 📲 Sending OTP Messages with Fast2SMS API

Fast2SMS API allows us to send OTP messages efficiently. The process includes:
- Signing up for a Fast2SMS account.
- Using the Dev API option to copy the API Authorization Key.
- Making requests to the API using the `requests` module and reading data with the `json` module.



![image](https://github.com/user-attachments/assets/6ac762b6-f9ef-48b6-a49e-673dfa7f559c)

SMTP Server

## 🧩 Algorithm Description

### Encryption
1. **Grayscale Image**: α-bit, size M x N.
2. **Random Vectors**: KR (rows) & KC (columns).
3. **Iterations**: ITER MAX.
4. **Circular Shifts**: Apply shifts based on row/column sums.
5. **Bitwise XOR**: Scramble image using KR & KC vectors.

### Decryption
1. **Initialize**: Start with encrypted image.
2. **Bitwise XOR**: Reverse XOR using KR & KC.
3. **Unscrambling**: Apply circular shifts to restore the image.
4. **Iterations**: Repeat until original image is recovered.

---

Join us in exploring this fascinating encryption algorithm inspired by the Rubik's Cube! 🚀🔒

Feel free to contribute, raise issues, or suggest improvements. Happy encrypting! 📸✨
