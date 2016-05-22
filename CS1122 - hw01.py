import time
import random

'''
programmer: Yohann Abittan
netid:yaa243
filename: hw01.py
Aim: Testing out three different algorithms
'''
def insertionSort(firstList):
   for index in range(1,len(firstList)):

     currentvalue = firstList[index]
     position = index

     while position>0 and firstList[position-1]>currentvalue:
         firstList[position]=firstList[position-1]
         position = position-1

     firstList[position]=currentvalue

def quickSort(firstList):
   quickSortHelper(firstList,0,len(firstList)-1)

def quickSortHelper(firstList,first,last):
   if first<last:

       splitpoint = partition(firstList,first,last)

       quickSortHelper(firstList,first,splitpoint-1)
       quickSortHelper(firstList,splitpoint+1,last)


def partition(firstList,first,last):
   pivotvalue = firstList[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and firstList[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while firstList[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = firstList[leftmark]
           firstList[leftmark] = firstList[rightmark]
           firstList[rightmark] = temp

   temp = firstList[first]
   firstList[first] = firstList[rightmark]
   firstList[rightmark] = temp


   return rightmark

def selectionSort(firstList):
   for fillslot in range(len(firstList)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if firstList[location]>firstList[positionOfMax]:
               positionOfMax = location

       temp = firstList[fillslot]
       firstList[fillslot] = firstList[positionOfMax]
       firstList[positionOfMax] = temp

def main():
	t0 = time.time()
	firstList = range(1,1000,1)
	random.shuffle(firstList)
	insertionSort(firstList)
	print(firstList)
	t1 = time.time()
	firstTotal = t1-t0

	print(firstTotal)

	t2 = time.time()
 	secondList = range(1,1000,1)
 	random.shuffle(secondList)
 	quickSort(secondList)
 	print(secondList)
 	t3 = time.time()
 	secondTotal = t3-t2

 	print(secondTotal)

	t4 = time.time()
	thirdList = range(1,1000,1)
	random.shuffle(thirdList)
	selectionSort(thirdList)
	print(thirdList)
	t5 = time.time()
	thirdTotal = t5-t4

	print(thirdTotal)


if __name__ == "__main__":
    main()