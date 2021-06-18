FROM python:3-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt

RUN \
 apk add --update --no-cache postgresql-libs && \
 apk add --update --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk add --update --no-cache --virtual .temp gcc libc-dev linux-headers
RUN pip3 install -r /requirements.txt
RUN apk del .temp

RUN mkdir /app 
COPY ./django_search /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/static

RUN adduser -D app
RUN chown -R app /vol
RUN chmod -R 755 /vol/web
USER app

CMD ["entrypoint.sh"]
