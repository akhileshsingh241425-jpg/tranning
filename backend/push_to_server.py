#!/usr/bin/env python3
import requests
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Course

SERVER_URL = "https://trainingprotec.com"

ADMIN_LOGIN_URL = f"{SERVER_URL}/admin/login"
COURSE_API_URL = f"{SERVER_URL}/api/courses/sync"

ADMIN_CREDS = {
    "username": "admin",
    "password": "Vishal@123"
}

def login_and_get_session():
    session = requests.Session()
    try:
        response = session.post(ADMIN_LOGIN_URL, data=ADMIN_CREDS, allow_redirects=False)
        if response.status_code in [302, 303]:
            print("  Login successful!")
            return session
    except Exception as e:
        print(f"  Login failed: {e}")
    return None

def update_course_via_api(session, course_data):
    try:
        response = session.post(COURSE_API_URL, json=course_data, timeout=30)
        if response.status_code == 200:
            return True
        print(f"  API error: {response.status_code} - {response.text}")
        return False
    except Exception as e:
        print(f"  API error: {e}")
        return False

def get_local_courses():
    with app.app_context():
        courses = Course.query.all()
        print(f"Found {len(courses)} courses in local database")
        return courses

def push_to_server():
    courses = get_local_courses()
    if not courses:
        print("No courses in local database!")
        return

    session = login_and_get_session()
    if not session:
        print("Could not login to server!")
        return

    updated = 0
    for course in courses:
        print(f"Updating: {course.title}")
        
        course_data = course.to_detail_dict()
        
        if update_course_via_api(session, course_data):
            updated += 1
            print(f"  Success!")
        else:
            print(f"  Failed!")

    print(f"\n=== Done ===")
    print(f"Updated: {updated}/{len(courses)} courses")

if __name__ == "__main__":
    push_to_server()