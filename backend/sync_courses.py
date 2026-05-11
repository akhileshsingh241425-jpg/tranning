#!/usr/bin/env python3
import requests
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Course

SERVER_URL = ""
SERVER_URLS = [
    "http://147.93.19.87",
    "https://trainingprotec.com",
    "http://trainingprotec.com",
    "http://147.93.19.87:5050"
]

def fetch_courses_from_server():
    print("Fetching courses from server...")
    courses = []
    for url in SERVER_URLS:
        try:
            print(f"  Trying: {url}/api/courses")
            response = requests.get(f"{url}/api/courses", timeout=10)
            if response.status_code == 200:
                courses = response.json()
                print(f"  Success! Found {len(courses)} courses")
                global SERVER_URL
                SERVER_URL = url
                return courses
        except Exception as e:
            print(f"  Failed: {e}")
            continue
    print("Could not connect to any server URL")
    return []

def fetch_course_detail(slug):
    try:
        response = requests.get(f"{SERVER_URL}/api/courses/{slug}", timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching detail for {slug}: {e}")
        return None

def sync_courses():
    server_courses = fetch_courses_from_server()
    if not server_courses:
        print("No courses found on server!")
        return

    with app.app_context():
        updated = 0
        created = 0

        for sc in server_courses:
            print(f"Processing: {sc.get('title', 'Unknown')}")
            
            detail = fetch_course_detail(sc.get('slug'))
            if not detail:
                print(f"  - Skipping {sc.get('slug')} - no detail data")
                continue

            course = Course.query.filter_by(slug=sc.get('slug')).first()
            
            if not course:
                course = Course(slug=sc.get('slug'))
                db.session.add(course)
                created += 1
                print(f"  - Created new course")
            else:
                updated += 1
                print(f"  - Updating existing course")

            course.title = detail.get('title', '')
            course.description = detail.get('description', '')
            course.image = detail.get('image', '')
            course.icon = detail.get('icon', 'FaBookOpen')
            course.price = detail.get('price', 0)
            course.original_price = detail.get('originalPrice', 0)
            course.rating = detail.get('rating', 4.5)
            course.reviews = detail.get('reviews', 0)
            course.learners = detail.get('learners', '0')
            course.duration = detail.get('duration', '')
            course.level = detail.get('level', 'Beginner')
            course.tag = detail.get('tag', '')
            course.modules = detail.get('modules', 0)
            course.projects = detail.get('projects', 0)
            course.instructor_name = detail.get('instructor', {}).get('name', '')
            course.instructor_role = detail.get('instructor', {}).get('role', '')
            course.instructor_image = detail.get('instructor', {}).get('image', '')
            course.instructor_experience = detail.get('instructor', {}).get('experience', '')
            course.curriculum = ','.join(detail.get('curriculum', []))
            course.is_published = detail.get('is_published', True)
            course.sort_order = detail.get('sort_order', 0)

            course.tagline = detail.get('tagline', '')
            course.hero_image = detail.get('heroImage', '')
            course.overview = detail.get('overview', '')
            course.key_benefits = '\n'.join(detail.get('keyBenefits', [])) if detail.get('keyBenefits') else ''
            course.modules_detail = json.dumps(detail.get('modulesDetail', []))
            course.learning_path = json.dumps(detail.get('learningPath', []))
            course.technologies_list = ','.join(detail.get('technologies', [])) if detail.get('technologies') else ''
            course.faq = json.dumps(detail.get('faq', []))
            course.detail_stats = json.dumps(detail.get('detailStats', []))
            course.topic_wise_content = json.dumps(detail.get('topicWiseContent', []))
            course.eligibility = detail.get('eligibility', '')
            course.projects_list = json.dumps(detail.get('projectsList', []))
            course.benefits = json.dumps(detail.get('benefits', []))
            course.advisor = json.dumps(detail.get('advisor', {}))
            course.reviews_list = json.dumps(detail.get('reviewsList', []))
            course.why_join = json.dumps(detail.get('whyJoin', []))
            course.certification = json.dumps(detail.get('certification', {}))

            db.session.commit()
            print(f"  - Saved: {course.title}")

        print(f"\n=== Sync Complete ===")
        print(f"Created: {created} courses")
        print(f"Updated: {updated} courses")

if __name__ == "__main__":
    sync_courses()