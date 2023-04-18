FROM python:3.9

ADD app.py .
ADD employees.txt .

RUN pip install flask

CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]

