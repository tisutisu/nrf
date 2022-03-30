FROM python:3.8-alpine

WORKDIR /app
COPY . /app

ENV FLASK_APP=src/nrfApp.py

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"] 
CMD ["-m" , "flask", "run", "--host=0.0.0.0"]

