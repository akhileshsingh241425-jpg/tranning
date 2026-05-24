import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
sys.stdout.reconfigure(encoding='utf-8')

from app import app, db, Course

courses = [
  {
    "slug": "comptia-pentest-plus",
    "title": "CompTIA PenTest+ Certification Training",
    "tagline": "Master penetration testing and earn PenTest+ certification",
    "description": "A successful candidate for CompTIA PenTest+ certification will demonstrate their ability to perform a penetration test, including vulnerability scanning, understanding legal and compliance requirements, analyzing the results, and producing a written report.",
    "overview": "CompTIA PenTest+ is one of the most comprehensive courses that cover all the PenTesting stages. PenTest+ is the only exam that incorporates all aspects of vulnerability management. This course also includes all the latest techniques used against the expanded attack surfaces.",
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
    "topic_wise_content": json.dumps([
      {"heading": "Module 1: Planning and scoping", "items": [
        {"title": "Governance and scoping", "subtopics": ["Compare governance, risk, and compliance concepts", "Explain importance of scoping requirements", "Demonstrate ethical hacking mindset"]}
      ]},
      {"heading": "Module 2: Information gathering and vulnerability scanning", "items": [
        {"title": "Reconnaissance and scanning", "subtopics": ["Passive reconnaissance techniques", "Active reconnaissance techniques", "Analyze reconnaissance results", "Perform vulnerability scanning"]}
      ]},
      {"heading": "Module 3: Attacks and exploits", "items": [
        {"title": "Network and wireless attacks", "subtopics": ["Research attack vectors and perform network attacks", "Perform wireless attacks", "Perform application-based attacks", "Attacks on cloud technologies"]},
        {"title": "Post-exploitation", "subtopics": ["Common attacks on specialized systems", "Social engineering and physical attacks", "Post-exploitation techniques"]}
      ]},
      {"heading": "Module 4: Reporting and communication", "items": [
        {"title": "Reports and communication", "subtopics": ["Written report components", "Analyze findings and recommend remediation", "Communication during penetration testing", "Post-report delivery activities"]}
      ]},
      {"heading": "Module 5: Tools and code analysis", "items": [
        {"title": "Scripting and tools", "subtopics": ["Basic scripting and software development concepts", "Analyze scripts for penetration testing", "Use cases of penetration testing tools"]}
      ]}
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
    "description": "SecurityX is an advanced cybersecurity certification for security architects and senior security engineers. It proves you have the skills to design, build, and implement secure solutions across complex environments.",
    "overview": "The CompTIA SecurityX Certification Training is an advanced cybersecurity program designed for experienced IT professionals who want to validate their expertise in enterprise security architecture, risk management, security engineering, incident response, and governance. SecurityX is the updated advanced-level certification from CompTIA.",
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
    "topic_wise_content": json.dumps([
      {"heading": "Module 1: Governance, risk, and compliance", "items": [
        {"title": "Security program documentation", "subtopics": ["Policies, procedures, standards, guidelines", "Program management, training, communication, RACI matrix"]},
        {"title": "Risk management", "subtopics": ["Impact analysis, quantitative vs. qualitative assessment", "Third-party risk, threat modeling, ATT&CK, STRIDE"]},
        {"title": "Compliance strategies", "subtopics": ["PCI DSS, ISO/IEC 27000, NIST CSF, CSA"]}
      ]},
      {"heading": "Module 2: Security architecture", "items": [
        {"title": "Cloud architecture", "subtopics": ["CASB, shadow IT detection, shared responsibility model", "CI/CD, Terraform, Ansible, container security, serverless"]},
        {"title": "Network architecture and zero trust", "subtopics": ["Segmentation, microsegmentation, VPN, SASE, SD-WAN", "Zero trust concepts, deperimeterization"]}
      ]},
      {"heading": "Module 3: Security engineering", "items": [
        {"title": "Automation and cryptography", "subtopics": ["Scripting: PowerShell, Bash, Python, SOAR, IaC", "Advanced cryptography: PQC, homomorphic encryption, blockchain"]}
      ]},
      {"heading": "Module 4: Security operations", "items": [
        {"title": "Monitoring and threat hunting", "subtopics": ["SIEM, aggregate analysis, behavior baselines", "Internal/external intelligence, TIPs, STIX/TAXII, Sigma, YARA"]},
        {"title": "Incident response", "subtopics": ["Malware analysis, reverse engineering, IoC extraction, root cause analysis"]}
      ]}
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
    "description": "Cloud solutions continue to dominate the technology market. The CompTIA Cloud+ certification validates the skills you need to maintain cloud infrastructure services and secure cloud environments.",
    "overview": "The CompTIA Cloud+ certification places an emphasis on incorporating and managing cloud technologies as part of a broader system of operations. It includes new technologies to support the changing cloud market as more organizations depend on cloud-based technologies to run mission-critical systems. It is the only vendor-neutral, performance-based certification.",
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
    "topic_wise_content": json.dumps([
      {"heading": "Module 1: Cloud architecture", "items": [
        {"title": "Cloud models and virtualization", "subtopics": ["Public, private, hybrid, multi-cloud models", "Virtualization technologies, cloud networking, VPN"]},
        {"title": "Containerization and orchestration", "subtopics": ["Containerization, orchestration techniques", "Database concepts, resource optimization, billing"]}
      ]},
      {"heading": "Module 2: Deployment", "items": [
        {"title": "Migration and IaC", "subtopics": ["System requirements analysis", "Infrastructure as Code (IaC) techniques", "Workload migrations, resource provisioning"]}
      ]},
      {"heading": "Module 3: Operations", "items": [
        {"title": "Lifecycle and observability", "subtopics": ["Lifecycle management, scaling, updates", "Backup and recovery, monitoring and optimization"]}
      ]},
      {"heading": "Module 4: Security", "items": [
        {"title": "Cloud security", "subtopics": ["Vulnerability management, IAM", "Container security, compliance (PCI DSS, SOC 2, ISO 27001)"]}
      ]},
      {"heading": "Module 5: DevOps fundamentals", "items": [
        {"title": "CI/CD and automation", "subtopics": ["Automation tools, source control", "CI/CD pipelines, Kubernetes, Ansible, Jenkins"]}
      ]},
      {"heading": "Module 6: Troubleshooting", "items": [
        {"title": "Cloud troubleshooting", "subtopics": ["Deployment issues, network connectivity", "Security incidents, service disruptions, misconfigurations"]}
      ]}
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
    "description": "CompTIA Data+ is an early-career data analytics certification that shows you have the practical skills to turn raw data into meaningful insights.",
    "overview": "The CompTIA Data+ certification is for professionals who are in charge of making data-driven decisions. It equates to 18-24 months of practical experience in business intelligence or data analyst capacity. Holders have knowledge to translate business requirements into data-driven decisions through data mining, manipulation, statistical procedures, and analysis.",
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
    "topic_wise_content": json.dumps([
      {"heading": "Module 1: Data concepts and environments", "items": [
        {"title": "Data fundamentals", "subtopics": ["Database types, data structures, file extensions, data types"]},
        {"title": "Data sources and infrastructure", "subtopics": ["Databases, APIs, website data, cloud, on-premise, storage"]},
        {"title": "AI concepts", "subtopics": ["AI models, NLP, robotic automation"]}
      ]},
      {"heading": "Module 2: Data acquisition and preparation", "items": [
        {"title": "Data collection", "subtopics": ["Data integration methods, queries to gather and combine data"]},
        {"title": "Data exploration and transformation", "subtopics": ["Find missing values, duplication, redundancy, outliers", "Cleansing, merging, parsing, formatting data"]}
      ]},
      {"heading": "Module 3: Data analysis", "items": [
        {"title": "Analysis methods", "subtopics": ["Communicate results, select methods for audiences", "Statistical methods, troubleshooting analysis issues"]}
      ]},
      {"heading": "Module 4: Visualization and reporting", "items": [
        {"title": "Visuals and reports", "subtopics": ["Charts, maps, tables, design elements", "Dashboards, summaries, validation and review"]}
      ]},
      {"heading": "Module 5: Data governance", "items": [
        {"title": "Data management", "subtopics": ["Documentation, versioning, data lineage"]},
        {"title": "Compliance and quality", "subtopics": ["Retention, audits, regulations, access control, encryption", "Profiling, monitoring, testing for data quality"]}
      ]}
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
    "description": "The CompTIA Linux Plus training is designed to equip participants with the essential knowledge and skills to effectively configure, manage, operate, and troubleshoot Linux server environments.",
    "overview": "This CompTIA Linux Plus training provides a deep dive into the intricacies of Linux system administration, preparing you for the CompTIA Linux+ certification. It covers system management, security, automation, scripting, containerization, virtualization, and troubleshooting.",
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
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: System management", "items": [
        {"title": "Linux basics and storage", "subtopics": ["Boot process, kernel, filesystems, device management", "LVM, RAID, partitions, mounted storage"]},
        {"title": "Network and virtualization", "subtopics": ["Network configuration, DNS, interfaces", "Hypervisors, VMs, disk images"]}
      ]},
      {"heading": "Domain 2: Services and user management", "items": [
        {"title": "Files and accounts", "subtopics": ["Permissions, links, special files, user/group management"]},
        {"title": "Process and software", "subtopics": ["Process monitoring, job scheduling, package management", "Containers, container runtimes"]}
      ]},
      {"heading": "Domain 3: Security", "items": [
        {"title": "Authentication and firewalls", "subtopics": ["PAM, LDAP, Kerberos, auditing", "iptables, nftables, UFW"]},
        {"title": "Hardening and compliance", "subtopics": ["OS hardening, sudo, MFA, cryptography", "Integrity verification, scanning"]}
      ]},
      {"heading": "Domain 4: Automation and scripting", "items": [
        {"title": "Automation tools", "subtopics": ["Ansible, Puppet, CI/CD tools", "Shell scripting, Python basics, Git"]}
      ]},
      {"heading": "Domain 5: Troubleshooting", "items": [
        {"title": "System and network troubleshooting", "subtopics": ["System monitoring, hardware/storage diagnostics", "Network troubleshooting, security fixes, performance analysis"]}
      ]}
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
    "description": "The CompTIA Project+ (v5) Certification Training is a globally recognized certification tailored for IT professionals managing small to medium-sized projects.",
    "overview": "The CompTIA Project+ (v5) Certification Training is designed to equip IT professionals with the foundational skills to manage projects efficiently in tech environments. Covering both traditional and agile methodologies, this course dives into core project management concepts, tools, life cycle phases, documentation practices, and IT governance.",
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
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: Project management concepts", "items": [
        {"title": "Methodologies and frameworks", "subtopics": ["Project characteristics, methodologies, Agile vs. Waterfall", "Change control, risk management, issue management"]},
        {"title": "Schedule and communication", "subtopics": ["Schedule management, milestones, quality management", "Communication management, meeting management, resource management"]}
      ]},
      {"heading": "Domain 2: Project life cycle phases", "items": [
        {"title": "Discovery to closing", "subtopics": ["Discovery artifacts, business cases", "Initiation, planning, execution, closing"]}
      ]},
      {"heading": "Domain 3: Tools and documentation", "items": [
        {"title": "Project tools", "subtopics": ["Gantt charts, burndown charts, PERT charts", "Issue logs, change logs, risk registers, dashboards"]}
      ]},
      {"heading": "Domain 4: IT and governance", "items": [
        {"title": "ESG and compliance", "subtopics": ["Environmental, social, governance impacts", "Information security, compliance, privacy, change control"]}
      ]}
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
    "description": "This program isn't just about learning; it's about mastering server technology through an immersive, expert-led experience aligned with CompTIA's official standards.",
    "overview": "The CompTIA Server+ certification validates essential skills for IT professionals working with servers, from traditional data centers to modern hybrid cloud setups. The program covers server operations, hardware installation, administration, security, disaster recovery, and troubleshooting.",
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
    "topic_wise_content": json.dumps([
      {"heading": "Domain 1: Server hardware installation and management", "items": [
        {"title": "Hardware and storage", "subtopics": ["Racking, cabling, power, cooling management", "RAID levels, shared storage, capacity planning", "Hardware maintenance, firmware upgrades"]}
      ]},
      {"heading": "Domain 2: Server administration", "items": [
        {"title": "OS and network services", "subtopics": ["OS installation, partition types, file systems", "IP addressing, DNS, DHCP, VLANs"]},
        {"title": "High availability and virtualization", "subtopics": ["Clustering, load balancing, failover", "Virtualization: host vs. guest, resource allocation"]},
        {"title": "Scripting and asset management", "subtopics": ["Scripting basics, loops, variables", "Asset management, lifecycle management"]}
      ]},
      {"heading": "Domain 3: Security and disaster recovery", "items": [
        {"title": "Data and physical security", "subtopics": ["Encryption, retention policies, access controls", "Identity management, MFA, server hardening"]},
        {"title": "Mitigation and decommissioning", "subtopics": ["Malware prevention, DLP, SIEM", "Media destruction, recycling, asset management"]}
      ]},
      {"heading": "Domain 4: Troubleshooting", "items": [
        {"title": "Hardware and software troubleshooting", "subtopics": ["Power issues, storage failures, connectivity", "OS errors, application issues, patching failures"]},
        {"title": "Network and disaster recovery", "subtopics": ["Latency, misconfigurations, security breaches", "Backup strategies, recovery testing, failover validation"]}
      ]}
    ]),
    "faq": json.dumps([
      {"question": "What is CompTIA Server+ certification?", "answer": "Server+ validates skills in server hardware, installation, administration, and troubleshooting."},
      {"question": "What are the prerequisites?", "answer": "A+ certification or equivalent knowledge plus 2 years server experience recommended."},
      {"question": "Does Server+ cover cloud?", "answer": "Yes, it covers both traditional data centers and modern hybrid cloud environments."}
    ])
  }
]

print(f"Adding {len(courses)} remaining courses...")

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

print("Done! All courses synced.")
