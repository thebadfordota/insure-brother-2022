from server.celery import app
from .services import SendEmailServices


@app.task
def send_user_info(customer_info):
    SendEmailServices(customer_info).send()
