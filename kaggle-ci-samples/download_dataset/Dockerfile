FROM python:3.7
ENV KAGGLE_USERNAME= [Your kaggle username] \
    KAGGLE_KEY= [Your kaggle key]
RUN pip install kaggle
RUN pip install google-cloud-storage
COPY ./download_data.py .
CMD ["python", "download_data.py"]