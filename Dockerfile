# Use a maintained Python slim image
FROM python:3.10-slim-bookworm

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        git curl wget neofetch ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir wheel && \
    pip3 install --no-cache-dir -U -r requirements.txt

# Copy the whole app
COPY . .

# Expose Koyeb expected port
EXPOSE 8080

# Run Flask in background and ggn in foreground
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=8080 & python3 -m ggn"]
