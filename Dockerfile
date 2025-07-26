FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install streamlit
RUN pip install streamlit

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY app/ app/

# Run Streamlit app
CMD streamlit run app/main.py --server.port $PORT --server.address 0.0.0.0
