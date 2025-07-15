FROM python:3.11-slim

# Create working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Default shell
CMD ["bash"]
