FROM python:3.12
WORKDIR /app/chat_service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    libpq-dev \
    libjpeg-dev \
    libpng-dev \
	gcc \
    && rm -rf /var/lib/apt/lists/*

COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8002"]