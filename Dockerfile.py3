FROM centos:8

MAINTAINER Hoyin "kuangfeng05@163.com"

RUN yum update -y \
&& yum install epel-release -y \
&& yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel \
readline-devel tk-devel gcc make libffi-devel wget git -y \
&& wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz \
&& tar -zxvf Python-3.8.3.tgz \
&& cd Python-3.8.3 && ./configure prefix=/usr/local/python3 && make && make install \
&& ln -s /usr/local/python3/bin/python3.8 /usr/bin/python3 \
&& ln -s /usr/local/python3/bin/pip3.8 /usr/bin/pip3



ENTRYPOINT /bin/sh

