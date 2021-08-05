FROM python:3.9

RUN pip install fastapi uvicorn
RUN pip install sqlalchemy

EXPOSE 10000

COPY ./app /app

COPY ./data.json /app/data.json

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]