class Dev:
    address= """
        CREATE TABLE IF NOT EXISTS addresses(
            id INTEGER NOT NULL
            , city VARCHAR(200) NOT NULL
            , postal_code BIGINT NOT NULL
            , country VARCHAR(200) NOT NULL
            , country_code VARCHAR(3) NOT NULL
            , state VARCHAR(300) NOT NULL
            , PRIMARY KEY (id)
        );
    """

    customers = """        
        CREATE TABLE IF NOT EXISTS customers (
            id INT NOT NULL
            , first_name TEXT NOT NULL
            , last_name TEXT NOT NULL
            , email TEXT NOT NULL
            , gender TEXT NOT NULL
            , address_id INT NULL
        )
    """

    storages = """
        CREATE TABLE IF NOT EXISTS storages (
            
            id INT NOT NULL
            , room_number INT NOT NULL
            , street_address TEXT NOT NULL
            , state VARCHAR(500) NOT NULL
            , country VARCHAR(500) NOT NULL
            , opens_at INT NOT NULL
            , closes_at INT NOT NULL
            , charge_per_space VARCHAR(500) NOT NULL
        )
    """

    transactions = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INT NOT NULL
            , customer  INT NOT NULL
            , storage_center  INT NOT NULL
            , space_qty  INT NOT NULL
            , action VARCHAR(200) NOT NULL
            , date TEXT NOT NULL
            , PRIMARY KEY (id)
        )
    """


class Staging:
    schema = """
        CREATE SCHEMA IF NOT EXISTS {};
    """

    storage_transactions = """
        CREATE TABLE IF NOT EXISTS {}.{} (
        _id INT IDENTITY(0,1)
        , transaction_id INT NOT NULL
        , customer_id INT NOT NULL
        , storage_id INT NOT NULL
        , date_id INT NOT NULL
        , action_id INT NOT NULL
        , space_qty INT NOT NULL
        , charge_per_space REAL  NULL
        , total_amount REAL NULL
        );
    """
    actions = """
        CREATE TABLE IF NOT EXISTS {}.{} (
            _id INT IDENTITY(0,1)
            , name TEXT NOT NULL
        );
    """
    customers ="""
            CREATE TABLE IF NOT EXISTS {}.{} (
            _id INT IDENTITY(0,1)
            , id INT NOT NULL
            , first_name TEXT NOT NULL
            , last_name TEXT NOT NULL
           , email TEXT NOT NULL
           , gender TEXT NOT NULL
           , city TEXT NOT NULL
           , postal_code BIGINT NOT NULL
           , state TEXT NOT NULL
           , country TEXT NOT NULL
        );
    """
    storages = """
        CREATE TABLE IF NOT EXISTS {}.{} (
        _id INT IDENTITY(0,1)
           , id INT NOT NULL
            , room_number INT NOT NULL
            , street_address TEXT NOT NULL
            , state TEXT NOT NULL
            , country TEXT NOT NULL
            , opens_at INT NOT NULL
            , closes_at INT NOT NULL
            , charge_per_space REAL NOT NULL
         );
    """
    dates = """
    CREATE TABLE IF NOT EXISTS {}.{} (
    _id INT IDENTITY(0,1)
        , date DATE NOT NULL
        , year INT NOT NULL
        , quater INT NOT NULL
        , month INT NOT NULL
        , day INT NOT NULL
    );
    """