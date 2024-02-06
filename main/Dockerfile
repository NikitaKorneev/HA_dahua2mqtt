FROM python:3.9-slim
RUN pip install -r requirements.txt
COPY run.sh /
RUN chmod a+x /run.sh
CMD ["/run.sh"]