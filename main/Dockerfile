FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN chmod +x /app/run.sh
RUN ls -la /app  # List files in /app to verify that run.sh is there
CMD ["/app/run.sh"]