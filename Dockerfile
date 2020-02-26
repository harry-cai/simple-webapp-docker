FROM python:3.6.8-alpine
# RUN apk add --no-cache build-base tzdata
# set the timezone to China
# ENV TZ=Asia/Shanghai
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
COPY app.py /app/
RUN export FLASK_APP=app
# "app.run(port=8080)" not working, specify the port here
ENTRYPOINT flask run -h 0.0.0.0 -p 8080
