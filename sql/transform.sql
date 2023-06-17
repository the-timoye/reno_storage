-- DIMENSIONS

-- customer
SELECT   id
 , first_name
 , last_name
 , email
 , gender
 , website
  ,city
  , postal_code
  , state
  ,country
FROM customers
LEFT JOIN adresses
ON customers.address_id = address.id

-- action (dim)
SELECT DISTINCT t.action
FROM transactions AS t


-- storage_spaces (dim)

-- dates (dim)



-- FACT

-- storage_transactions(fact)

