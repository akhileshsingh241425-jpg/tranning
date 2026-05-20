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

def add_or_update_comptia_courses():
    with app.app_context():
        
        # ============================================
        # 1. CompTIA A+ Certification Training
        # ============================================
        courses_data = [
            {
                'title': 'CompTIA A+ Certification Training',
                'slug': 'comptia-a-certification-training',
                'description': 'Our CompTIA A+ training program is designed to equip participants with the essential skills and knowledge needed to excel in entry-level IT roles. The program covers a comprehensive curriculum that includes hardware and software troubleshooting, operating systems, networking, and security.',
                'tagline': 'Master CompTIA A+ Certification - Hardware, Software, Networking & Security',
                'overview': '''The CompTIA A+ certification training course is created for all entry-level and aspiring IT professionals to validate their skills and knowledge in the IT domain. The certification course is made for learners to properly understand the hardware and software technologies that they will be working with so that they can support various IT infrastructures. Organizations often look for this certification as a marker and validation of the prospective employee's skills. The certification has two examinations that candidates need to clear to become certified CompTIA A+ professionals.''',
                'key_benefits': '''• Prepare and pass the CompTIA A+ certification exams
• Install and configure the components of the PC system and peripheral devices
• Install, configure, and troubleshoot internal system components
• Understand how to identify, use, and connect hardware components and devices
• Understand the concepts of network infrastructure
• Understand how to set up network connections and troubleshoot them
• Learn laptop support and troubleshooting
• Understand how to troubleshoot and support mobile devices
• Understand how to set up, configure, and troubleshoot printing devices
• Understand how to put client virtualization and cloud computing into practice
• Learn how to identify and defend devices and their network connections against security risks''',
                'topic_wise_content': '''Domain 1: Mobile devices (13%) - Hardware setup, Accessory options, Network setup, Troubleshooting
Domain 2: Networking (23%) - Protocols and ports, SOHO networks, Networking tools
Domain 3: Hardware (25%) - Component installation, Cables and connectors, Peripheral devices, Motherboards and power
Domain 4: Virtualization and cloud computing - Virtualization concepts, Cloud models
Domain 5: Hardware and network troubleshooting - Diagnosing issues, Troubleshooting tools
Domain 1 (Core 2): Operating systems - OS installation, Windows tools, File systems
Domain 2 (Core 2): Security - Security measures, Malware prevention
Domain 3 (Core 2): Software troubleshooting - OS issues, Mobile troubleshooting, Security concerns
Domain 4 (Core 2): Operational procedures - Documentation, Safety and communication, Backup and recovery''',
                'prerequisites': '''• Basic computer knowledge
• No prior IT experience required
• Interest in IT career
• Willingness to learn''',
                'skills_covered': 'Hardware Installation, Software Configuration, Networking Basics, Security Fundamentals, Troubleshooting, Operating Systems, Mobile Device Support, Virtualization, Cloud Computing, Printer Support, Laptop Support',
                'tools_covered': 'Windows, macOS, Linux, Command Prompt, Task Manager, Disk Management, Device Manager, BIOS/UEFI',
                'target_audience': '''• Individuals interested in pursuing a profession in IT
• Individuals who want to get their CompTIA A+ certification
• Beginners starting IT career
• Help Desk Technicians
• Desktop Support Engineers
• Entry-level IT Support Staff''',
                'duration': '6 Months',
                'level': 'Beginner',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 299,
                'original_price': 799,
                'discount_percent': 62,
                'rating': 4.5,
                'reviews': 1200,
                'learners': '1500+',
                'modules': 14,
                'projects': 8,
                'emi_options': 'No Cost EMI starting @ $25/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 1st June 2026',
                'exam_code': '220-1101 (Core 1) & 220-1102 (Core 2)',
                'exam_questions': 'Maximum 90 Questions each',
                'exam_duration': '90 Minutes each',
                'exam_format': 'Multiple Choice + Performance-Based Questions',
                'exam_passing_score': '675 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA A+ Certification - Industry-recognized entry-level IT certification',
                'course_objectives': '''• Prepare and pass the CompTIA A+ certification exams
• Install and configure the components of the PC system and peripheral devices
• Install, configure, and troubleshoot internal system components
• Understand how to identify, use, and connect hardware components and devices
• Understand the concepts of network infrastructure
• Understand how to set up network connections and troubleshoot them
• Learn laptop support and troubleshooting
• Understand how to troubleshoot and support mobile devices
• Understand how to set up, configure, and troubleshoot printing devices
• Understand how to put client virtualization and cloud computing into practice
• Learn how to identify and defend devices and their network connections against security risks''',
                'faq': '''Q: Is the CompTIA A+ certification a suitable place to start?|A: Yes, the CompTIA A+ certification might help you get entry-level IT roles such as Desktop Support, Help Desk Tech, Desktop Support Administrator. It's a wonderful place to begin and provides core information for bigger IT careers.
Q: What jobs can you obtain with CompTIA A+?|A: Service Desk Analyst, Help Desk Tech, Desktop Support Administrator, Technical Support Specialist, End-User Computing Technician, Field Service Technician, Help Desk Technician, Associate Network Engineer, System Support Specialist, Data Support Technician
Q: What does the CompTIA A+ certification cost?|A: The CompTIA A+ certification costs $232 USD per exam (total $464 for both exams).
Q: How to Pass the CompTIA A+ Exam?|A: You can prepare through CompTIA A+ study guide, self-study using online resources, instructor-led CompTIA A+ certification training, and practice tests.
Q: Is CompTIA A+ a difficult exam?|A: The CompTIA A+ is a professional industry certification on par with other entry-level licenses. With proper preparation and strategy, you can pass the two exams.
Q: What is the next step after CompTIA A+?|A: You can pursue CompTIA Network+, Security+, Cloud+, or specialize in cybersecurity, networking, or cloud computing.
Q: Is CompTIA A+ required for Network+?|A: No, obtaining a CompTIA A+ certification is not a prerequisite for obtaining Network+, though it builds a strong foundation.
Q: How much earnings can I make with CompTIA A+?|A: According to Glassdoor: Associate Network Engineer ($67,162), Desktop Support Administrator ($50,903), Service Desk Analyst ($43,679), Help Desk Tech ($40,424)''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800'
            },

            # ============================================
            # 2. CompTIA Network+ Certification Training
            # ============================================
            {
                'title': 'CompTIA Network+ Certification Training',
                'slug': 'comptia-network-plus-certification-training',
                'description': 'The Network+ certification exam training provided is an entry-level training for IT professionals that helps them acquire the necessary skills to manage, maintain, troubleshoot, install, and configure basic computer networks.',
                'tagline': 'Master Network Management, Troubleshooting & Advanced Networking Technologies',
                'overview': '''The CompTIA Network+ certification validates your knowledge and skills of installing, managing, and troubleshooting networks on various platforms. This course is composed to help you learn all the required objectives to gain the CompTIA Network+ certification. You will learn the latest networking technologies available, various networks and networking protocols, identify VPN and VLAN features, DNS concepts, and implement wireless networks.''',
                'key_benefits': '''• Learn latest networking technologies and methodologies
• Hands-on practical skills for complex networking issues
• Industry-recognized baseline networking credential
• Covers wired and wireless network management
• Validates network infrastructure expertise
• Prepares for advanced certifications like CCNA
• Applicable across most today's job roles
• Focus on connectivity and performance optimization''',
                'topic_wise_content': '''Domain 1: Networking concepts - OSI model, Networking appliances, Cloud concepts, Ports and protocols, Traffic types, Transmission media, Network topologies, IPv4 addressing
Domain 2: Network implementation - Routing technologies, Switching technologies, Wireless devices, Physical installations
Domain 3: Network operations - Documentation, Life-cycle management, Change management, Configuration management, Network monitoring, Disaster recovery, Network services, Access and management
Domain 4: Network security - Logical security, Physical security, Deception technologies, Security terminology, Audits and compliance, Network segmentation, Types of attacks, Security features and defense
Domain 5: Network troubleshooting - Troubleshooting methodology, Cabling and physical interface issues, Network services issues, Performance issues, Tools and protocols''',
                'prerequisites': '''• No required pre-requisites for Network+ certification
• CompTIA A+ certification recommended
• 9 months of networking experience recommended
• Basic IT knowledge
• Understanding of networking fundamentals''',
                'skills_covered': 'Network Architecture, Routing and Switching, Wireless Networking, Network Security, Troubleshooting, Cloud Networking, VPN Management, VLAN Configuration, DNS, DHCP, Load Balancing, Disaster Recovery',
                'tools_covered': 'Protocol Analyzers, Command Line Tools, Cable Testers, Wi-Fi Analyzers, SIEM Tools, Network Monitoring Tools, Packet Capture Tools',
                'target_audience': '''• Anyone who wishes to enhance networking knowledge
• Professionals in network support and administration
• Students starting cybersecurity career
• IT Consultants
• Computer Technicians
• Help Desk Technicians
• System Engineers
• Network Support Specialists
• Network Analysts''',
                'duration': '4 Months',
                'level': 'Intermediate',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 349,
                'original_price': 899,
                'discount_percent': 61,
                'rating': 4.6,
                'reviews': 950,
                'learners': '1200+',
                'modules': 12,
                'projects': 10,
                'emi_options': 'No Cost EMI starting @ $29/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 1st June 2026',
                'exam_code': 'N10-008',
                'exam_questions': 'Maximum 90 Questions',
                'exam_duration': '90 Minutes',
                'exam_format': 'Multiple Choice + Performance-Based Questions',
                'exam_passing_score': '720 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA Network+ Certification - Valid for 3 years from passing date',
                'course_objectives': '''• Explain the purpose and uses of ports and protocols
• Explain devices, application protocols, and services on their appropriate OSI layers
• Explain the characteristics and concepts of routing and switching
• Understand to configure the appropriate IP address
• Understanding of network topologies types and technologies
• Implement the appropriate wireless technologies and configurations
• Explain the use cases for advanced networking devices
• Explain various types of networking attacks
• Learn how to identify and defend devices against security risks''',
                'faq': '''Q: What is the importance of CompTIA Network+ certification?|A: CompTIA Network+ validates your knowledge and skills required to troubleshoot, configure and manage wired and wireless networks found in corporations.
Q: What other courses are recommended before and after CompTIA Network+?|A: CompTIA A+ is recommended before. CCNA and CEHv11 are recommended after.
Q: Can you take the Network+ exam without CompTIA A+ certification?|A: CompTIA recommends A+ first, but if you have basic IT and hardware knowledge, you can directly pursue Network+.
Q: What is CompTIA Network+ retake policy?|A: You don't need to wait for second attempt. Before third or subsequent attempts, wait at least 14 days from your last attempt.
Q: What job can I get with CompTIA Network+ certification?|A: IT Consultant, Computer Technician, Help Desk Technician, System Engineer, Network Support Specialist, Network Analyst
Q: Will I get recording of sessions?|A: Yes, you will get the recording of sessions after completion of training.
Q: Do your instructors hold current certifications?|A: Yes, all instructors are certified in CompTIA A+, Network+, Security+ and other certifications.
Q: What is the validity of CompTIA Network+ certificate?|A: CompTIA Network+ certification is valid for three years from the day you pass your exam.
Q: What study materials will you provide?|A: Course Notes, Slides, Handouts, eBooks, and lab practice questions.
Q: What study materials will be provided?|A: You will receive Course Notes, Slides, Handouts, eBooks, and lab practice questions for practical knowledge.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800'
            },

            # ============================================
            # 3. CompTIA Security+ Certification Training
            # ============================================
            {
                'title': 'CompTIA Security+ Certification Training',
                'slug': 'comptia-security-plus-certification-training',
                'description': 'Our CompTIA Security+ training is designed to provide you with a comprehensive understanding of the principles and best practices required to secure networks, systems, and data.',
                'tagline': 'Advanced Cybersecurity Foundation - Network Security, Encryption & Compliance',
                'overview': '''CompTIA Security+ Training covers many areas of network security, including cloud security, encryption, security protocols, system security and network infrastructure. Our training is ideal for network administrators, security consultants, security engineers, security analysts and people looking to enter into cybersecurity. Learn about general security concepts, communications security and operational and organizational security.''',
                'key_benefits': '''• Comprehensive network security understanding
• Cloud security best practices
• Encryption and security protocols
• System and infrastructure security
• Compliance and operational security
• Industry-recognized foundational certification
• Average salary ~$199K per annum
• Gateway to advanced cybersecurity certifications
• Essential skills for security professionals
• Government compliance requirements''',
                'topic_wise_content': '''Domain 1: General security concepts - Security controls, Fundamental concepts (CIA, AAA, Zero Trust), Change management, Cryptographic solutions
Domain 2: Threats, vulnerabilities, and mitigations - Threat actors, Threat vectors, Vulnerabilities, Malicious activity, Mitigation techniques
Domain 3: Security architecture - Architecture models, Enterprise infrastructure, Data protection, Resilience and recovery
Domain 4: Security operations - Computing resources, Asset management, Vulnerability management, Alerting and monitoring, Enterprise security, Identity and access management, Automation and orchestration, Incident response, Data sources
Domain 5: Security program management - Security governance, Risk management, Third-party risk, Security compliance, Audits and assessments, Security awareness''',
                'prerequisites': '''• No formal prerequisites required
• Basic networking knowledge helpful but not necessary
• Basic information security understanding helpful
• Interest in cybersecurity field
• Foundational IT knowledge recommended''',
                'skills_covered': 'Information Security Controls, Security Policies, Authentication Methods, Cryptography Fundamentals, Vulnerability Assessment, Wireless Security, Mobile Security Management, Risk Management, Incident Response, Compliance and Governance',
                'tools_covered': 'Encryption tools, Firewall configurations, SIEM platforms, VPN technologies, PKI systems, Security protocols, Network monitoring tools',
                'target_audience': '''• Network Administrators
• System Administrators
• Cyber Security Enthusiasts
• Security Engineers
• Security Analysts
• Network Security Professionals
• Anyone advancing CyberSecurity career
• Aspiring cybersecurity professionals
• IT professionals seeking specialization''',
                'duration': '5 Months',
                'level': 'Intermediate',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 399,
                'original_price': 999,
                'discount_percent': 60,
                'rating': 4.7,
                'reviews': 1450,
                'learners': '1800+',
                'modules': 15,
                'projects': 12,
                'emi_options': 'No Cost EMI starting @ $33/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 1st June 2026',
                'exam_code': 'SY0-601',
                'exam_questions': 'Maximum 90 Questions',
                'exam_duration': '90 Minutes',
                'exam_format': 'Multiple Choice + Performance-Based Questions',
                'exam_passing_score': '750 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA Security+ Certification - Industry-recognized cybersecurity foundation certification',
                'course_objectives': '''• Develop comprehensive understanding of foundational security concepts
• Learn to identify, assess, and mitigate threats, vulnerabilities, and risks
• Master principles of designing and implementing robust security architecture
• Gain expertise in day-to-day security operations
• Acquire knowledge for effective security program management
• Understand incident response and security monitoring
• Learn compliance and governance frameworks
• Implement security controls and best practices''',
                'faq': '''Q: Why should you learn CompTIA Security Plus?|A: The CompTIA Security Plus Certification is extensively recognized by IT industry and empowers professionals with skills for cybersecurity roles. Average salary is around $199K per annum.
Q: What are the prerequisites?|A: No formal prerequisites. Basic networking and security knowledge is helpful but not necessary.
Q: Who should take this course?|A: Network Administrators, System Administrators, Cyber Security Enthusiasts, Security Engineers, and anyone advancing cybersecurity career.
Q: What will I learn?|A: Information Security Controls, Security Policies, Authentication, Cryptography, Vulnerabilities, Wireless Threats, Mobile Security, Risk Management, and Incident Response.
Q: Is this for beginners?|A: Yes, though intermediate IT knowledge is recommended. It's the foundational cybersecurity certification.
Q: What certifications should I pursue after?|A: You can pursue CySA+, PenTest+, CISSP, or specialize in cloud or network security.
Q: How long is the course?|A: Typically 5 months with live classes, but self-paced options available.
Q: What's the job market like?|A: Security+ opens doors to various cybersecurity roles with strong salary prospects.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800'
            },

            # ============================================
            # 4. CompTIA CySA+ Certification Training
            # ============================================
            {
                'title': 'CompTIA CySA+ Certification Training',
                'slug': 'comptia-cysa-plus-certification-training',
                'description': 'The CompTIA CySA+ (Cybersecurity Analyst+) (CS0-003) certification training focuses on cybersecurity technical and hands-on aspects, encompassing cyber threats, secure network architecture, risk management, and incident response.',
                'tagline': 'Advanced Threat Detection, Analysis & Incident Response for Security Professionals',
                'overview': '''The CompTIA Cybersecurity Analyst (CySA+) certification showcases your proficiency in utilizing behavioral analytics and detection techniques to spot and respond to cybersecurity threats. Upon successful completion, individuals are equipped with necessary knowledge and skills to effectively identify, analyze, and interpret indicators of malicious activity. They gain comprehensive understanding of threat intelligence and management, enabling them to respond to attacks and vulnerabilities proactively.''',
                'key_benefits': '''• Behavioral analytics and detection techniques
• Threat intelligence and management expertise
• Hands-on incident response methodologies
• Log analysis and data interpretation
• Vulnerability assessment and prioritization
• Advanced threat detection tools proficiency
• Network monitoring expertise
• Risk mitigation strategies
• Security breach identification
• Effective response protocols implementation''',
                'topic_wise_content': '''Domain 1: Security operations - System and network architecture, Malicious activity indicators, Tools and techniques, Threat intelligence and hunting, Process improvement
Domain 2: Vulnerability management - Vulnerability scanning, Assessment tool output, Vulnerability prioritization, Mitigation controls, Vulnerability response
Domain 3: Incident response management - Attack methodology frameworks, Incident response activities, Incident management life cycle
Domain 4: Reporting and communication - Vulnerability management reporting, Incident response reporting''',
                'prerequisites': '''• Basic knowledge of Network+, Security+, or equivalent discipline
• Minimum 4 years hands-on experience as:
  - Incident Response Analyst
  - Security Operations Center (SOC) Analyst
  - Similar cybersecurity domain''',
                'skills_covered': 'Threat Detection, Log Analysis, SIEM Tools, Behavioral Analytics, Incident Response, Vulnerability Assessment, Threat Hunting, Risk Management, Attack Analysis, Evidence Preservation',
                'tools_covered': 'Wireshark, SIEM platforms, VirusTotal, Python, PowerShell, Forensic tools, Threat intelligence platforms, Network analyzers',
                'target_audience': '''• IT Security Analysts
• Vulnerability Analysts
• Threat Intelligence Analysts
• SOC Analysts
• Incident Response Professionals
• Security Operations Center staff
• Cybersecurity specialists
• Anyone pursuing advanced security analysis role''',
                'duration': '4 Months',
                'level': 'Advanced',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 449,
                'original_price': 1099,
                'discount_percent': 59,
                'rating': 4.8,
                'reviews': 680,
                'learners': '800+',
                'modules': 13,
                'projects': 15,
                'emi_options': 'No Cost EMI starting @ $37/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 8th June 2026',
                'exam_code': 'CS0-003',
                'exam_questions': 'Maximum 85 Questions',
                'exam_duration': '165 Minutes (2 hours 45 minutes)',
                'exam_format': 'Multiple Choice + Simulation Questions',
                'exam_passing_score': '750 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA CySA+ Certification - Advanced cybersecurity analyst credential',
                'course_objectives': '''• Detect and analyze indicators of malicious activity
• Understand threat hunting and threat intelligence concepts
• Use appropriate tools and methods to manage, prioritize and respond to attacks
• Perform incident response processes
• Understand reporting and communication concepts
• Analyze vulnerabilities and prioritize remediation
• Apply advanced detection techniques
• Integrate threat intelligence into security operations''',
                'faq': '''Q: What is CySA+ certification?|A: CySA+ (Cybersecurity Analyst+) is an advanced CompTIA certification validating skills in threat detection, analysis, and incident response.
Q: Who should take CySA+?|A: Security analysts, threat hunters, SOC analysts, and cybersecurity professionals with 4+ years experience.
Q: What are prerequisites?|A: Basic Network+ or Security+ knowledge and 4 years hands-on cybersecurity experience.
Q: What does CySA+ focus on?|A: Threat detection, behavioral analytics, incident response, vulnerability management, and log analysis.
Q: How is CySA+ different from Security+?|A: Security+ is foundational; CySA+ is advanced technical certification focusing on threat analysis and incident response.
Q: What tools will I learn?|A: Wireshark, SIEM tools, VirusTotal, Python, PowerShell, forensic tools, and threat intelligence platforms.
Q: What jobs can I get?|A: SOC Analyst, Threat Hunter, Security Analyst, Incident Response Analyst, Vulnerability Analyst.
Q: Is CySA+ valuable?|A: Yes, highly valued for hands-on cybersecurity roles with strong career prospects.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1550439062-1d5142147f17?w=800'
            },

            # ============================================
            # 5. CompTIA SecAI+ Certification Training
            # ============================================
            {
                'title': 'CompTIA SecAI+ Certification Training',
                'slug': 'comptia-secai-plus-certification-training',
                'description': 'The CompTIA SecAI+ (v1) Certification Training is a vendor-neutral, security-focused program designed to validate skills required to identify, mitigate, and manage security risks introduced by Artificial Intelligence systems.',
                'tagline': 'Secure AI Systems - Threat Detection, Governance & AI-Driven Security Operations',
                'overview': '''The CompTIA SecAI+ (v1) Certification Course equips cybersecurity professionals with knowledge to secure AI-enabled systems and defend against AI-driven threats. The course covers basic AI concepts (17%), securing AI systems (40%), AI-assisted security (24%), and AI governance, risk, and compliance (19%). Participants gain practical insight into how attackers misuse AI, how defenders can secure AI models and data pipelines, and how organizations can govern AI responsibly.''',
                'key_benefits': '''• Secure AI-enabled systems and models
• Defend against AI-driven threats
• Protect AI data pipelines and training data
• AI-assisted threat detection techniques
• Adversarial machine learning defense
• Data poisoning protection
• Model exploitation attack prevention
• Cloud, on-premises, and hybrid security
• AI governance and compliance
• Responsible AI implementation''',
                'topic_wise_content': '''Domain 1: Basic AI concepts related to cybersecurity - Core AI principles, Machine learning, Deep learning, Natural language processing, Automation, AI applications in security, AI-driven threats
Domain 2: Securing AI systems - Security controls for AI, AI deployment environment security, Adversarial risk mitigation, Data and model protection
Domain 3: AI-assisted security - Threat detection enhancement, Security workflow automation, AI in incident response, Continuous monitoring, Behavior analysis
Domain 4: AI governance, risk, and compliance - Regulatory frameworks (GDPR, NIST AI RMF), GRC integration, Responsible AI use, Ethical guidelines''',
                'prerequisites': '''• 3-4 years experience in IT
• 2+ years hands-on cybersecurity experience
• Security+, CySA+, PenTest+ or equivalent discipline
• Understanding of AI concepts helpful
• Familiarity with security operations preferred''',
                'skills_covered': 'AI Security Fundamentals, Machine Learning Security, Adversarial Attack Defense, Data Pipeline Security, Model Protection, AI-Assisted Detection, Security Automation, Threat Hunting with AI, Governance and Compliance, Risk Management',
                'tools_covered': 'AI Security platforms, SIEM with AI capabilities, Machine learning frameworks, Data governance tools, Compliance management systems, Threat detection tools, Automation platforms',
                'target_audience': '''• Cybersecurity Analysts & Engineers
• SOC Analysts & Incident Responders
• Security Architects & Consultants
• Risk, GRC, and Compliance Professionals
• Cloud Security Professionals
• Security Leaders responsible for AI adoption
• Professionals securing AI-enabled systems
• Advanced security professionals''',
                'duration': '3 Months',
                'level': 'Advanced',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 499,
                'original_price': 1199,
                'discount_percent': 58,
                'rating': 4.9,
                'reviews': 450,
                'learners': '550+',
                'modules': 12,
                'projects': 14,
                'emi_options': 'No Cost EMI starting @ $42/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 15th June 2026',
                'exam_code': 'SecAI+ (v1)',
                'exam_questions': 'Maximum 90 Questions',
                'exam_duration': '90 Minutes',
                'exam_format': 'Multiple Choice Questions',
                'exam_passing_score': '750 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA SecAI+ Certification - AI Security specialty credential',
                'course_objectives': '''• Explain core AI concepts and terminology relevant to cybersecurity
• Identify AI applications in threat detection and security
• Recognize AI-driven threats including adversarial and generative AI misuse
• Implement security controls for AI systems, data, and models
• Secure AI deployment across cloud, on-prem, and hybrid platforms
• Mitigate adversarial risks targeting AI pipelines
• Apply AI-assisted techniques for detection and response
• Automate security workflows using AI-enabled tools
• Integrate governance, risk, and compliance into AI initiatives
• Ensure responsible and ethical AI use
• Prepare for CompTIA SecAI+ certification exam''',
                'faq': '''Q: What makes SecAI+ unique?|A: It's the first CompTIA certification specifically addressing security of AI systems and AI-driven threats.
Q: Is this for beginners?|A: No, it's advanced-level requiring 3-4 years IT and 2+ years cybersecurity experience.
Q: What will I learn about AI?|A: Machine learning, deep learning, NLP, and automation from security perspective, not model development.
Q: How does AI help security?|A: AI enhances threat detection, automates workflows, improves incident response, and supports continuous monitoring.
Q: What about responsible AI?|A: The course covers ethical guidelines, legal standards, and frameworks like GDPR and NIST AI RMF.
Q: What jobs can I pursue?|A: Security roles focused on AI systems, AI governance, threat detection, and compliance.
Q: When should I take this?|A: After Security+ or CySA+ as next career advancement in emerging AI security field.
Q: Is this certification valuable?|A: Highly valuable as AI security is rapidly growing demand in cybersecurity industry.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1677442d019cecf8d9f53b3051d016f9?w=800'
            },

            # ============================================
            # 6. CompTIA PenTest+ Certification Training
            # ============================================
            {
                'title': 'CompTIA PenTest+ Certification Training',
                'slug': 'comptia-pentest-plus-certification-training',
                'description': 'A comprehensive penetration testing course covering vulnerability scanning, legal compliance, analysis, and reporting. PenTest+ is the only exam incorporating all aspects of vulnerability management.',
                'tagline': 'Professional Penetration Testing - Scanning, Exploitation & Reporting',
                'overview': '''CompTIA PenTest+ is one of the most comprehensive courses covering all PenTesting stages. PenTest+ is the only exam that incorporates all aspects of vulnerability management. This course includes the latest techniques used against expanded attack surfaces. You will learn to plan and scope a penetration testing engagement, perform pen-testing using correct techniques and tools, analyze outcomes, and understand compliance and legal requirements.''',
                'key_benefits': '''• Comprehensive penetration testing methodology
• Planning and scoping expertise
• Advanced reconnaissance techniques
• Multiple attack vector exploration
• Vulnerability scanning and assessment
• Legal and compliance understanding
• Professional reporting skills
• Post-exploitation techniques
• Coding and scripting proficiency
• Real-world scenario practice''',
                'topic_wise_content': '''Module 1: Planning and scoping - Governance and compliance, Organizational requirements, Ethical hacking mindset, Professionalism and integrity
Module 2: Information gathering and vulnerability scanning - Passive reconnaissance, Active reconnaissance, Reconnaissance analysis, Vulnerability scanning
Module 3: Attacks and Exploits - Network attacks, Wireless attacks, Application-based attacks, Cloud technology attacks, Specialized systems, Social engineering, Physical attacks, Post-exploitation techniques
Module 4: Reporting and Communication - Written report components, Findings analysis, Remediation recommendations, Communication during testing, Post-report activities
Module 5: Tools and Code Analysis - Scripting concepts, Script and code analysis, Tool usage during penetration testing phases''',
                'prerequisites': '''• Minimum 3-4 years experience in IT security or related field
• Network and security knowledge
• Understanding of networking concepts
• Basic system administration knowledge''',
                'skills_covered': 'Penetration Testing Methodology, Vulnerability Scanning, Reconnaissance, Network Attacks, Wireless Attacks, Application Security Testing, Cloud Security Testing, Social Engineering, Physical Security Testing, Post-Exploitation, Technical Writing, Python/Bash Scripting',
                'tools_covered': 'Nmap, Burp Suite, Metasploit, Wireshark, Nessus, OpenVAS, Hydra, SQLMap, Python, Ruby, Bash, PowerShell, Web proxies, Packet analyzers',
                'target_audience': '''• IT Security Analysts
• Penetration Testers
• Vulnerability Testers
• Network Security Operational staff
• Application Security Analysts
• Red Team Professionals
• Security Consultants
• Advanced security professionals''',
                'duration': '5 Months',
                'level': 'Advanced',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 499,
                'original_price': 1199,
                'discount_percent': 58,
                'rating': 4.8,
                'reviews': 720,
                'learners': '900+',
                'modules': 15,
                'projects': 20,
                'emi_options': 'No Cost EMI starting @ $42/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 8th June 2026',
                'exam_code': 'PT0-002',
                'exam_questions': 'Maximum 85 Questions',
                'exam_duration': '165 Minutes (2 hours 45 minutes)',
                'exam_format': 'Multiple Choice + Performance-Based Questions',
                'exam_passing_score': '750 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA PenTest+ Certification - Professional penetration testing credential',
                'course_objectives': '''• Knowledge on performing penetration testing and vulnerability scanning
• Analysing results and data to communicate through effective reporting
• Understanding importance of planning and compliance aspects
• Explore network, wireless, RF vulnerabilities and physical security attacks
• Perform post-exploitation techniques
• Understand penetration testing through coding scripts (Python, Ruby, Bash, PowerShell)
• Understand network vulnerability to attacks and mitigation strategies
• Knowledge on improving IT security across an organization
• Plan and scope penetration testing engagements professionally
• Analyze and remediate findings with appropriate recommendations''',
                'faq': '''Q: What is PenTest+ certification?|A: CompTIA PenTest+ validates skills to perform penetration testing including planning, vulnerability scanning, analysis, and professional reporting.
Q: Who should take PenTest+?|A: Security professionals with 3-4 years IT security experience seeking advanced penetration testing skills.
Q: What are prerequisites?|A: 3-4 years IT security experience, network and security knowledge, system administration basics.
Q: What tools will I learn?|A: Nmap, Burp Suite, Metasploit, Wireshark, Nessus, and various attack and analysis tools.
Q: What coding languages?|A: Python, Ruby, Bash, and PowerShell for information gathering and exploitation.
Q: What's the difference with CEH?|A: PenTest+ focuses on vulnerability management; CEH is broader hacking methodology. Both are valuable.
Q: What jobs can I get?|A: Penetration Tester, Red Team member, Security Consultant, Vulnerability Analyst, Security Engineer.
Q: Is this for beginners?|A: No, requires 3-4 years cybersecurity experience. Start with Security+ first.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800'
            },

            # ============================================
            # 7. CompTIA SecurityX Training
            # ============================================
            {
                'title': 'CompTIA SecurityX Certification Training',
                'slug': 'comptia-securityx-certification-training',
                'description': 'SecurityX is an advanced cybersecurity certification for security architects and senior security engineers. It proves you have the skills to design, build, and implement secure solutions across complex environments.',
                'tagline': 'Advanced Security Architecture - Enterprise Security Design & Governance',
                'overview': '''The CompTIA SecurityX Certification Training is an advanced cybersecurity program designed for experienced IT professionals validating expertise in enterprise security architecture, risk management, security engineering, incident response, and governance. SecurityX is the updated advanced-level certification from CompTIA, focused on hands-on technical security skills required to secure complex enterprise environments.''',
                'key_benefits': '''• Enterprise security architecture expertise
• Advanced security solution design
• Cloud security across multiple platforms
• Zero trust architecture implementation
• Risk and governance management
• Incident response leadership
• Security automation and orchestration
• Compliance framework integration
• Advanced threat management
• Enterprise infrastructure security''',
                'topic_wise_content': '''Module 1: Governance, risk, and compliance - Security documentation, Program management, Frameworks (COBIT, ITIL), Configuration management, GRC tools, Data governance, Risk management, Threat modeling, Attack surface analysis, Compliance strategies, Security frameworks (NIST, CSF)
Module 2: Security architecture - Cloud capabilities (CASB, CI/CD), Cloud data security, Control strategies, Network architecture, Security boundaries, Deperimeterization (SASE, SD-WAN), Zero trust concepts
Module 3: Security engineering - Automation, Vulnerability management, Advanced cryptography, Cryptographic use cases, Cryptographic techniques
Module 4: Security operations - Monitoring and data analysis, Vulnerabilities and attack surface, Threat hunting, Incident response, Malware analysis''',
                'prerequisites': '''• Basic understanding of networking and cybersecurity concepts
• Experience with operating systems, networking, security administration
• Knowledge equivalent to CompTIA Security+ or CySA+ certification
• 5+ years hands-on IT security experience recommended but not mandatory''',
                'skills_covered': 'Enterprise Security Architecture, Security Design Principles, Cloud Security, Zero Trust Models, Risk Management, Governance Frameworks, Incident Response Leadership, Vulnerability Management, Advanced Cryptography, Security Operations, Threat Hunting, SIEM Management, Automation and Orchestration',
                'tools_covered': 'Cloud security platforms, CASB solutions, SIEM tools, Security automation (SOAR), Vulnerability scanners, Forensic tools, Network monitoring, Threat intelligence platforms, Configuration management tools',
                'target_audience': '''• Security Architects
• Senior Security Engineers
• Cybersecurity Analysts
• SOC Analysts and Leaders
• Network Security Professionals
• Cloud Security Engineers
• Penetration Testing professionals
• Security Consultants
• System Administrators
• IT Managers in security operations
• Professionals moving to advanced roles''',
                'duration': '6 Months',
                'level': 'Expert',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 599,
                'original_price': 1499,
                'discount_percent': 60,
                'rating': 4.9,
                'reviews': 580,
                'learners': '700+',
                'modules': 18,
                'projects': 25,
                'emi_options': 'No Cost EMI starting @ $50/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 15th June 2026',
                'exam_code': 'SY0-701',
                'exam_questions': 'Maximum 90 Questions',
                'exam_duration': '90 Minutes',
                'exam_format': 'Multiple Choice + Performance-Based Scenarios',
                'exam_passing_score': '750 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA SecurityX Certification - Expert-level enterprise security architecture credential',
                'course_objectives': '''• Understand enterprise cybersecurity architecture and design
• Implement advanced security solutions for enterprise environments
• Manage risk, governance, and compliance frameworks
• Perform threat detection, analysis, and incident response
• Secure cloud, hybrid, and on-premises infrastructures
• Apply zero trust and defense-in-depth security models
• Implement identity and access management solutions
• Analyze vulnerabilities and recommend remediation
• Understand security automation and orchestration
• Prepare successfully for CompTIA SecurityX certification exam
• Design resilient enterprise security solutions
• Lead security program management initiatives''',
                'faq': '''Q: What is SecurityX certification?|A: CompTIA SecurityX is an expert-level certification for security architects validating enterprise security design and implementation skills.
Q: Who should take SecurityX?|A: Security architects, senior engineers, and experienced professionals with 5+ years security experience.
Q: What are prerequisites?|A: Security+ or CySA+ knowledge and 5+ years hands-on IT security experience recommended.
Q: How is SecurityX different from Security+?|A: Security+ is foundational; SecurityX is expert-level for architecture and design of enterprise security solutions.
Q: What will I design?|A: Enterprise architectures, cloud security solutions, zero trust models, incident response procedures, and governance frameworks.
Q: What about cloud security?|A: Comprehensive coverage of AWS, Azure, GCP security, hybrid cloud, multi-cloud, and cloud-native security.
Q: What jobs can I pursue?|A: Security Architect, Principal Security Engineer, Security Director, Consultant, Chief Information Security Officer (CISO) pathway.
Q: Is this the highest CompTIA security cert?|A: Yes, SecurityX is CompTIA's highest security certification for hands-on technical experts.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1516321497487-e288fb19713f?w=800'
            },

            # ============================================
            # 8. CompTIA Cloud+ Certification Training
            # ============================================
            {
                'title': 'CompTIA Cloud+ Certification Training',
                'slug': 'comptia-cloud-plus-certification-training',
                'description': 'Cloud+ solutions continue to dominate the technology market. The CompTIA Cloud+ certification validates the skills you need to maintain cloud infrastructure services and secure cloud environments.',
                'tagline': 'Cloud Infrastructure Management - Deployment, Security & Optimization',
                'overview': '''The CompTIA Cloud+ certification places an emphasis on incorporating and managing cloud technologies as part of a broader system of operations. It includes new technologies to support the changing cloud market as more organizations depend on cloud-based technologies to run mission-critical systems. It is the only vendor-neutral, performance-based certification, now compliant with ISO 17024 standards and approved by US DoD.''',
                'key_benefits': '''• Vendor-neutral cloud expertise
• Cloud infrastructure management
• Multi-cloud and hybrid cloud skills
• Cloud security best practices
• Cost optimization knowledge
• Container and orchestration expertise
• DevOps fundamentals
• Cloud compliance and governance
• DoD 8570.01-M approved
• ISO 17024 compliant certification''',
                'topic_wise_content': '''Module 1: Cloud architecture - Cloud models (public, private, hybrid, multi-cloud), Virtualization, Cloud networking, Containerization, Orchestration, Database fundamentals, Resource optimization, Billing management
Module 2: Deployment - System requirements, Infrastructure as Code (IaC), Workload migrations, Resource provisioning
Module 3: Operations - Lifecycle management, Backup and recovery, Observability and monitoring
Module 4: Security - Vulnerability management, Identity and access management, Container security, Compliance standards (PCI DSS, SOC 2, ISO 27001), Security controls
Module 5: DevOps fundamentals - Automation, Source control, CI/CD pipelines, System integration, DevOps tools (Kubernetes, Ansible, Jenkins), Event-driven architectures
Module 6: Troubleshooting - Deployment issues, Network connectivity, Security incidents, Service disruptions, Misconfigurations''',
                'prerequisites': '''• 2-3 years work experience in IT systems administration or networking
• CompTIA Network+ and Server+ or equivalent knowledge
• Familiarity with major hypervisor technology
• Knowledge of cloud service models
• IT service management knowledge
• Hands-on experience with at least one public or private cloud IaaS platform''',
                'skills_covered': 'Cloud Architecture Design, Virtualization, Cloud Networking, Containerization and Orchestration, IaaS/PaaS/SaaS Implementation, Cloud Security, Identity and Access Management, Cloud Compliance, DevOps Practices, Cost Optimization, Disaster Recovery, Cloud Troubleshooting',
                'tools_covered': 'AWS, Microsoft Azure, Google Cloud Platform, Docker, Kubernetes, Terraform, Ansible, Jenkins, Prometheus, CloudFormation, ARM templates, Helm',
                'target_audience': '''• System Administrators
• Systems Engineers
• Network Administrators
• Network Engineers
• Cloud Developers
• Cloud Specialists
• Cloud Engineers
• Project Managers (Cloud)
• Cloud Computing Business Analysts
• Data Center Managers
• Professionals transitioning to cloud roles''',
                'duration': '4 Months',
                'level': 'Intermediate',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 399,
                'original_price': 999,
                'discount_percent': 60,
                'rating': 4.7,
                'reviews': 850,
                'learners': '1100+',
                'modules': 14,
                'projects': 16,
                'emi_options': 'No Cost EMI starting @ $33/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 1st June 2026',
                'exam_code': 'CV0-003',
                'exam_questions': 'Maximum 90 Questions',
                'exam_duration': '90 Minutes',
                'exam_format': 'Multiple Choice + Scenario-Based Questions',
                'exam_passing_score': '750 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA Cloud+ Certification - Vendor-neutral cloud infrastructure credential',
                'course_objectives': '''• Understand cloud architecture and design
• Deploy cloud services and solutions
• Successfully maintain, secure, and optimize cloud environments
• Troubleshoot common cloud management issues
• Manage multi-cloud and hybrid cloud environments
• Implement infrastructure as code
• Perform cloud migrations
• Ensure cloud compliance and security
• Optimize cloud costs and resources
• Leverage DevOps practices in cloud environments
• Design disaster recovery and backup strategies''',
                'faq': '''Q: What is CompTIA Cloud+ certification?|A: Cloud+ validates skills to maintain cloud infrastructure, deploy services, and secure cloud environments across public, private, and hybrid clouds.
Q: Who should take Cloud+?|A: Cloud engineers, system administrators, network administrators, and IT professionals managing cloud infrastructure.
Q: What are prerequisites?|A: 2-3 years IT administration/networking experience, Network+ and Server+ knowledge, and hands-on cloud platform experience.
Q: Which cloud platforms?|A: Vendor-neutral, covers AWS, Azure, GCP concepts. Hands-on with at least one IaaS platform required.
Q: What about DevOps?|A: Module 5 covers DevOps fundamentals including CI/CD, automation, and container orchestration.
Q: Is this DoD approved?|A: Yes, approved by US DoD to meet directive 8570.01-M requirements and ISO 17024 compliant.
Q: What jobs can I pursue?|A: Cloud Engineer, Cloud Architect, Cloud Operations Manager, Cloud Security Engineer, DevOps Engineer.
Q: What tools will I learn?|A: Docker, Kubernetes, Terraform, Ansible, AWS, Azure, GCP, Jenkins, and automation tools.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800'
            },

            # ============================================
            # 9. CompTIA Data+ Certification Training
            # ============================================
            {
                'title': 'CompTIA Data+ Certification Training',
                'slug': 'comptia-data-plus-certification-training',
                'description': 'CompTIA Data+ is an early-career data analytics certification showing you have practical skills to turn raw data into meaningful insights for business decisions.',
                'tagline': 'Data Analytics & Business Intelligence - Transform Data Into Insights',
                'overview': '''The CompTIA Data+ certification is for professionals who are in charge of making data-driven decisions in their businesses. This equates to 18-24 months of practical experience working in business intelligence or data analyst capacity. CompTIA Data+ certification holders have knowledge and abilities to translate business requirements into data-driven decisions through data mining, manipulation, and statistical analysis.''',
                'key_benefits': '''• Data analytics fundamentals
• Business intelligence skills
• Data mining and manipulation
• Statistical analysis expertise
• Data visualization proficiency
• Governance and quality assurance
• Data lifecycle management
• Real-world business problem solving
• Enhanced decision-making
• Entry-level data career foundation''',
                'topic_wise_content': '''Module 1: Data concepts and environments - Data concepts, Data sources, Infrastructure concepts, Data tools, AI concepts in data
Module 2: Data acquisition and preparation - Data acquisition methods, Data exploration, Data transformation and cleansing
Module 3: Data analysis - Communicate analysis results, Statistical methods, Troubleshoot analysis issues
Module 4: Visualization and reporting - Create effective visuals, Deliver reports and dashboards, Validate reporting accuracy
Module 5: Data governance - Data management practices, Compliance requirements, Privacy and protection strategies, Quality assurance and testing''',
                'prerequisites': '''• 18-24 months experience as report or business analyst
• Exposure to databases and analytical tools
• Basic statistics understanding
• Experience with data visualization
• Business analysis background helpful''',
                'skills_covered': 'Data Analysis, Data Mining, Data Manipulation, Statistical Methods, Data Visualization, Business Intelligence, Database Management, Data Governance, Data Quality, Report Creation, Dashboard Development, Compliance and Privacy',
                'tools_covered': 'Tableau, Power BI, Excel, SQL, Python, R, Looker, Google Analytics, Alteryx, SPSS, Statistical software, BI platforms',
                'target_audience': '''• Aspiring Data Analysts
• Business Data Analysts
• Reporting Analysts
• Financial Analysts
• Marketing Specialists
• Human Resource Analysts
• Clinical Health Care Analysts
• Business Intelligence Professionals
• Junior Analytics Professionals
• Career changers into data field''',
                'duration': '3 Months',
                'level': 'Beginner',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 349,
                'original_price': 899,
                'discount_percent': 61,
                'rating': 4.6,
                'reviews': 720,
                'learners': '950+',
                'modules': 11,
                'projects': 12,
                'emi_options': 'No Cost EMI starting @ $29/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 1st June 2026',
                'exam_code': 'DA0-001',
                'exam_questions': 'Maximum 70 Questions',
                'exam_duration': '90 Minutes',
                'exam_format': 'Multiple Choice Questions',
                'exam_passing_score': '675 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA Data+ Certification - Data analytics foundation credential',
                'course_objectives': '''• Improve business judgments through data insights
• Assist in increasing organizational productivity
• Provide critical information to businesses
• Find and use data sources for competitive advantage
• Explain data concepts and identify data sources
• Recognize infrastructure and tools for data analysis
• Use data acquisition methods and perform exploration
• Apply data transformation and cleansing techniques
• Select and apply statistical methods
• Create effective data visualizations
• Deliver professional reports and dashboards
• Implement data governance and quality practices
• Ensure compliance and data privacy''',
                'faq': '''Q: What is CompTIA Data+ certification?|A: Data+ validates practical skills to analyze data, create insights, and support business decisions using data.
Q: Who should take Data+?|A: Data analysts, business analysts, reporting analysts, and professionals making data-driven decisions.
Q: What are prerequisites?|A: 18-24 months analytics/reporting experience, database tools knowledge, basic statistics, data visualization experience.
Q: Is this for beginners?|A: Yes, it's entry-level in data careers, though 18-24 months analytics experience required.
Q: What tools will I learn?|A: Data visualization (Tableau, Power BI), SQL databases, Excel, Python basics, BI platforms, and analytics software.
Q: What about statistics?|A: Basic statistical methods covered for data analysis, not advanced statistics.
Q: What jobs can I pursue?|A: Data Analyst, Business Analyst, Reporting Analyst, BI Developer, Data Scientist (entry-level).
Q: How is this different from programming certs?|A: Data+ focuses on analytics and insights; programming certs focus on coding skills.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800'
            },

            # ============================================
            # 10. CompTIA Linux+ Certification Training
            # ============================================
            {
                'title': 'CompTIA Linux+ Certification Training',
                'slug': 'comptia-linux-plus-certification-training',
                'description': 'The CompTIA Linux Plus training is designed to equip participants with essential knowledge to effectively configure, manage, operate, and troubleshoot Linux server environments with emphasis on security and automation.',
                'tagline': 'Linux System Administration - Server Management, Security & Automation',
                'overview': '''This CompTIA Linux Plus training provides a deep dive into Linux system administration, preparing you for the CompTIA Linux+ certification. The course covers fundamental system management and user services to advanced security, automation, and troubleshooting techniques. Whether aiming for certification or enhancing existing skillset, this program offers robust knowledge and practical experience for diverse IT environments.''',
                'key_benefits': '''• Linux system administration mastery
• Server management expertise
• Security best practices
• Automation and scripting proficiency
• Container and virtualization skills
• Performance optimization
• Troubleshooting methodology
• 12 months hands-on equivalent experience
• Cloud-ready Linux skills
• DevOps integration knowledge''',
                'topic_wise_content': '''Domain 1: System Management - Linux basics, Device management, Storage management, Network configuration, Shell operations, Backups and restores, Virtualization
Domain 2: Services and User Management - Files & directories, Account management, Process control, Software management, Systems management, Containers
Domain 3: Security - Authentication & accounting, Firewalls, OS hardening, Account security, Cryptography, Compliance
Domain 4: Automation, Orchestration, and Scripting - Automation (Ansible, Puppet), Shell scripting, Python basics, Version control (Git), AI best practices
Domain 5: Troubleshooting - System monitoring, Hardware/storage, Networking, Security, Performance optimization''',
                'prerequisites': '''• 12 months hands-on experience with Linux servers recommended
• CompTIA A+, Network+, or Server+ recommended
• Basic Linux command line knowledge
• Understanding of IT concepts
• System administration fundamentals''',
                'skills_covered': 'Linux Administration, Server Configuration, User and Group Management, Storage Management, Network Configuration, Firewall Configuration, Cryptography, Shell Scripting, Python Scripting, Container Management, Virtualization, Security Hardening, System Monitoring, Performance Tuning',
                'tools_covered': 'Linux distributions (Ubuntu, CentOS, Red Hat), Bash, Python, Git, Ansible, Puppet, Docker, Kubernetes, OpenSSL, FirewallD, systemd, LVM, RAID, SSH',
                'target_audience': '''• IT Professionals advancing Linux skills
• Individuals seeking Linux+ certification
• Aspiring Linux System Administrators
• Professionals with A+, Network+ or Server+ expanding into Linux
• DevOps engineers
• Cloud infrastructure professionals
• System administrators
• IT operations staff''',
                'duration': '5 Months',
                'level': 'Intermediate',
                'mode': 'Live Online + Self-Paced + Recorded Sessions + Lab Environment',
                'language': 'English',
                'price': 399,
                'original_price': 999,
                'discount_percent': 60,
                'rating': 4.7,
                'reviews': 680,
                'learners': '850+',
                'modules': 16,
                'projects': 18,
                'emi_options': 'No Cost EMI starting @ $33/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 8th June 2026',
                'exam_code': 'XK0-005',
                'exam_questions': 'Maximum 90 Questions',
                'exam_duration': '120 Minutes',
                'exam_format': 'Multiple Choice + Hands-On Lab Simulations',
                'exam_passing_score': '750 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA Linux+ Certification - Professional Linux administration credential',
                'course_objectives': '''• Configure and manage Linux systems, storage, networks, and services
• Apply security best practices including permissions and hardening
• Automate administration tasks with shell scripting and Python
• Deploy, maintain, and monitor containers and VMs
• Troubleshoot system, network, security, and application issues
• Implement firewalls and security configurations
• Manage user accounts, permissions, and access control
• Perform system backups and recovery
• Optimize system performance
• Work with version control systems (Git)
• Understand cloud and containerization concepts
• Manage software packages and repositories''',
                'faq': '''Q: What is CompTIA Linux+ certification?|A: Linux+ validates skills to configure, manage, and troubleshoot Linux servers in diverse IT environments.
Q: Who should take Linux+?|A: System administrators, DevOps engineers, cloud professionals, and anyone specializing in Linux.
Q: What are prerequisites?|A: 12 months Linux server experience recommended; A+/Network+/Server+ helpful.
Q: Which Linux distributions?|A: Vendor-neutral, covers concepts applicable to Ubuntu, CentOS, Red Hat, Debian, and others.
Q: Will I learn programming?|A: Bash and Python scripting for automation, not full programming development.
Q: What about cloud?|A: Includes containers (Docker, Kubernetes), virtualization, and cloud-native concepts.
Q: What jobs can I pursue?|A: Linux Administrator, DevOps Engineer, Cloud Engineer, System Engineer, Infrastructure Engineer.
Q: Is this hands-on?|A: Yes, includes practical labs and real server environment simulations.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800'
            },

            # ============================================
            # 11. CompTIA Project+ Certification Training
            # ============================================
            {
                'title': 'CompTIA Project+ Certification Training',
                'slug': 'comptia-project-plus-certification-training',
                'description': 'The CompTIA Project+ (v5) Certification Training is tailored for IT professionals managing small to medium-sized projects, offering practical project management skills backed by industry standards.',
                'tagline': 'Project Management for IT Professionals - Planning, Execution & Leadership',
                'overview': '''The CompTIA Project+ (v5) Certification Training is designed to equip IT professionals with foundational skills to manage projects efficiently in tech environments. Covering both traditional and agile methodologies, this course dives into core project management concepts, tools, life cycle phases, documentation practices, and IT governance. Whether new to project management or seeking certification validation, this course builds knowledge and confidence to lead IT projects successfully.''',
                'key_benefits': '''• Project management fundamentals
• Agile and Waterfall methodologies
• Resource and team management
• Risk and change management
• Stakeholder communication
• Project documentation skills
• Budget and cost management
• Schedule and timeline management
• Quality assurance practices
• Real-world project scenarios''',
                'topic_wise_content': '''Domain 1: Project Management Concepts - Characteristics and methodologies, Agile vs. Waterfall, Change control, Risk management, Issue management, Schedule management, Quality and performance management, Communication management, Meeting management, Team and resource management, Procurement and vendor selection
Domain 2: Project Life Cycle Phases - Discovery phase artifacts, Project initiation, Project planning, Project execution, Project closing
Domain 3: Tools and Documentation - Project tools (Gantt, burndown, PERT charts), Productivity tools, Quality and performance charts
Domain 4: Basics of IT and Governance - ESG concepts, Information security, Compliance and privacy, IT concepts, Change control''',
                'prerequisites': '''• 6-12 months hands-on experience managing projects in tech environment
• Basic understanding of IT projects
• Familiarity with project management concepts
• Technical background helpful but not required''',
                'skills_covered': 'Project Planning, Project Scheduling, Resource Management, Team Leadership, Stakeholder Communication, Risk Management, Budget Management, Quality Assurance, Documentation, Change Control, Agile Project Management, Waterfall Methodology, Project Governance, Compliance',
                'tools_covered': 'Microsoft Project, Asana, Jira, Monday.com, Trello, Gantt Charts, Burndown Charts, PERT Charts, Confluence, Slack, Zoom, Email, Project management software',
                'target_audience': '''• IT Support Professionals
• Junior Project Managers
• System Administrators
• Network Engineers
• Team Leads
• Aspiring Project Managers
• Technical Coordinators
• Business Analysts
• CompTIA Certification Holders
• Project Assistants in IT''',
                'duration': '3 Months',
                'level': 'Intermediate',
                'mode': 'Live Online + Self-Paced + Recorded Sessions',
                'language': 'English',
                'price': 349,
                'original_price': 899,
                'discount_percent': 61,
                'rating': 4.6,
                'reviews': 590,
                'learners': '720+',
                'modules': 13,
                'projects': 14,
                'emi_options': 'No Cost EMI starting @ $29/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 1st June 2026',
                'exam_code': 'PK0-005',
                'exam_questions': 'Maximum 80 Questions',
                'exam_duration': '90 Minutes',
                'exam_format': 'Multiple Choice + Scenario-Based Questions',
                'exam_passing_score': '710 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA Project+ Certification - IT project management credential',
                'course_objectives': '''• Gain foundation in project phases, methodologies (agile vs. waterfall), and scheduling
• Identify and navigate project risks, resource gaps, and scope changes
• Create project charters, stakeholder matrices, communication plans, and closure reports
• Utilize Gantt charts, burndown charts, dashboards, and time-management software
• Apply team management and communication techniques
• Apply ESG principles and information security to projects
• Track progress, manage conflicts, and ensure smooth closure
• Compare retrospectives, sprint reviews, and service-level agreements
• Understand procurement and vendor selection
• Document findings and project outcomes
• Lead and coordinate project teams effectively''',
                'faq': '''Q: What is CompTIA Project+ certification?|A: Project+ validates skills to manage IT projects efficiently using industry standards and best practices.
Q: Who should take Project+?|A: IT professionals managing small to medium projects, team leads, and aspiring project managers.
Q: What are prerequisites?|A: 6-12 months project management or technical coordination experience in IT environment.
Q: Does it cover Agile?|A: Yes, covers both traditional (Waterfall) and Agile methodologies with comparisons.
Q: What tools will I learn?|A: Microsoft Project, Jira, Asana, Gantt charts, Burndown charts, and project management platforms.
Q: Is this different from PMP?|A: Yes, Project+ is for IT professionals; PMP (PMBOK) is broader. Project+ is more accessible starting point.
Q: What jobs can I pursue?|A: Project Manager, Program Manager, IT Project Coordinator, Scrum Master, Agile Coach.
Q: Can I transition to PMP later?|A: Yes, Project+ is good foundation and can lead to PMP certification later.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=800'
            },

            # ============================================
            # 12. CompTIA Server+ Certification Training
            # ============================================
            {
                'title': 'CompTIA Server+ Certification Training',
                'slug': 'comptia-server-plus-certification-training',
                'description': 'This program is about mastering server technology through immersive expert-led experience. We offer curriculum aligned with CompTIA standards with focus on troubleshooting, security, and practical job-ready skills.',
                'tagline': 'Server Administration - Hardware, OS Configuration & Disaster Recovery',
                'overview': '''The CompTIA Server+ certification validates essential skills for IT professionals working with servers from traditional data centers to modern hybrid cloud setups. The program covers server operations including hardware installation, efficient administration, robust security measures, thorough disaster recovery planning, and effective troubleshooting. Earning CompTIA Server+ gives practical abilities to excel in server management and advance IT career in this vital expanding field.''',
                'key_benefits': '''• Server hardware installation expertise
• Operating system configuration skills
• Server administration and management
• High availability and clustering
• Storage and RAID management
• Virtualization and cloud integration
• Security hardening practices
• Disaster recovery planning
• Backup and recovery strategies
• Hands-on server troubleshooting''',
                'topic_wise_content': '''Domain 1: Server hardware installation and management - Physical hardware installation, Storage deployment (RAID), Hardware maintenance
Domain 2: Server administration - OS installation, Network services configuration, Server functions, High availability, Virtualization, Scripting basics, Asset management
Domain 3: Security and disaster recovery - Data security and encryption, Physical security, Identity and access management, Mitigation strategies, Server hardening, Decommissioning
Domain 4: Troubleshooting - Hardware troubleshooting, Software troubleshooting, Network troubleshooting, Disaster recovery, Backup validation''',
                'prerequisites': '''• CompTIA A+ certification recommended
• Equivalent foundational IT knowledge
• At least 2 years hands-on server environment experience
• Understanding of operating systems
• Basic networking knowledge
• Server administration fundamentals''',
                'skills_covered': 'Server Hardware Configuration, Operating System Installation, Network Services, Storage Management, RAID Configuration, Virtualization, High Availability, Security Hardening, Data Encryption, Disaster Recovery, Backup and Restore, Server Monitoring, Performance Optimization, Troubleshooting',
                'tools_covered': 'Windows Server, Linux, Hypervisors (Hyper-V, vSphere), Storage solutions, RAID controllers, Backup software, Monitoring tools, Virtualization platforms, Cloud services',
                'target_audience': '''• System Administrators
• Server Support Technicians
• Network Administrators
• Data Center Technicians
• IT Professionals specializing in servers
• Infrastructure Engineers
• IT Operations Staff
• Professionals validating server skills
• Career advancement seekers''',
                'duration': '5 Months',
                'level': 'Intermediate',
                'mode': 'Live Online + Self-Paced + Recorded Sessions + Lab Environment',
                'language': 'English',
                'price': 399,
                'original_price': 999,
                'discount_percent': 60,
                'rating': 4.7,
                'reviews': 620,
                'learners': '800+',
                'modules': 15,
                'projects': 17,
                'emi_options': 'No Cost EMI starting @ $33/month',
                'training_schedule': 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
                'start_date': 'Every Monday',
                'next_batch': 'Starting 8th June 2026',
                'exam_code': 'SK0-005',
                'exam_questions': 'Maximum 90 Questions',
                'exam_duration': '120 Minutes',
                'exam_format': 'Multiple Choice + Performance-Based Simulations',
                'exam_passing_score': '750 (on a scale of 100-900)',
                'exam_languages': 'English',
                'certification': 'CompTIA Server+ Certification - Professional server administration credential',
                'course_objectives': '''• Set up physical server hardware and carry out routine maintenance
• Administer server operating systems and manage network services
• Enable high availability and leverage virtualization technologies
• Implement server hardening and data security protocols
• Design disaster recovery and backup plans
• Identify and troubleshoot hardware, software, network, storage issues
• Utilize scripting for server automation
• Manage asset documentation and lifecycle
• Ensure compliance and security standards
• Optimize server performance
• Plan and execute server migrations
• Monitor and maintain server health''',
                'faq': '''Q: What is CompTIA Server+ certification?|A: Server+ validates skills to install, configure, manage, and troubleshoot servers in diverse environments.
Q: Who should take Server+?|A: System administrators, server technicians, infrastructure engineers, and IT professionals managing servers.
Q: What are prerequisites?|A: CompTIA A+ recommended, 2 years server experience, OS and networking knowledge.
Q: Does it cover cloud?|A: Yes, includes hybrid and cloud server concepts, virtualization, and cloud integration.
Q: What operating systems?|A: Covers Windows Server and Linux from vendor-neutral perspective.
Q: Will I learn scripting?|A: Yes, basics of scripting for automation, not advanced programming.
Q: What jobs can I pursue?|A: System Administrator, Server Administrator, Infrastructure Engineer, Data Center Technician.
Q: What's the difference with Linux+?|A: Server+ covers multiple OSes and server-specific roles; Linux+ focuses on Linux specialization.''',
                'category': 'Cyber Security',
                'is_published': True,
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800'
            },
        ]

        # Process each course
        for course_data in courses_data:
            slug = course_data['slug']
            existing = Course.query.filter_by(slug=slug).first()
            
            if existing:
                print(f"\n✅ Updating: {course_data['title']}")
                # Update all fields
                for key, value in course_data.items():
                    if hasattr(existing, key):
                        setattr(existing, key, value)
                print(f"   ✓ Updated successfully!")
            else:
                print(f"\n✨ Creating: {course_data['title']}")
                course = Course(**course_data)
                db.session.add(course)
                print(f"   ✓ Created successfully!")
        
        # Commit all changes
        db.session.commit()
        
        print("\n" + "="*70)
        print("🎉 ALL COMPTIA COURSES UPDATED/CREATED SUCCESSFULLY! 🎉")
        print("="*70)
        
        # Print summary
        total_courses = Course.query.filter(
            Course.slug.ilike('%comptia%')
        ).count()
        
        print(f"\n📊 Summary:")
        print(f"   Total CompTIA Courses in Database: {total_courses}")
        print(f"   All courses published and ready!")
        
if __name__ == "__main__":
    add_or_update_comptia_courses()