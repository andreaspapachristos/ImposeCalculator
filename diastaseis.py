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
        if width/i[0] < 1 or width/i[1] < 1:            
            if width/i[0] > width/i[1]:
                if width/i[0] > 1:
                    temp.append([i[1], i[0]])
                else: 
                    temp.append([i[0], i[1]])
               # i[1] = height/i[1]
            elif width/i[0] < width/i[1]:
                if width/i[1] > 1:
                    temp.append([i[0], i[1]])
                else:                 
                    temp.append([i[0], i[1]])
               # i[1] = height/i[0]

        print(temp)
def find4up(diaireteos, dieretis):
    an = (2,3,4,6,8,9,12)
    z = -1
    for i in an:
        if (diaireteos//dieretis) >= i:
         z += 1   
        else: break
    return an[z]
       # else: break
    


    
def matchMontaz(**kwargs):
    ph = kwargs.get('pageHeight')   
    pph = kwargs.get('paperHeight')
    temp = []
    if kwargs.get('monofyllo', True):
        pw = kwargs.get('pagewidth')
        ppw = kwargs.get('paperWidth')
        temp.append([ppw//pw, pph//ph])
        temp.append([ppw//ph, pph//pw])
        print(temp)
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

        elif ppw/pw > 0 and pph/ph < 0 :
            if ppw/ph > 0 :
                v = ph
                z = 0
            for i in range(0,8):                            
                if(v < ppw):
                    v += ph
                    z += 1 
                   
    else:            
        pw = kwargs.get('pagewidth') *2 
        ppw = kwargs.get('paperWidth') #/2    
        
       
        temp.append([ppw//pw, find4up(pph, ph)]) #pph//ph]
        temp.append([find4up(ppw, ph), pph//pw]) #ppw//ph

            
        print(temp)
   


if __name__ == '__main__':
    #print(find4up(880, 150))
    matchMontaz(pagewidth=280, pageHeight=150, paperWidth=880, paperHeight=640, monofyllo=False)