import sys

#Finds prime numbers which can devide the number we define.
def asal_carpan_bul(n):
    primeMultipliers=[]
    multiplier=2
    while multiplier<=int(n):
        if n%multiplier==0:
            primeMultipliers.append(multiplier)
            n=n/multiplier
        else:
            multiplier+=1
    return primeMultipliers

#Makes a number list which contains the numbers untill the number we define. (contains 1).
def tilNumber(n):
    numbers=[]
    for num in range(1,n):
        numbers.append(num)
    
    return numbers

#It compares the 2 lists about whether the prime numbers we found can devide the numbers in the list of numbers. İf it is true, function removes the number from list.
def testMethod(primes,numList):
    for sayi in primes:
        for sayi2 in numList:
            if sayi2%sayi==0:
                numList.remove(sayi2)
    return numList




get_num=int(sys.argv[1])
asal_carpan_listesi=asal_carpan_bul(get_num)
num_list=tilNumber(get_num)



sonuc=testMethod(asal_carpan_listesi,num_list)



print(len(sonuc))