# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:23:33 2020

@author: Tyler-Razer
"""

import pandas as pd
import seaborn as sns
import numpy as np
import os
import math


"""QA)"""
def QA():
    loop = True
    while(loop):
        try:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            c = int(input('Enter c: '))
            loop = False
        except:
            print('Invalid input, try again')
    
    try:
        ans1 = ((b - 2 * b) + (math.sqrt(b * b - 4 * a * c)))/2 * a
        ans2 = ((b - 2 * b) - (math.sqrt(b * b - 4 * a * c)))/2 * a
        if ans1 == ans2:
            print('The solution of {}, {}, {} is {}'.format(a,b,c,ans1))
        else:
            print('First solution of {}, {}, {} is {}'.format(a,b,c,ans1))
            print('Second solution of {}, {}, {} is {}'.format(a,b,c,ans2))
    except:
        print('{}, {}, {} does not have any real solutions'.format(a,b,c))

"""QB)"""
def QB():

    loop = True
    while(loop):
      mydir = input('Enter an absolute path to a file directory:\n')
      
      if os.path.isdir(mydir):
          mylist = os.listdir(mydir)
          for i in mylist:
              if os.path.isfile(i):
                  print(i)
          loop = False
      else:
         print('That is not a valid directory, please try again.')
         continue 

"""QB1"""
def QC():
    loop = True
    while(loop):
      mydir = input('Enter an absolute path to a file directory:\n')
      
      if os.path.isdir(mydir):
          mylist = os.listdir(mydir)
          for i in mylist:
              if os.path.isdir(i):
                  print(i)
          loop = False
      else:
         print('That is not a valid directory, please try again.')
         continue       
            
        
"""main"""
##QA()
##QB()
QC()