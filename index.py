from etl.load import run_jobs
import pandas as pd


if __name__ == "__main__":
    try:
        run_jobs()
    except Exception as e:
        print(e)

    
