FROM python
RUN mkdir /app
COPY task /app/task
COPY task_lesson /app/task_lesson
COPY manage.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8888
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
