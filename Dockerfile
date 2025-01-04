FROM redhat/ubi8

EXPOSE 5000

RUN yum install python3-pip -y && pip3 install flask

COPY app.py /app.py

ENTRYPOINT ["python3","app.py"]
