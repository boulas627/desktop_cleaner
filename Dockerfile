FROM python:3

WORKDIR /Python_Projects/desktop_cleaner

# COPY requirements.txt requirements.txt 
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./main.py"]
