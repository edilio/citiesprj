FROM nginx
MAINTAINER Edilio Gallardo, edilio73@gmail.com

RUN apt-get update

RUN apt-get install -y git vim python python-pip supervisor

RUN export VERSION=0.1 && git clone https://github.com/edilio/citiesprj.git

RUN echo "DEBUG=1" > /citiesprj/.env
RUN mkdir /var/cities
RUN mkdir /var/cities/static

ENV STATIC_ROOT=/var/cities/static/

RUN cd /citiesprj && pip install -r requirements/python/base.txt
RUN cd /citiesprj && ./manage.py collectstatic --noinput
RUN pip install gunicorn==18.0
RUN cd /citiesprj && gunicorn -w 2 -b 127.0.0.1:8000 -n cities citiesprj.wsgi:application &

COPY  django-nginx.conf /etc/nginx/conf.d/default.conf

# restart nginx to load the config
RUN service nginx stop

COPY cities.conf /etc/supervisor/supervisord.conf
# start supervisor to run our wsgi server
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
