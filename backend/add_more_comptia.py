import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
sys.stdout.reconfigure(encoding='utf-8')

from app import app, db, Course

courses = [
  {
    "slug": "comptia-cysa-plus",
    "title": "CompTIA CySA+ Certification Training",
    "tagline": "Become a Cybersecurity Analyst with CySA+ certification",
    "description": "The CompTIA CySA+ (Cybersecurity Analyst+) (CS0-003) certification training program from Trainingprotec focuses on cybersecurity's technical and hands-on aspects, encompassing cyber threats, secure network architecture, risk management, log analysis, configuration assessments, and more.",
    "overview": "The CompTIA Cybersecurity Analyst (CySA+) certification showcases your proficiency in utilizing behavioral analytics and detection techniques to spot and respond to cybersecurity threats. To earn the CySA+ certification, you'll need to thoroughly understand the key topics covered in its body of knowledge, such as threat intelligence, data interpretation, and vulnerability management.",
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
    "course_objective": "[\"Detect and analyze indicators of malicious activity\",\"Understand threat hunting and threat intelligence concepts\",\"Use appropriate tools to manage, prioritize and respond to attacks\",\"Perform incident response processes\",\"Understand reporting and communication concepts related to vulnerability management\"]",
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
    "description": "The CompTIA SecAI+ (v1) Certification Training Course from TrainingProtec is a vendor-neutral, security-focused program designed to validate the skills required to identify, mitigate, and manage security risks introduced by Artificial Intelligence systems.",
    "overview": "The CompTIA SecAI+ (v1) Certification Course equips cybersecurity professionals with the knowledge required to secure AI-enabled systems and defend against AI-driven threats. The course begins with basic AI concepts related to cybersecurity (17%), ensuring learners understand machine learning, deep learning, NLP, and automation from a security and risk perspective. The core focuses on securing AI systems (40%), AI-assisted security (24%), and AI governance, risk, and compliance (19%).",
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
    "course_objective": "[\"Explain core AI concepts and terminology relevant to cybersecurity\",\"Identify AI applications used in threat detection and security operations\",\"Recognize AI-driven threats including adversarial and generative AI\",\"Implement security controls to protect AI systems and models\",\"Secure AI deployment environments across cloud and hybrid platforms\",\"Apply AI-assisted techniques to improve detection and response\",\"Integrate governance, risk, and compliance into AI initiatives\"]",
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
  }
]

print(f"Adding {len(courses)} more courses...")

with app.app_context():
    for data in courses:
        slug = data["slug"]
        course = Course.query.filter_by(slug=slug).first()
        if not course:
            course = Course(slug=slug)
            db.session.add(course)
            action = "Created"
        else:
            action = "Updated"
        
        for key, value in data.items():
            if key == "slug":
                continue
            setattr(course, key, value)
        
        try:
            db.session.commit()
            print(f"  [OK] {action}: {course.title}")
        except Exception as e:
            db.session.rollback()
            print(f"  [ERR] {slug}: {e}")

print("Done!")
