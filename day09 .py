#LINK: https://www.hackerrank.com/challenges/py-if-else/problem
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n<=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")
#LINK: https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

year = int(input())
