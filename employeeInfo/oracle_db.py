import cx_Oracle
import pyodbc
from django.conf import settings


# def check_oracle_connection():
#     try:
#         # Attempt to establish connection to the Oracle database
#         credentials = settings.ORACLECRED
#         connection = cx_Oracle.connect(credentials)
#         print("Oracle connection established successfully.")
#         oracle_cursor = connection.cursor()
#         oracle_cursor.execute('SELECT PYOFMAIL,PYAMOUNT, PYEMPFLN, PYEMPCDE FROM ORBHRM.V_EMP_DUTY_DSK_DTL')
#         oracle_data = oracle_cursor.fetchall()
#         for entry in oracle_data:
#             print(entry)
#         oracle_cursor.close()
#         connection.close()  # Close the connection after checking
        
#         # print(oracle_data)
#         return oracle_data
#     except cx_Oracle.Error as error:
#         print(f"Error connecting to Oracle: {error}")
#         return False