FROM python

WORKDIR /app

COPY templates .

RUN pip install flask mysql-connector-python
RUN mkdir templates
RUN mv messages.jinja2 templates

COPY app.py .

CMD flask run --host 0.0.0.0