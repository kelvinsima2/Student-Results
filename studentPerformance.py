import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from DAFunction import test_id

def student_performance(chosen_test, researchid):
    """Finds absolute and relative performance of a student and plots them both:
       chosen_test = test to be displayed (str)
       researchid = student ID number (int). """

    conn = sqlite3.connect('DataFiles/ResultDatabase.db')

    # The next lines of code saves data in dataframes after validating
    # student ID.
    [test_1_id, test_2_id, test_3_id, test_4_id, test_mock_id,
     test_sum_id] = test_id(conn)
    
    if (chosen_test == 'test1' and researchid in test_1_id) or (chosen_test ==
                                                                'test2'
        and researchid in test_2_id) or (chosen_test == 'test3' and
                                         researchid in test_3_id):
        df_test=pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6
        FROM ''' + chosen_test,conn)
        student_test = pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6
        FROM ''' + chosen_test + ' WHERE researchid == ' + str(researchid),conn)
    elif chosen_test == 'test4' and researchid in test_4_id:
        df_test=pd.read_sql('SELECT Grade, Q1, Q2 FROM ' + chosen_test,conn)
        student_test = pd.read_sql('''SELECT Grade, Q1, Q2 FROM
        ''' + chosen_test + ' WHERE researchid == ' + str(researchid),conn)
    elif chosen_test == 'MockTest' and researchid in test_mock_id:
        df_test=pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9,
        Q10 FROM ''' + chosen_test,conn)
        student_test = pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6, Q7,
        Q8, Q9, Q10 FROM ''' + chosen_test + ''' WHERE researchid
        == ''' + str(researchid),conn)
    elif chosen_test == 'SumTest' and researchid in test_sum_id:
        df_test=pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9,
        Q10, Q11, Q12, Q13 FROM ''' + chosen_test,conn)
        student_test = pd.read_sql('''SELECT Grade, Q1, Q2, Q3, Q4, Q5, Q6, Q7,
        Q8, Q9, Q10, Q11, Q12, Q13 FROM ''' + chosen_test + ''' WHERE
        researchid == ''' + str(researchid),conn)
    else:
        print("Student ID not found in the test. Try again.")
        
        
    
    
    


    conn.close()
    # Calculate relative performance from absolute oerformance
    mean_df = df_test.mean()
    print("Absolute performance: ")
    print(student_test)
    difference = student_test - mean_df
    print("Relative performance: ")
    print(difference)

    # Plot figure
    labels = []
    for i in range(1, student_test.columns.str.startswith("Q").sum()+1):
        labels.append("Q" + str(i))

    labels = ['Grade'] + labels

    x = np.arange(0,student_test.columns.str.startswith("Q").sum()+1,1)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    student_test.iloc[0].plot(kind = 'bar',ax=ax1, title = '''Absolute
                              Performance''', ylabel = 'Percentage', fontsize = 7)
    difference.iloc[0].plot(kind = 'bar',ax=ax2, title = '''Relative
    Performance''', ylabel = 'Percentage difference', fontsize = 7)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, rotation=90)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, rotation=90)
    fig.suptitle('Student ID number ' + str(researchid) + ' Performance')
    plt.show()
