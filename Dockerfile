FROM python:3.12-slim
WORKDIR /app
RUN pip install boto3
COPY lambda_function.py .
CMD ["python", "lambda_function.py"]
