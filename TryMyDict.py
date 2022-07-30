from AdvancedDict import AdvacedDict
import random
def main():
    lis = []
    dicttims = {}
    for i in range(0, 10):
        lis.append(random.randint(1, 10))
    print("original values",lis)
    for i in lis:
        tims = lis.count(i)
        keyy = lis.index(i)
        dicttims[keyy] = tims
    print("(key/number)/times",dicttims)

    maxvalue = max(dicttims.values())

    mydict=AdvacedDict()            #create object
    mydict.InviteDict(dicttims)     #use method with dict
    keyys=mydict.GetAllKeys()       #get keys
    keynumber=mydict.GetKeyForDigit(keyys,maxvalue) #get key

    if mydict.KeyAndDigit(keynumber)==maxvalue:
        print(lis[keynumber],"повторяется",maxvalue,"раз/раза")

if __name__ == '__main__':
    main()










