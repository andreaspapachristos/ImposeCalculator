# from itertools import chain

import csv
import numpy as np


def createCsv():
    with open("/home/master/diastaseis.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        for i in range(100, 250, 5):
            for z in range(100, 350, 5):
                data = [i, z]
                writer.writerows([data])


def fixPaper(width, height):
    list = []
    for i in range(0, 5):
        if width > height:
            width /= 2
        else:
            height /= 2
        list.append([width, height])
    return (list)


def matchPage(width, height):
    width *= 2
    list = fixPaper(1000, 700)
    for i in list:
        temp = []
        if width / i[0] < 1 or width / i[1] < 1:
            if width / i[0] > width / i[1]:
                if width / i[0] > 1:
                    temp.append([i[1], i[0]])
                else:
                    temp.append([i[0], i[1]])
            # i[1] = height/i[1]
            elif width / i[0] < width / i[1]:
                if width / i[1] > 1:
                    temp.append([i[0], i[1]])
                else:
                    temp.append([i[0], i[1]])
            # i[1] = height/i[0]

        print(temp)


def find4up(diaireteos, dieretis):
    an = (12, 9, 8, 6, 4, 3, 2)

    for i in an:
        if (diaireteos // dieretis) >= i:
            return i
    return 0


""" def dokimi():
    if ppw/pw > 0 and pph/ph > 0 :
            if ppw/pw > pph/ph:
                t = ph
                ph = pw
                pw = t
            v = pw
            z = 0
            for i in range(0,9):                            
                if(v < ppw): 
                    v += pw
                    z += 1
                elif(v > ppw): break
            print(z)
            v = ph
            z = 0 
            for i in range(0,7):
                if(v < pph): 
                    v += ph
                    z += 1
                elif(v > pph): break                    
            print(z)

        elif ppw/pw > 0 and pph/ph < 0:
            if ppw/ph > 0 :
                v = ph
                z = 0
            for i in range(0,8):                            
                if(v < ppw):
                    v += ph
                    z += 1 
 """


def matchMontaz(**kwargs):
    ph = kwargs.get('pageHeight') + 6
    pph = kwargs.get('paperHeight')
    temp = []
    if kwargs.get('monofyllo', True):
        pw = kwargs.get('pagewidth') + 6
        ppw = kwargs.get('paperWidth')
        temp.append([ppw // pw, pph // ph])
        temp.append([ppw // ph, pph // pw])
        print(temp)
        return (temp)
    else:
        pw = (kwargs.get('pagewidth') * 2) + 6
        ppw = kwargs.get('paperWidth')  # /2
        temp.append([ppw // pw, find4up(pph, ph)])  # pph//ph]
        temp.append([find4up(ppw, ph), pph // pw])  # ppw//ph
        print(temp)
        return (temp)


def betterUse(papers, page, monofyllo):
    embadonp = page[0] * page[1]
    for p in papers:
        m = matchMontaz(pagewidth=page[0], pageHeight=page[1], paperWidth=p[0], paperHeight=p[1], monofyllo=False)
        embadon = (p[0] * p[1])
        print(p)
        for p in m:
            if (monofyllo):
                y = (p[0] * p[1]) * embadonp
            else:
                y= (p[0] * p[1]) * embadonp *2 
            print(format(y/embadon, '.2f'))
 
def getScheme(pages):
    dekaksi = pages//4
    n = dekaksi%4
    if (n):
        okto = n//2
        tessera = n%2

if __name__ == '__main__':
    #print(find4up(880, 80))
    #matchMontaz(pagewidth=210, pageHeight=280, paperWidth=860, paperHeight=610, monofyllo=False)
    betterUse([[610,860],[640,880],[700,1000]], [320,490], False)


