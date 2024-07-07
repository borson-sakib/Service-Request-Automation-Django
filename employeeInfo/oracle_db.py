import cx_Oracle
import pyodbc
from django.conf import settings

query = 'SELECT PYOFMAIL,PYAMOUNT, PYEMPFLN, PYEMPCDE, PYEMPNAM, PRESENT_DESIGNATION, PYHEADER, PYEMPSEX, PYEMPDOB, PYACCTNO, TIN, NID, PHONE_NUMBER, DISTICT, PYBLDGRP, RELIGION, PYRLGCDE, DUTY_DESK, DUTY_DESK_CODE, PYDEPCDE, PYJOINDT, DIVISION_CODE, PYDEPNAM, JOINING_DESIGNATION, SUB_DIVISION, LAST_PROMOTION_DATE, LAST_INCREMENT_DATE, LAST_TRANSFER_DATE, BASIC_SALARY, PYOFMAIL, FATHRNAM, MOTHRNAM, PYSPSNAM, EMP_STATUS, LAST_BRANCH FROM ORBHRM.V_EMP_DUTY_DSK_DTL WHERE PYEMPCDE='
# query = 'SELECT PYOFMAIL, PYEMPCDE, PYEMPNAM, PRESENT_DESIGNATION, PYHEADER, PHONE_NUMBER, DUTY_DESK, DUTY_DESK_CODE, PYDEPNAM, SUB_DIVISION, PYOFMAIL, EMP_STATUS, LAST_BRANCH,PYEMPDOB FROM ORBHRM.V_EMP_DUTY_DSK_DTL WHERE PYEMPCDE='
def check_oracle_connection(empid):

    try:
        # Attempt to establish connection to the Oracle database
        final_query = query+str(empid)
        credentials = settings.ORACLECRED
        connection = cx_Oracle.connect(credentials)
        print("Oracle connection established successfully.")
        oracle_cursor = connection.cursor()
        oracle_cursor.execute(final_query)
        oracle_data = oracle_cursor.fetchall()
        
        connection.close()  # Close the connection after checking
        
        return oracle_data
    except cx_Oracle.Error as error:
        print(f"Error connecting to Oracle: {error}")
        return False