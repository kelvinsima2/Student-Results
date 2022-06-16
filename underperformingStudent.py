import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from DAFunction import df_create

def underperforming():

    """Prints out a list of underperforming students and visualizes their
    grades."""

    underperforming = []

    conn = sqlite3.connect('DataFiles/ResultDatabase.db')

    id_list = pd.read_sql('''SELECT researchid FROM
                          SumTest''',conn)['researchid'].tolist()
    for researchid in id_list:
        # This part takes counts how many times a student has scored
        # between 1 and 50 in all tests.
        [grades1, grades2, grades3, grades4, grades_mock,
         grades_sum, grades_all] = df_create(researchid,conn)
        grades_all = pd.concat([grades1, grades2, grades3,
                                grades4, grades_mock, grades_sum])
        grades_all = grades_all.apply(lambda x : True if x['Grade'] >= 1
                                      and x['Grade'] <50 else False, axis = 1)
        num_rows = len(grades_all[grades_all == True].index)
        if num_rows > 2:
            underperforming.append(researchid)
        

    results = []
    for student in underperforming:
        results.append(pd.read_sql('''SELECT Grade FROM
        SumTest WHERE researchid == ''' + str(student),conn)['Grade'][0])


    results = {'researchid' : underperforming, 'Grade' : results}
    results_df = pd.DataFrame.from_dict(results).sort_values('Grade')
    sorted_underperforming = results_df['researchid'].tolist()


    from testResults import display_result
    tests = ['test1', 'test2', 'test3', 'test4', 'Mock Test']

    for student in sorted_underperforming:
        [grades1, grades2, grades3, grades4,
         grades_mock, grades_sum, grades_all] = df_create(student,conn)
        # The next line of code highlists which test
        # the student scored the lowest.
        string = tests[grades_all['Grade'].tolist().index(min(grades_all['Grade']))] + ' is the lowest scored at ' + str(min(grades_all['Grade']))
        display_result(student)
        print("\nFor student number " + str(student) + ", " + string)

    conn.close()


