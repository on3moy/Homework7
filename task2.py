"""
The “scores.csv” is a csv file exported from an Excel file. It has the scores for each student in three courses. It has the following content:

,Adrian Alice,Alexis Bruce,Braxton Conley,Bruce Lee,Cindy Kim
IS101,87,100,94,100,83
IS102,96,87,77,81,65
IS103,70,90,90,82,85

Use the DataFrame of Python’s pandas package to calculate and print the required output.

1)	calculate the grade for each student according to the following rules:

>= 90 A
>= 80 B
>= 70 C
>= 60 D
<60    F

2)	calculate the class GPA with two decimal places according to the following rule:

A 4.00
B 3.00
C 2.00
D 1.00
F 0.00

3)	Print the GPA for each student and the whole class:

Adrian Alice 3.21
Alexis Bruce 2.74
Braxton Conley 2.32
…

The class GPA is 2.62
"""

import pandas as pd 
import numpy as np 

FILE_NAME = 'scores.csv'
DF_SCORES = pd.read_csv(FILE_NAME, header=0, index_col=0)

def get_grade(score):
    """Returns the letter grade corresponding to score"""
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter

def get_gpa(score):
    """Returns the number point corresponding to score"""
    if score >= 90:
        gpa = 4.0
    elif score >= 80:
        gpa = 3.0
    elif score >= 70:
        gpa = 2.0
    elif score >= 60:
        gpa = 1.0
    else:
        gpa = 0
    return gpa

def gpa_df(df):
    """Returns a new DF with GPA values only"""
    DF_COLUMNS = df.columns
    for column in DF_COLUMNS:
        df[column] = df[column].apply(get_gpa)
    return df

MEANS = DF_SCORES.mean()
GRADES = MEANS.apply(get_grade)
GPA_SCORES = gpa_df(DF_SCORES)
STUDENT_GPA = round(GPA_SCORES.mean(),2)
CLASS_GPA = round(GPA_SCORES.mean().mean(),2)

print('The Grades for each student are:')
print(GRADES,'\n')
print('The GPAs for each student are:')
print(STUDENT_GPA)
print('\nThe Class GPA is:')
print(CLASS_GPA)