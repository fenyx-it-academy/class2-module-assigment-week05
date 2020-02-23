# 5x5 'lik tahtada, oyuncunun, bilgisayar tarafından rastgele yerleştirilen gemileri tahmin etmesine yönelik hazırlandı.
# ayrıca oluşturulan print_module.py dosyasından import yapıldı.
import time
import random

comp_ship_board=[
[" "," 1"," 2"," 3"," 4"," 5"],
["A",11,12,13,14,15],
["B",21,22,23,24,25],
["C",31,32,33,34,35],
["D",41,42,43,44,45],
["E",51,52,53,54,55]]

letter_dict={"A":1,"B":2,"C":3,"D":4,"E":5}

triplex_ship=random.choice(["horizontal","vertical"])
#program önce üç birimlik gemiyi yerleştirecek. Burada yatay mı dikey mi yerleşeceğini rastgele seçiyoruz.

if triplex_ship == "horizontal": #üçlü gemileri yatay olarak yerleştirme ihtimali.
    possibilities_of_lines=[] # Tahtaya yatay olarak yerleşebilecek bütün ihtimaller burada listelenecek.

    for i in comp_ship_board[1:]: #tahtanın ilk satırında sütun isimleri yer alıyor. O yüzden ilk satırı atlıyoruz.
        a = 1
        b = 2
        c = 3
        for j in range(3): # her satırda geminin yerleşebileceği üç ihtimal olabilir. Örn: [1,2,3],[2,3,4],[3,4,5]
            possibilities_of_lines.append([i[a],i[b],i[c]]) # Üç birimlik gemi icin üç birim koordinat olusturuyoruz.
            a += 1
            b += 1
            c += 1

    horizontal_coordinate = random.choice(possibilities_of_lines) # bir tane yatay koordinat seçiyoruz.
    horizontal_coordinate_2 = horizontal_coordinate.copy() #yukarıda seçilen koordinata ekleme yapacağım için,
    # orjinalin kopyasını alıyorum.
    horizontal_coordinate.append(horizontal_coordinate[2]+1)
    horizontal_coordinate.insert(0, horizontal_coordinate[0]-1)
    # ikinci geminin yerleştirilemeyeceği koordinatları belirlemek icin, ilk elemanın bir eksiği,
    # son elemanın ise bir fazlasını alıyoruz.

    for i in range(1,6):
        for j in range(1,6):
            if comp_ship_board[i][j] in horizontal_coordinate_2:
                comp_ship_board[i][j] = "S3" # random seçilen koordinatlara tahtada S3 yazacak.

    for i in horizontal_coordinate:
# yatay olarak seçilen koordinatın, alt ve üst satırlarına başka gemi yerleştirilmemesi için.
        line_control=[]
        line_control += [i-10, i, i+10]
# örneğin 53,54,55 koordinatı seçilsin. yukarıda bu listenin başına ve sonuna ekleme yaparak listeyi 52,53,54,55,56
# haline getirdik. Sonra sırasyla bu listedeki her bir elemanın 10 eksiği ve 10 fazlasını alıp
# tahtada böyle bir koordinat var mı diye bakacak. Varsa o koordinatı ** olarak işaretleyecek.
        for j in line_control:
            for k in comp_ship_board[1:]:
                for l in k[1:]: # satırların ilk elemanını almayacak. çünkü orada harfler var.
                    if j ==l: # l tahtadaki her bir eleman, j ise line_control'deki her bir eleman.
                        comp_ship_board[comp_ship_board.index(k)][k.index(l)]="**"

###########################################################

if triplex_ship == "vertical": # üçlü gemileri dikey olarak yerleştirme ihtimali.
    possibilities_of_pillars=[]  # Tahtaya dikey olarak yerleşebilecek bütün ihtimaller burada listelenecek.
    x=1
    y=4
    # x ve y degiskenleri birinci satırdan-üçüncü satıra, ikinci satırdan-dördüncü satıra ve
    # dördüncü satırdan-beşince satıra kadar ayrı ayrı döngü kurabilmemizi sağlayacak.
    while y<=6:
        stn = []
        t=0 # ikinci while döngüsü sayacı.
        z=1 # sütun numarası. döngüye birinci sütundan başlanacak.
        while t<5: # beş sütun olduğu için for her bir i'yi 5 kez dolanacak.
            stn = [] #her turda alınan üçlü koordinat, bu listeye atılacak.
            for i in comp_ship_board[x:y]:
                stn.append(i[z])
            #her bir satırın önce birinci sütununu, sonra ikinci sütununu, sonra üçüncü sütununu alacak.
            #sonra ihtimaller listesine eklenecek.
            t += 1
            z += 1
            possibilities_of_pillars.append(stn)
        x += 1
        y += 1

    vertical_coordinate= random.choice(possibilities_of_pillars)
    vertical_coordinate_2=vertical_coordinate.copy()

    vertical_coordinate.append(vertical_coordinate[2]+10)
    vertical_coordinate.insert(0,vertical_coordinate[0]-10)
    # ikinci geminin yerleştirilemeyeceği koordinatları belirlemek icin, ilk elemanın 10 eksiği,
    # son elemanın 10 fazlasını alıyoruz.

    for i in range(1,6):
        for j in range(1,6):
            if comp_ship_board[i][j] in vertical_coordinate_2:
                comp_ship_board[i][j] = "S3"

    for i in vertical_coordinate:
        pillar_control=[]
        pillar_control += [i-1, i, i+1]
# örneğin 35,45,55 koordinatı seçilsin. yukarıda bu listenin başına ve sonuna ekleme yaparak listeyi 25,35,45,55,66
# haline getirdik. Sonra sırasyla bu listedeki her bir elemanın bir eksiği ve bir fazlasını alıp
# tahtada böyle bir koordinat var mı diye bakacak. Varsa o koordinatı ** olarak işaretleyecek.

        for j in pillar_control:
            for k in comp_ship_board[1:]: # tahtanın ilk listesini almayacak.
                for l in k[1:]: # l tahtadaki her bir eleman. j ise pillar_control'deki her bir eleman.
                    if j ==l:
                        comp_ship_board[comp_ship_board.index(k)][k.index(l)]="**"

##############################################################################
### Üçlü gemiler yerleştikten sonra...

if comp_ship_board[2][3]=="S3" and comp_ship_board[3][3]=="S3" and comp_ship_board[4][3]=="S3":
    duplex_ship="vertical"
elif comp_ship_board[3][2]=="S3" and comp_ship_board[3][3]=="S3" and comp_ship_board[3][4]=="S3":
    duplex_ship = "horizontal"
# Dikey [23,33,43] koordinatı tahtanın tam ortası olduğu için ikinci gemi için yatay konumlandıracak yer kalmıyor.
# O yüzden ikinci gemi mecbur dikey oluyor. [32,33,34] de yatay ihitimal için aynı şekilde.
#eğer bu iki koordinat değilse ikinci geminin yatay mı dikey mi olacağını rastgele seçiyor.
else:
    duplex_ship=random.choice(["horizontal","vertical"])


##### ÜÇLÜDEN SONRA YATAY OLARAK İKİLİ GEMİ YERLEŞTİRME BİLGİSAYAR İÇİN. #####
if duplex_ship == "horizontal": # ikili gemileri dikey olarak yerleştirme ihtimali.

    hor_possibilities_for_second_ship=[]
    # ikinci geminin yatay olarak yerleşebileceği bütün ihtimaller burada listelenecek.

    for i in comp_ship_board[1:]:
        a = 1 #sütun numarası olarak kullanılacak.
        b = 2 #sütun numarası olarak kullanılacak.
        for j in range(4): # "a" en fazla sondan bir önceki sütunda olabilir, o yüzden 4 döngü lazım.
            hor_possibilities_for_second_ship.append([i[a],i[b]]) #ikili gemi için iki birim koordinat oluşturuyoruz.
            a += 1
            b += 1

    remainder_possibilities=[] # ikinci geminin yerleşebileceği kalan ihtimaller burada listelenecek.

    for i in hor_possibilities_for_second_ship:
         if "**" not in i and "xx" not in i and "S3" not in i:
             remainder_possibilities.append(i)

    horizontal_coordinate_for_second_ship=random.choice(remainder_possibilities) #kalan olasılıklardan seçim yapıyor.
    for i in range(1,6):
        for j in range(1,6):
            if comp_ship_board[i][j] in horizontal_coordinate_for_second_ship:
                comp_ship_board[i][j] = "S2" # seçilen koordinatlara tahtada S2 yazacak.


##### ÜÇLÜDEN SONRA DİKEY OLARAK İKİLİ GEMİ YERLEŞTİRME BİLGİSAYAR İÇİN. #####
if duplex_ship == "vertical":

    vert_possibilities_for_second_ship=[]
    # ikinci geminin dikey olarak yerleşebileceği bütün ihtimaller burada listelenecek.
    x=1
    y=3
    while y<=6:
        stn = []
        t=0
        z=1
        while t<5:
            stn = []
            for i in comp_ship_board[x:y]:
                stn.append(i[z])
            t += 1
            z += 1
            vert_possibilities_for_second_ship.append(stn)
        x += 1
        y += 1

    remainder_possibilities=[] #ikinci geminin yerleşebileceği kalan ihtimaller burada listelenecek.

    for i in vert_possibilities_for_second_ship:
         if "**" not in i and "xx" not in i and "S3" not in i:
             remainder_possibilities.append(i)

    vert_coordinate_for_second_ship=random.choice(remainder_possibilities)
    vert_coordinate_for_second_ship_2=vert_coordinate_for_second_ship.copy()

    for i in range(1,6):
        for j in range(1,6):
            if comp_ship_board[i][j] in vert_coordinate_for_second_ship_2:
                comp_ship_board[i][j] = "S2"

##############################################
#OYUNCUDAN TAHMİN ALMA.
start_time=int(time.time())

from print_module import * # ekrana yazdırma fonksiyonu başka bir py dosyasında hazırlandı.
print_board() #önce boş tahtayı ekrana yazdırıyoruz.

s2=["S2","S2"]
s3=["S3","S3","S3"]
# gemiler yerleştiğinde tahtada iki tane S2 üç tane S3 olmuş olacak.
meter=0 #oyuncuya 10 ıska hakkı veriyorum. bu sayaç onu tutacak.
while True:
    try:
        line=input("\nEnter a line: ").upper()
        pillar=int(input("Enter a pillar: "))

        if players_screen[letter_dict[line]][pillar] != " X" and players_screen[letter_dict[line]][pillar] != " O":

            if comp_ship_board[letter_dict[line]][pillar]=="S3":
                players_screen[letter_dict[line]][pillar] = " X"
                s3.pop() #üçlü geminin bir parçası vurulduğunda s3 listesinden bir eleman silecek.
                print("You have hit the ship!")
                print_board()

                if len(s3)==0: #üç parça da vurulduğunda yani s3 listesinde eleman kalmadığında gemi batmış olacak.
                    print("TRIPLEX SHIP IS SINKED!")

            elif comp_ship_board[letter_dict[line]][pillar]=="S2":
                players_screen[letter_dict[line]][pillar] = " X"
                s2.pop()
                print("You have hit the ship!")
                print_board()

                if len(s2)==0:
                    print("DUPLEX SHIP IS SINKED!")

            else:
                print("YOU MISSED!")
                players_screen[letter_dict[line]][pillar] = " O"
                print_board()
                meter += 1 #her yanlışında sayaç bir artacak.

            if len(s2)==0 and len(s3)==0:
                print("THE ALL ENEMY SHIPS ARE SINKED! YOU WON!")
                end_time = int(time.time())
                print(f"Game time is {end_time - start_time} seconds!")
                break

            if meter==10:
                print("YOU LOST!")
                break
        else:
            print("You have already shot there! Try Again!")

    except KeyError:
        print("Lines input must be A, B, C, D or E.")
    except ValueError:
        print("Pillar input must be 1,2,3,4 or 5.")
    except IndexError:
        print("Pillar input must be 1,2,3,4 or 5.")