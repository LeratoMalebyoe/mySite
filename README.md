# mySite

Django Capstone Project with Docker and Virtual Environment support.

## Getting Started

### 1. Using Virtual Environment
```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
