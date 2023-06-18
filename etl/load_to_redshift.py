import os
from sql.create import Staging
import redshift_connector
from configparser import ConfigParser

# read environment variables
config = ConfigParser()
config.read('.env')

DWH_HOST = config['WAREHOUSE_STAGING']['HOST']
DWH_DB = config['WAREHOUSE_STAGING']['STAGING']
DWH_USERNAME = config['WAREHOUSE_STAGING']['USERNAME']
DWH_PASSWORD = config['WAREHOUSE_STAGING']['PASSWORD']
DWH_SCHEMA = config['WAREHOUSE_STAGING']['SCHEMA']

# tables
STORAGE_TRANSACTIONS = config['WAREHOUSE_TABLES']['STORAGE_TRANSACTIONS']
CUSTOMERS = config['WAREHOUSE_TABLES']['CUSTOMERS']
DATES = config['WAREHOUSE_TABLES']['DATES']
ACTIONS = config['WAREHOUSE_TABLES']['ACTIONS']
STORAGES = config['WAREHOUSE_TABLES']['STORAGES']



def connect_to_redshift():
    conn = redshift_connector.connect(
         host = DWH_HOST
        , database=DWH_DB
        , user=DWH_USERNAME
        , password=DWH_PASSWORD
    )

    print("connected to DWH")
    return conn


def create_dev_tables():
    connection = connect_to_redshift()
    cursor = connection.cursor()
    cursor.execute(Staging.address)
    cursor.execute(Staging.customers)
    cursor.execute(Staging.storages)
    cursor.execute(Staging.transactions)
    connection.commit()
    print("done")
    cursor.close()
    connection.close()


def load_to_redshift():
    conn = connect_to_redshift()
    cursor = conn.cursor()
    cursor.execute(f"""
        COPY {DWH_DB}.{DWH_SCHEMA}.addresses (id, city, postal_code, country, country_code, state) 
        FROM 's3://tenalytics-internship-bucket/reno_storage/cleaned/addresses.csv' 
        IAM_ROLE 'arn:aws:iam::837511535567:role/service-role/AmazonRedshift-CommandsAccessRole-20230618T085945' 
        FORMAT AS CSV 
        DELIMITER ',' 
        QUOTE '"' 
        IGNOREHEADER 1 
        REGION AS 'us-east-1'
    """)
    # cursor.execute("""
    #     COPY customers FROM 's3://tenalytics-internship-bucket/reno_storage/cleaned/customers.csv'
    #     iam_role 'arn:aws:iam::706864904003:user/songstreams_s3'
    # """)
    conn.commit()
    cursor.close()
    conn.close()