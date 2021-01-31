import pandas as pd
import pymysql
import yaml

import sshtunnel
from xlsxwriter import Workbook

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0
hostname = '127.0.0.1'
password = 'root'
command = 'ls'
sql_hostname = '127.0.0.1'
sql_username = 'root'
sql_password = 'root'
sql_port = 3306
username = "root"
localhost = '127.0.0.1'
port = 3306
def query(q):
        connection = pymysql.connect(
            user=sql_username, password=sql_password,
            host='127.0.0.1',
            database='onlinebanking',
        )
        query = q
        data = pd.read_sql_query(query, connection)
        data = pd.DataFrame(data)
        val = data.loc[:,'account_balance']

        print("Value of pd is {}".format(data.loc[:,'account_balance']))

        connection.close()
        return val

#query('SELECT * FROM onlinebanking.savings_transaction;')

