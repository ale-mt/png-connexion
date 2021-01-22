FROM alemt/repo:PythonNginxGunicorn

WORKDIR /tmp

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . ./gunicorn/

COPY ./default /etc/nginx/sites-enabled/

EXPOSE 80/tcp

WORKDIR /tmp/gunicorn

RUN chmod -R 777 /var/log/nginx/

CMD nginx && gunicorn -w 2 -b 0.0.0.0:8000 wsgi:app


