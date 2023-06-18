class Staging:
    actions = """
        INSERT INTO {}.{} (name)
        SELECT DISTINCT action
        FROM public.transactions
    """

    customers = """
        INSERT INTO {}.{} (id, first_name, last_name, email, gender, city, postal_code, state, country)
        SELECT 
            c.id
            ,c.first_name
            ,c.last_name
            ,c.email
            ,c.gender
            ,a.city,a.postal_code,a.state, a.country
        FROM public.customers c
        LEFT JOIN public.addresses AS a 
        ON c.address_id = a.id
    """

    dates = """
        INSERT INTO {}.{} (date, year, quater, month, day)
        select t.date :: DATE as date
            , extract( year from t.date :: DATE) AS year
            , case 
                when extract(month from t.date :: DATE) <= 3 THEN 1
                when extract(month from t.date :: DATE) > 3
                    AND extract(month from t.date :: DATE) <= 6 THEN 2
                when extract(month from t.date :: DATE) > 6
                    AND extract(month from t.date :: DATE) <= 9 THEN 3
                when extract(month from t.date :: DATE) > 9 THEN 4
            end as quater
            , extract(month from t.date :: DATE) AS month
            , extract(day from t.date :: DATE) AS day

        from public.transactions t
    """


    storage_spaces = """
        INSERT INTO {}.{} (id, room_number, street_address, state, country, opens_at, closes_at, charge_per_space )
        SELECT id
        , room_number
        , street_address
        , state
        , country
        , opens_at :: integer
        , closes_at :: integer
        , SUBSTRING(charge_per_space, 2) :: real AS charge_per_space
        from public.storages
    """


    storage_transactions = """
        INSERT INTO {}.{} (transaction_id, customer_id, storage_id, date_id, action_id, space_qty, charge_per_space, total_amount)
        SELECT 
            t.id AS transaction_id
            , t.customer AS customer_id
            , t.storage_center AS storage_id
            , dates._id AS date_id
            , a._id AS action_id
            , t.space_qty::integer as space_qty
            , ssp.charge_per_space as charge_per_space
            , (ssp.charge_per_space * space_qty) as total_amount
            from public.transactions t
            left join timi_oye.actions a
            on a.name = t.action
            left join timi_oye.storages_spaces ssp
            on ssp.id = t.storage_center
            left join timi_oye.dates
            on t.date = dates.date
    """

