import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db, Course

hero_images = {
    "data-science-ai": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1920&q=80",
    "cloud-computing-devops": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80",
    "cyber-security": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1920&q=80",
    "web-development": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1920&q=80",
    "digital-marketing": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1920&q=80",
    "business-analytics": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1920&q=80",
    "ui-ux-design": "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=1920&q=80",
    "mobile-app-development": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1920&q=80",
    "aws-solution-architect": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80",
    "python-refresher-ai": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1920&q=80",
    "sql-certification": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=1920&q=80",
    "comptia-network-course": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920&q=80",
    "microsoft-azure-developer-certification-associate-az-204-training": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80",
    "comptia-security": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1920&q=80",
    "aws-course-certification-training": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80",
    "aws-fundamentals-specialization": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80",
    "pmp-certification-training": "https://images.unsplash.com/photo-1507925921958-8a62f3d1a50d?w=1920&q=80"
}

def update():
    with app.app_context():
        for slug, hero_url in hero_images.items():
            course = Course.query.filter_by(slug=slug).first()
            if course:
                course.hero_image = hero_url
                print(f"Updated: {course.title[:30]}")
        db.session.commit()
        print("\nAll hero images updated!")

if __name__ == '__main__':
    update()