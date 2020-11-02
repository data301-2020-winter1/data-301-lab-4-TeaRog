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
import matplotlib.pyplot as plt

"""QA)"""
def getSolution():
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
            print('The solution of ({}, {}, {}) is {}'.format(a,b,c,ans1))
        else:
            print('First solution of ({}, {}, {}) is {}'.format(a,b,c,ans1))
            print('Second solution of ({}, {}, {}) is {}'.format(a,b,c,ans2))
    except:
        print('{}, {}, {} does not have any real solutions'.format(a,b,c))

"""QB)"""
def ListFiles():
    loop = True
    while(loop):
      mydir = input('Enter a path to a file directory: Currently in pwd\n')
      mydir = os.getcwd() + mydir
      if os.path.isdir(mydir):
          mylist = os.listdir(mydir)
          for i in mylist:
              if os.path.isfile(mydir + i):
                  print('{}{}'.format(mydir,i))
          loop = False
      else:
         print('That is not a valid directory, please try again.')
         continue 

"""QB1"""
def ListDirectories():
    loop = True
    while(loop):
      mydir = input('Enter a path to a file directory:\n')
      mydir = os.getcwd() + mydir
      if os.path.isdir(mydir):
          mylist = os.listdir(mydir)
          for i in mylist:
              if os.path.isdir(mydir + i):
                  print('{}{}'.format(mydir,i))
          loop = False
      else:
         print('That is not a valid directory, please try again.')
         continue 
    
"""QB3"""    
def Tree():
    loop = True
    while(loop):
      mydir = input('Enter a path to a file directory:\n')
      mydir = os.getcwd() + mydir
      if os.path.isdir(mydir):
          for root, sub, file in os.walk(mydir):
              print('-' * 30)
              print('Root Directory: {}\nSub Directories: {}\nFiles: {}'.format(root, sub, file))       
          loop = False
          print('-' * 30)
      else:
         print('That is not a valid directory, please try again.')
         continue 

"""QC1"""
def MyVector():
    vector = np.zeros(10, dtype=int)
    print(vector)
    print('\n')
    
"""QC2"""
def MyRandomVector():
    arr = np.random.rand(1,10)
    vector = np.array(arr)
    print(vector)
    print('\nmax: {}, min: {}, sum: {}, mean: {}'.format(np.max(vector),np.min(vector),np.sum(vector),np.mean(vector)))

"""QC4"""
def MyOperationVector():
    arr = np.random.randint(100,size=(15))
    vector = np.array(arr)
    print('\n')
    print(vector)
    print(np.mean(vector))
    print('\n')
   
    indexOfMax = np.argmax(vector)
    indexOfMin = np.argmin(vector)
    
    np.put(vector, indexOfMin, 100)
    np.put(vector, indexOfMax, 0)
    print(vector)
    print(np.mean(vector))
    
"""QD1"""
def LoadData():
    df = pd.read_csv("http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv")
    print(df)
    return df
"""QD2"""
def CountCaseBySex(df):    
    sns.countplot(y="Sex", data=df).set_title("Number of Covid-19 Cases By Sex")
    
"""QD3"""
def CountCaseByAgeGroup(df):    
    sns.countplot(y="Age_Group", data=df, order=['<10','10-19','20-29','40-49','50-59','60-69','70-79','80-89','90+','Unknown']).set_title("Number of Covid-19 Cases By Age Group")
"""QD4"""
def CountByAuthority(df):
    sns.countplot(y="HA", hue="Sex", palette="pastel", data=df).set_title("Number of Covid-19 Cases By Regional Health Authority split by sex")
"""QD5""" 
def DataWrangling(df):
    df["Reported_Date"] = pd.to_datetime(df["Reported_Date"]).dt.date
    df["Reported_Date"] = df["Reported_Date"].astype("datetime64[ns]")
    return df
"""QD6""" 
def DataWranglingII(df):
    print("The earliest reported case of COVID-19 was: ", df["Reported_Date"].min())
    print("The latest reported case of COVID-19 was:", df["Reported_Date"].max())
"""QD7""" 
def DataWranglingIII(df):
    df['days_since'] = df["Reported_Date"] - df["Reported_Date"].min()
    print(df['days_since'].dt.days)
    df['days_since'] = df['days_since'].dt.days
    return df
"""QD8""" 
def DaysSincePlot(df):
    sns.countplot(x="days_since", hue='Sex', data=df)
"""QD9BONUS""" 
def QD8BONUS1(df):
    sns.countplot(x="days_since", hue='Sex', data=df).legend(loc='upper left')
def QD8BONUS2(df):
    sns.countplot(x="days_since", hue='Sex', data=df, order = df['HA'].value_counts().index).legend(loc='upper left')
    

def main():
    print('-A------------------------------------------')
    getSolution()
    print('-B1------------------------------------------')
    ListFiles()
    print('-B2------------------------------------------')
    ListDirectories()
    print('-B3------------------------------------------')
    Tree()
    print('-C1------------------------------------------')
    MyVector()
    print('-C2------------------------------------------')
    MyRandomVector()
    print('-C4------------------------------------------')
    MyOperationVector()
    print('-D1------------------------------------------')
    df = LoadData()
    print('-D2------------------------------------------')
    CountCaseBySex(df)
    print('-D3------------------------------------------')
    CountCaseByAgeGroup(df)
    print('-D4------------------------------------------')
    CountByAuthority(df)
    print('-D5------------------------------------------')
    df2 = DataWrangling(df)
    print('-D6------------------------------------------')
    DataWranglingII(df2)
    print('-D7------------------------------------------')
    df3 = DataWranglingIII(df2)
    print('-D8------------------------------------------')
    DaysSincePlot(df3)
    print('-D8Bonus------------------------------------------')
    QD8BONUS1(df3)
    print('-D8Bonus------------------------------------------')
    QD8BONUS2(df3)   
    print('-------------------------------------------')
    
main()