import random
import time
print("1--100 Arasında Rəqəm Təxmin Edin ! ")
reqem = random.randint(1, 100)
şans = 7
while True:
    təxmin = int(input("Təxmininizi Daxil Edin: "))
    if  təxmin == reqem:
        print("Rəqəm Yoxlanılır... ")
        time.sleep(1)
        print("Təbriklər! Düz Təxmin Etdiz !")
        break
    elif təxmin > reqem:
        print("Rəqəm Yoxlanılır... ")
        time.sleep(1)
        şans -= 1
        print("Daha kiçik rəqəm daxil edin ")
        print("Qalan Şans : ", şans)
    else:
        print("Rəqəm Yoxlanılır... ")
        time.sleep(1)
        şans-= 1
        print("Daha böyük rəqəm daxil edin ")
        print("Qalan Şans: ", şans)
    if şans == 0:
        print("Şansınız Bitti !")
        print("Şanslı Rəqəm : ", reqem)
        break
