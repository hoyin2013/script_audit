FROM xdjk/py3.8
MAINTAINER Hoyin "kuangfeng05@163.com"

WORKDIR /opt

RUN git clone https://github.com/hoyin2013/script_audit.git && \
pip3 install -r /opt/requirement/requirement.txt -i https://pypi.douban.com/simple

ENTRYPOINT /usr/bin/python3 manage.py runserver 0.0.0.0:8000
