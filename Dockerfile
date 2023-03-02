FROM python:3.11

RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip cache purge
RUN  pip install --no-cache-dir -r requirements.txt

COPY venv/lib/python3.11/site-packages/flask_wtf/form.py venv/lib/python3.11/site-packages/flask_wtf/form.py
COPY . .

CMD ["python", "app.py"]