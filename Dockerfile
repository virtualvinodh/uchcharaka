# our base image
# espeak py won't work for other version and it should be debian
# else it will try to build the wheel and fail miserably
FROM python:3.10-bullseye

# copy frontend
ADD ./uchcharaka-front/dist/spa-mat/ /var/www/html
ADD ./uchcharaka-front/dist/.htaccess /var/www/html/.htaccess

# Copy python files
ADD ./uchcharaka-back/ /var/www/html
ADD ./start.sh /var/www/html

# Get Ubuntu packages
RUN apt update
#RUN apt install -y -q build-essential curl
RUN pip install gunicorn
RUN apt install espeak-ng -y
RUN apt install espeak-ng-data -y
RUN apt install apache2 -y
RUN apt install dos2unix -y

WORKDIR /var/www/html

RUN pip3 install -r requirements.txt

RUN chmod +x start.sh
RUN sed -i '/LoadModule rewrite_module/s/^#//g' /etc/apache2/apache2.conf
RUN sed -i 's#AllowOverride [Nn]one#AllowOverride All#' /etc/apache2/apache2.conf
RUN a2enmod rewrite
RUN a2enmod proxy
RUN a2enmod proxy_http

ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf
RUN dos2unix /etc/apache2/sites-available/000-default.conf


# tell the port number the container should expose
EXPOSE 80

# run the application
CMD ["./start.sh"]
#CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]





