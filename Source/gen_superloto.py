#Generator for Super Loto
#------------------
#1 	3	11
#2	9	20
#3	16	28
#4	23	36
#5	32	44
#6	42	50
#------------------
# summ	132	183
#------------------

import sys
import os
import random

loto = [0, 0, 0, 0, 0, 0]

#limits = [[3,11], [9,20], [16,28], [23,36], [32,44], [42,50]]
limits = [[2,11], [9,24], [16,29], [25,37], [31,44], [39,50]]
#limits = [[1,52], [1,52], [1,52], [1,52], [1,52], [1,52]]
summ_min = 132
summ_max = 183
#summ_min = 1
#summ_max = 300

#----------------------------------------------------------------
def GenLoto(loto):
    loto[0] = random.randint(limits[0][0], limits[0][1])
    for i in range(1, 6):
        N = loto[i-1]
        while (N == loto[i-1]):
            N = random.randint(limits[i][0], limits[i][1])
            loto[i] = N    
    pass
#----------------------------------------------------------------
def GenLoto2(loto):
    #lucky_list = [42, 5, 15, 13, 30, 33, 50, 17, 21, 48, 52, 18, 34, 29, 51, 14, 19, 23, 3, 35, 44, 4, 10, 16, 36, 26]
    lucky_list = [42, 5, 15, 13, 30, 33, 50, 17, 21, 48, 52, 18, 34, 29, 51, 14, 19, 23, 3, 35, 44, 4]
    random.shuffle(lucky_list)
    for i in range(0, 6):
        loto[i] = lucky_list[i]
    pass
#----------------------------------------------------------------

def GenTicket(loto):
    random.seed()
    summ = 0
    while ((summ<summ_min)or(summ>summ_max)):
        GenLoto(loto)
        #GenLoto2(loto)
        
        # Check if summ of all balls in need wide
        summ = sum((int(loto[i]) for i in range(0, int(len(loto)))))
        for i in loto:
            if loto.count(i)!=1:
                summ = 0
        
        # Check if we have at one 2 numbers One-by-One
        Found = False
        for i in range(1, 6):
            if (loto[i]-loto[i-1])==1:
                Found = True
        if Found==False:
            summ = 0
                
        pass
    return summ


# Code for Generating lottery
summ = GenTicket(loto)
print (loto)
print (summ)

