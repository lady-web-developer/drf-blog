# Dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Run tests
RUN python manage.py test

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
