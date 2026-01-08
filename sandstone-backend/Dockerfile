# 1. Base image
FROM python:3.11

# 2. Working directory
WORKDIR /app

# 3. Copy requirements
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy backend code
COPY . .

# 6. Expose API port
EXPOSE 8000

# 7. Start FastAPI server inside container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
