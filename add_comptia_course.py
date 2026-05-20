import sys
import os

# Get the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))
backend_path = os.path.join(project_root, 'backend')

# Add backend to path and change to backend directory
sys.path.insert(0, backend_path)
os.chdir(backend_path)

# Set Flask environment
os.environ['FLASK_ENV'] = 'production'

from app import app, db, Course

def add_comptia_course():
    with app.app_context():
        # Check if course already exists
        existing = Course.query.filter_by(slug='comptia-a-certification-training').first()
        if existing:
            print("Course exists, updating...")
            course = existing
        course = Course(
            title="CompTIA A+ Certification Training",
            slug="comptia-a-certification-training",
            description="Our CompTIA A+ training program is designed to equip participants with the essential skills and knowledge needed to excel in entry-level IT roles.",
            tagline="Master CompTIA A+ Certification - Hardware, Software, Networking & Security",
            overview="""The CompTIA A+ certification training course is created for all entry-level and aspiring IT professionals to validate their skills and knowledge in the IT domain. The certification course is made for learners to properly understand the hardware and software technologies that they will be working with so that they can support various IT infrastructures.

Organizations often look for this certification as a marker and validation of the prospective employee's skills. The certification has two examinations that candidates need to clear to become certified CompTIA A+ professionals.""",
            key_benefits="""Prepare and pass the CompTIA A+ certification exams
Install and configure the components of the PC system and peripheral devices
Install, configure, and troubleshoot internal system components
Understand how to identify, use, and connect hardware components and devices
Understand the concepts of network infrastructure
Understand how to set up network connections and troubleshoot them
Learn laptop support and troubleshooting
Understand how to troubleshoot and support mobile devices
Understand how to set up, configure, and troubleshoot printing devices
Understand how to put client virtualization and cloud computing into practice
Learn how to identify and defend devices and their network connections against security risks""",
            topic_wise_content="""CompTIA A+ 220-1101 (Core 1) | Mobile devices (13%), Hardware setup, Accessory options, Network setup, Troubleshooting
CompTIA A+ 220-1101 (Core 1) | Networking (23%), Protocols and ports, SOHO networks, Networking tools
CompTIA A+ 220-1101 (Core 1) | Hardware (25%), Component installation, Cables and connectors, Peripheral devices, Motherboards and power
CompTIA A+ 220-1101 (Core 1) | Virtualization and cloud computing, Virtualization concepts, Cloud models
CompTIA A+ 220-1101 (Core 1) | Hardware and network troubleshooting, Diagnosing issues, Troubleshooting tools
CompTIA A+ 220-1102 (Core 2) | Operating systems, OS installation, Windows tools, File systems
CompTIA A+ 220-1102 (Core 2) | Security, Security measures, Malware prevention
CompTIA A+ 220-1102 (Core 2) | Software troubleshooting, OS issues, Mobile troubleshooting, Security concerns
CompTIA A+ 220-1102 (Core 2) | Operational procedures, Documentation, Safety and communication, Backup and recovery""",
            prerequisites="""Basic computer knowledge
No prior IT experience required
Interest in IT career
Willingness to learn""",
            skills_covered="Hardware, Software, Networking, Security, Troubleshooting, Operating Systems, Mobile Devices, Virtualization, Cloud Computing, Printers, Laptop Support",
            tools_covered="Windows, macOS, Linux, Command Prompt, Task Manager, Disk Management",
            target_audience="""Individuals interested in pursuing a profession in IT
Individuals who want to get their CompTIA A+ certification
Beginners starting IT career
Help Desk Technicians
Desktop Support Engineers""",
            duration="6 Months",
            level="Beginner",
            mode="Live Online + Self-Paced",
            language="English",
            price=299,
            original_price=799,
            discount_percent=62,
            rating=4.5,
            reviews=1200,
            learners="1500+",
            modules=14,
            projects=8,
            emi_options="No Cost EMI starting @ $25/month",
            training_schedule="Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
            start_date="Every Monday",
            next_batch="Starting 1st June 2026",
            exam_code="220-1101 & 220-1102",
            exam_questions="Maximum 90 Questions each",
            exam_duration="90 Minutes each",
            exam_format="Multiple Choice + Performance-Based",
            exam_passing_score="675 (on a scale of 100-900)",
            exam_languages="English",
            certification="CompTIA A+ Certification - Industry-recognized entry-level IT certification",
            course_objectives="""Prepare and pass the CompTIA A+ certification exams
Install and configure the components of the PC system and peripheral devices
Install, configure, and troubleshoot internal system components
Understand how to identify, use, and connect hardware components and devices
Understand the concepts of network infrastructure
Understand how to set up network connections and troubleshoot them
Learn laptop support and troubleshooting
Understand how to troubleshoot and support mobile devices
Understand how to set up, configure, and troubleshoot printing devices
Understand how to put client virtualization and cloud computing into practice
Learn how to identify and defend devices and their network connections against security risks""",
            faq="""Q: Is the CompTIA A+ certification a suitable place to start?|A: Yes, it helps you get entry-level IT roles such as Desktop Support, Help Desk Tech, etc.
Q: What jobs can you obtain with CompTIA A+?|A: Service Desk Analyst, Help Desk Tech, Desktop Support Administrator, Technical Support Specialist, etc.
Q: What does the CompTIA A+ certification cost?|A: The CompTIA A+ certification costs $232 USD per exam.
Q: How to Pass the CompTIA A+ Exam?|A: Through study guide, self-study, instructor-led training, and practice tests.
Q: Is CompTIA A+ a difficult exam?|A: With proper preparation and strategy, you can pass the exams.
Q: What is the next step after CompTIA A+?|A: You can pursue Network+, Security+, or cloud certifications.
Q: Is CompTIA A+ required for Network+?|A: No, it's not required but helps build foundation.
Q: How much can I earn with CompTIA A+?|A: Salaries range from $40,000 to $67,000+ annually.""",
            category="Cyber Security",
            is_published=True,
            image="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800"
        )
        
        db.session.add(course)
        db.session.commit()
        
        print("Course added successfully!")
        print("Title:", course.title)
        print("Slug:", course.slug)
        print("Category:", course.category)

if __name__ == "__main__":
    add_comptia_course()