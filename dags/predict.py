import os
import sys
from datetime import timedelta, datetime

import pendulum
from airflow.decorators import dag, task

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # So that airflow can find config files

from dags.config import GENERATED_DATA_PATH, DATA_FOLDER, MODEL_PATH, PREDICTIONS_FOLDER, TRAIN_DATA_PATH, GENERATED_DATA_FOLDER
from formation_indus_ds_avancee.data_loading import get_data_from_csv
from formation_indus_ds_avancee.feature_engineering import prepare_features_with_io
from formation_indus_ds_avancee.train_and_predict import predict_with_io


@dag(default_args={'owner': 'airflow'}, schedule=timedelta(minutes=2),
     start_date=pendulum.today('UTC').add(hours=-1))
def predict():
    @task
    def get_data_from_csv_task():
        generated_data_path = get_data_from_csv(train_data_path=TRAIN_DATA_PATH, data_folder=GENERATED_DATA_FOLDER)
        return generated_data_path

    @task
    def prepare_features_with_io_task(generated_data_path):
        features_path = os.path.join(DATA_FOLDER, f'prepared_features_{datetime.now()}.parquet')
        prepare_features_with_io(data_path=generated_data_path,
                                 features_path=features_path,
                                 training_mode=False)
        return features_path

    # Start completing predict task
    # End completing predict task
    @task
    def predict_with_io_task(feature_path: str):
        predict_with_io(features_path=feature_path, model_path=MODEL_PATH, predictions_folder=PREDICTIONS_FOLDER)
        
        
    generated_data_path = get_data_from_csv_task()
    feature_path = prepare_features_with_io_task(generated_data_path)
    predict_with_io_task(feature_path=feature_path)


predict_dag = predict()
