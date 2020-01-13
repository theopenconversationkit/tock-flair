FROM python:3.7

WORKDIR /usr/src/app

ADD . .

RUN chmod +x build/download_models.sh && ./build/download_models.sh

RUN pip install --no-cache-dir -r requirements/common.txt

EXPOSE  5000

CMD [ "python", "application.py" ]