# reno_storage
data engineering on storage space services

## How To Run
- create a virtual environment `virtualenv venv` and activate `source/bin/activate`
- install the following:
    - pandas `pip install pandas`
    - fsspec `pip install fsspec`
    - s3fs `pip install s3fs`
    - configparser `pip install configparser`
- set up your `.env` file
- in your terminal, ensure you are in the appropraite working directory, and the virtual environment is activated.
- run `python index.py`
- a successful script execution will have the transformed file in the `/data/transformed` folder
