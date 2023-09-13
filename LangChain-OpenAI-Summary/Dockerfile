FROM public.ecr.aws/lambda/python:3.11

WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# SET THE API KEY
RUN python /app/app/model/model.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]