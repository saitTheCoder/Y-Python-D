# word = input("Please type in a word: ")
# print(word)

# word = input("And another word: ")
# print(word)

# word = "third"
# print(word)

# toplam = 0

# sayi = 10
# toplam = toplam + sayi # 10

# sayi = 5
# toplam = toplam + sayi # 15

# word = input("Please type in a word: ") #"kitap"
# print(word) # kitap

# word = word + "!!!" # kitap!!!
# print(word)

# age = 10
# print(type(age))
# print("ahmet "+str(age)+" yasinda.") # "10"

# tip degistirme fonksiyonlari 
# int ---> int()
# str ---> str()
# float----> float()

# yas hesaplamasi yapan bir program yaziniz

ad = input("adiniz: ")
dogum_yili = int(input("dogum yili: ")) # 2014
simdiki_yil = int(input("icinde bulundugumuz yil: ")) # 2023

yas = simdiki_yil - dogum_yili

# print("salih "+yas+" yasinda")
# print(10,30,"sait",10.99)
# yas=30
# print("yas","=",yas,sep="")
# print("yas="+str(yas)) # pass by value
# print(yas - 10)
# print(1,end='')
# print(2,end='')
# print(3)
# print(10,"sait",10.88)

# f-string
print(f"'{ad}'  {yas} yasinda.")