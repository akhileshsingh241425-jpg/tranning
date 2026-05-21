import sys, os, json

sys.path.insert(0, os.path.dirname(__file__))
sys.stdout.reconfigure(encoding='utf-8')

from app import app, db, Course

# Add curriculum_html column if missing (for existing databases)
with app.app_context():
    try:
        import sqlalchemy
        insp = sqlalchemy.inspect(db.engine)
        if 'curriculum_html' not in [c['name'] for c in insp.get_columns('course')]:
            db.session.execute('ALTER TABLE course ADD COLUMN curriculum_html TEXT DEFAULT \'\'')
            db.session.commit()
            print("Added curriculum_html column")
    except Exception as e:
        print(f"Note: curriculum_html column check: {e}")

GENERAL_COURSES = [
  {
    "slug": "data-science-ai",
    "title": "Data Science & AI Master's Program",
    "tagline": "Become a Data Scientist — Learn Python, ML, Deep Learning & AI",
    "price": 199, "original_price": 999, "rating": 4.8, "reviews": 2840, "learners": "12,500+",
    "duration": "6 Months", "level": "Beginner to Advanced", "tag": "Popular",
    "modules": 6, "projects": 15,
    "instructor_name": "", "instructor_role": "", "instructor_experience": "",
    "curriculum": "Python, ML, Deep Learning, Data Analysis, NLP, Deployment",
    "is_published": True, "sort_order": 0,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Beginners and professionals who want to transition into data science",
    "eligibility": "No prior programming experience required! We start from Python basics.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "tools_covered": "Python, Pandas, NumPy, scikit-learn, TensorFlow, Keras, SQL, Tableau, Power BI",
    "skills_covered": "Data Science, Machine Learning, Deep Learning, Data Analysis, NLP",
    "certification": "Yes, Certificate of Completion",
    "key_benefits": "Master Python, Pandas, NumPy & data visualization libraries\nBuild ML models with scikit-learn & TensorFlow\nComplete 15+ real-world projects including capstone\nPlacement assistance with 200+ hiring partners\nLive instructor-led classes with doubt resolution\nEarn industry-recognized certificate",
    "why_join": "Industry-Recognized Certification|Gold standard for data science careers\nHands-on Projects|15+ real-world projects for your portfolio\nExpert Instructors|Learn from industry professionals\nCareer Support|Resume building and interview preparation",
    "benefits": "Live Instructor-Led Sessions\nHands-on Projects\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "category": "Data Science & AI",
    "technologies_list": "Python, Pandas, NumPy, scikit-learn, TensorFlow, Keras, SQL, Tableau, Power BI, Spark, AWS, Git",
    "detail_stats": json.dumps([{"number": "12,500+", "label": "Learners"}, {"number": "4.8", "label": "Rating"}, {"number": "180+", "label": "Hours Content"}, {"number": "15+", "label": "Projects"}]),
    "modules_detail": json.dumps([
      {"title": "Python for Data Science", "description": "Master Python programming, Pandas, NumPy, Matplotlib & Seaborn for data manipulation, analysis and visualization."},
      {"title": "Machine Learning", "description": "Learn supervised & unsupervised algorithms \u2014 regression, classification, clustering, ensemble methods & model evaluation."},
      {"title": "Deep Learning & Neural Networks", "description": "Build CNNs, RNNs & transformers with TensorFlow/Keras for image recognition, NLP & generative AI applications."},
      {"title": "Data Analysis & Visualization", "description": "Transform raw data into insights using EDA, statistical methods, interactive dashboards with Plotly & Tableau."},
      {"title": "Natural Language Processing", "description": "Process text data using NLP techniques \u2014 sentiment analysis, text classification, chatbots & LLM applications."},
      {"title": "ML Model Deployment", "description": "Deploy models using Flask, FastAPI & cloud platforms. Build end-to-end ML pipelines for production."}
    ]),
    "learning_path": json.dumps([
      {"step": 1, "title": "Python & Statistics", "description": "Master Python, statistics & probability \u2014 the foundation for all data science work."},
      {"step": 2, "title": "Data Analysis & SQL", "description": "Learn SQL, data wrangling, EDA & visualization techniques with real datasets."},
      {"step": 3, "title": "Machine Learning", "description": "Build predictive models \u2014 regression, classification, clustering & recommendation systems."},
      {"step": 4, "title": "Deep Learning & AI", "description": "Master neural networks, computer vision, NLP & generative AI technologies."},
      {"step": 5, "title": "Capstone Projects", "description": "Build 3 end-to-end projects solving real business problems for your portfolio."},
      {"step": 6, "title": "Interview & Placement Prep", "description": "Resume building, mock interviews, coding challenges & placement assistance."}
    ]),
    "faq": json.dumps([
      {"question": "Do I need prior programming experience?", "answer": "No! We start from Python basics and build up. Complete beginners are welcome."},
      {"question": "Is there placement assistance?", "answer": "Yes! We provide dedicated placement assistance including resume reviews, mock interviews, and direct referrals."},
      {"question": "What salary can I expect after completion?", "answer": "Entry-level data science roles start at $60,000-$90,000/year."},
      {"question": "Are classes live or recorded?", "answer": "Both! You get live instructor-led sessions plus recordings for revision."}
    ]),
    "topic_wise_content": json.dumps([
      {"heading": "Python for Data Science", "items": [
        {"title": "Python Fundamentals", "description": "Core Python programming concepts and syntax for data science workflows.", "subtopics": ["Variables & Data Types", "Control Flow & Loops", "Functions & Modules", "File Handling & Exceptions"]},
        {"title": "Data Manipulation with Pandas", "description": "Learn to work with DataFrames for data cleaning, transformation, and analysis.", "subtopics": ["DataFrames & Series", "Data Cleaning & Preprocessing", "Merging & Joining Data", "GroupBy Operations"]},
        {"title": "NumPy & Mathematical Computing", "description": "Perform efficient numerical computations with NumPy arrays.", "subtopics": ["Array Operations", "Linear Algebra", "Broadcasting", "Random Number Generation"]},
        {"title": "Data Visualization", "description": "Create compelling visualizations to communicate data insights.", "subtopics": ["Matplotlib Basics", "Seaborn Statistical Plots", "Plotly Interactive Charts"]}
      ]},
      {"heading": "Machine Learning & AI", "items": [
        {"title": "Supervised Learning", "description": "Build predictive models using regression and classification techniques.", "subtopics": ["Linear & Logistic Regression", "Decision Trees & Random Forest", "SVM & KNN", "Model Evaluation & Hyperparameter Tuning"]},
        {"title": "Unsupervised Learning", "description": "Discover patterns in data without labeled outcomes.", "subtopics": ["K-Means Clustering", "Hierarchical Clustering", "PCA & Dimensionality Reduction"]},
        {"title": "Deep Learning with TensorFlow", "description": "Build and train neural networks for complex AI tasks.", "subtopics": ["Neural Network Fundamentals", "CNNs for Image Recognition", "RNNs & LSTMs", "Transfer Learning"]},
        {"title": "Natural Language Processing", "description": "Process and analyze text data for various NLP applications.", "subtopics": ["Text Preprocessing", "Sentiment Analysis", "Named Entity Recognition", "Transformers & BERT"]}
      ]}
    ])
  },
  {
    "slug": "cloud-computing-devops",
    "title": "Cloud Computing & DevOps Engineer",
    "tagline": "Master AWS, Azure, Docker, Kubernetes & CI/CD Pipelines",
    "price": 179, "original_price": 999, "rating": 4.7, "reviews": 1950, "learners": "9,800+",
    "duration": "5 Months", "level": "Intermediate", "tag": "Popular",
    "modules": 6, "projects": 12,
    "instructor_name": "", "instructor_role": "", "instructor_experience": "",
    "curriculum": "AWS, Azure, Docker, Kubernetes, CI/CD, Linux",
    "is_published": True, "sort_order": 0,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "IT professionals looking to transition into cloud and DevOps roles",
    "eligibility": "Basic programming knowledge recommended. Familiarity with any programming language is sufficient.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "tools_covered": "AWS, Azure, Docker, Kubernetes, Terraform, Jenkins, Ansible, Linux, Git",
    "skills_covered": "Cloud Architecture, DevOps, Containerization, CI/CD, IaC",
    "certification": "Yes, Certificate of Completion",
    "key_benefits": "Master AWS, Azure & GCP cloud platforms\nLearn Docker, Kubernetes & container orchestration\nBuild CI/CD pipelines with Jenkins, GitHub Actions\nAWS Solutions Architect certification prep\nInfrastructure as Code with Terraform & Ansible\nPlacement support with cloud-focused companies",
    "why_join": "Industry-Valued Credential|Cloud skills are in highest demand\nHands-on Labs|Practice on real cloud environments\nComprehensive Curriculum|Covers all major cloud platforms\nCareer Growth|Highest paid IT roles",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "category": "Cloud Computing",
    "technologies_list": "AWS, Azure, Docker, Kubernetes, Terraform, Jenkins, Ansible, Linux, Python, Git, Prometheus, Grafana",
    "detail_stats": json.dumps([{"number": "9,800+", "label": "Learners"}, {"number": "4.7", "label": "Rating"}, {"number": "150+", "label": "Hours Content"}, {"number": "12+", "label": "Projects"}]),
    "modules_detail": json.dumps([
      {"title": "AWS Cloud Services", "description": "Master EC2, S3, Lambda, RDS, VPC, IAM & 30+ AWS services."},
      {"title": "Azure & Multi-Cloud", "description": "Learn Azure VMs, App Service, AKS & multi-cloud strategies."},
      {"title": "Docker & Containerization", "description": "Build, ship & run containerized applications."},
      {"title": "Kubernetes Orchestration", "description": "Deploy & manage containers at scale with K8s."},
      {"title": "CI/CD & Automation", "description": "Build automated pipelines with Jenkins, GitHub Actions."},
      {"title": "Linux & Scripting", "description": "Master Linux administration, Bash scripting, Python automation."}
    ]),
    "learning_path": json.dumps([
      {"step": 1, "title": "Linux & Networking", "description": "Master Linux commands, networking fundamentals, and shell scripting basics."},
      {"step": 2, "title": "AWS Cloud Mastery", "description": "Learn 30+ AWS services, cloud architecture patterns, and security best practices."},
      {"step": 3, "title": "Containers & Docker", "description": "Containerize applications with Docker, understand microservices architecture."},
      {"step": 4, "title": "Kubernetes & Orchestration", "description": "Deploy, scale & manage containerized apps with Kubernetes in production."},
      {"step": 5, "title": "CI/CD & IaC", "description": "Build end-to-end automated pipelines and manage infrastructure with Terraform."},
      {"step": 6, "title": "Certification & Placement", "description": "Prepare for AWS/Azure certifications and get dedicated placement support."}
    ]),
    "faq": json.dumps([
      {"question": "Do I need coding experience?", "answer": "Basic programming knowledge helps, but we cover Linux and scripting from scratch."},
      {"question": "Which cloud certification is included?", "answer": "We prepare you for AWS Solutions Architect Associate and Azure Administrator certifications."},
      {"question": "What job roles can I target?", "answer": "Cloud Engineer, DevOps Engineer, SRE, Cloud Architect - $70,000-$180,000/year."},
      {"question": "Is hands-on lab access provided?", "answer": "Yes! You get free AWS/Azure lab credits to practice on real cloud environments."}
    ]),
    "topic_wise_content": json.dumps([
      {"heading": "AWS Cloud Services", "items": [
        {"title": "EC2 & Compute Services", "description": "Launch and manage virtual servers, auto-scaling, and load balancing on AWS.", "subtopics": ["EC2 Instance Types & Launching", "Auto Scaling Groups", "Elastic Load Balancing", "AWS Lambda Serverless"]},
        {"title": "S3 & Storage", "description": "Object storage solutions for backup, archival, and application data.", "subtopics": ["S3 Buckets & Objects", "EBS Volumes", "EFS File System", "Glacier Archive Storage"]},
        {"title": "VPC & Networking", "description": "Private network isolation and secure connectivity in AWS.", "subtopics": ["VPC Creation & Subnets", "Security Groups & NACLs", "Route Tables & Internet Gateways", "VPN & Direct Connect"]},
        {"title": "IAM & Security", "description": "Identity management and access control for AWS resources.", "subtopics": ["Users, Groups & Roles", "Policies & Permissions", "MFA & Root Account Protection"]}
      ]},
      {"heading": "Docker & Kubernetes", "items": [
        {"title": "Docker Fundamentals", "description": "Containerize applications and build production-ready Docker images.", "subtopics": ["Dockerfile Best Practices", "Docker Compose Multi-Container", "Image Optimization", "Docker Networking & Volumes"]},
        {"title": "Kubernetes Orchestration", "description": "Deploy and manage containerized applications at scale.", "subtopics": ["Pods, Deployments & Services", "ConfigMaps & Secrets", "Ingress Controllers", "Helm Charts"]},
        {"title": "CI/CD Pipelines", "description": "Automate the software delivery process with modern tools.", "subtopics": ["Jenkins Pipeline Creation", "GitHub Actions Workflows", "ArgoCD & GitOps", "Automated Testing in Pipelines"]}
      ]}
    ])
  },
  {
    "slug": "cyber-security",
    "title": "Cyber Security Professional",
    "tagline": "Learn Ethical Hacking, Penetration Testing & Security Operations",
    "price": 189, "original_price": 999, "rating": 4.8, "reviews": 1620, "learners": "7,200+",
    "duration": "5 Months", "level": "Beginner to Advanced", "tag": "Popular",
    "modules": 6, "projects": 20,
    "instructor_name": "", "instructor_role": "", "instructor_experience": "",
    "curriculum": "Ethical Hacking, Network Security, App Security, SOC, Compliance, Forensics",
    "is_published": True, "sort_order": 0,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "IT professionals wanting to transition into cybersecurity",
    "eligibility": "Basic computer knowledge is enough. We cover networking and OS fundamentals first.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "tools_covered": "Kali Linux, Metasploit, Burp Suite, Wireshark, Nmap, Splunk, Nessus, Snort",
    "skills_covered": "Ethical Hacking, Penetration Testing, Network Security, SOC Operations",
    "certification": "Yes, Certificate of Completion",
    "key_benefits": "Learn ethical hacking & penetration testing with hands-on labs\nMaster network security & firewall management\nCEH & CompTIA Security+ certification prep\nHands-on labs with real attack/defense scenarios\nLearn SIEM, SOC operations & incident response\nPlacement assistance in cybersecurity roles",
    "why_join": "Industry Standard|CEH and Security+ certified curriculum\nHands-on Labs|Real attack/defense scenarios in our cyber range\nExpert Instructors|Learn from certified security professionals\nCareer Boost|Fastest growing IT field",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "category": "Cyber Security",
    "technologies_list": "Kali Linux, Metasploit, Burp Suite, Wireshark, Nmap, Splunk, Nessus, Snort, Python, PowerShell, AWS Security, OWASP",
    "detail_stats": json.dumps([{"number": "7,200+", "label": "Learners"}, {"number": "4.8", "label": "Rating"}, {"number": "160+", "label": "Hours Content"}, {"number": "20+", "label": "Lab Exercises"}]),
    "modules_detail": json.dumps([
      {"title": "Ethical Hacking & Pen Testing", "description": "Learn reconnaissance, scanning, exploitation & reporting using Kali Linux, Metasploit, Burp Suite & Nmap."},
      {"title": "Network Security", "description": "Master firewalls, IDS/IPS, VPNs, network monitoring & defense against DDoS, MITM & other attacks."},
      {"title": "Application Security", "description": "Understand OWASP Top 10, web app vulnerabilities, API security, secure coding & security testing tools."},
      {"title": "Security Operations (SOC)", "description": "Learn SIEM tools (Splunk, ELK), log analysis, threat hunting, incident detection & response workflows."},
      {"title": "Compliance & Governance", "description": "Understand ISO 27001, GDPR, PCI-DSS, risk assessment frameworks & security audit procedures."},
      {"title": "Digital Forensics", "description": "Investigate security incidents \u2014 disk forensics, memory analysis, malware analysis & evidence preservation."}
    ]),
    "learning_path": json.dumps([
      {"step": 1, "title": "Security Fundamentals", "description": "Learn networking basics, operating system security & cryptography foundations."},
      {"step": 2, "title": "Ethical Hacking", "description": "Master reconnaissance, scanning, exploitation with hands-on Kali Linux labs."},
      {"step": 3, "title": "Network & App Security", "description": "Defend networks and applications against common attack vectors."},
      {"step": 4, "title": "SOC & Incident Response", "description": "Operate SIEM tools, analyze threats, and respond to security incidents."},
      {"step": 5, "title": "Advanced Topics", "description": "Cloud security, mobile security, IoT security & emerging threat landscape."},
      {"step": 6, "title": "Certification & Career", "description": "CEH/Security+ exam preparation and dedicated placement support."}
    ]),
    "faq": json.dumps([
      {"question": "Is this legal to learn?", "answer": "Absolutely! Ethical hacking is a legitimate and highly sought-after skill."},
      {"question": "What certifications does this prepare for?", "answer": "CEH (Certified Ethical Hacker), CompTIA Security+, and foundational knowledge for CISSP and OSCP."},
      {"question": "What salary can cybersecurity professionals expect?", "answer": "Entry-level roles start at $55,000-$80,000/year."},
      {"question": "Do I need a technical background?", "answer": "Basic computer knowledge is enough. We cover networking and OS fundamentals."}
    ]),
    "topic_wise_content": json.dumps([])
  },
  {
    "slug": "web-development",
    "title": "Full Stack Web Development",
    "tagline": "Master MERN Stack \u2014 React, Node.js, MongoDB & Express",
    "price": 149, "original_price": 799, "rating": 4.9, "reviews": 3200, "learners": "15,000+",
    "duration": "6 Months", "level": "Beginner to Advanced", "tag": "Popular",
    "modules": 6, "projects": 10,
    "instructor_name": "", "instructor_role": "", "instructor_experience": "",
    "curriculum": "HTML/CSS, JavaScript, React, Node.js, MongoDB, Deployment",
    "is_published": True, "sort_order": 0,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Beginners wanting to become full-stack developers",
    "eligibility": "No prior coding experience required! Starts from HTML basics.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "tools_covered": "HTML5, CSS3, JavaScript, React, Node.js, Express, MongoDB, Git, Docker, Tailwind CSS",
    "skills_covered": "Full Stack Development, MERN Stack, Responsive Design, Deployment",
    "certification": "Yes, Certificate of Completion",
    "key_benefits": "Build 10+ real-world projects for your portfolio\nMaster React, Node.js, Express & MongoDB (MERN)\nLearn responsive design & mobile-first development\nDeploy projects on AWS, Vercel & Netlify\nMaster Git, GitHub & collaboration workflows\nJob-ready with resume building & mock interviews",
    "why_join": "Comprehensive Curriculum|Covers entire MERN stack\nHands-on Projects|10+ real-world projects\nExpert Instructors|Industry professionals\nCareer Support|100% placement assistance",
    "benefits": "Live Instructor-Led Sessions\nHands-on Projects\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "category": "Web Development",
    "technologies_list": "HTML5, CSS3, JavaScript, React, Next.js, Node.js, Express, MongoDB, PostgreSQL, Git, Docker, Tailwind CSS, TypeScript",
    "detail_stats": json.dumps([{"number": "15,000+", "label": "Learners"}, {"number": "4.9", "label": "Rating"}, {"number": "200+", "label": "Hours Content"}, {"number": "10+", "label": "Projects"}]),
    "modules_detail": json.dumps([
      {"title": "HTML5, CSS3 & JavaScript", "description": "Build responsive websites with semantic HTML, modern CSS & ES6+ JavaScript."},
      {"title": "React.js & Frontend", "description": "Master React components, hooks, state management, React Router & Next.js."},
      {"title": "Node.js & Express Backend", "description": "Build RESTful APIs, middleware, authentication, file uploads & real-time features."},
      {"title": "MongoDB & SQL Databases", "description": "Design schemas, write queries, CRUD operations, aggregation pipelines."},
      {"title": "Advanced CSS & Frameworks", "description": "Master Tailwind CSS, Bootstrap, CSS-in-JS, Sass preprocessors."},
      {"title": "Deployment & DevOps Basics", "description": "Deploy on Vercel, Netlify, AWS. Learn Docker, CI/CD, production monitoring."}
    ]),
    "learning_path": json.dumps([
      {"step": 1, "title": "Web Foundations", "description": "Master HTML, CSS & JavaScript fundamentals with 5+ mini-projects."},
      {"step": 2, "title": "Frontend with React", "description": "Build interactive SPAs with React, routing, state management & API integration."},
      {"step": 3, "title": "Backend with Node.js", "description": "Create server-side applications, REST APIs & database integrations."},
      {"step": 4, "title": "Full Stack Projects", "description": "Build e-commerce, social media & dashboard apps."},
      {"step": 5, "title": "Advanced & Testing", "description": "Learn TypeScript, testing, performance optimization & security."},
      {"step": 6, "title": "Portfolio & Placement", "description": "Build portfolio, prepare for interviews & apply to jobs."}
    ]),
    "faq": json.dumps([
      {"question": "Can a complete beginner join?", "answer": "Yes! This course starts from HTML basics."},
      {"question": "What job roles can I get?", "answer": "Frontend, Backend, Full Stack Developer - $50,000-$120,000/year."},
      {"question": "How are classes conducted?", "answer": "Live instructor-led sessions with recordings available."},
      {"question": "Do you provide placement support?", "answer": "Yes! 100% placement assistance with resume prep and mock interviews."}
    ]),
    "topic_wise_content": json.dumps([])
  },
  {
    "slug": "digital-marketing",
    "title": "Digital Marketing Specialist",
    "tagline": "Master SEO, Google Ads, Social Media & Analytics \u2014 Get Certified",
    "price": 119, "original_price": 599, "rating": 4.7, "reviews": 2100, "learners": "18,000+",
    "duration": "4 Months", "level": "Beginner", "tag": "Popular",
    "modules": 6, "projects": 10,
    "instructor_name": "", "instructor_role": "", "instructor_experience": "",
    "curriculum": "SEO, Google Ads, Social Media, Email Marketing, Analytics, Content Strategy",
    "is_published": True, "sort_order": 0,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Complete beginners who want to start a digital marketing career",
    "eligibility": "No marketing background required. Designed for complete beginners.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "tools_covered": "Google Analytics 4, Google Ads, SEMrush, Ahrefs, Mailchimp, HubSpot, Meta Ads Manager",
    "skills_covered": "SEO, SEM, Social Media Marketing, Email Marketing, Analytics, Content Strategy",
    "certification": "Yes, Certificate of Completion",
    "key_benefits": "Google Ads & Google Analytics certification prep\nWork on live campaigns with real budgets\nMaster SEO, SEM, SMM & content marketing\nLearn marketing automation & email marketing\nBuild data-driven strategies with analytics\nFreelance-ready with client management skills",
    "why_join": "Certification Prep|Google and HubSpot certifications included\nLive Campaigns|Work on real campaigns with real budgets\nComprehensive|All digital marketing channels covered\nCareer Ready|Freelance or corporate career paths",
    "benefits": "Live Instructor-Led Sessions\nHands-on Campaigns\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "category": "Digital Marketing",
    "technologies_list": "Google Analytics 4, Google Ads, SEMrush, Ahrefs, Mailchimp, HubSpot, Meta Ads Manager, Canva, WordPress",
    "detail_stats": json.dumps([{"number": "18,000+", "label": "Learners"}, {"number": "4.7", "label": "Rating"}, {"number": "120+", "label": "Hours Content"}, {"number": "10+", "label": "Live Projects"}]),
    "modules_detail": json.dumps([
      {"title": "SEO & Content Strategy", "description": "Learn keyword research, on-page/off-page SEO, technical SEO, content planning & link building."},
      {"title": "Google Ads & PPC", "description": "Master campaign setup, audience targeting, ad copywriting, bidding strategies, conversion tracking."},
      {"title": "Social Media Marketing", "description": "Build strategies for Instagram, LinkedIn, Facebook & YouTube."},
      {"title": "Email Marketing & CRM", "description": "Create automated sequences, drip campaigns, segmentation & A/B testing."},
      {"title": "Analytics & Performance", "description": "Master Google Analytics 4, Meta Pixel, UTM tracking, attribution modeling."},
      {"title": "Content & Brand Strategy", "description": "Develop content calendars, write compelling copy, create video content plans."}
    ]),
    "learning_path": json.dumps([
      {"step": 1, "title": "Marketing Fundamentals", "description": "Learn digital marketing landscape, customer journey & funnel strategies."},
      {"step": 2, "title": "SEO & Content", "description": "Master organic growth through search engine optimization & content marketing."},
      {"step": 3, "title": "Paid Advertising", "description": "Run Google Ads & social media advertising campaigns with live budgets."},
      {"step": 4, "title": "Social & Email", "description": "Build social media presence & automated email marketing systems."},
      {"step": 5, "title": "Analytics & Optimization", "description": "Measure, analyze & optimize campaigns using data-driven approaches."},
      {"step": 6, "title": "Portfolio & Freelancing", "description": "Build case studies, prepare for certifications & learn freelance skills."}
    ]),
    "faq": json.dumps([
      {"question": "Do I need a marketing background?", "answer": "Not at all! Designed for complete beginners."},
      {"question": "Will I get Google certified?", "answer": "Yes! We prepare you for Google Analytics and Google Ads certifications."},
      {"question": "Can I use this for my own business?", "answer": "Absolutely! Every technique is immediately applicable."}
    ]),
    "topic_wise_content": json.dumps([])
  },
  {
    "slug": "business-analytics",
    "title": "Business Analytics & Intelligence",
    "tagline": "Master Excel, SQL, Tableau, Power BI & Statistical Analysis",
    "price": 139, "original_price": 699, "rating": 4.6, "reviews": 1200, "learners": "8,500+",
    "duration": "4 Months", "level": "Beginner to Intermediate", "tag": "",
    "modules": 6, "projects": 8,
    "instructor_name": "", "instructor_role": "", "instructor_experience": "",
    "curriculum": "Excel, SQL, Tableau, Power BI, Python, Statistics",
    "is_published": True, "sort_order": 0,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Professionals who want to become data-driven decision makers",
    "eligibility": "No programming background required. Start with Excel and SQL.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "tools_covered": "Excel, SQL, Tableau, Power BI, Python, Pandas, R, SPSS, Google Sheets, Looker",
    "skills_covered": "Business Analytics, Data Visualization, Statistical Analysis, SQL",
    "certification": "Yes, Certificate of Completion",
    "key_benefits": "Master Excel, SQL, Tableau & Power BI\nLearn Python for business analytics\nBuild interactive dashboards & reports\nUnderstand statistics & data storytelling\nIndustry case studies from real companies\nCertification valued by consulting firms",
    "why_join": "Practical Skills|Immediately applicable to any business role\nIndustry Tools|Master the most in-demand analytics tools\nCase Studies|Real business problems from multiple industries\nCareer Growth|High demand across all sectors",
    "benefits": "Live Instructor-Led Sessions\nHands-on Projects\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "category": "Data Science & AI",
    "technologies_list": "Excel, SQL, Tableau, Power BI, Python, Pandas, R, SPSS, Google Sheets, Looker",
    "detail_stats": json.dumps([{"number": "8,500+", "label": "Learners"}, {"number": "4.6", "label": "Rating"}, {"number": "100+", "label": "Hours Content"}, {"number": "8+", "label": "Case Studies"}]),
    "modules_detail": json.dumps([
      {"title": "Advanced Excel & VBA", "description": "Master pivot tables, VLOOKUP, Power Query, macros & VBA automation."},
      {"title": "SQL for Business", "description": "Write complex queries, join tables, aggregate data, create views."},
      {"title": "Tableau & Power BI", "description": "Build interactive dashboards and automated reports."},
      {"title": "Python for Analytics", "description": "Use Python with Pandas & Matplotlib for data analysis and automation."},
      {"title": "Statistical Analysis", "description": "Learn hypothesis testing, regression analysis, A/B testing, forecasting."},
      {"title": "Business Case Studies", "description": "Solve real-world problems from e-commerce, banking, healthcare."}
    ]),
    "learning_path": json.dumps([
      {"step": 1, "title": "Excel & Data Basics", "description": "Master advanced Excel, data cleaning & fundamental analytics concepts."},
      {"step": 2, "title": "SQL & Databases", "description": "Query relational databases & extract business insights."},
      {"step": 3, "title": "Visualization Tools", "description": "Build dashboards with Tableau & Power BI."},
      {"step": 4, "title": "Statistics & Python", "description": "Apply statistical methods & Python for deeper analysis."},
      {"step": 5, "title": "Industry Projects", "description": "Solve real business problems across different domains."},
      {"step": 6, "title": "Career Preparation", "description": "Build portfolio, practice case interviews & get placement support."}
    ]),
    "faq": json.dumps([
      {"question": "Who is this course for?", "answer": "Anyone wanting to make data-driven decisions."},
      {"question": "Do I need programming skills?", "answer": "No! Start with Excel and SQL which require no programming."},
      {"question": "How is this different from Data Science?", "answer": "Business Analytics focuses on dashboards & decisions, Data Science goes deeper into ML/AI."}
    ]),
    "topic_wise_content": json.dumps([])
  },
  {
    "slug": "ui-ux-design",
    "title": "UI/UX Design Professional",
    "tagline": "Master Figma, User Research, Wireframing & Prototyping",
    "price": 129, "original_price": 599, "rating": 4.8, "reviews": 980, "learners": "6,200+",
    "duration": "4 Months", "level": "Beginner", "tag": "",
    "modules": 6, "projects": 8,
    "instructor_name": "", "instructor_role": "", "instructor_experience": "",
    "curriculum": "Figma, User Research, Wireframing, Visual Design, Design Systems, Portfolio",
    "is_published": True, "sort_order": 0,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Beginners who want to launch a design career",
    "eligibility": "No artistic skills required. UI/UX is about problem-solving, not drawing.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "tools_covered": "Figma, Adobe XD, Sketch, InVision, Maze, Hotjar, Miro, Notion, Framer",
    "skills_covered": "UI Design, UX Research, Prototyping, Design Systems, Visual Design",
    "certification": "Yes, Certificate of Completion",
    "key_benefits": "Master Figma \u2014 the industry standard design tool\nLearn user research, personas & journey mapping\nBuild interactive prototypes & design systems\nCreate 8+ portfolio projects\nUnderstand accessibility & responsive design\nPlacement assistance for product design roles",
    "why_join": "Industry Tools|Master Figma and industry-standard tools\nPortfolio Focus|Build 8+ projects for your portfolio\nUser-Centered|Learn research-driven design process\nCareer Ready|Product design roles at top companies",
    "benefits": "Live Instructor-Led Sessions\nHands-on Projects\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "category": "Design",
    "technologies_list": "Figma, Adobe XD, Sketch, InVision, Maze, Hotjar, Miro, Notion, Framer",
    "detail_stats": json.dumps([{"number": "6,200+", "label": "Learners"}, {"number": "4.8", "label": "Rating"}, {"number": "100+", "label": "Hours Content"}, {"number": "8+", "label": "Projects"}]),
    "modules_detail": json.dumps([
      {"title": "Figma Mastery", "description": "Learn auto-layout, components, variants, design tokens, prototyping & collaboration."},
      {"title": "User Research & Testing", "description": "Conduct user interviews, surveys, usability testing, create personas & journey maps."},
      {"title": "Wireframing & Prototyping", "description": "Create low-fidelity wireframes, high-fidelity mockups & interactive prototypes."},
      {"title": "Visual Design", "description": "Master color theory, typography, spacing, iconography & visual hierarchy."},
      {"title": "Design Systems", "description": "Build scalable component libraries, style guides & design tokens."},
      {"title": "Portfolio & Case Studies", "description": "Document your design process in compelling case studies."}
    ]),
    "learning_path": json.dumps([
      {"step": 1, "title": "Design Fundamentals", "description": "Learn core design principles \u2014 balance, contrast, hierarchy, alignment."},
      {"step": 2, "title": "Figma & Tools", "description": "Get hands-on with Figma through guided exercises."},
      {"step": 3, "title": "UX Research", "description": "Conduct user research, create personas, journey maps."},
      {"step": 4, "title": "UI Design", "description": "Design beautiful interfaces for web & mobile."},
      {"step": 5, "title": "Prototyping & Testing", "description": "Build interactive prototypes and conduct usability tests."},
      {"step": 6, "title": "Portfolio Building", "description": "Create detailed case studies and portfolio website."}
    ]),
    "faq": json.dumps([
      {"question": "Do I need artistic skills?", "answer": "No! UI/UX is about problem-solving, not drawing."},
      {"question": "What tools do I need?", "answer": "Just a laptop and internet! Figma is free."},
      {"question": "What is the career outlook?", "answer": "Entry-level salaries start at $55,000-$80,000/year."}
    ]),
    "topic_wise_content": json.dumps([])
  },
  {
    "slug": "mobile-app-development",
    "title": "Mobile App Development",
    "tagline": "Build Professional iOS & Android Apps with React Native & Flutter",
    "price": 179, "original_price": 899, "rating": 4.7, "reviews": 850, "learners": "5,400+",
    "duration": "5 Months", "level": "Intermediate", "tag": "",
    "modules": 6, "projects": 5,
    "instructor_name": "", "instructor_role": "", "instructor_experience": "",
    "curriculum": "React Native, Flutter, Firebase, Mobile UI/UX, Advanced Features, App Store",
    "is_published": True, "sort_order": 0,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Developers who want to build cross-platform mobile apps",
    "eligibility": "JavaScript knowledge recommended for React Native.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "tools_covered": "React Native, Flutter, Dart, Firebase, Redux, TypeScript, Expo, SQLite, GraphQL",
    "skills_covered": "Mobile App Development, React Native, Flutter, Cross-Platform Development",
    "certification": "Yes, Certificate of Completion",
    "key_benefits": "Build cross-platform apps with React Native & Flutter\nLearn mobile UI/UX patterns & navigation\nIntegrate APIs, Firebase & push notifications\nPublish apps to App Store & Google Play\nBuild 5+ portfolio-ready mobile apps\nPlacement support for mobile developer roles",
    "why_join": "Dual Framework|Master both React Native and Flutter\nCross-Platform|Build for iOS and Android from single codebase\nApp Store Ready|Publish your apps to both stores\nCareer Boost|High demand for mobile developers",
    "benefits": "Live Instructor-Led Sessions\nHands-on Projects\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "category": "Mobile Development",
    "technologies_list": "React Native, Flutter, Dart, Firebase, Redux, TypeScript, Expo, SQLite, GraphQL, Xcode, Android Studio",
    "detail_stats": json.dumps([{"number": "5,400+", "label": "Learners"}, {"number": "4.7", "label": "Rating"}, {"number": "140+", "label": "Hours Content"}, {"number": "5+", "label": "App Projects"}]),
    "modules_detail": json.dumps([
      {"title": "React Native Development", "description": "Build cross-platform apps with React Native \u2014 components, navigation, state management."},
      {"title": "Flutter & Dart", "description": "Create beautiful apps with Flutter \u2014 widget composition, state management."},
      {"title": "Backend & Firebase", "description": "Integrate REST/GraphQL APIs, Firebase Auth, Firestore, Cloud Functions."},
      {"title": "Mobile UI/UX Patterns", "description": "Implement iOS and Material Design guidelines."},
      {"title": "Advanced Features", "description": "Add push notifications, camera, geolocation, maps, payments."},
      {"title": "App Store Deployment", "description": "Complete deployment process \u2014 app signing, store listings, review guidelines."}
    ]),
    "learning_path": json.dumps([
      {"step": 1, "title": "Mobile Fundamentals", "description": "Understand mobile development concepts and framework basics."},
      {"step": 2, "title": "UI Development", "description": "Build mobile interfaces with navigation and responsive layouts."},
      {"step": 3, "title": "State & API Integration", "description": "Master state management, APIs, Firebase & local storage."},
      {"step": 4, "title": "Native Features", "description": "Access camera, location, notifications & other device capabilities."},
      {"step": 5, "title": "Testing & Optimization", "description": "Test, debug & optimize app performance across devices."},
      {"step": 6, "title": "Publishing & Career", "description": "Deploy to stores, build portfolio & prepare for interviews."}
    ]),
    "faq": json.dumps([
      {"question": "React Native or Flutter?", "answer": "We cover both! Knowing both makes you versatile."},
      {"question": "Do I need a Mac?", "answer": "For React Native with Expo, you can develop on Windows."},
      {"question": "What prior knowledge is needed?", "answer": "JavaScript knowledge recommended for React Native."}
    ]),
    "topic_wise_content": json.dumps([])
  }
]

COMPTIA_COURSES = [
  {
    "slug": "comptia-a-plus",
    "title": "CompTIA A+ Certification Training",
    "tagline": "Start your IT career with CompTIA A+ certification",
    "price": 399, "original_price": 999, "rating": 4.7, "reviews": 2840, "learners": "15,000+",
    "duration": "4 Months", "level": "Beginner", "tag": "Bestseller",
    "modules": 10, "projects": 8,
    "instructor_name": "Dr. Amit Sharma", "instructor_role": "CompTIA Certified Trainer | 14+ Years",
    "instructor_experience": "14+ years",
    "curriculum": "Hardware, Networking, OS, Security, Troubleshooting",
    "is_published": True, "sort_order": 1,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Individuals interested in pursuing a profession in IT\nIndividuals who want to get their CompTIA A+ certification",
    "eligibility": "Anyone with basic computer knowledge is eligible to apply for this certification.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "220-1101 & 220-1102",
    "tools_covered": "Windows, Linux, macOS, Cisco CLI, Wireshark, Multimeter",
    "skills_covered": "Hardware Troubleshooting, OS Administration, Networking, Security, Cloud Computing",
    "certification": "Yes, Certificate of Completion. Prepares for CompTIA A+ (220-1101 & 220-1102) exams.",
    "key_benefits": "Prepare and pass the CompTIA A+ certification exams\nInstall and configure PC systems and peripheral devices\nTroubleshoot internal system components\nUnderstand network infrastructure concepts\nLearn laptop and mobile device support\nMaster printer setup and troubleshooting\nUnderstand virtualization and cloud computing\nLearn security best practices for devices and networks",
    "why_join": "Industry-Recognized Certification|CompTIA A+ is the gold standard for IT careers\nHands-on Labs|Practice with real hardware and software simulations\nExpert Instructors|Learn from certified professionals with years of experience\nCareer Support|Resume building and interview preparation included",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "course_objectives": json.dumps(["Prepare and pass the CompTIA A+ certification exams","Install and configure the components of the PC system and peripheral devices","Install, configure, and troubleshoot internal system components","Understand how to identify, use, and connect hardware components and devices","Understand the concepts of network infrastructure","Understand how to set up network connections and troubleshoot them","Learn laptop support and troubleshooting","Understand how to troubleshoot and support mobile devices","Learn to configure and troubleshoot printing devices","Implement client virtualization and cloud computing","Identify and defend devices against security risks"]),
    "prerequisites": "Anyone with basic computer knowledge is eligible. No prior IT experience required.",
    "category": "Cyber Security",
    "topic_wise_content": json.dumps([
      {"heading": "CompTIA A+ 220-1101 (Core 1) Domains", "items": [
        {"title": "Domain 1: Mobile devices (13%)", "description": "Hardware setup: installing components like batteries, cameras, and Wi-Fi antennas.", "subtopics": ["Hardware setup: installing components like batteries, cameras, and Wi-Fi antennas", "Accessory options: configuring USB, Bluetooth, NFC, and docking stations", "Network setup: configuring Wi-Fi, Bluetooth, cellular data, and synchronization settings", "Troubleshooting: identifying and fixing hardware and connectivity issues"]},
        {"title": "Domain 2: Networking (23%)", "description": "Protocols and ports: learning about networking protocols, ports, and wireless technologies.", "subtopics": ["Protocols and ports: learning about networking protocols, ports, and wireless technologies", "SOHO networks: setting up small office/home office networks, including IP addressing and VPNs", "Networking tools: troubleshooting with crimpers, cable testers, and Wi-Fi analyzers"]},
        {"title": "Domain 3: Hardware (25%)", "description": "Component installation: setting up RAM, CPUs, and storage devices.", "subtopics": ["Component installation: setting up RAM, CPUs, and storage devices", "Cables and connectors: working with HDMI, Ethernet, and USB cables", "Peripheral devices: installing and maintaining printers, scanners, and other peripherals", "Motherboards and power: configuring motherboards, power supplies, and cooling solutions"]},
        {"title": "Domain 4: Virtualization and cloud computing", "description": "Virtualization concepts: understanding virtual machines, hypervisors, and desktop virtualization.", "subtopics": ["Virtualization concepts: understanding virtual machines, hypervisors, and desktop virtualization", "Cloud models: learning about IaaS, SaaS, and PaaS"]},
        {"title": "Domain 5: Hardware and network troubleshooting", "description": "Diagnosing issues: identifying and fixing hardware, network, and connectivity problems.", "subtopics": ["Diagnosing issues: identifying and fixing hardware, network, and connectivity problems", "Troubleshooting tools: using multimeters, cable testers, and loopback plugs"]}
      ]},
      {"heading": "CompTIA A+ 220-1102 (Core 2) Domains", "items": [
        {"title": "Domain 1: Operating systems", "description": "OS installation: working with Windows, macOS, Linux, and mobile operating systems.", "subtopics": ["OS installation: working with Windows, macOS, Linux, and mobile operating systems", "Windows tools: managing systems with Task Manager, Command Prompt, and Disk Management", "File systems: handling file systems, updates, and OS upgrades"]},
        {"title": "Domain 2: Security", "description": "Security measures: using encryption, access controls, and wireless security protocols.", "subtopics": ["Security measures: using encryption, access controls, and wireless security protocols", "Malware prevention: detecting, removing, and preventing malware threats"]},
        {"title": "Domain 3: Software troubleshooting", "description": "OS issues: diagnosing and resolving problems with operating systems and applications.", "subtopics": ["OS issues: diagnosing and resolving problems with operating systems and applications", "Mobile troubleshooting: addressing connectivity, app, and performance issues", "Security concerns: fixing unauthorized access and malware issues"]},
        {"title": "Domain 4: Operational procedures (21%)", "description": "Documentation: using best practices for system changes and documentation.", "subtopics": ["Documentation: using best practices for system changes and documentation", "Safety and communication: following safety protocols and communicating effectively", "Backup and recovery: setting up workstation backups and recovery processes"]}
      ]}
    ]),
    "faq": json.dumps([
      {"question": "Is the CompTIA A+ certification a suitable place to start?", "answer": "The CompTIA A+ certification might help you get entry-level IT roles such as Desktop Support, Data Support Technician, Desktop Support Administrator, or Help Desk Tech."},
      {"question": "What jobs can you obtain with CompTIA A+?", "answer": "Service Desk Analyst, Help Desk Tech, Desktop Support Administrator, Technical Support Specialist, Field Service Technician, Associate Network Engineer, System Support Specialist, Data Support Technician."},
      {"question": "What does the CompTIA A+ certification cost?", "answer": "The CompTIA A+ certification costs $232 USD per exam."},
      {"question": "How to Pass the CompTIA A+ Exam?", "answer": "You can prepare for the CompTIA A+ exam in a variety of methods: CompTIA A+ study guide, Self-study, Instructor-led training, Practice test."},
      {"question": "Is CompTIA A+ a difficult exam to master?", "answer": "With the proper preparation and strategy, you can pass the two CompTIA A+ certification exams."},
      {"question": "What is the next step after I have earned my CompTIA A+ certification?", "answer": "You might want to pursue an IT specialty, such as networking, cybersecurity, or cloud computing."},
      {"question": "Is CompTIA A+ required for Network+?", "answer": "Obtaining a CompTIA A+ certification is not a prerequisite for obtaining a Network+ certification."},
      {"question": "How much can I earn with CompTIA A+ certification?", "answer": "Associate Network Engineer: $67,162, Desktop Support Administrator: $50,903, Service Desk Analyst: $43,679, Help Desk Tech: $40,424."}
    ])
  },
  {
    "slug": "comptia-network-plus",
    "title": "CompTIA Network+ Certification Training",
    "tagline": "Master networking concepts and earn your Network+ certification",
    "price": 399, "original_price": 999, "rating": 4.6, "reviews": 2150, "learners": "12,000+",
    "duration": "4 Months", "level": "Intermediate", "tag": "Bestseller",
    "modules": 5, "projects": 6,
    "instructor_name": "Rajesh Verma", "instructor_role": "CompTIA Certified Trainer | CCNP | 12+ Years",
    "instructor_experience": "12+ years",
    "curriculum": "Networking Concepts, Network Implementation, Network Operations, Network Security, Troubleshooting",
    "is_published": True, "sort_order": 2,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Anyone who wishes to enhance their knowledge and understanding of networking concepts\nProfessionals looking forward to acquiring job skills in network support and administration\nStudents who are willing to start their career in cybersecurity",
    "eligibility": "No required pre-requisites for Network+ certification. CompTIA A+ certification and/or 9 months of networking experience is recommended.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "N10-009",
    "tools_covered": "Wireshark, Cisco CLI, Nmap, Cable Testers, Wi-Fi Analyzer, PuTTY",
    "skills_covered": "Network Configuration, Troubleshooting, Security, Cloud Networking, Wireless Technologies",
    "certification": "Yes, Certificate of Completion. Prepares you for CompTIA Network+ (N10-009) exam.",
    "key_benefits": "Explain ports and protocols and their purposes\nConfigure appropriate IP addressing schemes\nUnderstand network topologies and technologies\nImplement wireless technologies and configurations\nExplain advanced networking devices use cases\nIdentify and defend against various network attacks\nTroubleshoot network issues systematically",
    "why_join": "Industry-Valued Credential|Network+ is trusted by employers worldwide\nHands-on Labs|Practice with real networking equipment and simulators\nComprehensive Curriculum|Covers all N10-009 exam objectives\nCareer Growth|Opens doors to networking and cybersecurity roles",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "course_objectives": json.dumps(["Explain the purpose and uses of ports and protocols","Explain devices, applications protocols, and services on their appropriate OSI layers","Explain the characteristics and concepts of routing and switching","Configure the appropriate IP address","Understand network topologies types and technologies","Implement the appropriate wireless technologies and configurations","Explain the use cases for advanced networking devices","Explain various types of networking attacks","Learn how to identify and defend devices and their network connections against security risks"]),
    "prerequisites": "CompTIA A+ certification and/or 9 months of networking experience is recommended but not required.",
    "category": "Cyber Security",
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: Networking concepts", "items": [
        {"title": "OSI model and network appliances", "description": "OSI model layers and networking appliances.", "subtopics": ["OSI model layers: physical, data link, network, transport, session, presentation, application", "Networking appliances: routers, switches, firewalls, IDS/IPS, load balancers, proxies, NAS, SAN, wireless devices"]},
        {"title": "Cloud concepts and ports", "description": "Cloud concepts, ports, and protocols.", "subtopics": ["Cloud concepts: NFV, VPC, network security groups, cloud gateways, deployment models", "Ports and protocols: FTP, SFTP, SSH, Telnet, SMTP, DNS, DHCP, HTTP, HTTPS, SNMP, LDAP, RDP, SIP"]},
        {"title": "Transmission media and topologies", "description": "Transmission media and network topologies.", "subtopics": ["Transmission media: wireless (802.11, cellular, satellite), wired (fiber, coaxial, DAC)", "Transceivers and connectors: SC, LC, ST, MPO, RJ11, RJ45, F-type, BNC", "Network topologies: mesh, hybrid, star/hub and spoke, spine and leaf, point-to-point", "IPv4 addressing: public vs. private, APIPA, RFC1918, loopback, subnetting"]}
      ]},
      {"heading": "Domain 2: Network implementation", "items": [
        {"title": "Routing and switching", "description": "Routing technologies and switching technologies.", "subtopics": ["Routing: static and dynamic routing (BGP, EIGRP, OSPF), NAT, PAT, FHRP", "Switching: VLANs, interface configuration, spanning tree, MTU, jumbo frames"]},
        {"title": "Wireless and physical installations", "description": "Wireless devices and physical installations.", "subtopics": ["Wireless: channels, frequency options, SSID, encryption, authentication, antennas", "Physical installations: installation implications, power considerations, environmental factors"]}
      ]},
      {"heading": "Domain 3: Network operations", "items": [
        {"title": "Documentation and monitoring", "description": "Documentation and network monitoring.", "subtopics": ["Documentation: physical vs. logical diagrams, rack diagrams, cable maps, IPAM", "Network monitoring: SNMP, flow data, packet capture, baseline metrics, log aggregation"]},
        {"title": "Disaster recovery and services", "description": "Disaster recovery and network services.", "subtopics": ["Disaster recovery: RPO, RTO, MTTR, cold/warm/hot sites, active-active/passive", "Network services: DHCP, SLAAC, DNS, NTP, VPNs, SSH, API"]}
      ]},
      {"heading": "Domain 4: Network security", "items": [
        {"title": "Logical and physical security", "description": "Security controls and defense mechanisms.", "subtopics": ["Logical security: encryption, PKI, IAM, MFA, SSO, RADIUS, LDAP, SAML, TACACS+", "Physical security: cameras, locks, biometric systems"]},
        {"title": "Attacks and defense", "description": "Types of attacks and security features.", "subtopics": ["Types of attacks: DoS/DDoS, VLAN hopping, MAC flooding, ARP poisoning, DNS poisoning, evil twin, social engineering", "Security features: device hardening, NAC, ACL, URL/content filtering, screened subnet"]}
      ]},
      {"heading": "Domain 5: Network troubleshooting", "items": [
        {"title": "Troubleshooting methodology", "description": "Systematic troubleshooting approach.", "subtopics": ["Identifying the problem, establishing a theory, testing, planning, implementing, verifying, documenting"]},
        {"title": "Cabling and network issues", "description": "Cabling issues and network services issues.", "subtopics": ["Cabling: incorrect type, signal degradation, improper termination, TX/RX transposed", "Network services: STP, VLAN assignment, ACLs, routing table, address pool exhaustion", "Performance: congestion, latency, packet loss, wireless interference"]}
      ]}
    ]),
    "faq": json.dumps([
      {"question": "What is the importance of CompTIA Network+ certification?", "answer": "CompTIA Network+ validates your knowledge and skills required to troubleshoot, configure and manage wired and wireless networks."},
      {"question": "What other courses are recommended before and after CompTIA Network+?", "answer": "CompTIA A+ is recommended before, and CCNA, CEHv11 is recommended after."},
      {"question": "Can you take the Network+ exam without taking CompTIA A+ certification?", "answer": "If you have a basic understanding of IT, you can directly go for CompTIA Network+ certification."},
      {"question": "What is CompTIA Network+ retake policy?", "answer": "Before your third attempt, you need to wait at least fourteen days."},
      {"question": "What job can I get with CompTIA Network+ certification?", "answer": "IT consultant, Computer technician, Help desk technician, System engineer, Network support specialist, Network analyst."},
      {"question": "What is the validity of this CompTIA Network+ certificate?", "answer": "CompTIA Network+ certification is valid for three years from the day you pass your exam."}
    ])
  },
  {
    "slug": "comptia-security-plus",
    "title": "CompTIA Security+ Certification Training",
    "tagline": "Master cybersecurity fundamentals and earn your Security+ certification",
    "price": 449, "original_price": 1099, "rating": 4.7, "reviews": 3200, "learners": "18,000+",
    "duration": "4 Months", "level": "Intermediate", "tag": "Bestseller",
    "modules": 5, "projects": 8,
    "instructor_name": "Vikram Singh", "instructor_role": "CompTIA Security+ Certified | CISSP | 15+ Years",
    "instructor_experience": "15+ years",
    "curriculum": "Security Concepts, Threats & Vulnerabilities, Security Architecture, Security Operations, Program Management",
    "is_published": True, "sort_order": 3,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Network Administrators\nSystem Administrators\nCyber Security Enthusiasts\nSecurity Engineers\nAnyone who wants to advance their CyberSecurity career",
    "eligibility": "Having a fundamental understanding of Networking and Information Security concepts is helpful but unnecessary.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "SY0-701",
    "tools_covered": "Wireshark, Nmap, Burp Suite, Metasploit, SIEM tools, Nessus, Kali Linux",
    "skills_covered": "Security Controls, Cryptography, Risk Management, Incident Response, Compliance, Identity Management",
    "certification": "Yes, Certificate of Completion. Prepares you for CompTIA Security+ (SY0-701) exam.",
    "key_benefits": "Develop comprehensive understanding of foundational security concepts\nLearn to identify, assess, and mitigate threats and vulnerabilities\nMaster designing and managing robust security architecture\nGain expertise in security operations and incident response\nAcquire knowledge to manage security programs effectively\nUnderstand cryptography and PKI implementation",
    "why_join": "Industry Standard|Security+ is the most widely adopted ISO/ANSI accredited cybersecurity certification\nHands-on Labs|Practice with real security tools and scenarios\nExpert Instructors|Learn from certified cybersecurity professionals\nCareer Boost|Average salary of Information Security Analyst is $199K per annum",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "course_objectives": json.dumps(["Develop a comprehensive understanding of foundational security concepts and principles","Learn to identify, assess, and mitigate various threats, vulnerabilities, and risks","Master the principles and practices of designing a robust security architecture","Gain expertise in day-to-day security operations including incident response and monitoring","Acquire the knowledge and skills required to oversee and manage a security program","Understand compliance, governance, and the protection of valuable data"]),
    "prerequisites": "Fundamental understanding of Networking and Information Security concepts is helpful but not required.",
    "category": "Cyber Security",
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: General security concepts", "items": [
        {"title": "Security controls and fundamental concepts", "description": "Security controls and fundamental security concepts.", "subtopics": ["Security controls: technical, preventive, managerial, deterrent, operational, detective, physical, corrective", "Fundamental concepts: CIA triad, non-repudiation, AAA, zero trust, deception/disruption technology"]},
        {"title": "Change management and cryptography", "description": "Change management and cryptographic solutions.", "subtopics": ["Change management: business processes, technical implications, documentation, version control", "Cryptographic solutions: PKI, encryption, obfuscation, hashing, digital signatures, blockchain"]}
      ]},
      {"heading": "Domain 2: Threats, vulnerabilities, and mitigations", "items": [
        {"title": "Threat actors and attack surfaces", "description": "Understanding threat actors and attack vectors.", "subtopics": ["Threat actors: nation-states, unskilled attackers, hacktivists, insider threats, organized crime", "Attack surfaces: message-based, unsecure networks, social engineering, file-based, supply chain"]},
        {"title": "Vulnerabilities and malicious activity", "description": "Identifying vulnerabilities and analyzing attacks.", "subtopics": ["Vulnerabilities: application, hardware, mobile, virtualization, OS, cloud, web-based", "Malicious activity: malware attacks, password attacks, application attacks, network attacks"]},
        {"title": "Mitigation techniques", "description": "Techniques to mitigate security threats.", "subtopics": ["Segmentation, access control, configuration enforcement, hardening, isolation, patching"]}
      ]},
      {"heading": "Domain 3: Security architecture", "items": [
        {"title": "Architecture models and enterprise infrastructure", "description": "Security architecture models.", "subtopics": ["Architecture models: on-premises, cloud, virtualization, IoT, ICS, IaC", "Enterprise infrastructure: security principles, control selection, secure communication"]},
        {"title": "Data protection and resilience", "description": "Data protection and disaster recovery.", "subtopics": ["Data protection: data types, securing methods, classifications", "Resilience: high availability, site considerations, backups, continuity of operations"]}
      ]},
      {"heading": "Domain 4: Security operations", "items": [
        {"title": "Computing resources and asset management", "description": "Securing computing resources and managing assets.", "subtopics": ["Computing resources: secure baselines, mobile solutions, hardening, wireless security", "Asset management: acquisition, disposal, assignment, monitoring/tracking"]},
        {"title": "Vulnerability and alerting", "description": "Vulnerability management and security monitoring.", "subtopics": ["Vulnerability management: identifying, analyzing, remediating, validating, reporting", "Alerting: monitoring tools, firewalls, IDS/IPS, DNS filtering, DLP, NAC, EDR/XDR"]},
        {"title": "IAM and incident response", "description": "Identity management and incident response.", "subtopics": ["Identity and access management: provisioning, SSO, MFA, privileged access tools", "Incident response: processes, training, testing, root cause analysis, threat hunting, forensics"]}
      ]},
      {"heading": "Domain 5: Security program management and oversight", "items": [
        {"title": "Security governance and risk management", "description": "Security governance and risk management.", "subtopics": ["Security governance: policies, standards, procedures, monitoring, governance structures", "Risk management: identification, assessment, analysis, strategies, BIA"]},
        {"title": "Third-party risk and compliance", "description": "Third-party risk management and compliance.", "subtopics": ["Third-party risk: vendor assessment, selection, agreements, monitoring", "Security compliance: compliance reporting, consequences of non-compliance, privacy"]},
        {"title": "Audits and security awareness", "description": "Audits, assessments, and security awareness.", "subtopics": ["Audits: attestation, internal/external audits, penetration testing", "Security awareness: phishing training, anomalous behavior recognition, user guidance"]}
      ]}
    ]),
    "faq": json.dumps([
      {"question": "What is the importance of CompTIA Security+ certification?", "answer": "CompTIA Security+ is the most widely adopted ISO/ANSI accredited cybersecurity certification."},
      {"question": "What jobs can I get with Security+ certification?", "answer": "Network Administrator, Security Administrator, Security Analyst, Security Engineer, Cybersecurity Specialist."},
      {"question": "Is Security+ harder than Network+?", "answer": "Security+ builds on networking concepts but is considered more conceptual."}
    ])
  },
  {
    "slug": "comptia-cysa-plus",
    "title": "CompTIA CySA+ Certification Training",
    "tagline": "Become a Cybersecurity Analyst with CySA+ certification",
    "price": 449, "original_price": 1099, "rating": 4.6, "reviews": 1800, "learners": "9,000+",
    "duration": "4 Months", "level": "Intermediate", "tag": "Trending",
    "modules": 4, "projects": 6,
    "instructor_name": "Ananya Gupta", "instructor_role": "CySA+ Certified | CEH | 12+ Years",
    "instructor_experience": "12+ years",
    "curriculum": "Security Operations, Vulnerability Management, Incident Response, Reporting",
    "is_published": True, "sort_order": 4,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "IT Security Analysts\nVulnerability Analysts\nThreat Intelligence Analysts\nAnyone trying to understand cybersecurity analysis",
    "eligibility": "Basic knowledge of Network+, Security+, or equivalent discipline. Minimum of 4 years of hands-on experience as an Incident Response Analyst or SOC Analyst recommended.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "CS0-003",
    "tools_covered": "Wireshark, SIEM, Nessus, Nmap, Metasploit, Burp Suite, Kali Linux",
    "skills_covered": "Threat Detection, Vulnerability Management, Incident Response, Security Analytics",
    "certification": "Yes, Certificate of Completion. Prepares you for CompTIA CySA+ (CS0-003) exam.",
    "key_benefits": "Detect and analyze indicators of malicious activity\nUnderstand threat hunting and threat intelligence concepts\nUse appropriate tools to manage and respond to attacks\nPerform incident response processes\nUnderstand reporting and communication concepts",
    "why_join": "Hands-on Analytics|Learn practical threat detection and analysis\nIndustry Recognition|CySA+ is valued by global enterprises\nExpert Faculty|Learn from certified cybersecurity analysts\nCareer Growth|Open doors to SOC analyst and threat hunter roles",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "course_objectives": json.dumps(["Detect and analyze indicators of malicious activity","Understand threat hunting and threat intelligence concepts","Use appropriate tools to manage, prioritize and respond to attacks","Perform incident response processes","Understand reporting and communication concepts related to vulnerability management"]),
    "prerequisites": "Basic knowledge of Network+, Security+, or equivalent discipline. 4+ years hands-on experience recommended.",
    "category": "Cyber Security",
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: Security operations", "items": [
        {"title": "System and network architecture", "description": "System architecture and network monitoring.", "subtopics": ["Log ingestion, OS concepts, infrastructure, network architecture, IAM, encryption"]},
        {"title": "Malicious activity indicators", "description": "Detecting malicious activity across systems.", "subtopics": ["Network anomalies: bandwidth spikes, rogue devices", "Host issues: unauthorized software, data exfiltration", "Application irregularities: unexpected communication, service interruptions"]},
        {"title": "Threat intelligence and hunting", "description": "Threat intelligence concepts and hunting techniques.", "subtopics": ["Threat actors, TTP, confidence levels, collection methods, intelligence sharing", "Hunting techniques and process improvement"]}
      ]},
      {"heading": "Domain 2: Vulnerability management", "items": [
        {"title": "Vulnerability scanning", "description": "Scanning techniques and assessment tools.", "subtopics": ["Asset discovery, internal vs. external scanning, agent vs. agentless", "Credentialed vs. non-credentialed, passive vs. active scanning"]},
        {"title": "Vulnerability prioritization and response", "description": "Prioritizing and responding to vulnerabilities.", "subtopics": ["CVSS interpretation, validating findings, exploitability assessment", "Compensating controls, patching, configuration management, threat modeling"]}
      ]},
      {"heading": "Domain 3: Incident response management", "items": [
        {"title": "Attack methodology frameworks", "description": "Understanding attack frameworks.", "subtopics": ["Cyber kill chain, diamond model of intrusion, MITRE ATT&CK, OSSTMM, OWASP"]},
        {"title": "Incident response activities", "description": "Incident response lifecycle.", "subtopics": ["Detection, analysis, containment, eradication, recovery", "Incident response plans, playbooks, tabletop exercises, forensic analysis"]}
      ]},
      {"heading": "Domain 4: Reporting and communication", "items": [
        {"title": "Vulnerability and incident reporting", "description": "Effective reporting and communication.", "subtopics": ["Compliance reports, action plans, KPIs, stakeholder communication", "Incident declaration, escalation, root cause analysis, lessons learned"]}
      ]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA CySA+ certification?", "answer": "CySA+ (Cybersecurity Analyst+) validates skills in behavioral analytics, threat detection, and incident response."},
      {"question": "What are the prerequisites for CySA+?", "answer": "Basic knowledge of Network+ and Security+ is recommended, along with 4 years of hands-on experience."},
      {"question": "What jobs can I get with CySA+?", "answer": "IT Security Analyst, Vulnerability Analyst, Threat Intelligence Analyst, SOC Analyst."}
    ])
  },
  {
    "slug": "comptia-secai-plus",
    "title": "CompTIA SecAI+ Certification Training",
    "tagline": "Secure AI systems and defend against AI-driven threats",
    "price": 499, "original_price": 1199, "rating": 4.5, "reviews": 650, "learners": "3,200+",
    "duration": "3 Months", "level": "Advanced", "tag": "New",
    "modules": 4, "projects": 5,
    "instructor_name": "Dr. Priya Mehta", "instructor_role": "AI Security Expert | CISSP | 15+ Years",
    "instructor_experience": "15+ years",
    "curriculum": "AI Security Concepts, Securing AI Systems, AI-Assisted Security, AI Governance",
    "is_published": True, "sort_order": 5,
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Cybersecurity Analysts & Engineers\nSOC Analysts & Incident Responders\nSecurity Architects & Consultants\nRisk, GRC, and Compliance Professionals\nCloud Security Professionals",
    "eligibility": "3-4 years experience in IT, inclusive of 2+ years hands-on cybersecurity. Security+, CySA+, PenTest+, or equivalent recommended.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 15th June 2026",
    "exam_code": "SecAI-001",
    "tools_covered": "Python, TensorFlow, PyTorch, MLflow, Docker, Kubernetes, Cloud AI Services",
    "skills_covered": "AI Security, Adversarial ML, AI Governance, GRC, AI Risk Management",
    "certification": "Yes, Certificate of Completion. Prepares you for CompTIA SecAI+ (v1) exam.",
    "key_benefits": "Explain core AI concepts and terminology relevant to cybersecurity\nIdentify AI applications used in threat detection\nRecognize AI-driven threats including adversarial and generative AI\nImplement security controls to protect AI systems\nSecure AI deployment environments across cloud, on-prem, and hybrid\nMitigate adversarial risks targeting AI pipelines",
    "why_join": "Emerging Field|Be among the first to earn AI security certification\nCutting-edge Curriculum|Covers latest AI threats and defenses\nExpert Instructors|Learn from AI security pioneers\nFuture-Proof Skills|AI security is the fastest growing cybersecurity domain",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "course_objectives": json.dumps(["Explain core AI concepts and terminology relevant to cybersecurity","Identify AI applications used in threat detection and security operations","Recognize AI-driven threats including adversarial and generative AI","Implement security controls to protect AI systems and models","Secure AI deployment environments across cloud and hybrid platforms","Apply AI-assisted techniques to improve detection and response","Integrate governance, risk, and compliance into AI initiatives"]),
    "prerequisites": "3-4 years IT experience, 2+ years cybersecurity. Security+ or equivalent recommended.",
    "category": "Cyber Security",
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: Basic AI concepts related to cybersecurity", "items": [
        {"title": "Core AI principles", "description": "Understanding AI and ML concepts.", "subtopics": ["Machine learning, deep learning, NLP, automation", "AI applications in security: threat detection, defense, security operations"]},
        {"title": "AI-driven threats", "description": "Recognizing AI-powered threats.", "subtopics": ["Automated phishing, polymorphic malware, adversarial ML", "Malicious use of generative AI"]}
      ]},
      {"heading": "Domain 2: Securing AI systems", "items": [
        {"title": "Security controls for AI", "description": "Protecting AI systems and data.", "subtopics": ["Implement security controls for AI systems", "Secure AI deployment across on-prem, cloud, hybrid"]},
        {"title": "Adversarial risk mitigation", "description": "Defending against AI-specific attacks.", "subtopics": ["Attacks targeting AI models, data pipelines, inference layers", "Defense strategies for adversarial ML"]}
      ]},
      {"heading": "Domain 3: AI-assisted security", "items": [
        {"title": "AI-driven detection", "description": "Using AI for security operations.", "subtopics": ["AI tools for anomaly detection, threat identification", "Automate security workflows, event triage, alert correlation"]},
        {"title": "AI in operations", "description": "Integrating AI into security operations.", "subtopics": ["Threat modeling, behavior analysis, continuous monitoring"]}
      ]},
      {"heading": "Domain 4: AI governance, risk, and compliance", "items": [
        {"title": "Regulatory frameworks", "description": "Understanding AI governance.", "subtopics": ["Global governance requirements, GDPR, NIST AI RMF"]},
        {"title": "Responsible AI", "description": "Ensuring ethical AI use.", "subtopics": ["Ethical guidelines, legal standards, compliance throughout AI lifecycle"]}
      ]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA SecAI+ certification?", "answer": "SecAI+ validates skills to secure AI systems and defend against AI-driven threats."},
      {"question": "What are the prerequisites?", "answer": "3-4 years IT experience with 2+ years in cybersecurity is recommended."},
      {"question": "Is this a vendor-neutral certification?", "answer": "Yes, SecAI+ is vendor-neutral and covers AI security broadly."}
    ])
  },
  {
    "slug": "comptia-pentest-plus",
    "title": "CompTIA PenTest+ Certification Training",
    "tagline": "Master penetration testing and earn PenTest+ certification",
    "price": 499, "original_price": 1199, "rating": 4.6, "reviews": 1200, "learners": "6,500+",
    "duration": "4 Months", "level": "Advanced", "tag": "Trending",
    "modules": 5, "projects": 8, "is_published": True, "sort_order": 6,
    "instructor_name": "Arun Kumar", "instructor_role": "OSCP | CEH | PenTest+ | 14+ Years",
    "instructor_experience": "14+ years",
    "curriculum": "Planning, Reconnaissance, Attacks, Exploits, Reporting, Tools",
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "IT Security Analyst\nPenetration and Vulnerability Tester\nNetwork Security Professional\nApplication Security Vulnerability Analyst",
    "eligibility": "Minimum 3 to 4 years of experience in IT security or related field. Network and security knowledge required.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "PT0-002",
    "tools_covered": "Metasploit, Nmap, Burp Suite, Wireshark, Nessus, Python, Kali Linux",
    "skills_covered": "Penetration Testing, Vulnerability Assessment, Exploit Development, Security Assessment",
    "certification": "Yes, Certificate of Completion. Prepares for CompTIA PenTest+ (PT0-002) exam.",
    "category": "Cyber Security",
    "key_benefits": "Perform comprehensive penetration tests\nConduct vulnerability scanning and analysis\nUnderstand legal and compliance requirements\nAnalyze results and produce professional reports",
    "why_join": "Hands-on|Real penetration testing scenarios\nComprehensive|Covers all stages of pen testing\nCareer Growth|High demand for pen testers",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "course_objectives": json.dumps(["Perform comprehensive penetration tests","Conduct vulnerability scanning and analysis","Understand legal and compliance requirements","Analyze results and produce professional reports"]),
    "prerequisites": "3-4 years of IT security experience and network/security knowledge is recommended.",
    "topic_wise_content": json.dumps([
      {"heading": "Module 1: Planning and scoping", "items": [{"title": "Governance and scoping", "subtopics": ["Compare governance, risk, and compliance concepts", "Explain importance of scoping requirements", "Demonstrate ethical hacking mindset"]}]},
      {"heading": "Module 2: Information gathering and vulnerability scanning", "items": [{"title": "Reconnaissance and scanning", "subtopics": ["Passive reconnaissance techniques", "Active reconnaissance techniques", "Analyze reconnaissance results", "Perform vulnerability scanning"]}]},
      {"heading": "Module 3: Attacks and exploits", "items": [{"title": "Network and wireless attacks", "subtopics": ["Research attack vectors and perform network attacks", "Perform wireless attacks", "Perform application-based attacks", "Attacks on cloud technologies"]}, {"title": "Post-exploitation", "subtopics": ["Common attacks on specialized systems", "Social engineering and physical attacks", "Post-exploitation techniques"]}]},
      {"heading": "Module 4: Reporting and communication", "items": [{"title": "Reports and communication", "subtopics": ["Written report components", "Analyze findings and recommend remediation", "Communication during penetration testing", "Post-report delivery activities"]}]},
      {"heading": "Module 5: Tools and code analysis", "items": [{"title": "Scripting and tools", "subtopics": ["Basic scripting and software development concepts", "Analyze scripts for penetration testing", "Use cases of penetration testing tools"]}]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA PenTest+ certification?", "answer": "PenTest+ validates skills in penetration testing, vulnerability management, and reporting."},
      {"question": "What are the prerequisites?", "answer": "3-4 years of IT security experience and network/security knowledge is recommended."},
      {"question": "What tools will I learn?", "answer": "Metasploit, Nmap, Burp Suite, Wireshark, Nessus, Python, Kali Linux."}
    ])
  },
  {
    "slug": "comptia-securityx",
    "title": "CompTIA SecurityX Certification Training",
    "tagline": "Advanced cybersecurity certification for security architects",
    "price": 599, "original_price": 1499, "rating": 4.7, "reviews": 850, "learners": "4,000+",
    "duration": "5 Months", "level": "Advanced", "tag": "Bestseller",
    "modules": 4, "projects": 6, "is_published": True, "sort_order": 7,
    "instructor_name": "Dr. Rajat Verma", "instructor_role": "SecurityX Certified | CISSP | CISM | 20+ Years",
    "instructor_experience": "20+ years",
    "curriculum": "GRC, Security Architecture, Security Engineering, Security Operations",
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Cybersecurity Analysts\nSecurity Engineers\nSOC Analysts\nCloud Security Engineers\nPenetration Testers",
    "eligibility": "5+ years of hands-on IT security experience recommended. Knowledge equivalent to Security+ or CySA+.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "SCX-001",
    "tools_covered": "SIEM, SOAR, Terraform, Ansible, Kubernetes, Docker, Cloud Security Tools",
    "skills_covered": "Security Architecture, Risk Management, Incident Response, Cloud Security, GRC",
    "certification": "Yes, Certificate of Completion. Prepares for CompTIA SecurityX exam.",
    "category": "Cyber Security",
    "key_benefits": "Design enterprise security architecture\nImplement risk management frameworks\nLead incident response operations\nApply security engineering principles",
    "why_join": "Advanced Level|CompTIA's highest level cybersecurity certification\nArchitecture Focus|Design secure enterprise solutions\nCareer Peak|Qualifies for security architect roles",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "topic_wise_content": json.dumps([
      {"heading": "Module 1: Governance, risk, and compliance", "items": [{"title": "Security program documentation", "subtopics": ["Policies, procedures, standards, guidelines", "Program management, training, communication, RACI matrix"]}, {"title": "Risk management", "subtopics": ["Impact analysis, quantitative vs. qualitative assessment", "Third-party risk, threat modeling, ATT&CK, STRIDE"]}, {"title": "Compliance strategies", "subtopics": ["PCI DSS, ISO/IEC 27000, NIST CSF, CSA"]}]},
      {"heading": "Module 2: Security architecture", "items": [{"title": "Cloud architecture", "subtopics": ["CASB, shadow IT detection, shared responsibility model", "CI/CD, Terraform, Ansible, container security, serverless"]}, {"title": "Network architecture and zero trust", "subtopics": ["Segmentation, microsegmentation, VPN, SASE, SD-WAN", "Zero trust concepts, deperimeterization"]}]},
      {"heading": "Module 3: Security engineering", "items": [{"title": "Automation and cryptography", "subtopics": ["Scripting: PowerShell, Bash, Python, SOAR, IaC", "Advanced cryptography: PQC, homomorphic encryption, blockchain"]}]},
      {"heading": "Module 4: Security operations", "items": [{"title": "Monitoring and threat hunting", "subtopics": ["SIEM, aggregate analysis, behavior baselines", "Internal/external intelligence, TIPs, STIX/TAXII, Sigma, YARA"]}, {"title": "Incident response", "subtopics": ["Malware analysis, reverse engineering, IoC extraction, root cause analysis"]}]}
    ]),
    "faq": json.dumps([
      {"question": "What is SecurityX certification?", "answer": "SecurityX is CompTIA's advanced-level cybersecurity certification for security architects."},
      {"question": "What are the prerequisites?", "answer": "5+ years of IT security experience. Security+ or CySA+ knowledge recommended."},
      {"question": "How is SecurityX different from Security+?", "answer": "SecurityX is advanced-level focusing on architecture, while Security+ is foundational."}
    ])
  },
  {
    "slug": "comptia-cloud-plus",
    "title": "CompTIA Cloud+ Certification Training",
    "tagline": "Master cloud infrastructure and earn Cloud+ certification",
    "price": 449, "original_price": 1099, "rating": 4.5, "reviews": 980, "learners": "5,500+",
    "duration": "4 Months", "level": "Intermediate", "tag": "Trending",
    "modules": 6, "projects": 6, "is_published": True, "sort_order": 8,
    "instructor_name": "Sneha Patel", "instructor_role": "AWS Certified | Azure | Cloud+ | 12+ Years",
    "instructor_experience": "12+ years",
    "curriculum": "Cloud Architecture, Deployment, Operations, Security, DevOps, Troubleshooting",
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "System Administrator\nSystems Engineer\nNetwork Administrator\nCloud Developer\nCloud Engineer",
    "eligibility": "2-3 years work experience in IT systems administration or networking. Familiarity with hypervisor technology recommended.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "CV0-004",
    "tools_covered": "AWS, Azure, GCP, Docker, Kubernetes, Terraform, Jenkins, Ansible",
    "skills_covered": "Cloud Architecture, Deployment, Security, DevOps, Troubleshooting",
    "certification": "Yes, Certificate of Completion. Prepares for CompTIA Cloud+ (CV0-004) exam.",
    "category": "Cloud Computing",
    "key_benefits": "Master cloud architecture and deployment\nImplement cloud security best practices\nManage cloud operations and optimization\nTroubleshoot cloud infrastructure issues",
    "why_join": "Vendor Neutral|Covers AWS, Azure, GCP\nComprehensive|Full cloud lifecycle management\nCareer Growth|Cloud skills in highest demand",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "topic_wise_content": json.dumps([
      {"heading": "Module 1: Cloud architecture", "items": [{"title": "Cloud models and virtualization", "subtopics": ["Public, private, hybrid, multi-cloud models", "Virtualization technologies, cloud networking, VPN"]}, {"title": "Containerization and orchestration", "subtopics": ["Containerization, orchestration techniques", "Database concepts, resource optimization, billing"]}]},
      {"heading": "Module 2: Deployment", "items": [{"title": "Migration and IaC", "subtopics": ["System requirements analysis", "Infrastructure as Code (IaC) techniques", "Workload migrations, resource provisioning"]}]},
      {"heading": "Module 3: Operations", "items": [{"title": "Lifecycle and observability", "subtopics": ["Lifecycle management, scaling, updates", "Backup and recovery, monitoring and optimization"]}]},
      {"heading": "Module 4: Security", "items": [{"title": "Cloud security", "subtopics": ["Vulnerability management, IAM", "Container security, compliance (PCI DSS, SOC 2, ISO 27001)"]}]},
      {"heading": "Module 5: DevOps fundamentals", "items": [{"title": "CI/CD and automation", "subtopics": ["Automation tools, source control", "CI/CD pipelines, Kubernetes, Ansible, Jenkins"]}]},
      {"heading": "Module 6: Troubleshooting", "items": [{"title": "Cloud troubleshooting", "subtopics": ["Deployment issues, network connectivity", "Security incidents, service disruptions, misconfigurations"]}]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA Cloud+ certification?", "answer": "Cloud+ validates skills in cloud infrastructure, deployment, security, and management."},
      {"question": "What are the prerequisites?", "answer": "2-3 years IT experience with networking or systems administration."},
      {"question": "Is Cloud+ vendor-neutral?", "answer": "Yes, it covers AWS, Azure, GCP and other cloud platforms."}
    ])
  },
  {
    "slug": "comptia-data-plus",
    "title": "CompTIA Data+ Certification Training",
    "tagline": "Transform raw data into meaningful insights with Data+ certification",
    "price": 399, "original_price": 899, "rating": 4.4, "reviews": 720, "learners": "4,000+",
    "duration": "3 Months", "level": "Beginner", "tag": "",
    "modules": 5, "projects": 4, "is_published": True, "sort_order": 9,
    "instructor_name": "Neha Joshi", "instructor_role": "Data+ Certified | Data Scientist | 10+ Years",
    "instructor_experience": "10+ years",
    "curriculum": "Data Concepts, Data Acquisition, Data Analysis, Visualization, Data Governance",
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "Data Analysts\nBusiness Data Analysts\nReporting Analysts",
    "eligibility": "18-24 months of experience as a report or business analyst recommended.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "DA0-001",
    "tools_covered": "Excel, SQL, Python, Tableau, Power BI, R",
    "skills_covered": "Data Analysis, Statistics, Data Visualization, Data Governance, SQL",
    "certification": "Yes, Certificate of Completion. Prepares for CompTIA Data+ (DA0-001) exam.",
    "category": "Data Science & AI",
    "key_benefits": "Master data analysis and visualization\nUnderstand statistical methods\nImplement data governance practices\nTransform raw data into insights",
    "why_join": "Entry Level|Perfect for starting data career\nPractical Skills|Real-world data analysis\nIndustry Valued|Recognized by employers",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "topic_wise_content": json.dumps([
      {"heading": "Module 1: Data concepts and environments", "items": [{"title": "Data fundamentals", "subtopics": ["Database types, data structures, file extensions, data types"]}, {"title": "Data sources and infrastructure", "subtopics": ["Databases, APIs, website data, cloud, on-premise, storage"]}, {"title": "AI concepts", "subtopics": ["AI models, NLP, robotic automation"]}]},
      {"heading": "Module 2: Data acquisition and preparation", "items": [{"title": "Data collection", "subtopics": ["Data integration methods, queries to gather and combine data"]}, {"title": "Data exploration and transformation", "subtopics": ["Find missing values, duplication, redundancy, outliers", "Cleansing, merging, parsing, formatting data"]}]},
      {"heading": "Module 3: Data analysis", "items": [{"title": "Analysis methods", "subtopics": ["Communicate results, select methods for audiences", "Statistical methods, troubleshooting analysis issues"]}]},
      {"heading": "Module 4: Visualization and reporting", "items": [{"title": "Visuals and reports", "subtopics": ["Charts, maps, tables, design elements", "Dashboards, summaries, validation and review"]}]},
      {"heading": "Module 5: Data governance", "items": [{"title": "Data management", "subtopics": ["Documentation, versioning, data lineage"]}, {"title": "Compliance and quality", "subtopics": ["Retention, audits, regulations, access control, encryption", "Profiling, monitoring, testing for data quality"]}]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA Data+ certification?", "answer": "Data+ validates skills in data analytics, visualization, and data-driven decision making."},
      {"question": "What are the prerequisites?", "answer": "18-24 months of experience as a report or business analyst recommended."},
      {"question": "What tools will I learn?", "answer": "Excel, SQL, Python, Tableau, Power BI, R."}
    ])
  },
  {
    "slug": "comptia-linux-plus",
    "title": "CompTIA Linux+ Certification Training",
    "tagline": "Master Linux system administration with Linux+ certification",
    "price": 399, "original_price": 999, "rating": 4.5, "reviews": 1100, "learners": "6,000+",
    "duration": "4 Months", "level": "Intermediate", "tag": "",
    "modules": 5, "projects": 5, "is_published": True, "sort_order": 10,
    "instructor_name": "Vivek Sharma", "instructor_role": "Linux+ Certified | RHCE | 15+ Years",
    "instructor_experience": "15+ years",
    "curriculum": "System Management, Services, Security, Automation, Troubleshooting",
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "IT Professionals advancing Linux skills\nAspiring Linux System Administrators\nProfessionals with A+, Network+, or Server+ knowledge",
    "eligibility": "12 months of hands-on experience with Linux servers recommended. A+, Network+, or Server+ knowledge helpful.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "XK0-005",
    "tools_covered": "Linux (Ubuntu, CentOS, RHEL), Bash, Python, Ansible, Docker, Git, Kubernetes",
    "skills_covered": "Linux Administration, Shell Scripting, Security, Automation, Containerization",
    "certification": "Yes, Certificate of Completion. Prepares for CompTIA Linux+ (XK0-005) exam.",
    "category": "Cloud Computing",
    "key_benefits": "Master Linux system administration\nImplement security best practices\nAutomate tasks with scripting\nManage containers and virtualization",
    "why_join": "Industry Standard|Most widely recognized Linux certification\nHands-on|Real Linux server management\nCareer Essential|Linux skills required for cloud and DevOps",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: System management", "items": [{"title": "Linux basics and storage", "subtopics": ["Boot process, kernel, filesystems, device management", "LVM, RAID, partitions, mounted storage"]}, {"title": "Network and virtualization", "subtopics": ["Network configuration, DNS, interfaces", "Hypervisors, VMs, disk images"]}]},
      {"heading": "Domain 2: Services and user management", "items": [{"title": "Files and accounts", "subtopics": ["Permissions, links, special files, user/group management"]}, {"title": "Process and software", "subtopics": ["Process monitoring, job scheduling, package management", "Containers, container runtimes"]}]},
      {"heading": "Domain 3: Security", "items": [{"title": "Authentication and firewalls", "subtopics": ["PAM, LDAP, Kerberos, auditing", "iptables, nftables, UFW"]}, {"title": "Hardening and compliance", "subtopics": ["OS hardening, sudo, MFA, cryptography", "Integrity verification, scanning"]}]},
      {"heading": "Domain 4: Automation and scripting", "items": [{"title": "Automation tools", "subtopics": ["Ansible, Puppet, CI/CD tools", "Shell scripting, Python basics, Git"]}]},
      {"heading": "Domain 5: Troubleshooting", "items": [{"title": "System and network troubleshooting", "subtopics": ["System monitoring, hardware/storage diagnostics", "Network troubleshooting, security fixes, performance analysis"]}]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA Linux+ certification?", "answer": "Linux+ validates skills in Linux system administration, security, and automation."},
      {"question": "What are the prerequisites?", "answer": "12 months of Linux experience recommended. A+ or Network+ knowledge helpful."},
      {"question": "What distributions are covered?", "answer": "Ubuntu, CentOS, RHEL, and other major Linux distributions."}
    ])
  },
  {
    "slug": "comptia-project-plus",
    "title": "CompTIA Project+ Certification Training",
    "tagline": "Master IT project management with Project+ certification",
    "price": 349, "original_price": 799, "rating": 4.3, "reviews": 580, "learners": "3,200+",
    "duration": "3 Months", "level": "Beginner", "tag": "",
    "modules": 4, "projects": 3, "is_published": True, "sort_order": 11,
    "instructor_name": "Meera Iyer", "instructor_role": "PMP | Project+ | 15+ Years",
    "instructor_experience": "15+ years",
    "curriculum": "Project Concepts, Life Cycle, Tools, IT Governance",
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "IT Support Professionals\nJunior Project Managers\nSystem Administrators\nTeam Leads\nAspiring Project Managers",
    "eligibility": "6-12 months of hands-on experience managing projects in a tech environment or equivalent knowledge.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "PK0-005",
    "tools_covered": "Jira, Trello, Microsoft Project, Gantt Charts, Slack, Confluence",
    "skills_covered": "Project Management, Agile, Waterfall, Risk Management, Communication",
    "certification": "Yes, Certificate of Completion. Prepares for CompTIA Project+ (PK0-005) exam.",
    "category": "Project Management",
    "key_benefits": "Master project management methodologies\nManage project life cycle effectively\nUse project management tools\nUnderstand IT governance and compliance",
    "why_join": "IT Focused|Tailored for IT project management\nDual Methodology|Both Agile and Waterfall covered\nCareer Starter|Perfect for aspiring project managers",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: Project management concepts", "items": [{"title": "Methodologies and frameworks", "subtopics": ["Project characteristics, methodologies, Agile vs. Waterfall", "Change control, risk management, issue management"]}, {"title": "Schedule and communication", "subtopics": ["Schedule management, milestones, quality management", "Communication management, meeting management, resource management"]}]},
      {"heading": "Domain 2: Project life cycle phases", "items": [{"title": "Discovery to closing", "subtopics": ["Discovery artifacts, business cases", "Initiation, planning, execution, closing"]}]},
      {"heading": "Domain 3: Tools and documentation", "items": [{"title": "Project tools", "subtopics": ["Gantt charts, burndown charts, PERT charts", "Issue logs, change logs, risk registers, dashboards"]}]},
      {"heading": "Domain 4: IT and governance", "items": [{"title": "ESG and compliance", "subtopics": ["Environmental, social, governance impacts", "Information security, compliance, privacy, change control"]}]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA Project+ certification?", "answer": "Project+ validates skills in IT project management using both agile and waterfall methodologies."},
      {"question": "What are the prerequisites?", "answer": "6-12 months experience managing tech projects recommended."},
      {"question": "How is Project+ different from PMP?", "answer": "Project+ is entry-level for IT projects, while PMP is advanced for any industry."}
    ])
  },
  {
    "slug": "comptia-server-plus",
    "title": "CompTIA Server+ Certification Training",
    "tagline": "Master server administration with Server+ certification",
    "price": 399, "original_price": 999, "rating": 4.4, "reviews": 640, "learners": "3,800+",
    "duration": "4 Months", "level": "Intermediate", "tag": "",
    "modules": 4, "projects": 4, "is_published": True, "sort_order": 12,
    "instructor_name": "Rohit Desai", "instructor_role": "Server+ Certified | MCSE | 16+ Years",
    "instructor_experience": "16+ years",
    "curriculum": "Hardware Installation, Administration, Security, Troubleshooting",
    "mode": "Live Online / Self-Paced", "language": "English",
    "target_audience": "System Administrators\nServer Support Technicians\nNetwork Administrators\nData Center Technicians",
    "eligibility": "CompTIA A+ certification or equivalent knowledge recommended, plus 2 years hands-on server experience.",
    "training_schedule": "Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)",
    "start_date": "Every Monday", "next_batch": "Starting 1st June 2026",
    "exam_code": "SK0-005",
    "tools_covered": "Windows Server, Linux Server, VMware, Hyper-V, RAID, PowerShell, Bash",
    "skills_covered": "Server Installation, Administration, Security, Virtualization, Troubleshooting",
    "certification": "Yes, Certificate of Completion. Prepares for CompTIA Server+ (SK0-005) exam.",
    "category": "Cloud Computing",
    "key_benefits": "Master server hardware installation\nManage server administration\nImplement security and disaster recovery\nTroubleshoot server issues",
    "why_join": "Server Focus|Dedicated server administration certification\nHands-on|Real server management experience\nCareer Path|Essential for data center roles",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support",
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: Server hardware installation and management", "items": [{"title": "Hardware and storage", "subtopics": ["Racking, cabling, power, cooling management", "RAID levels, shared storage, capacity planning", "Hardware maintenance, firmware upgrades"]}]},
      {"heading": "Domain 2: Server administration", "items": [{"title": "OS and network services", "subtopics": ["OS installation, partition types, file systems", "IP addressing, DNS, DHCP, VLANs"]}, {"title": "High availability and virtualization", "subtopics": ["Clustering, load balancing, failover", "Virtualization: host vs. guest, resource allocation"]}, {"title": "Scripting and asset management", "subtopics": ["Scripting basics, loops, variables", "Asset management, lifecycle management"]}]},
      {"heading": "Domain 3: Security and disaster recovery", "items": [{"title": "Data and physical security", "subtopics": ["Encryption, retention policies, access controls", "Identity management, MFA, server hardening"]}, {"title": "Mitigation and decommissioning", "subtopics": ["Malware prevention, DLP, SIEM", "Media destruction, recycling, asset management"]}]},
      {"heading": "Domain 4: Troubleshooting", "items": [{"title": "Hardware and software troubleshooting", "subtopics": ["Power issues, storage failures, connectivity", "OS errors, application issues, patching failures"]}, {"title": "Network and disaster recovery", "subtopics": ["Latency, misconfigurations, security breaches", "Backup strategies, recovery testing, failover validation"]}]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA Server+ certification?", "answer": "Server+ validates skills in server hardware, installation, administration, and troubleshooting."},
      {"question": "What are the prerequisites?", "answer": "A+ certification or equivalent knowledge plus 2 years server experience recommended."},
      {"question": "Does Server+ cover cloud?", "answer": "Yes, it covers both traditional data centers and modern hybrid cloud environments."}
    ])
  }
]

all_courses = GENERAL_COURSES + COMPTIA_COURSES
print(f"Total courses to sync: {len(all_courses)}")

SKIP_FIELDS = {"slug", "description", "overview", "image"}

with app.app_context():
    for data in all_courses:
        slug = data["slug"]
        course = Course.query.filter_by(slug=slug).first()
        if not course:
            course = Course(slug=slug)
            db.session.add(course)
            action = "Created"
        else:
            action = "Updated"

        for key, value in data.items():
            if key in SKIP_FIELDS:
                continue
            setattr(course, key, value)

        course.description = data.get("description", data.get("overview", ""))
        course.overview = data.get("overview", data.get("description", ""))

        try:
            db.session.commit()
            print(f"  [OK] {action}: {course.title}")
        except Exception as e:
            db.session.rollback()
            print(f"  [ERR] {slug}: {e}")

print("\nDone! All courses synced.")
