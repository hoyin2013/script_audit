FROM xdjk/py3.8
MAINTAINER Hoyin "kuangfeng05@163.com"

RUN cd /opt && git clone https://github.com/hoyin2013/script_audit.git && \
pip3 install -r /opt/script_audit/requirement/requirement.txt -i https://pypi.douban.com/simple

WORKDIR /opt/script_audit

RUN /usr/bin/python3 manage.py makemigrations && /usr/bin/python3 manage.py migrate
RUN /usr/bin/python3 manage.py loaddata data/init.json

ENTRYPOINT /usr/bin/python3 manage.py runserver 0.0.0.0:8000
