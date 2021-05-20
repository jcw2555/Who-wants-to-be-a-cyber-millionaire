FROM nginx:latest
 

RUN mkdir /cybermillionaire
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

COPY cybermillionaire.crt /etc/nginx/cybermillionaire.crt
COPY cybermillionaire.com.key /etc/nginx/cybermillionaire.com.key


WORKDIR /cybermillionaire
