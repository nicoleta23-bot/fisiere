f=open('c:/Users/User/Desktop/Lista_clasei_11D.txt','r')
linii=f.readlines()
f.close()
f=open('c:/Users/User/Desktop/grupa1.txt','w')
for i in range(0,len(linii)):
    if 'leng1'in linii[i]:
        f.write(str(linii[i]))
f.close() 
f=open('c:/Users/User/Desktop/grupa2.txt','w')
for i in range(0,len(linii)):
    if 'leng2'in linii[i]:
        f.write(str(linii[i]))
f.close()  
f=open('c:/Users/User/Desktop/Lista_clasei_11D.txt','r')
linii=list(f)
f.close()
media=0
note=[]
for linie in linii:
    camp=linie.split()
    nota=int(camp[2])
    note.append(nota)
    note=[int(i) for i in note]
media=(sum(note))/len(note)
m=round(media, 2)
f=open('c:/Users/User/Desktop/Lista_clasei_11D.txt','r')
linii2=f.read()
f.close()
f=open('c:/Users/User/Desktop/Lista_clasei_11D_media.txt','w')
f.write(str(linii2))
f.write('\n')
f.write('Media = ')
f.write(str(m))
f.close()