from celery import shared_task
from habits.models import Habit

import datetime
from habits.services import send_telegram_message


@shared_task
def send_habit():
    habits = Habit.objects.all()
    current_date = datetime.datetime.now()
    for habit in habits:
        if habit.time >= current_date:
            tg_chat = habit.user.tg_chat_id
            message = f"""
Вы должны выполнить: {habit.action}
Место: {habit.place}
Время: {habit.time} """
            send_telegram_message(tg_chat, message)
