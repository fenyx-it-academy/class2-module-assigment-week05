def Topla(x, y):
    return x + y

def Cikar(x, y):
    return x - y

def Carp(x, y):
    return x * y

def Bol(x, y):
    return x / y


print("Yapmak istediginiz islemi seciniz \n"
      "1.Toplama \n"
      "2.Çıkarma \n"
      "3.Çarpma \n"
      "4.Bölme")
secim = input("Seçiminiz :")
while True:

    try:
        sayi1 = int(input("1. Sayı: "))
        sayi2 = int(input("2. Sayı: "))

        if secim == '1':
            print(sayi1, "+", sayi2, "=", Topla(sayi1, sayi2))

        elif secim == '2':
            print(sayi1, "-", sayi2, "=", Cikar(sayi1, sayi2))

        elif secim == '3':
            print(sayi1, "*", sayi2, "=", Carp(sayi1, sayi2))

        elif secim == '4':
            print(sayi1, "/", sayi2, "=", Bol(sayi1, sayi2))
    except ValueError:
            print('Please enter a number ')

