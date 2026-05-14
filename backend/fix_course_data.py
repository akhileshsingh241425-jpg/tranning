from app import app, db, Course
import json

def fix_course_data():
    with app.app_context():
        courses = Course.query.all()
        for c in courses:
            # Fix course_objectives
            if c.course_objectives:
                try:
                    # Try to parse as JSON
                    json.loads(c.course_objectives)
                except:
                    # It's plain text, convert to JSON array
                    lines = [l.strip() for l in c.course_objectives.split('\n') if l.strip()]
                    c.course_objectives = json.dumps(lines)
            
            # Fix other fields that might have issues
            if c.modules_detail and c.modules_detail.startswith('['):
                try:
                    json.loads(c.modules_detail)
                except:
                    c.modules_detail = '[]'
            
            if c.learning_path and c.learning_path.startswith('['):
                try:
                    json.loads(c.learning_path)
                except:
                    c.learning_path = '[]'
            
            if c.detail_stats and c.detail_stats.startswith('['):
                try:
                    json.loads(c.detail_stats)
                except:
                    c.detail_stats = '[]'
        
        db.session.commit()
        print("Fixed course data!")

if __name__ == '__main__':
    fix_course_data()