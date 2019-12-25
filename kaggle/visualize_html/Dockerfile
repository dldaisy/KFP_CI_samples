FROM tensorflow/tensorflow:2.0.0-py3
RUN pip install pandas matplotlib seaborn
COPY ./visualize.py .
CMD ["python", 'visualize.py']