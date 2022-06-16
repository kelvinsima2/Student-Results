import pandas as pd
import numpy as np
import sqlite3



    

def df_create(researchid, conn):
    """ Creates data frames from SQL tables:
         researchid = StudentID (int)
         conn = database connection. """
    grades1 =  pd.read_sql('''SELECT Grade FROM test1
    WHERE researchid == ''' + str(researchid),conn)
    grades2 =  pd.read_sql('''SELECT Grade FROM test2 WHERE
    researchid == ''' + str(researchid),conn)
    grades3 =  pd.read_sql('''SELECT Grade FROM test3 WHERE
    researchid == ''' + str(researchid),conn)
    grades4 =  pd.read_sql('''SELECT Grade FROM test4 WHERE
    researchid == ''' + str(researchid),conn)
    grades_mock =  pd.read_sql('''SELECT Grade FROM MockTest WHERE
    researchid == ''' + str(researchid),conn)
    grades_sum =  pd.read_sql('''SELECT Grade FROM SumTest WHERE
    researchid == ''' + str(researchid),conn)
    grades_all = pd.concat([grades1, grades2, grades3, grades4,
                            grades_mock, grades_sum])

    return [grades1, grades2, grades3, grades4, grades_mock, grades_sum,
            grades_all]


def test_id(conn):
    """ Creates a list of students who have taken a particular test:
        conn = connection to the database. """
    test_1_id = pd.read_sql('''SELECT researchid FROM
    test1''',conn)['researchid'].tolist()
    test_2_id = pd.read_sql('''SELECT researchid FROM
    test2''',conn)['researchid'].tolist()
    test_3_id = pd.read_sql('''SELECT researchid FROM
    test3''',conn)['researchid'].tolist()
    test_4_id = pd.read_sql('''SELECT researchid FROM
    test4''',conn)['researchid'].tolist()
    test_mock_id = pd.read_sql('''SELECT researchid FROM
    MockTest''',conn)['researchid'].tolist()
    test_sum_id = pd.read_sql('''SELECT researchid FROM
    SumTest''',conn)['researchid'].tolist()

    return [test_1_id, test_2_id, test_3_id, test_4_id, test_mock_id,
            test_sum_id]
    

