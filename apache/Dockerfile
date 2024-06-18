#run apache on port 80

FROM httpd

RUN rm -r /usr/local/apache2/htdocs/*

COPY ./index.html /usr/local/apache2/htdocs/


EXPOSE 80
