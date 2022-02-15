FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/* /app/
EXPOSE 8080
ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "--port", "8080", "main:app" ]