FROM python:2.7.16-alpine


RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./cybermillionaire /cybermillionaire

WORKDIR /cybermillionaire

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]