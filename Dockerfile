FROM alpine:latest

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY guid-service.py /src/guid-service.py

EXPOSE  8000
CMD ["python", "/src/guid-service.py", "-p 8000"]