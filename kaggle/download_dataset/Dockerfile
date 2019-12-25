FROM python:3.7
ENV KAGGLE_USERNAME=ludai98 \
    KAGGLE_KEY=fe98f9b3c4993ea73633e42bd8882bd8
RUN pip install kaggle
RUN pip install google-cloud-storage
CMD ["python", "download_data.py"]