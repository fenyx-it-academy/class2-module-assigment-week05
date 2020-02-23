import random
from board import*#diger sayfada fonksiyon olusturulup import edildi
board=[]#oyun icin tahta olusturuldu
for i in range(5): # bos oyun tahtasina 5*5 '_' altcizgi eklendi. Ayrica liste bu seklide tahta gorunumu aldi
    board.append([" _ "] * 5)
    #print(board)
#def printboard(board):#fonksiyon import icin diger sayfaya alindi. comment kalidirilinca importsuz calisir
 #  for i in board:
  #      print("  ".join(i))

shipList=[]#gemilerin rastgele olusturulup eklenecegi liste olusturuldu
for i in range(1):#for dongusu sayesinde otomatik olusturulan gemilerden sadece bir tanesi alindi. dongu kurulmazsa cift gemi seciyor program
    row1=random.randint(0,2)
    col1=random.randint(0,2)
    ship1row=[[row1,col1],[row1+1,col1],[row1+2,col1]]#yatay gemi
    ship1col=[[row1,col1],[row1,col1+1],[row1,col1+2]]#dikey gemi
    ship1=random.choice([ship1row,ship1col])#yatay veya dikey secimi rastgele bilgisayara sectirildi
    shipList.append(ship1)#secilen gemi listeye eklendi

for i in range(1):#denizalti(gemilerin ustuste cakismaisi ihtimaline karsi bunu deniz alti yapildi.)
    row2=random.randint(0,2)
    col2=random.randint(0,2)
    ship2row=[[row2,col2],[row2+1,col2]]#denizalti
    ship2col=[[row2,col2],[row2,col2+1]]#denizalti
    ship2=random.choice([ship2row,ship2col])
    if ship2 not in shipList:
        shipList.append(ship2)
#print(shipList)
right=1#oyuncunun hamle sayisi birden baslatildi
moves=[]#hamle sayisi
rightMoves=[]#dogru hamle sayisi listesi
while right<=10:#oyuncuya 10 hak tanindi
    r=int(input('please enter any number between 0 and 4 for row : '))#koordinat icin satir girdisi alindi
    c=int(input('please enter any number between 0 and 4 for coloum : '))# koordinat icin sutun giridisi alindi

    if 0<=r<=4 and 0<=c<=4:#girdi icin sayilar sinirlandirildi
        hit = [r, c]#girilen koordinatlar icin atis listesine alindi
        if hit in moves:#atislarin tekrarinin onlenmesi icin kosul olusturuldu
            print('you did again that move')#
            continue
        else:
            moves.append(hit)#daha once bu atis yoksa hamlelere eklendi
            board[r][c]=':( '#hedef tutmamasi durumunda tahtadaki konuma eklendi
            if hit in shipList[0]:#hedefin herhangi bir noktasina isabet saglandiginda butun geminin gorunmesi saglandi
                board[shipList[0][0][0]][shipList[0][0][1]]=  '\o/'#3 luk geminin 1. elemani
                board[shipList[0][1][0]][shipList[0][1][1]] = '\o/'#2. elemani
                board[shipList[0][2][0]][shipList[0][2][1]] = '\o/'#3. elemani
                print('you hit big ship')
                rightMoves.append(hit)#hamleler dogru hamleler listesine eklendi
                for i in shipList:
                    moves.append(i)
            if hit in shipList[1]:
                board[shipList[1][0][0]][shipList[1][0][1]]= '\o/'#2 lik geminin 1. elemani
                board[shipList[1][1][0]][shipList[1][1][1]]= '\o/'#2. elemani
                print('you hit little ship')
                rightMoves.append(hit)
                for i in shipList:
                    moves.append(i)
            #print(ship1, ship2)
            printboard(board)#tahta surekli yazdirilmak icin fonksiyon cagirildi
            right+=1#oyuncunun her hamlesinden sonra hak sayisi 1 azaldi
            print('your {}. right '.format(right))# kacinci hak oldugu yazdirildi.


            #for i in board:#bu sekilde en yukarda tanimlanirsa tahta tek satir olarak gorunuyor. Ya fonksiyon olarak taninmali
                #print("  ".join(i)) # programin cagirilinca gelmesi icin ya da bu sekilde islemin hemen arkasina yazilmalidir
    else:
        print('please enter valid numbers')
    if len(rightMoves) == 2:#gemilerin ikisinin de vurulmasi durumunda oyun sonlandirildi
        print('Bravo you are a really shoter ')
        quit()









