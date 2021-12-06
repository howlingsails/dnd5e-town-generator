FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HOST='::'

VOLUME [ "/data" ]
VOLUME [ "/saves" ]

EXPOSE 8090

CMD ["python", "main.py"]