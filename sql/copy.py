class CopyToRedshift:
    storages = """
        COPY dev.public.storages 
        FROM 's3://tenalytics/reno_storage/cleaned/storages.csv' 
        IAM_ROLE 'arn:aws:iam::706864904003:role/service-role/AmazonRedshift-CommandsAccessRole-20230618T113013' 
        FORMAT AS CSV 
        DELIMITER ',' 
        QUOTE '"' 
        IGNOREHEADER 1 
        REGION AS 'eu-west-2'
    """