# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")





#RO'YXAT BO'SH EMASLIGINI TEKSHIRISH



# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")




#Amalityot


#1-misol

# son = int(input("Juft son kiriting:"))
# if son%2==0:
#     print("Rahmat")
# else:
#     print("Bu juft son emas")


#2-misol

# yosh = int(input("Yoshingizni kirting:"))
# if yosh<=4:
#     narh = 0
# elif yosh<18 :
#     narh = 10000
# elif yosh<=59 :
#     narh = 20000
# elif yosh>=60 :
#     narh = 0
# print(f"Siz {yosh}da bo`lganligingiz uchun sizga {narh} so`m bo`ladi hayvonat bog`iga kirish")
    


#3-misol

# print("2 ta son kirting:")
# first = int(input("birinchi son:"))
# second = int(input("Ikkinchi son:"))
# if first == second :
#     print("Sonlar teng!")
# elif first>second :
#     print(f"{first}>{second}")
# else: 
#     print(f"{first}<{second}")



#4-misol

# mahsulotlar = ["olma","anor","non","un","choy","tuxum","yog","gosht","shakar"]
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulot:"))
    
# for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print("Mahsulot do'konimizda bor")
#         else:
#             print("Mahsulot do'konimizda yo'q")



#5-misol


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
# print("Siz so'ragan barcha mahsulotlar do'konimizda bor")




























































