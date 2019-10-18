FROM python:3.7-slim 

# Create the directory 
WORKDIR /app 

# Move files 
COPY . /app 

RUN pip install -r requirements.txt 

EXPOSE 5000 

CMD ["python3.7", "run.py"]