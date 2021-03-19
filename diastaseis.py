# from itertools import chain
'''''
Copyright [2021] [Andreas Papachristos]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''''

def find4up(diaireteos, dieretis):
    an = (12, 9, 8, 6, 4, 3, 2)

    for i in an:
        if (diaireteos // dieretis) >= i:
            return i
    return 0



def matchMontaz(**kwargs):
    if 'bleed' in kwargs:
        bleed = kwargs.get('bleed') *2
    else: bleed = 6
    ph = kwargs.get('pageHeight') + bleed #kwargs.get('bleed') *2
    #else: ph = kwargs.get('pageHeight') + 6
    if 'gap' in kwargs:
        gap = kwargs.get('gap')
    else:
        gap = 10
    if kwargs.get('paperHeight') < kwargs.get('paperWidth'):

        pph = kwargs.get('paperHeight') - gap
        #else: pph = kwargs.get('paperHeight') - 10
    else:
        pph = kwargs.get('paperWidth') - gap #kwargs.get('gap')

    temp = []
    if kwargs.get('monofyllo', True):
        pw = kwargs.get('pagewidth') + bleed #kwargs.get('bleed') * 2
        if (kwargs.get('paperHeight') < kwargs.get('paperWidth')):
            ppw = kwargs.get('paperWidth')
        else:
            ppw = kwargs.get('paperHeight')
        #ppw = kwargs.get('paperWidth')
        temp.append([ppw // pw, pph // ph, 0])
        temp.append([ppw // ph, pph // pw, 1])
        #print(temp)
        return (temp)
    else:
        pw = (kwargs.get('pagewidth') * 2) + bleed #kwargs.get('bleed') *2
        #ppw = kwargs.get('paperWidth')  # /2
        if kwargs.get('paperHeight') < kwargs.get('paperWidth'):
            ppw = kwargs.get('paperWidth')
        else:
            ppw = kwargs.get('paperHeight')
        temp.append([ppw // pw, find4up(pph, ph), 0])  # pph//ph]
        temp.append([find4up(ppw, ph), pph // pw, 1])  # ppw//ph
        #print(temp)
        return (temp)


def betterUse(papers, page, monofyllo, bleed, gap):
    embadonp = page[0] * page[1]
    temp = 0
    result = []
    for n in papers:
        m = matchMontaz(pagewidth=page[0], pageHeight=page[1], paperWidth=n[0], paperHeight=n[1], monofyllo=monofyllo, bleed=int(bleed), gap=int(gap))
        embadon = (n[0] * n[1]) #- (gap * n[0])
        #print(p)
        for p in m:
            if monofyllo:
                y = (p[0] * p[1]) * embadonp
                #pages = p[0] * p[1]
            else:
                y = (p[0] * p[1]) * embadonp * 2
            #print(format(y / embadon, '.2f'))
            if float(format(y / embadon, '.4f')) >= float(temp):
                temp = format(y/embadon,'.2f')
                xarti = n[0], n[1]
                grid = p[0], p[1], p[2]
                if(monofyllo):
                    pages = p[0] * p[1]
                else:
                    pages = p[0] * p[1] * 2
    result.append(temp)
    result.append(xarti)
    result.append(pages)
    result.append(grid)
    print(result[0], result[1], result[2], result[3])
    return result


def getScheme(pages):
    dekaksi = pages // 4
    n = dekaksi % 4
    if (n):
        okto = n // 2
        tessera = n % 2
        print(okto, tessera)
    print(dekaksi//4)


