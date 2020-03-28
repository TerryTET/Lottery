import sys
import os
import random
from gen_superloto import GenLoto
from gen_superloto import GenTicket

loto = [0, 0, 0, 0, 0, 0]
testset = []

#============================================================================================
def LoadTestSet(fname):
    test_file=open(fname, "r", encoding="latin-1", errors='ignore')
    try:
        s = test_file.readline()
        while len(s)>12:
            s = s.replace("\n", "")
            s = s.replace("\r", "")
            blocks = s.split(";")
            if len(blocks)==7:
                testset.append([int(blocks[1]),int(blocks[2]),int(blocks[3]),int(blocks[4]),int(blocks[5]),int(blocks[6])])

            s = test_file.readline()
    finally:
        test_file.close()
#============================================================================================
def SearchLotoInSet(loto, testset):
    cnt3 = 0
    cnt4 = 0
    cnt5 = 0
    cnt6 = 0
    for i in testset:
        cnt = 0
        for j in loto:
            if (i.count(j)==1):
                cnt = cnt + 1
        if cnt == 3:
            cnt3 = cnt3 + 1
        if cnt == 4:
            cnt4 = cnt4 + 1
        if cnt == 5:
            cnt5 = cnt5 + 1
        if cnt == 6:
            cnt6 = cnt6 + 1
        cnt = 0;        
        pass
    
    
    return cnt3, cnt4, cnt5, cnt6
#============================================================================================
def SearchLotoInLast10(loto, testset):
    cnt3 = 0
    cnt4 = 0
    cnt5 = 0
    cnt6 = 0
    for i in range(len(testset)-10, len(testset)):
        cnt = 0
        for j in loto:
            if (testset[i].count(j)==1):
                cnt = cnt + 1
        if cnt == 3:
            cnt3 = cnt3 + 1
        if cnt == 4:
            cnt4 = cnt4 + 1
        if cnt == 5:
            cnt5 = cnt5 + 1
        if cnt == 6:
            cnt6 = cnt6 + 1
        cnt = 0;        
        pass
    
    
    return cnt3, cnt4, cnt5, cnt6
#============================================================================================
def CheckOneByOne(testset):
    cnt = 0;
    cnt2 = 0;
    for i in testset:
        Found = False
        for j in range (1, 6):
            if (i[j]-i[j-1])==1:
                cnt = cnt + 1
                Found = True
        if Found:
            cnt2 = cnt2 + 1
    return cnt, cnt2
#============================================================================================
def CheckOneOverOne(testset):
    cnt = 0;
    cnt2 = 0;
    for i in testset:
        Found = False
        for j in range (1, 6):
            if (i[j]-i[j-1])==2:
                cnt = cnt + 1
                Found = True
        if Found:
            cnt2 = cnt2 + 1
    return cnt, cnt2



#============================================================================================
def TestSystem1(loto, testset):
    f3 = 0
    f4 = 0
    f5 = 0
    f6 = 0
    for k in range(1, 10000):
        GenTicket(loto)
        #fres3, fres4, fres5, fres6 = SearchLotoInSet(loto, testset)
        fres3, fres4, fres5, fres6 = SearchLotoInLast10(loto, testset)
        f3 = f3 + fres3
        f4 = f4 + fres4
        f5 = f5 + fres5
        f6 = f6 + fres6
        print (loto, "\t", fres3, "\t", fres4, "\t", fres5, "\t", fres6)
        
    print("3 balls = ", f3)
    print("4 balls = ", f4)
    print("5 balls = ", f5)
    print("6 balls = ", f6)
    pass
#============================================================================================
def VirtualGame(loto, testset):
    i = random.randint(len(testset)-20, len(testset)-1)
    
    for k in range(0, 10):
        cnt = 0
        GenTicket(loto)
        for j in range(0, 6):
            if testset[i].count(loto[j])==1:
                cnt = cnt + 1
        
        print(loto,"\tGame ",i," - ",testset[i],"\tResult = ",cnt)
    pass
#============================================================================================
    



LoadTestSet("../TestSet/testset.csv")

TestSystem1(loto, testset)

#print(len(testset))
#print(CheckOneByOne(testset))
#print(CheckOneOverOne(testset))

#VirtualGame(loto, testset)