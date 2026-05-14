import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cyber-security-website', 'backend'))

from app import app, db, Course
import json

course_data = {
    "data-science-ai": {
        "title": "Data Science & AI Course",
        "tagline": "Become a Data Scientist - Master Python, ML, Deep Learning & AI",
        "description": "Master Python, Statistics, Machine Learning, Deep Learning & AI with hands-on projects. Build real-world models using TensorFlow, scikit-learn & pandas.",
        "overview": """The Data Science & AI training program is designed to make you job-ready in one of the highest-paying careers in tech. This comprehensive course covers Python programming, statistics, machine learning, deep learning, NLP, and computer vision.

You will work on real-world datasets and build 18+ industry projects including predictive models, recommendation systems, image classifiers, and AI chatbots. The curriculum is designed by industry experts and updated regularly to match current market requirements.

This program is suitable for beginners with no prior coding experience as well as professionals looking to switch careers into Data Science and AI.""",
        "key_benefits": """Master Python programming from scratch
Learn statistics and probability for data science
Build machine learning models with scikit-learn
Create deep learning models with TensorFlow and Keras
Work with natural language processing (NLP)
Build computer vision applications
Create recommendation systems
Deploy ML models to production
Work with big data tools like Spark and Hadoop
Get career guidance and interview preparation""",
        "eligibility": """This course is ideal for:
- Beginners with no prior programming experience
- Working professionals looking to switch to Data Science
- IT professionals wanting to add AI/ML skills
- Engineering and Science graduates
- Business analysts wanting to learn predictive modeling

No prior coding experience required. Basic computer knowledge is sufficient.""",
        "training_schedule": """Weekdays: Mon-Fri (7-10 PM IST)
Weekends: Sat-Sun (10 AM-2 PM IST)
Start Date: Every Monday""",
        "start_date": "Every Monday",
        "next_batch": "Starting 1st June 2026",
        "exam_code": "DS-001",
        "exam_questions": "Maximum 90 Questions",
        "exam_duration": "90 Minutes",
        "exam_passing_score": "750 (on a scale of 100-900)",
        "exam_format": "Multiple Choice and Performance-Based",
        "exam_languages": "English, Japanese, Portuguese, Spanish",
        "course_objectives": """["Develop a comprehensive understanding of foundational security concepts and principles that serve as the cornerstone of cybersecurity.","Learn to identify, assess, and mitigate various threats, vulnerabilities, and risks that can compromise the security of digital environments.","Master the principles and practices of designing, implementing, and managing a robust security architecture that can withstand diverse cyber threats.","Gain expertise in day-to-day security operations, including incident response, monitoring, and safeguarding critical assets.","Acquire the knowledge and skills required to oversee and manage a security program effectively, ensuring compliance, governance, and the protection of valuable data."]""",
        "faq": """Q: Do I need prior coding experience?|No, this course starts from basics. We have dedicated Python modules for beginners.
Q: What is the course duration?|6 months with weekday and weekend batch options. Lifetime access to course materials.
Q: Are there any prerequisites?|Basic mathematical knowledge (class 10 level) is sufficient. No prior programming needed.
Q: Do you provide job assistance?|Yes, we provide resume building, mock interviews, and have tie-ups with 200+ hiring partners.
Q: Can I learn at my own pace?|Yes, we provide self-paced learning option with lifetime access to all course materials.
Q: What tools will I learn?|Python, NumPy, Pandas, Scikit-learn, TensorFlow, Keras, NLP, Computer Vision, SQL, and deployment tools.
Q: Is the certificate recognized?|Yes, our certificates are recognized by top companies and can be showcased on LinkedIn.
Q: Do you offer EMI options?|Yes, we offer easy EMI options starting at affordable monthly installments.
Q: What kind of projects will I work on?|18+ projects including house price prediction, fraud detection, recommendation systems, face recognition, and more.
Q: How is the course delivered?|Live instructor-led online sessions with practical hands-on exercises and assignments.
Q: What is the average salary after this course?|Our students typically get 40-150% salary hike. Average starting salary is ₹5-12 LPA for freshers.
Q: Can I switch careers after this course?|Yes, many students have successfully transitioned from non-tech roles to Data Science and AI.
Q: Is the content updated?|Yes, our curriculum is regularly updated to include latest industry trends and technologies.
Q: What support is available?|24/7 support through chat, email, and live sessions. Dedicated TA support for doubt resolution.
Q: Do I need to buy any software?|No, all tools used are free. We provide access to Jupyter notebooks and Google Colab.""",
        "certification": "Yes, Certificate of Completion with unique ID",
        "why_join": """Expert Mentors|Learn from industry experts with 10+ years experience
18+ Live Projects|Work on real-world projects with industry datasets
Certificate|Get recognized certificate upon completion
24/7 Support|Round-the-clock doubt resolution""",
        "projects_list": """House Price Prediction Model
Fraud Detection System
Customer Churn Prediction
Movie Recommendation System
Email Spam Classifier
Face Recognition System
Stock Price Prediction
Customer Segmentation
Medical Diagnosis AI
Sentiment Analysis Tool
Object Detection Model
Chatbot Development
Credit Score Prediction
Market Basket Analysis
Traffic Flow Prediction
Handwritten Digit Recognition
Customer Lifetime Value Prediction
AI-Powered Resume Parser""",
        "reviews_list": """Amit Sharma | Data Analyst at TCS | This course changed my career completely. The projects were exactly what I needed for my job.
Priya Singh | ML Engineer at Flipkart | Best investment I made. The deep learning modules are fantastic!
Rajesh Kumar | Data Scientist at Amazon | The instructors are amazing. Got placed within 2 months of completion.
Sofia Ahmed | Analytics Manager | The hands-on projects helped me apply learning immediately at work.
Vikram Patel | Senior Data Analyst | The NLP and CV modules are top-notch. Highly recommend!""",
        "benefits": """Live Instructor-Led Sessions
Hands-on Projects
Industry-Recognized Certificate
Resume Building & Mock Interviews
24/7 Support
Lifetime Access to Materials
Placement Assistance
EMI Options Available""",
        "tools_covered": "Python, NumPy, Pandas, Scikit-learn, TensorFlow, Keras, PyTorch, OpenCV, NLTK, SQL, MongoDB, Jupyter, Google Colab",
        "skills_covered": "Python, Machine Learning, Deep Learning, NLP, Computer Vision, Data Analysis, Statistical Modeling, SQL",
        "mode": "Live Online / Self-Paced",
        "language": "English"
    },
    "cloud-computing-devops": {
        "title": "Cloud Computing & DevOps",
        "tagline": "Master AWS, Azure, Docker, Kubernetes & CI/CD",
        "description": "Learn AWS, Azure, Docker, Kubernetes & CI/CD pipelines. Deploy real applications to the cloud.",
        "overview": """The Cloud Computing & DevOps training program is designed to make you job-ready in cloud and DevOps roles. This comprehensive course covers AWS, Azure, Docker, Kubernetes, and CI/CD pipelines.

You will work on real-world cloud projects and deploy applications to production. The curriculum is designed by industry experts and includes AWS Solutions Architect certification prep.""",
        "key_benefits": """Master AWS core services
Learn Azure cloud platform
Deploy applications with Docker
Orchestrate containers with Kubernetes
Build CI/CD pipelines
Implement Infrastructure as Code
Monitor cloud infrastructure
Implement security best practices
Manage cloud costs
Get career guidance and interview preparation""",
        "eligibility": """This course is ideal for:
- IT professionals looking to switch to cloud
- Developers wanting to learn DevOps
- System administrators
- Network engineers
- Anyone interested in cloud computing

Basic understanding of IT concepts is recommended.""",
        "training_schedule": """Weekdays: Mon-Fri (8-11 PM IST)
Weekends: Sat-Sun (9 AM-1 PM IST)
Start Date: Every Monday""",
        "start_date": "Every Monday",
        "next_batch": "Starting 15th June 2026",
        "exam_code": "CLD-001",
        "faq": """Q: Do I need prior cloud experience?|No, we start from basics. The course covers everything you need.
Q: What certifications are included?|AWS Solutions Architect and Azure Administrator prep included.
Q: How many projects will I work on?|12+ real-world projects including auto-scaling, load balancing, and more.
Q: Do you provide lab access?|Yes, free AWS and Azure lab access included.
Q: Is this suitable for beginners?|Yes, designed for both beginners and experienced professionals.""",
        "certification": "Yes, Certificate of Completion with unique ID",
        "why_join": """Expert Mentors|Learn from industry experts with 10+ years experience
12+ Live Projects|Work on real-world cloud projects
Certificate|Get recognized certificate upon completion
Lab Access|Free AWS and Azure lab access
24/7 Support|Round-the-clock doubt resolution""",
        "projects_list": """Deploy Scalable Web Application on AWS
Build CI/CD Pipeline with Jenkins
Containerize Application with Docker
Orchestrate with Kubernetes
Infrastructure as Code with Terraform
Serverless Application with Lambda
Build Multi-Cloud Architecture
Monitoring with CloudWatch
Auto-scaling Architecture
Load Balancer Configuration""",
        "benefits": """Live Instructor-Led Sessions
Hands-on Projects
Industry-Recognized Certificate
Resume Building & Mock Interviews
24/7 Support
Lifetime Access to Materials
Placement Assistance""",
        "tools_covered": "AWS, Azure, Docker, Kubernetes, Jenkins, Terraform, Ansible, Git, Linux, CloudWatch",
        "skills_covered": "AWS, Azure, Docker, Kubernetes, DevOps, CI/CD, Infrastructure as Code",
        "mode": "Live Online / Self-Paced",
        "language": "English"
    },
    "cyber-security": {
        "title": "Cyber Security Course",
        "tagline": "Learn Ethical Hacking, Penetration Testing & Network Security",
        "description": "Learn ethical hacking, penetration testing, network security & compliance. Hands-on labs with Kali Linux.",
        "overview": """The Cyber Security training program is designed to make you job-ready in one of the most in-demand fields in tech. This comprehensive course covers ethical hacking, penetration testing, network security, and compliance.

You will work on real-world security projects and learn to identify and mitigate vulnerabilities. The curriculum includes CEH certification prep.""",
        "key_benefits": """Master ethical hacking fundamentals
Learn penetration testing techniques
Understand network security architecture
Work with Kali Linux and Metasploit
Implement security controls
Conduct vulnerability assessments
Respond to security incidents
Understand compliance frameworks
Get career guidance and interview preparation""",
        "eligibility": """This course is ideal for:
- IT professionals looking to switch to security
- Network administrators
- System administrators
- Anyone interested in cyber security

Basic understanding of networking is recommended.""",
        "training_schedule": """Weekdays: Mon-Fri (7-10 PM IST)
Weekends: Sat-Sun (10 AM-2 PM IST)
Start Date: Every Monday""",
        "start_date": "Every Monday",
        "next_batch": "Starting 1st June 2026",
        "exam_code": "CYB-001",
        "faq": """Q: Do I need prior security experience?|No, we start from basics and build up gradually.
Q: What tools will I learn?|Kali Linux, Metasploit, Burp Suite, Wireshark, Nmap, and more.
Q: Are there hands-on labs?|Yes, 15+ hands-on labs and real-world scenarios.
Q: Is CEH certification included?|Yes, CEH exam prep is included in the course.
Q: Is this suitable for beginners?|Yes, designed for both beginners and experienced professionals.""",
        "certification": "Yes, Certificate of Completion with unique ID",
        "why_join": """Expert Mentors|Learn from industry experts with 10+ years experience
15+ Live Projects|Work on real-world security projects
Certificate|Get recognized certificate upon completion
CEH Prep|Included in curriculum
Lab Access|Free Kali Linux lab access""",
        "projects_list": """Network Security Assessment
Penetration Testing Project
Vulnerability Assessment
Security Incident Response
Web Application Security Testing
Social Engineering Awareness
Wireless Network Security
Buffer Overflow Exploit
Malware Analysis
Security Audit""",
        "benefits": """Live Instructor-Led Sessions
Hands-on Projects
Industry-Recognized Certificate
CEH Exam Prep
24/7 Support
Placement Assistance""",
        "tools_covered": "Kali Linux, Metasploit, Burp Suite, Wireshark, Nmap, Nessus, OpenVAS",
        "skills_covered": "Ethical Hacking, Penetration Testing, Network Security, Vulnerability Assessment, Incident Response",
        "mode": "Live Online / Self-Paced",
        "language": "English"
    },
    "web-development": {
        "title": "Full Stack Web Development",
        "tagline": "Master MERN Stack - React, Node.js, MongoDB, Express",
        "description": "Master MERN Stack — React, Node.js, MongoDB, Express. Build 10+ real-world projects including e-commerce platform.",
        "overview": """The Full Stack Web Development training program is designed to make you job-ready as a full-stack developer. This comprehensive course covers HTML, CSS, JavaScript, React, Node.js, MongoDB, and Express.

You will build 12+ real-world projects including an e-commerce platform, social media app, and REST APIs. The curriculum is designed by industry experts and updated regularly.""",
        "key_benefits": """Master HTML, CSS, and JavaScript
Build dynamic web applications with React
Create server-side applications with Node.js
Work with MongoDB database
Build REST APIs
Implement authentication and authorization
Deploy applications to production
Get career guidance and interview preparation""",
        "eligibility": """This course is ideal for:
- Beginners with no prior coding experience
- Anyone interested in web development
- Designers wanting to learn coding
- Students and professionals

No prior coding experience required.""",
        "training_schedule": """Weekdays: Mon-Fri (7-10 PM IST)
Weekends: Sat-Sun (10 AM-2 PM IST)
Start Date: Every Monday""",
        "start_date": "Every Monday",
        "next_batch": "Starting 1st June 2026",
        "exam_code": "WEB-001",
        "faq": """Q: Do I need prior coding experience?|No, we start from basics. HTML and CSS are covered first.
Q: How many projects will I build?|12+ real-world projects including e-commerce, social media, and more.
Q: What technologies will I learn?|React, Node.js, MongoDB, Express, JavaScript, HTML, CSS.
Q: Is deployment included?|Yes, deployment to Heroku and Vercel is covered.
Q: Can I get a job after this?|Yes, our placement team helps with job opportunities.""",
        "certification": "Yes, Certificate of Completion with unique ID",
        "why_join": """Expert Mentors|Learn from industry experts
12+ Live Projects|Build real-world applications
Certificate|Get recognized certificate upon completion
Placement|Get job assistance
24/7 Support|Round-the-clock doubt resolution""",
        "projects_list": """E-commerce Website
Social Media Application
Blog Platform
Todo Application
Weather App
Recipe App
Chat Application
Portfolio Website
Job Portal
Hospital Management System
Note Taking App
Task Manager""",
        "benefits": """Live Instructor-Led Sessions
Hands-on Projects
Industry-Recognized Certificate
Resume Building & Mock Interviews
24/7 Support
Placement Assistance""",
        "tools_covered": "HTML, CSS, JavaScript, React, Node.js, MongoDB, Express, Git, Heroku, Vercel",
        "skills_covered": "Full Stack Development, React, Node.js, MongoDB, REST APIs, Git",
        "mode": "Live Online / Self-Paced",
        "language": "English"
    },
    "digital-marketing": {
        "title": "Digital Marketing Course",
        "tagline": "Master SEO, Google Ads, Social Media Marketing & Analytics",
        "description": "Master SEO, Google Ads, Social Media Marketing, Analytics & Content Strategy. Run real campaigns with Google Ad credits.",
        "overview": """The Digital Marketing training program is designed to make you job-ready in digital marketing. This comprehensive course covers SEO, Google Ads, Social Media Marketing, Analytics, and Content Strategy.

You will run real campaigns with Google Ad credits and work on live projects. The curriculum is designed by industry experts and includes Google certification prep.""",
        "key_benefits": """Master SEO fundamentals
Learn Google Ads and PPC
Understand Social Media Marketing
Create effective content strategies
Analyze with Google Analytics
Implement email marketing campaigns
Get career guidance and interview preparation""",
        "eligibility": """This course is ideal for:
- Marketing professionals
- Business owners
- Students
- Anyone interested in digital marketing

No prior experience required.""",
        "training_schedule": """Weekdays: Mon-Fri (7-10 PM IST)
Weekends: Sat-Sun (10 AM-2 PM IST)
Start Date: Every Monday""",
        "start_date": "Every Monday",
        "next_batch": "Starting 1st June 2026",
        "exam_code": "DM-001",
        "faq": """Q: Do I need prior marketing experience?|No, we start from basics.
Q: Are Google Ads credits included?|Yes, ₹10,000 Google Ads credit included.
Q: How many projects will I work on?|6+ real campaigns and projects.
Q: What certifications are included?|Google Ads and Analytics certification prep.
Q: Is this suitable for beginners?|Yes, perfect for beginners.""",
        "certification": "Yes, Certificate of Completion with unique ID",
        "why_join": """Expert Mentors|Learn from industry experts
Google Ads Credit|₹10,000 credit included
Certificate|Get recognized certificate upon completion
6+ Live Projects|Work on real campaigns
Placement|Get job assistance""",
        "projects_list": """SEO Audit Project
Google Ads Campaign
Social Media Strategy
Content Marketing Plan
Email Marketing Campaign
Analytics Dashboard
Search Engine Optimization
PPC Campaign Management""",
        "benefits": """Live Instructor-Led Sessions
Hands-on Projects
Industry-Recognized Certificate
Google Ads Credit
24/7 Support
Placement Assistance""",
        "tools_covered": "Google Ads, Google Analytics, Facebook Ads, Instagram, LinkedIn, Twitter, Mailchimp, SEMrush",
        "skills_covered": "SEO, Google Ads, Social Media Marketing, Content Strategy, Analytics, Email Marketing",
        "mode": "Live Online / Self-Paced",
        "language": "English"
    },
    "business-analytics": {
        "title": "Business Analytics Course",
        "tagline": "Learn Excel, SQL, Tableau, Power BI & Statistical Analysis",
        "description": "Learn Excel, SQL, Tableau, Power BI & statistical analysis. Work on real business datasets.",
        "overview": """The Business Analytics training program is designed to make you job-ready as a business analyst. This comprehensive course covers Excel, SQL, Tableau, Power BI, and statistical analysis.

You will work on real business datasets from top companies and make data-driven decisions. The curriculum is designed by industry experts.""",
        "key_benefits": """Master Excel advanced functions
Learn SQL for data analysis
Create visualizations with Tableau
Build dashboards with Power BI
Understand statistical analysis
Make data-driven decisions
Get career guidance and interview preparation""",
        "eligibility": """This course is ideal for:
- Professionals looking to switch to analytics
- Business users
- Students
- Anyone interested in analytics

Basic computer knowledge is sufficient.""",
        "training_schedule": """Weekdays: Mon-Fri (7-10 PM IST)
Weekends: Sat-Sun (10 AM-2 PM IST)
Start Date: Every Monday""",
        "start_date": "Every Monday",
        "next_batch": "Starting 1st June 2026",
        "exam_code": "BA-001",
        "faq": """Q: Do I need prior analytics experience?|No, we start from basics.
Q: What tools will I learn?|Excel, SQL, Tableau, Power BI.
Q: How many projects will I work on?|8+ real business projects.
Q: Is Excel experience required?|No, Excel is taught from basics.
Q: Can I get a job after this?|Yes, high demand for business analysts.""",
        "certification": "Yes, Certificate of Completion with unique ID",
        "why_join": """Expert Mentors|Learn from industry experts
8+ Live Projects|Work on real business datasets
Certificate|Get recognized certificate upon completion
Placement|Get job assistance
24/7 Support|Round-the-clock doubt resolution""",
        "projects_list": """Sales Analytics Dashboard
Customer Segmentation Analysis
Financial Modeling Project
HR Analytics Dashboard
Marketing Campaign Analysis
Supply Chain Analytics
Risk Assessment Dashboard
Business Performance Report""",
        "benefits": """Live Instructor-Led Sessions
Hands-on Projects
Industry-Recognized Certificate
Resume Building
24/7 Support
Placement Assistance""",
        "tools_covered": "Excel, SQL, Tableau, Power BI, Python, Statistics",
        "skills_covered": "Business Analytics, Data Analysis, Visualization, SQL, Excel, Tableau, Power BI",
        "mode": "Live Online / Self-Paced",
        "language": "English"
    },
    "ui-ux-design": {
        "title": "UI/UX Design Course",
        "tagline": "Master Figma, Wireframing, Prototyping & User Research",
        "description": "Master Figma, wireframing, prototyping & user research. Build a professional 10+ piece design portfolio.",
        "overview": """The UI/UX Design training program is designed to make you job-ready as a designer. This comprehensive course covers Figma, wireframing, prototyping, and user research.

You will build a professional 10+ piece design portfolio with real client projects. The curriculum is designed by industry experts.""",
        "key_benefits": """Master Figma design tool
Create wireframes and prototypes
Conduct user research
Design mobile and web interfaces
Build design systems
Create a professional portfolio
Get career guidance and interview preparation""",
        "eligibility": """This course is ideal for:
- Design enthusiasts
- Developers wanting to design
- Students
- Anyone interested in design

No prior design experience required.""",
        "training_schedule": """Weekdays: Mon-Fri (7-10 PM IST)
Weekends: Sat-Sun (10 AM-2 PM IST)
Start Date: Every Monday""",
        "start_date": "Every Monday",
        "next_batch": "Starting 1st June 2026",
        "exam_code": "UX-001",
        "faq": """Q: Do I need design experience?|No, we start from basics.
Q: What tools will I learn?|Figma is the primary tool taught.
Q: How many projects will I build?|10+ portfolio projects.
Q: Is portfolio included?|Yes, you will have a professional portfolio.
Q: Can I get a job after this?|Yes, high demand for UI/UX designers.""",
        "certification": "Yes, Certificate of Completion with unique ID",
        "why_join": """Expert Mentors|Learn from industry experts
10+ Portfolio Projects|Build professional portfolio
Certificate|Get recognized certificate upon completion
Placement|Get job assistance
24/7 Support|Round-the-clock doubt resolution""",
        "projects_list": """Mobile App Design
Website Design
E-commerce Design
Dashboard Design
Landing Page Design
Social Media Design
Icon Set Design
Design System
User Research Report
Portfolio Website""",
        "benefits": """Live Instructor-Led Sessions
Hands-on Projects
Industry-Recognized Certificate
Professional Portfolio
24/7 Support
Placement Assistance""",
        "tools_covered": "Figma, Sketch, Adobe XD, Photoshop, Illustrator, Maze, Hotjar",
        "skills_covered": "UI Design, UX Design, Figma, Wireframing, Prototyping, User Research",
        "mode": "Live Online / Self-Paced",
        "language": "English"
    },
    "mobile-app-development": {
        "title": "Mobile App Development",
        "tagline": "Build iOS & Android Apps with React Native & Flutter",
        "description": "Build iOS & Android apps with React Native & Flutter. Publish to App Store & Google Play.",
        "overview": """The Mobile App Development training program is designed to make you job-ready as a mobile developer. This comprehensive course covers React Native and Flutter.

You will build and publish apps to both App Store and Google Play. The curriculum is designed by industry experts.""",
        "key_benefits": """Master React Native
Learn Flutter development
Build iOS and Android apps
Implement Firebase backend
Publish to App Store and Google Play
Create real-time features
Get career guidance and interview preparation""",
        "eligibility": """This course is ideal for:
- Developers wanting to build mobile apps
- Students
- Anyone interested in mobile development

Basic programming knowledge is helpful.""",
        "training_schedule": """Weekdays: Mon-Fri (7-10 PM IST)
Weekends: Sat-Sun (10 AM-2 PM IST)
Start Date: Every Monday""",
        "start_date": "Every Monday",
        "next_batch": "Starting 1st June 2026",
        "exam_code": "MOB-001",
        "faq": """Q: Do I need prior coding experience?|Basic programming knowledge helps, but we start from basics.
Q: What frameworks will I learn?|React Native and Flutter.
Q: How many apps will I build?|8+ complete mobile applications.
Q: Can I publish to stores?|Yes, we cover App Store and Google Play publishing.
Q: Is backend included?|Yes, Firebase backend is covered.""",
        "certification": "Yes, Certificate of Completion with unique ID",
        "why_join": """Expert Mentors|Learn from industry experts
8+ Live Projects|Build real mobile apps
Certificate|Get recognized certificate upon completion
Store Publishing|Learn to publish to stores
Placement|Get job assistance""",
        "projects_list": """E-commerce Mobile App
Social Media App
Chat Application
Fitness Tracking App
Food Delivery App
Music Player App
News Reader App
Todo List App""",
        "benefits": """Live Instructor-Led Sessions
Hands-on Projects
Industry-Recognized Certificate
Store Publishing
24/7 Support
Placement Assistance""",
        "tools_covered": "React Native, Flutter, Firebase, Xcode, Android Studio, Redux",
        "skills_covered": "Mobile Development, React Native, Flutter, iOS, Android, Firebase",
        "mode": "Live Online / Self-Paced",
        "language": "English"
    }
}

def update_courses():
    with app.app_context():
        for slug, data in course_data.items():
            course = Course.query.filter_by(slug=slug).first()
            if course:
                course.title = data.get('title', course.title)
                course.tagline = data.get('tagline', course.tagline or '')
                course.description = data.get('description', course.description)
                course.overview = data.get('overview', course.overview or '')
                course.key_benefits = data.get('key_benefits', course.key_benefits or '')
                course.eligibility = data.get('eligibility', course.eligibility or '')
                course.training_schedule = data.get('training_schedule', course.training_schedule or '')
                course.start_date = data.get('start_date', course.start_date or '')
                course.next_batch = data.get('next_batch', course.next_batch or '')
                course.exam_code = data.get('exam_code', course.exam_code or '')
                course.exam_questions = data.get('exam_questions', course.exam_questions or '')
                course.exam_duration = data.get('exam_duration', course.exam_duration or '')
                course.exam_passing_score = data.get('exam_passing_score', course.exam_passing_score or '')
                course.exam_format = data.get('exam_format', course.exam_format or '')
                course.exam_languages = data.get('exam_languages', course.exam_languages or '')
                course.course_objectives = data.get('course_objectives', course.course_objectives or '')
                course.faq = data.get('faq', course.faq or '')
                course.certification = data.get('certification', course.certification or '')
                course.why_join = data.get('why_join', course.why_join or '')
                course.projects_list = data.get('projects_list', course.projects_list or '')
                course.reviews_list = data.get('reviews_list', course.reviews_list or '')
                course.benefits = data.get('benefits', course.benefits or '')
                course.tools_covered = data.get('tools_covered', course.tools_covered or '')
                course.skills_covered = data.get('skills_covered', course.skills_covered or '')
                course.mode = data.get('mode', course.mode or '')
                course.language = data.get('language', course.language or 'English')
                
                print(f"Updated: {course.title}")
            else:
                print(f"Course not found: {slug}")
        
        db.session.commit()
        print("\nAll courses updated successfully!")

if __name__ == '__main__':
    update_courses()