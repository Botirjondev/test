# import math as matematika
# darajasi=0
# def sonlar(Son1,son2):
#     darajasi = matematika.pow(Son1,son2)
#     return darajasi    

# # About string a little !!!
# Seasons = ["Autumn","Spring","Winter","Summer"]
# Seasons.reverse()
# print(Seasons)

# # Tuples -> We can not change their value

# coordinates = (1,2,3)

# # Dictionaries -> it has key and value for example
# Customer =[ {
#     "Name":"Botirjon",
#     "age": 25,
#     "is_verified": True
# },
# {
#     "Name":"Ali",
#     "age": 30,
#     "is_verified": False
# },{
#     "Name":"Vali",
#     "age": 31,
#     "is_verified": True
# },{
#     "Name":"Gani",
#     "age": 32,
#     "is_verified": False,
#     "Bilmadim": True
# },{
#     "Name":"Umar",
#     "age": 26,
#     "is_verified": True
# }
# ]

# for person in Customer:
#     print(person)
#     for per in person:
#         print(per)

# import time 
# JustNow = time.localtime(min);
# print(JustNow) 

# sonlar2 = list(range(11))
# ildizlari = list(map(matematika.sqrt,sonlar2))
# print(ildizlari)

# Funksiyalar yaratish
# def qoshish(x, y):
#     return x + y

# def ayirish(x, y):
#     return x - y

# def kopaytirish(x, y):
#     return x * y

# def bolish(x, y):
#     return x / y

# # Foydalanuvchi kiritgan sonlarni olish
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))


# amal = input("Amal raqamini tanlang (+/-/*//): ")

# # Amalni bajarish va natijani ekranga chiqarish
# if amal == '+':
#     print(x,"+",y,"=", qoshish(x,y))
# elif amal == '-':
#     print(x,"-",y,"=", ayirish(x,y))
# elif amal == '*':
#     print(x,"*",y,"=", kopaytirish(x,y))
# elif amal == '/':
#     print(x,"/",y,"=", bolish(x,y))
# else:
#     print("Noto'g'ri amal raqami kiritildi")

#     import subprocess
#     # Example: Clone a Git repository
# repo_url = "https://github.com/example/repo.git"
# destination_path = "/path/to/destination"
# print(repo_url)

import random
import string
total = string.ascii_letters + string.digits + string.punctuation
passwordNewCalculate = "".join(random.sample(total,25))
print(passwordNewCalculate)

print(total)
