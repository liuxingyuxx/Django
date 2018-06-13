FROM python:3
MAINTAINER lxy <xingyu.liu@dasudian.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y vim
ADD . /code/
ENTRYPOINT ["python", "manage.py", "runserver"]
CMD ["0.0.0.0:8000"]

