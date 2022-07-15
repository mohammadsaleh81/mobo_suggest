FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /mobo
WORKDIR /mobo
COPY . /mobo

# Installing requirements
ADD ./requirements.txt /mobo
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "mobo", "--bind", ":8000", "mobo.wsgi:application"]