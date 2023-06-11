import configparser
import pandas as pd

# read .env file
config = configparser.ConfigParser()
config.read('.env')

# store variable names
bucket_url = config['SOURCE']['S3_URL']
addresses_file = config['FILES']['ADDRESS']
customers_file = config['FILES']['CUSTOMERS']
storage_spaces = config['FILES']['STORAGE_SPACES']
tnxs_I = config['FILES']['TXNS_1']
tnxs_II = config['FILES']['TXNS_2']


def extract_files():
    # read files from S3
    addresses = pd.read_csv(f"{bucket_url}/{addresses_file}")
    customers = pd.read_json(f"{bucket_url}/{customers_file}")
    storages = pd.read_json(f"{bucket_url}/{storage_spaces}")
    transactions_I = pd.read_csv(f"{bucket_url}/{tnxs_I}")
    transactions_II = pd.read_csv(f"{bucket_url}/{tnxs_II}")


    # save file to S3
    addresses.to_csv('data/addresses.csv')
    customers.to_csv('data/customers.csv')
    storages.to_csv('data/storages.csv')
    transactions_I.to_csv('data/transactions_I.csv')
    transactions_II.to_csv('data/transactions_II.csv')


