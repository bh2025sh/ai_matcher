# AI Matcher

AI Matcher is a job and candidate matching system built with **Django REST Framework**.  
It allows HRs to post jobs and candidates to register with their skills, experience, and resumes.  
The system then matches candidates with jobs using AI/ML logic.

---

## 🚀 Features
- User authentication with JWT tokens (Login / Register)
- Role-based system: **HR** and **Candidate**
- Candidate Profile: skills, experience, education, resume
- Job Posting: title, description, required skills, experience
- Matching service: recommend jobs to candidates and candidates to HR
- REST APIs (tested via Postman)



## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** SQLite / PostgreSQL
- **Authentication:** JWT (SimpleJWT)
- **Tools:** Postman for API testing


## 🚀 Steps to Run the Project

1. Clone the Project
git clone https://github.com/bh2025sh/ai_matcher.git
cd ai_matcher

2. Setup Virtual Environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3. Install Requirements
pip install -r requirements.txt

4. Create Migrations

First, create migrations for the accounts app:

python manage.py makemigrations accounts


Then, create migrations for the rest of the project:

python manage.py makemigrations

5. Apply Migrations
python manage.py migrate

6. Create Superuser (Admin/HR)
python manage.py createsuperuser

8. Run the Server
python manage.py runserver

The server will start at:
 http://127.0.0.1:8000

 ## API Testing with Postman
- Project contain a file `ai_matcher.postman_collection.json`
- Import this file in Postman:
  1. Open Postman → File → Import
  2. Select ``ai_matcher.postman_collection.json`
  3. Set `admin_token` and `cand_token` in Environment