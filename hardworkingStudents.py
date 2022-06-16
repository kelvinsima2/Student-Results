import pandas as pd
import numpy as np
import sqlite3
from DAFunction import df_create

def hardworking():
    """ Prints a list of hardworking students and their rates."""
    # First clean StudentRate file
    df_StudentRate = pd.read_csv("DataFiles/StudentRate.csv")
    df_CleanStudentRate = df_StudentRate.copy()
    df_CleanStudentRate.columns = ['researchid', 'what_is_true',
                                   'experienced_languages',
                                   'programming_level', 
                               'like_programming', 'sci-fi',
                                   'learning_programming', 'language_known']
    df_CleanStudentRate = df_CleanStudentRate.replace(np.nan, 0)

    print(df_CleanStudentRate.head())

    below_beginner=df_CleanStudentRate[df_CleanStudentRate['programming_level'] == 'Below beginner']
    beginner = df_CleanStudentRate[df_CleanStudentRate['programming_level']
                                   == 'Beginner']
    beginner_list = list(beginner['researchid'])
    below_beginner_list = list(below_beginner['researchid'])

    beginner_and_below = list(set(beginner_list + below_beginner_list))
    print(beginner_and_below)

    conn = sqlite3.connect('DataFiles/ResultDatabase.db')

    hardworking = []
    for researchid in beginner_and_below:
        grades_sum =  pd.read_sql('''SELECT Grade FROM SumTest WHERE
        researchid == ''' + str(researchid),conn)
        # Select hardworking students to be above 60 in summative test.
        grades_sum = grades_sum.apply(lambda x : True if
                                      x['Grade'] > 60 else False,
                                      axis = 1)
        num_rows = len(grades_sum[grades_sum == True].index)

        if num_rows == 1:
            hardworking.append(researchid)



    print(hardworking)

    hardworking_grades = []

    for student in hardworking:
        hardworking_grades.append(float(pd.read_sql('''SELECT Grade
        FROM SumTest WHERE researchid ==
        ''' + str(student),conn)['Grade'].values))



    print(hardworking_grades)

    df_CleanStudentRate_hardworking=df_CleanStudentRate[df_CleanStudentRate['researchid'].isin(hardworking)]
    df_CleanStudentRate_hardworking['Grade'] = hardworking_grades
    sorted_rates_df=df_CleanStudentRate_hardworking.sort_values('Grade',
                                                        ascending = False)

    for ind in sorted_rates_df.index:
        print("\nStudent ID: " +str(sorted_rates_df['researchid'][ind])
              + " Summative Grade: " +str(sorted_rates_df['Grade'][ind])
              + " Programming Education: " +str(sorted_rates_df['what_is_true'][ind])
              + " Known Languages: " +str(sorted_rates_df['experienced_languages'][ind])
              + " Programming Level: " +str(sorted_rates_df['programming_level'][ind])
              + " Like programming?: " +str(sorted_rates_df['like_programming'][ind])
              + " Sci-Fi Movies: " +  str(sorted_rates_df['sci-fi'][ind])
              + " Learning Programming: "+str(sorted_rates_df['learning_programming'][ind])
              + " Languages known: "+str(sorted_rates_df['language_known'][ind])
              )
    

    conn.close()
