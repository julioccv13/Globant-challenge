FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /globant-challenge

COPY . /globant-challenge

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]



