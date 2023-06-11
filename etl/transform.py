import pandas as pd


# join transactions data
def join_transactions_data():
    # read files
    transactions_I = pd.read_csv('data/transactions_I.csv')
    transactions_II = pd.read_csv('data/transactions_II.csv')
    # joins both files and saves to csv
    transactions = pd.concat([transactions_I, transactions_II], ignore_index=True)
    transactions.to_csv('data/transactions.csv')

    df = pd.read_csv('data/transactions.csv')
    return df

# convert date to datetime type
def convert_date_datatype(transactions_df):
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])
    return transactions_df


def add_columns(transactions_df):
    transactions_df['year'] = transactions_df['date'].dt.year
    transactions_df['month'] = transactions_df['date'].dt.month
    transactions_df['day'] = transactions_df['date'].dt.day
    return transactions_df

# save transformed df
def save_transformation(df):
    df.to_csv('data/transformed/transactions.csv')

# run all functions in one main function
def transform_files():
    transactions = join_transactions_data()
    transactions = convert_date_datatype(transactions)
    transactions = add_columns(transactions)
    columns = ['id','customer','storage_center','space_qty','action','date','year','month','day']
    save_transformation(transactions[columns])



