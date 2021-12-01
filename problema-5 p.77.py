f = open('c:/Users/User/Desktop/text.txt', 'r')
print(f.read())
f.close()
c=str(input('dati caracterele: '))
vc=[]
vocale=set()
for i in range(0,len(c)):
    if str(c[i])=='a' or str(c[i])=='e' or str(c[i])=='i' or str(c[i])=='o' or str(c[i])=='u' or str(c[i])=='A' or str(c[i])=='E' or str(c[i])=='I' or str(c[i])=='O' or str(c[i])=='U':
        vc.extend(c[i]) 
        vocale.update(c[i])      
f1=open('c:/Users/User/Desktop/textiesire.txt', 'w')
f1.write(c)
f1.write('\n')
f1.write('Vocalele sunt: ')
f1.write(str(vocale))
f1.close()