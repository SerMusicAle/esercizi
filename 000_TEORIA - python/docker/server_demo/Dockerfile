FROM python:3.10-alpine
ADD server.py .
RUN pip install flask
#manca html
RUN mkdir templates
ADD ./templates/index.html templates
#manca il mapping tra le porte
CMD ["python","./server.py"]

