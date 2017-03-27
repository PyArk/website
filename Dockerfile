FROM tiangolo/uwsgi-nginx-flask:flask-python3.5

MAINTAINER Sebastian Ramirez <tiangolo@gmail.com>

# Clone our private GitHub Repository
RUN git clone https://fa51ae4dbfbd34366c91968f7067ec5447a434cc:x-oauth-basic@github.com/PyArk/website /myapp/

#move repo and install requirements
RUN cp -R /myapp/* /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Clean-up and move a file
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /myapp/
RUN mv app.py main.py
