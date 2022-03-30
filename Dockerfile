FROM python:3.6-alpine

WORKDIR /app
COPY . /app

#ENV FLASK_APP=src/nrfApp.py

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"] 
CMD ["src/nrfApp.py"]

