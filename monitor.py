# import os
# import sys
# from datetime import timedelta

# from airflow.decorators import dag, task
# from sqlalchemy_utils.types.enriched_datetime.pendulum_date import pendulum

# sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

# from dags.config import PREDICTIONS_FOLDER, DB_CON_STR, MONITORING_TABLE_NAME
# from formation_indus_ds_avancee.monitoring import monitor_with_io


# @dag(default_args={'owner': 'airflow'}, schedule=timedelta(weeks=4),
#      start_date=pendulum.today('UTC').add(hours=-1))
# def monitor_model():
#     @task
#     def monitor_with_io_task() -> str:
#         monitor_with_io(predictions_folder=PREDICTIONS_FOLDER, db_con_str=DB_CON_STR, monitoring_table_name=MONITORING_TABLE_NAME)
#     monitor_with_io_task()
# monitor_model_dag = monitor_model()
