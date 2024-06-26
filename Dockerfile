FROM python:3.10-slim

# install requirements
COPY requirements.txt /
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt

# copy the pipe source code
COPY pipe.py /
COPY LICENSE README.md pipe.yml /

ENTRYPOINT ["python3", "/pipe.py"]