# Weather Forecast Django App with API and Frontend

This project is a Django application that consists an API Rest and a frontend interface. The API is built using Django REST Framework, while the frontend is a basic demo to test the API using Jquery.



## Prerequisites

- Python 3.8+

## Setup

1. Activate virtual environment
```
venv/bin/activate
```
2. Run Migration
```
python manage.py migrate
```
3. Run Server
```
python manage.py runserver
```
#### API Rest
You should now be able to access the API rest at
```http://localhost:8000/api/v1/weather-forecast/{PLACE_NAME}```
* Example: 
``` http://localhost:8000/api/v1/weather-forecast/monterrey. ```

#### Frontend App
You should now be able to access the APP at http://localhost:8000 (basic demo to test the API)
