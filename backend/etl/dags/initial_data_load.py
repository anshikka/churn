from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loads import mcc_load
from loads import network_load
from loads import bank_load

args = {
    'owner': 'Ansh Sikka',
    'start_date': days_ago(1)
}

dag = DAG(
    dag_id='initial-load-dag',
    default_args=args,
    schedule='@hourly'
)

with dag:
    bank_load_task = PythonOperator(
        task_id='t_load_banks',
        python_callable=bank_load.main,
    )

    network_load_task = PythonOperator(
        task_id='t_load_networks',
        python_callable=network_load.main,
    )

    mcc_load_task = PythonOperator(
        task_id='t_load_mcc',
        python_callable=mcc_load.main,
    )
        
bank_load_task >> network_load_task >> mcc_load_task