FROM python:2.7.16-alpine

RUN mkdir /cybermillionaire

WORKDIR /cybermillionaire

#ENV OPENAI_API_KEY="sk-svcacct-EDG_w-BQGpTfMLf7CHBA-1Uoj2vIoXQpJLMVSNxs7Rf16r_lnqaCf7-9TV-tH8hZogKT3BlbkFJUKsX6XSGAr6s1Pw-wljTYF97wUjx_uA_ycdA-t0jUqMze5UtwdAhUuGVy0yZPV-ZjwAA"

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./cybermillionaire /cybermillionaire

#RUN apk add --no-cache python3 py3-pip

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
