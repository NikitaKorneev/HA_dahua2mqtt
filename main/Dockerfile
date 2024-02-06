FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y jq
COPY . /app
RUN chmod +x run.sh
RUN ls -la /app  # List files in /app to verify that run.sh is there
CMD ["run.sh"]
