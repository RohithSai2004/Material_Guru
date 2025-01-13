# Material Guru Project

This project is a web application aimed at helping students access semester-specific notes based on their regulation and branch. It allows users to select their regulation (MIC18, MIC20, or MIC23) and branch (CSE, ECE, EEE, MECH, CIV, AID, AIM, MBA, MTECH, MCA). Once selected, the student can navigate to their semester and download relevant notes in PDF format.

## Features

- Select Regulation: Users can choose from different regulations.
- Select Branch: Based on regulation selection, users can select from multiple branches.
- Dynamic Semester Notes: Access notes for different semesters for the selected branch and regulation.
- File Upload: Administrators can upload semester-specific notes as PDFs.
  
## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django (Python)
- **Database:** SQLite (for local development) / PostgreSQL (or other databases for production)
- **File Storage:** Django FileField to store PDFs of notes

## Requirements

- Python 3.x
- Django 3.x+
- PostgreSQL (for production)
- Git (for version control)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/MaterialGuru.git
cd MaterialGuru
##Step 2: Create a Virtual Environment
python -m venv venv
##Step 3: Activate the Virtual Environment
##On Windows:
venv\Scripts\activate
##On macOS/Linux:
source venv/bin/activate
#Step 4: Install Dependencies
pip install -r requirements.txt
#Step 5: Set Up the Database
#Make sure to apply the migrations to set up the database schema.
python manage.py migrate
#Step 6: Create a Superuser (Optional)
#To access the Django admin interface, create a superuser account.
python manage.py createsuperuser
#Step 7: Run the Development Server
python manage.py runserver
# Your application will be available at 
http://127.0.0.1:8000/.

#Step 8: Access the Admin Panel
#Go to http://127.0.0.1:8000/admin/ and log in with the superuser account you created.