FROM python:3.10

# Create app directory
WORKDIR /app

# Install app dependencies
COPY . .

RUN pip install -r requirements.txt

# Bundle app source
EXPOSE 5000
CMD [ "python", "/app/run.py" ]