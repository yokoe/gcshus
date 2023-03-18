FROM python:3.8
WORKDIR /code
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
COPY . .
CMD ["sh", "run_test.sh"]
