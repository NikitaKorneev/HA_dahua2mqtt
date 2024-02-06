FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
RUN chmod +x /app/run.sh
RUN ls -la /app  # List files in /app to verify that run.sh is there
CMD ["run.sh"]