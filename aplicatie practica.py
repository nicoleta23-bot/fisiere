f = open('c:/Users/Statie-13-C100/Desktop/note_stud.txt', 'r')
while True:
    linie = f.readline()
    if len(linie)==0:
        break
    print(linie, end='')
f.close()