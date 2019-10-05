import mysql.connector as mariadb

## MariaDB connector
## Database is currently hosted locally on 127.0.0.1, to run this code one should download mariaDB locally,
## change the credentials as below, and create a database called candidates.

db = mariadb.connect(user='root', password='liwwa123', database='candidates')
