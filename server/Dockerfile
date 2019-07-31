FROM python:3

WORKDIR /usr/src/server

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP run.py

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]