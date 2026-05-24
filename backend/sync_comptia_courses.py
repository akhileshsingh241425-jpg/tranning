import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))

from app import app, db, Course

courses = [
  {
    "slug": "comptia-a-plus",
    "title": "CompTIA A+ Certification Training",
    "tagline": "Start your IT career with CompTIA A+ certification",
    "description": "Our CompTIA A+ training program is designed to equip participants with the essential skills and knowledge needed to excel in entry-level IT roles. The program covers a comprehensive curriculum that includes hardware and software troubleshooting, operating systems, networking, and security.",
    "overview": "The CompTIA A+ certification training course is created for all entry-level and aspiring IT professionals to validate their skills and knowledge in the IT domain. The certification course is made for learners to properly understand the hardware and software technologies that they will be working with so that they can support various IT infrastructures. Organizations often look for this certification as a marker and validation of the prospective employee's skills. The certification has two examinations that candidates need to clear to become certified CompTIA A+ professionals.",
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
    "certification": "Yes, Certificate of Completion with unique ID. Prepares you for CompTIA A+ (220-1101 & 220-1102) exams.",
    "key_benefits": "Prepare and pass the CompTIA A+ certification exams\nInstall and configure PC systems and peripheral devices\nTroubleshoot internal system components\nUnderstand network infrastructure concepts\nLearn laptop and mobile device support\nMaster printer setup and troubleshooting\nUnderstand virtualization and cloud computing\nLearn security best practices for devices and networks",
    "why_join": "Industry-Recognized Certification|CompTIA A+ is the gold standard for IT careers\nHands-on Labs|Practice with real hardware and software simulations\nExpert Instructors|Learn from certified professionals with years of experience\nCareer Support|Resume building and interview preparation included",
    "benefits": "Live Instructor-Led Sessions\nHands-on Labs\nExam Preparation\nCertificate of Completion\n24/7 Support\nLifetime Access",
    "course_objective": "[\"Prepare and pass the CompTIA A+ certification exams\",\"Install and configure the components of the PC system and peripheral devices\",\"Install, configure, and troubleshoot internal system components\",\"Understand how to identify, use, and connect hardware components and devices\",\"Understand the concepts of network infrastructure\",\"Understand how to set up network connections and troubleshoot them\",\"Learn laptop support and troubleshooting\",\"Understand how to troubleshoot and support mobile devices\",\"Learn to configure and troubleshoot printing devices\",\"Implement client virtualization and cloud computing\",\"Identify and defend devices against security risks\"]",
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
      {"question": "Is the CompTIA A+ certification a suitable place to start?", "answer": "The CompTIA A+ certification might help you get entry-level IT roles such as Desktop Support, Data Support Technician, Desktop Support Administrator, or Help Desk Tech. The new CompTIA A+ certification is a wonderful place to begin. It will provide you with the core information you will need for bigger and better careers in the future."},
      {"question": "What jobs can you obtain with CompTIA A+?", "answer": "The CompTIA A+ certification is generally recognized as an industry-standard credential frequently used to jumpstart a career in IT. Such as: Service Desk Analyst, Help Desk Tech, Desktop Support Administrator, Technical Support Specialist, End-User Computing Technician, Field Service Technician, Help Desk Technician, Associate Network Engineer, System Support Specialist, Data Support Technician."},
      {"question": "What does the CompTIA A+ certification cost?", "answer": "The CompTIA A+ certification costs $232 USD per exam."},
      {"question": "How to Pass the CompTIA A+ Exam?", "answer": "You can prepare for the CompTIA A+ exam in a variety of methods: CompTIA A+ study guide, Self-study using various online resources such as videos and books, Instructor-led CompTIA A+ certification training, CompTIA A+ practice test."},
      {"question": "Is CompTIA A+ a difficult exam to master?", "answer": "The CompTIA A+ is a professional industry certification on par with any other entry-level professional license exam in terms of difficulty. However, with the proper preparation and strategy, you can pass the two CompTIA A+ certification exams."},
      {"question": "What is the next step after I have earned my CompTIA A+ certification?", "answer": "The CompTIA A+ is the first of several certifications earned by many IT professionals throughout their careers. Because the CompTIA A+ is a general IT credential, you might want to pursue an IT specialty, such as networking, cybersecurity, or cloud computing."},
      {"question": "Is CompTIA A+ required for Network+?", "answer": "Obtaining a CompTIA A+ certification is not a prerequisite for obtaining a Network+ certification."},
      {"question": "How much can I earn with CompTIA A+ certification?", "answer": "According to Glassdoor: Associate Network Engineer: $67,162, Desktop Support Administrator: $50,903, Service Desk Analyst: $43,679, Help Desk Tech: $40,424."}
    ])
  },
  {
    "slug": "comptia-network-plus",
    "title": "CompTIA Network+ Certification Training",
    "tagline": "Master networking concepts and earn your Network+ certification",
    "description": "The Network+ certification exam training provided by TrainingProtec is an entry-level training for IT professionals that helps them acquire the necessary skills to manage, maintain, troubleshoot, install, and configure basic computer networks.",
    "overview": "The CompTIA Network+ certification validates your knowledge and skills of installing, managing, and troubleshooting networks on various platforms. This course is composed to help you learn all the required objectives to gain the CompTIA Network+ certification. You will learn the latest networking technologies available, various networks and networking protocols, identify VPN and VLAN features, DNS concepts, and implement wireless networks.",
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
    "course_objective": "[\"Explain the purpose and uses of ports and protocols\",\"Explain devices, applications protocols, and services on their appropriate OSI layers\",\"Explain the characteristics and concepts of routing and switching\",\"Configure the appropriate IP address\",\"Understand network topologies types and technologies\",\"Implement the appropriate wireless technologies and configurations\",\"Explain the use cases for advanced networking devices\",\"Explain various types of networking attacks\",\"Learn how to identify and defend devices and their network connections against security risks\"]",
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
      {"question": "What is the importance of CompTIA Network+ certification?", "answer": "CompTIA Network+ validates your knowledge and skills required to troubleshoot, configure and manage wired and wireless networks found in corporations around the world."},
      {"question": "What other courses are recommended before and after CompTIA Network+?", "answer": "CompTIA A+ is recommended before, and CCNA, CEHv11 is recommended after the CompTIA Network+."},
      {"question": "Can you take the Network+ exam without taking CompTIA A+ certification?", "answer": "CompTIA recommends you to take A+ certification before sitting for the Network+ exam. However, if you have a basic understanding of IT, you can directly go for CompTIA Network+ certification."},
      {"question": "What is CompTIA Network+ retake policy?", "answer": "If you fail in your first attempt, you do not need to wait for a second attempt. Before your third attempt, you need to wait at least fourteen days."},
      {"question": "What job can I get with CompTIA Network+ certification?", "answer": "IT consultant, Computer technician, Help desk technician, System engineer, Network support specialist, Network analyst."},
      {"question": "What is the validity of this CompTIA Network+ certificate?", "answer": "CompTIA Network+ certification is valid for three years from the day you pass your exam."}
    ])
  },
  {
    "slug": "comptia-security-plus",
    "title": "CompTIA Security+ Certification Training",
    "tagline": "Master cybersecurity fundamentals and earn your Security+ certification",
    "description": "Our CompTIA Security+ training is designed to provide you with a comprehensive understanding of the principles and best practices required to secure networks, systems, and data.",
    "overview": "CompTIA Security+ Training covers many areas of network security, including cloud security, encryption, security protocols, system security and network infrastructure. Our training is ideal for network administrators, security consultants, security engineers, security analysts and people looking to enter into cyber security. In this training course, you gain the foundational knowledge needed to pass the Security+ certification exam.",
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
    "course_objective": "[\"Develop a comprehensive understanding of foundational security concepts and principles\",\"Learn to identify, assess, and mitigate various threats, vulnerabilities, and risks\",\"Master the principles and practices of designing a robust security architecture\",\"Gain expertise in day-to-day security operations including incident response and monitoring\",\"Acquire the knowledge and skills required to oversee and manage a security program\",\"Understand compliance, governance, and the protection of valuable data\"]",
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
      {"question": "What is the importance of CompTIA Security+ certification?", "answer": "CompTIA Security+ is the most widely adopted ISO/ANSI accredited cybersecurity certification, validating foundational cybersecurity skills."},
      {"question": "What jobs can I get with Security+ certification?", "answer": "Network Administrator, Security Administrator, Security Analyst, Security Engineer, Cybersecurity Specialist."},
      {"question": "Is Security+ harder than Network+?", "answer": "Security+ builds on networking concepts but is considered more conceptual. Both are foundational certifications."}
    ])
  }
]

print(f"Total courses to sync: {len(courses)}")

import sys
sys.stdout.reconfigure(encoding='utf-8')

with app.app_context():
    for data in courses:
        slug = data["slug"]
        course = Course.query.filter_by(slug=slug).first()
        if not course:
            course = Course(slug=slug)
            db.session.add(course)
            print(f"Creating new course: {data['title']}")
        else:
            print(f"Updating existing course: {data['title']}")
        
        course.title = data.get("title", course.title or "")
        course.tagline = data.get("tagline", course.tagline or "")
        course.description = data.get("description", course.description or "")
        course.overview = data.get("overview", course.overview or "")
        course.image = data.get("image", course.image or "")
        course.icon = data.get("icon", course.icon or "FaBookOpen")
        course.price = data.get("price", course.price or 0)
        course.original_price = data.get("original_price", course.original_price or 0)
        course.rating = data.get("rating", course.rating or 4.5)
        course.reviews = data.get("reviews", course.reviews or 0)
        course.learners = data.get("learners", course.learners or "0")
        course.duration = data.get("duration", course.duration or "")
        course.level = data.get("level", course.level or "Beginner")
        course.tag = data.get("tag", course.tag or "")
        course.modules = data.get("modules", course.modules or 0)
        course.projects = data.get("projects", course.projects or 0)
        course.instructor_name = data.get("instructor_name", course.instructor_name or "")
        course.instructor_role = data.get("instructor_role", course.instructor_role or "")
        course.instructor_experience = data.get("instructor_experience", course.instructor_experience or "")
        course.curriculum = data.get("curriculum", course.curriculum or "")
        course.is_published = data.get("is_published", course.is_published if course.is_published is not None else True)
        course.sort_order = data.get("sort_order", course.sort_order or 0)
        course.mode = data.get("mode", course.mode or "")
        course.language = data.get("language", course.language or "English")
        course.target_audience = data.get("target_audience", course.target_audience or "")
        course.eligibility = data.get("eligibility", course.eligibility or "")
        course.training_schedule = data.get("training_schedule", course.training_schedule or "")
        course.start_date = data.get("start_date", course.start_date or "")
        course.next_batch = data.get("next_batch", course.next_batch or "")
        course.exam_code = data.get("exam_code", course.exam_code or "")
        course.tools_covered = data.get("tools_covered", course.tools_covered or "")
        course.skills_covered = data.get("skills_covered", course.skills_covered or "")
        course.certification = data.get("certification", course.certification or "")
        course.key_benefits = "\n".join(data.get("key_benefits", "").split("\n"))
        course.why_join = "\n".join(data.get("why_join", "").split("\n"))
        course.benefits = "\n".join(data.get("benefits", "").split("\n"))
        course.course_objectives = data.get("course_objective", course.course_objectives or "")
        course.prerequisites = data.get("prerequisites", course.prerequisites or "")
        course.category = data.get("category", course.category or "")
        course.topic_wise_content = data.get("topic_wise_content", "")
        course.faq = data.get("faq", "")
        course.technologies_list = data.get("technologies_list", "")
        course.detail_stats = data.get("detail_stats", "")
        course.projects_list = data.get("projects_list", "")
        course.reviews_list = data.get("reviews_list", "")
        course.learning_path = data.get("learning_path", "")
        course.modules_detail = data.get("modules_detail", "")
        course.advisor = data.get("advisor", "")
        course.vendors = data.get("vendors", "")
        course.emi_options = data.get("emi_options", "")
        course.discount_percent = data.get("discount_percent", 0)
        course.hero_image = data.get("hero_image", "")
        course.instructor_image = data.get("instructor_image", "")
        
        try:
            db.session.commit()
            print(f"  [OK] Synced: {course.title}")
        except Exception as e:
            db.session.rollback()
            print(f"  [ERR] Error syncing {slug}: {e}")

print("\nDone! All courses synced.")
