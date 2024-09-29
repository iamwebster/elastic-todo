FROM python:3.10-alpine

WORKDIR /code 

COPY ./requirements.txt .

RUN pip install -r requirements.txt 

COPY . . 

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
