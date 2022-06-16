import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
from DAFunction import test_id
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from tkinter import *

def display_result(researchid):
    """Plots formative and summative test results of a student:
        researchid = Student ID number (int). """

    conn = sqlite3.connect('DataFiles/ResultDatabase.db')

    df_test1=pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6
    FROM test1 WHERE researchid == ''' + str(researchid),conn)
    df_test2=pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6
    FROM test2 WHERE researchid == ''' + str(researchid) ,conn)
    df_test3=pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6
    FROM test3 WHERE researchid == ''' + str(researchid),conn)
    df_test4=pd.read_sql('''SELECT Grade, Q1, Q2 FROM test4 WHERE
                         researchid == ''' + str(researchid),conn)
    df_MockTest=pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5,
    Q6, Q7, Q8, Q9, Q10 FROM MockTest WHERE
    researchid == ''' + str(researchid),conn)
    df_SumTest=pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6, Q7,
    Q8, Q9, Q10, Q11, Q12, Q13 FROM SumTest
    WHERE researchid == ''' + str(researchid),conn)

    [test_1_id, test_2_id, test_3_id, test_4_id,
     test_mock_id, test_sum_id] = test_id(conn)

    conn.close()
    # Student ID validation
    print('Student ID number ' + str(researchid) + ' results')
    print("test1:")
    if researchid in test_1_id:
        print(df_test1.iloc[0].to_dict())
    else:
        print("Student ID not found in test1 database")
        df_test1 = pd.DataFrame(np.zeros((1, 6)))
    print("test2:")
    if researchid in test_2_id:
        print(df_test2.iloc[0].to_dict())
    else:
        print("Student ID not found in test2 database")
        df_test2 = pd.DataFrame(np.zeros((1, 6)))
    print("test3:")
    if researchid in test_3_id:
        print(df_test3.iloc[0].to_dict())
    else:
        print("Student ID not found in test3 database")
        df_test3 = pd.DataFrame(np.zeros((1, 6)))
    print("test4:")
    if researchid in test_4_id:
        print(df_test4.iloc[0].to_dict())
    else:
        print("Student ID not found in test4 database")
        df_test4 = pd.DataFrame(np.zeros((1, 3)))
    print("Mock Test:")
    if researchid in test_mock_id:
        print(df_MockTest.iloc[0].to_dict())
    else:
        print("Student ID not found in MockTest database")
        df_MockTest = pd.DataFrame(np.zeros((1, 10)))
    print("Sum Test:")
    if researchid in test_sum_id:
        print(df_SumTest.iloc[0].to_dict())
    else:
        print("Student ID not found in SumTest database")
        df_MockTest = pd.DataFrame(np.zeros((1, 13)))

        
    # Visualization
    fig, axes = plt.subplots(nrows=3, ncols=2)
    df_test1.iloc[0].plot(kind='bar', ax=axes[0,0],
                          title = 'test1', ylabel = 'Percentage', fontsize = 7)
    df_test2.iloc[0].plot(kind='bar', ax=axes[0,1],
                          title = 'test2', fontsize = 7)
    df_test3.iloc[0].plot(kind='bar', ax=axes[1,0],
                          title = 'test3', ylabel = 'Percentage', fontsize = 7)
    df_test4.iloc[0].plot(kind='bar', ax=axes[1,1],
                          title = 'test4', fontsize = 7)
    df_MockTest.iloc[0].plot(kind='bar', ax=axes[2,0],
                             title = 'MockTest', ylabel = 'Percentage', fontsize = 7)
    df_SumTest.iloc[0].plot(kind='bar', ax=axes[2,1],
                            title = 'SumTest', fontsize = 7)
    fig.suptitle('Student ID number ' + str(researchid) + ' results')


    window = Tk()
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
    canvas.get_tk_widget().pack()


    



