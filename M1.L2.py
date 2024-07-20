import random
karakter="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
kata=input("Masukan kata yang mau di jadikan kata sandi")
password=""
for i in range(int(kata)) :
    password += random.choice(karakter)
print(password)
