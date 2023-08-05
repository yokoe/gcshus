FROM python:3.9-bullseye
WORKDIR /code
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
COPY . .
CMD ["sh", "run_test.sh"]
