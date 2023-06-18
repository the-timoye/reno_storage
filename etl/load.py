import os
from sql.create import Staging
import redshift_connector
from configparser import ConfigParser

# read environment variables
config = ConfigParser()
config.read('.env')

DWH_HOST = config['WAREHOUSE_STAGING']['HOST']
DWH_DB = config['WAREHOUSE_STAGING']['DATABASE']
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


def create_schema():
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Staging.schema.format(DWH_SCHEMA))
    conn.commit()
    cur.close()
    conn.close()


# create tables
def create_fact():
    print("created fact table")
    pass

def create_actions_dim():
    print("created actions table")
    pass

def create_customers_dim():
    print("created customers table")
    pass

def create_dates_dim():
    print("created dates table")
    pass

def create_storage_dim():
    print("created storage table")
    pass

def create_tables():
    create_fact()
    create_actions_dim()
    create_dates_dim()
    create_customers_dim()
    create_storage_dim()




# insert into tables

def insert_into_fact():
    print("inserted into fact table")
    pass

def insert_into_actions_dim():
    print("inserted into actions table")
    pass

def insert_into_customers_dim():
    print("inserted into customers table")
    pass

def insert_into_dates_dim():
    print("inserted into dates table")
    pass

def insert_into_storage_dim():
    print("inserted into storage table")
    pass

def insert_into_tables():
    insert_into_fact()
    insert_into_actions_dim()
    insert_into_dates_dim()
    insert_into_customers_dim()
    insert_into_storage_dim()




def run_create_jobs():
    try:
        create_schema()
        create_tables()
        insert_into_tables()
    except Exception as e:
        print(e)
