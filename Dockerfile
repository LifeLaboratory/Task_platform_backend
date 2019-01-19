FROM python
RUN mkdir /app
COPY task /app/task
COPY task_lesson /app/task_lesson
COPY manage.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["DATABASE_HOST=$DATABASE_HOST", "python", "-u", "manage.py", "runserver", "0.0.0.0:8080"]
