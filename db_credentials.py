from variables import datawarehouse_name

# sql-server (target db, datawarehouse)
datawarehouse_db_config = {
  'Trusted_Connection': 'yes',
  'driver': '{SQL Server}',
  'server': 'AlishaDsouza',
  'database': '{}'.format(datawarehouse_name),
  'user': 'sa',
  'password': 'Wilma2024@',
  'autocommit': True,
}

sqlserver_db_config = {
  'Trusted_Connection': 'yes',
  'driver': '{SQL Server}',
  'server': 'AlishaDsouza',
  'database': '{}'.format(datawarehouse_name),
  'user': 'sa',
  'password': 'Wilma2024@',
  'autocommit': True,
}

# mysql
mysql_db_config = [
  {
    'user': 'root',
    'password': 'Wilma2024@',
    'host': 'localhost',
    'database': 'ORG',
  }
]
