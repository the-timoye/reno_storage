import os
from sql.create import Staging
from sql.insert import Staging as Insert
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
    print("creating fact table")
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Staging.storage_transactions.format(DWH_SCHEMA, STORAGE_TRANSACTIONS))
    conn.commit()
    cur.close()
    conn.close()
    print("created fact table")

def create_actions_dim():
    print("creating actions table")
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Staging.actions.format(DWH_SCHEMA, ACTIONS))
    conn.commit()
    cur.close()
    conn.close()
    print("created actions table")

def create_customers_dim():
        print("creating customers table")        
        conn = connect_to_redshift()
        cur = conn.cursor()
        cur.execute(Staging.customers.format(DWH_SCHEMA, CUSTOMERS))
        conn.commit()
        cur.close()
        conn.close()
        print("created customers table")

def create_dates_dim():
    print("creating dates table")      
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Staging.dates.format(DWH_SCHEMA, DATES))
    conn.commit()
    cur.close()
    conn.close()
    print("created dates table")

def create_storage_dim():
    print("creating storage table")      
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Staging.storages.format(DWH_SCHEMA, STORAGES))
    conn.commit()
    cur.close()
    conn.close()
    print("created storage table")

def create_tables():
    create_fact()
    create_actions_dim()
    create_dates_dim()
    create_customers_dim()
    create_storage_dim()




# insert into tables

def insert_into_fact():
    print("inserting into fact table")      
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Insert.storage_transactions.format(DWH_SCHEMA, STORAGE_TRANSACTIONS))
    conn.commit()
    cur.close()
    conn.close()
    print("inserted into fact table")



def insert_into_actions_dim():
    print("inserting into actions table")      
    conn = connect_to_redshift()
    cur = conn.cursor()
    print(Insert.actions.format(DWH_SCHEMA, ACTIONS))
    cur.execute(Insert.actions.format(DWH_SCHEMA, ACTIONS))
    conn.commit()
    cur.close()
    conn.close()
    print("inserted into actions table")

def insert_into_customers_dim():
    print("inserting into customers table")      
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Insert.customers.format(DWH_SCHEMA, CUSTOMERS))
    conn.commit()
    cur.close()
    conn.close()
    print("inserted into customers table")

def insert_into_dates_dim():
    print("inserting into dates table")      
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Insert.dates.format(DWH_SCHEMA, DATES))
    conn.commit()
    cur.close()
    conn.close()
    print("inserted into dates table")

def insert_into_storage_dim():
    print("inserting into storage spaces table")      
    conn = connect_to_redshift()
    cur = conn.cursor()
    cur.execute(Insert.storage_spaces.format(DWH_SCHEMA, STORAGES))
    conn.commit()
    cur.close()
    conn.close()
    print("inserted into storage table")

def insert_into_tables():
    insert_into_actions_dim()
    insert_into_dates_dim()
    insert_into_customers_dim()
    insert_into_storage_dim()
    insert_into_fact()




def run_jobs():
    try:
        create_schema()
        create_tables()
        insert_into_tables()
    except Exception as e:
        print(e)
