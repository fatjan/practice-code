from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.slack_operator import SlackAPIPostOperator
from datetime import datetime

def send_slack_notification():
    slack_message = "This is a notification from my trial app!"
    slack_operator = SlackAPIPostOperator(
        task_id="slack_notification",
        channel="#slack-notification",
        token="",
        text=slack_message
    )
    slack_operator.execute(context=None)

default_args = {
    'owner': 'Fatma Janna',
    'start_date': datetime(2023, 7, 11),
}

with DAG('slack_notification_dag', default_args=default_args, schedule_interval='@daily') as dag:
    send_notification_task = PythonOperator(
        task_id='send_notification',
        python_callable=send_slack_notification
    )
