# Truck Overload Detector and Monitoring System using IoT
The **Truck Overload Detector and Monitoring System using IoT** is an advanced solution designed to prevent vehicle overloading by integrating **Internet of Things (IoT) technology** with real-time monitoring. This system typically consists of **weight sensors (load cells)** installed on truck axles, **microcontrollers** (such as Arduino or Raspberry Pi) to process weight data, and **wireless communication modules** (such as Wi-Fi or GSM) to transmit data to a centralized server. The collected weight information is then displayed on a web-based dashboard, where administrators can monitor truck loads, detect overloading instances, and receive automated alerts when a truck exceeds the predefined weight limit. Additionally, GPS tracking can be integrated to provide real-time location updates of overloaded vehicles. This system enhances **road safety, reduces infrastructure damage, ensures regulatory compliance, and improves fleet management efficiency** by preventing illegal overloading.
This is a web-based Truck Overload Detector and Monitoring System built using Django, HTML, CSS, and JavaScript.

## Features
- Admin panel for truck data management.
- Client-side interface displaying truck details.
- Alerts when a truck exceeds the weight limit.
- Search functionality to find trucks by license plate.

## Installation and Setup

### Prerequisites
Ensure you have the following installed on your PC:
- Python (>= 3.8)
- pip
- Virtual environment (optional but recommended)

### Step 1: Clone the Repository
```sh
 git clone https://github.com/Ramadhan-Idi/system
 cd truck-monitoring-system
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### Step 3: Install Dependencies
Create a `requirements.txt` file and add the following dependencies:
```sh
asgiref==3.8.1
Django==5.1.6
sqlparse==0.5.3
tzdata==2025.1
```
Then install them using:
```sh
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (For Admin Access)
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### Step 6: Run the Development Server
```sh
python manage.py runserver
```

Access the system in your browser at:
```
http://127.0.0.1:8000/
```

### Step 7: Access the Admin Panel
Log in to the admin panel to add truck details:
```
http://127.0.0.1:8000/admin/
```

## Usage
1. Add truck details via the Django Admin panel.
2. View truck status on the client-side interface.
3. Use the search bar to find specific trucks.
4. Trucks exceeding the weight limit will trigger an alert.

## Technologies Used
- Django (Python)
- HTML, CSS, JavaScript
- SQLite


