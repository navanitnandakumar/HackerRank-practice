import math
import os
import random
import re
import sys
n = input()
if(int(n)%2!=0 and int(n)!=0): print("Weird")
elif(int(n)%2==0):
    if(int(n)>=2 and int(n)<=5): print("Not Weird")
    if(int(n)>=6 and int(n)<=20): print("Weird")
    if(int(n)>20): print("Not Weird")
        
#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
#Input Format

#A single line containing a positive integer, .

#Constraints

#Output Format

#Print Weird if the number is weird; otherwise, print Not Weird.

#Sample Input 0

#3
#Sample Output 0

#Weird
#Explanation 0


 #is odd and odd numbers are weird, so we print Weird.

#Sample Input 1

#24
#Sample Output 1

#Not Weird
#Explanation 1


 #and  is even, so it isn't weird. Thus, we print Not Weird.
