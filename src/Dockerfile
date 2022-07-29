FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

RUN apk add gcc libc-dev linux-headers \
    && apk add libffi-dev

COPY . /code

WORKDIR /code

RUN pip3 --no-cache-dir install -r requirements.txt

CMD [ "python3","app.py" ]