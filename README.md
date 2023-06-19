# reno_storage
data engineering on storage space services


## Airflow Setup
### For Windows OS Users Only
- Step 1: Install WSL
    - Open Microsoft Store
    - Install Ubuntu & restart your system
- Step 2: Install PIP
    - Open your CMD
    - type `wsl` you should have an output that looks like this: `<system_name>:/mnt/host/c/Users/<user_name>#`
    - type the following commands 
        - `sudo apt update && sudo apt upgrade` to upgrade deprecated tools & apps
        - `sudo apt-get install software-properties-common`
        - `sudo apt-add-repository universe`
        - `sudo apt-get update`
        - `sudo apt-get install python3-pip`

### For All OS Users
- Step 3: Install airflow
    - use the wsl bash in your project's terminal
    - type in the following commands in your project's virtual environment
        - `export AIRFLOW_HOME=~/airflow`
        - `AIRFLOW_VERSION=2.6.2`
        - `PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"`
        - `CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"`
        - `pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"`

- Step 4: Configure Airflow's home
    - in your wsl terminal, run:
        - `sudo nano /etc/wsl.conf`
        - in the file that opens, copy and past the below:
        ```
           [automount] 
            root = /
            options = "metadata"
        ```
        - save the file, then type `nano ~/.bashrc`
        - paste the below in the file
            ```
            export AIRFLOW_HOME=/c/users/YOURNAME/airflowhome
            ```
        - save the file

- Step 5: Configure Airflow's settings:
    - 

- Step 6: Set-up Airflow
    - Still n your virtual environment in your project's termnal, run the following code:
        - `airflow db init`
        - `airflow users create --username admin --firstname timi --lastname oye --role Admin --email thetimoye@gmail.com`
        - `airflow webserver --port 8080`
    - on another terminal window, run:
        - `airflow scheduler` 







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

