import mysql.connector
import sshtunnel
from mysql.connector import Error

with sshtunnel.SSHTunnelForwarder(
        ('10.75.49.60', 22),
        ssh_username='SHNN',
        ssh_password='HTb#1n@78dw',
        remote_bind_address=('10.75.49.60', 3306),
        #local_bind_address=(_local_bind_address, _local_mysql_port)
) as tunnel:
    connection = mysql.connector.connect(
        user='root',
        password='root',
        host='172.20.0.2',
        database='onlinebanking',
        port=3306)

try:

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM onlinebanking.appointment;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")