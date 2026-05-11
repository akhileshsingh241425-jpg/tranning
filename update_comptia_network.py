#!/usr/bin/env python3
"""
CompTIA Network+ Course Database Update Script
==============================================
This script updates the CompTIA Network+ course with comprehensive data including:
- Course details and metadata
- Full curriculum with 10 modules
- Detailed topic-wise content distribution
- Industry projects
- Career benefits
- Course advisors
- Student reviews
- Why join points
- FAQ section

Run with: source venv/bin/activate && python3 update_comptia_network.py
"""

import sys
sys.path.insert(0, '/var/www/tranning/backend')

from app import app, db
from models import Course
import json

def update_comptia_network_course():
    """Update CompTIA Network+ course with complete details"""
    
    with app.app_context():
        course = Course.query.filter_by(slug='comptia-network-course').first()
        
        if not course:
            print("ERROR: Course with slug 'comptia-network-course' not found!")
            print("Available courses:")
            all_courses = Course.query.all()
            for c in all_courses:
                print(f"  - {c.id}: {c.title} (slug: {c.slug})")
            return False
        
        print(f"Found course: {course.title} (ID: {course.id})")
        
        # =========================================================================
        # 1. BASIC COURSE INFORMATION
        # =========================================================================
        course.title = "CompTIA Network+ Course"
        course.description = """Prepare for the latest CompTIA Network+ N10-009 certification exam with industry-focused training designed to build strong networking fundamentals and hands-on practical skills. This course covers modern networking concepts, network implementation, troubleshooting, security, cloud technologies, virtualization, and enterprise networking solutions required for today's IT infrastructure environments.

The CompTIA Network+ certification is globally recognized and validates the technical skills needed to design, configure, manage, and troubleshoot wired and wireless networks in enterprise environments. The updated N10-009 exam focuses on modern networking technologies including SD-WAN, cloud networking, network security, virtualization, and advanced troubleshooting methodologies."""
        
        course.tagline = "Master Modern Networking Skills & Get Certified with CompTIA Network+ N10-009"
        
        # Pricing
        course.sale_price = 800
        course.original_price = 1200
        
        # Course stats
        course.duration = "40 Hours"
        course.level = "Beginner to Intermediate"
        course.modules_count = 10
        course.projects_count = 4
        course.tag = "Popular"
        
        # Detail page stats
        course.stats = json.dumps([
            {"value": "8000+", "label": "Learners Trained", "icon": "FaUsers"},
            {"value": "4.8/5", "label": "Average Rating", "icon": "FaStar"},
            {"value": "40+ Hours", "label": "Instructor-Led Training", "icon": "FaClock"},
            {"value": "20+ Hours", "label": "Hands-On Practical Labs", "icon": "FaLaptopCode"}
        ])
        
        # Instructor
        course.instructor_name = "Mr. Rajesh Kumar"
        course.instructor_experience = "15+ years"
        course.instructor_role = "Ex-Network Engineer at Cisco | CCIE Certified"
        course.instructor_bio = "Rajesh Kumar is a seasoned network professional with over 15 years of experience in enterprise networking. He holds CCIE Security and CCIE Routing & Switching certifications and has trained thousands of students for CompTIA certifications."
        
        # =========================================================================
        # 2. OVERVIEW / KEY BENEFITS
        # =========================================================================
        course.overview = """The CompTIA Network+ training program is ideal for IT professionals looking to start or advance their career in networking and infrastructure management. The course provides a combination of theoretical concepts, real-world scenarios, hands-on labs, and exam-oriented preparation to help candidates gain practical networking expertise."""
        
        course.key_benefits = json.dumps([
            "Understand networking concepts and architectures",
            "Configure and troubleshoot wired and wireless networks",
            "Implement network security best practices",
            "Manage IP addressing and subnetting",
            "Work with routing and switching technologies",
            "Configure VLANs, VPNs, and network services",
            "Understand cloud and virtualization concepts",
            "Monitor and troubleshoot network performance",
            "Prepare for the CompTIA Network+ N10-009 certification exam"
        ])
        
        # =========================================================================
        # 3. FULL CURRICULUM - 10 MODULES
        # =========================================================================
        course.curriculum = json.dumps([
            {
                "heading": "Module 1: Networking Fundamentals",
                "description": "Introduction to networking",
                "items": [
                    {"title": "Introduction to Networking", "subtopics": ["What is Networking", "Need for Networks", "Network Types", "Communication Models"]},
                    {"title": "OSI Model and TCP/IP Model", "subtopics": ["7 Layers of OSI", "TCP/IP Model", "Encapsulation/Decapsulation", "Protocol Data Units"]},
                    {"title": "Types of Networks", "subtopics": ["LAN (Local Area Network)", "WAN (Wide Area Network)", "MAN (Metropolitan Area Network)", "PAN (Personal Area Network)", "VPN (Virtual Private Network)"]},
                    {"title": "Network Topologies", "subtopics": ["Bus Topology", "Star Topology", "Ring Topology", "Mesh Topology", "Hybrid Topology"]},
                    {"title": "Ethernet Standards", "subtopics": ["10BASE-T", "100BASE-TX", "1000BASE-T", "10GBASE-T", "PoE (Power over Ethernet)"]},
                    {"title": "Ports and Protocols", "subtopics": ["Well-known Ports", "Registered Ports", "Dynamic Ports", "Common Protocols", "Port Number Ranges"]},
                    {"title": "MAC Addressing", "subtopics": ["MAC Address Structure", "unicast/multicast/broadcast", "ARP (Address Resolution Protocol)", "MAC Table", "Switching Logic"]},
                    {"title": "IPv4 Addressing", "subtopics": ["IP Address Classes", "Private vs Public IPs", "Subnet Masks", "Default Gateway", "Broadcast Address"]},
                    {"title": "IPv6 Addressing", "subtopics": ["IPv6 Address Types", "IPv6 Header", "IPv4 vs IPv6", "Dual Stack", "Tunneling"]},
                    {"title": "Subnetting Concepts", "subtopics": ["CIDR Notation", "Subnet Masks", "Network ID", "Host ID", "Supernetting"]}
                ]
            },
            {
                "heading": "Module 2: Network Devices and Infrastructure",
                "description": "Routers, switches, and network appliances",
                "items": [
                    {"title": "Routers and Routing", "subtopics": ["Router Functions", "Routing Tables", "Static Routes", "Default Routes", "Routing Decision Process"]},
                    {"title": "Switches and Switching", "subtopics": ["Layer 2 Switching", "Switching Methods", "MAC Address Learning", "VLAN Trunking", "Switch Port Security"]},
                    {"title": "Firewalls and Security Appliances", "subtopics": ["Firewall Types", "Stateful Inspection", "ACLs (Access Control Lists)", "DMZ (Demilitarized Zone)", "IDS/IPS"]},
                    {"title": "Wireless Access Points", "subtopics": ["AP Modes (Infrastructure/Ad-hoc)", "SSID Configuration", "Channel Selection", "AP Management", "Controller-based vs Autonomous"]},
                    {"title": "Load Balancers", "subtopics": ["Load Balancing Methods", "Health Checks", "SSL Offloading", "Global Server Load Balancing", "High Availability"]},
                    {"title": "Proxy Servers", "subtopics": ["Forward Proxy", "Reverse Proxy", "Content Filtering", "Caching", "Authentication"]},
                    {"title": "Network Appliances", "subtopics": ["UTM (Unified Threat Management)", "VPN Concentrators", "WAN Accelerators", "Content Filters", "Network Tap/Mirror"]},
                    {"title": "Network Cabling and Connectors", "subtopics": ["Copper Cabling (Cat5e, Cat6, Cat6a)", "Fiber Optic Cabling", "LC/SC/FC Connectors", "Cable Testing", "Crossover vs Straight-through"]},
                    {"title": "Fiber Optics and Transmission", "subtopics": ["Single Mode Fiber", "Multi Mode Fiber", "WDM (Wavelength Division Multiplexing)", "Fiber Loss Calculations", "OTDR Testing"]},
                    {"title": "Network Interface Cards", "subtopics": ["NIC Types", "Speed/Duplex Settings", "Driver Installation", "Teaming/Bonding", "Virtual NICs"]}
                ]
            },
            {
                "heading": "Module 3: Routing and Switching",
                "description": "Advanced routing and switching technologies",
                "items": [
                    {"title": "Static and Dynamic Routing", "subtopics": ["Static Route Configuration", "Default Route", "Dynamic Routing Overview", "Routing vs Switching", "Route Summarization"]},
                    {"title": "Routing Protocols", "subtopics": ["RIP (Routing Information Protocol)", "OSPF (Open Shortest Path First)", "EIGRP (Enhanced Interior Gateway Routing Protocol)", "BGP (Border Gateway Protocol)", "Route Selection Criteria"]},
                    {"title": "VLAN Configuration", "subtopics": ["VLAN Creation", "VLAN Trunking (802.1Q)", "Native VLAN", "VLAN Tagging", "Voice VLAN"]},
                    {"title": "Inter-VLAN Routing", "subtopics": ["Router on a Stick", "Layer 3 Switch", "SVI (Switch Virtual Interface)", "VLAN Routing Configuration", "DHCP Relay"]},
                    {"title": "Spanning Tree Protocol", "subtopics": ["STP Basics", "Root Bridge Selection", "Port States (Blocking/Forwarding)", "PortFast and BPDU Guard", "RSTP and MSTP"]},
                    {"title": "Link Aggregation", "subtopics": ["LACP (Link Aggregation Control Protocol)", "PAgP (Port Aggregation Protocol)", "EtherChannel", "Load Balancing", "Failover"]},
                    {"title": "NAT and PAT", "subtopics": ["Static NAT", "Dynamic NAT", "PAT (Port Address Translation)", "NAT Types", "NAT Traversal"]},
                    {"title": "DHCP and DNS", "subtopics": ["DHCP Server Configuration", "DHCP Relay/Helper", "IP Pools", "DNS Server Types", "Zone Transfers"]},
                    {"title": "Quality of Service (QoS)", "subtopics": ["QoS Models", "Traffic Classification", "Policing and Shaping", "DSCP and CoS", "QoS Implementation"]},
                    {"title": "Network Device Management", "subtopics": ["Console Access", "SSH/Telnet", "SNMP", "Syslog", "Network Time Protocol (NTP)"]}
                ]
            },
            {
                "heading": "Module 4: Wireless Networking",
                "description": "WiFi technologies and wireless network management",
                "items": [
                    {"title": "Wireless Standards and Technologies", "subtopics": ["IEEE 802.11 Standards (a/b/g/n/ac/ax)", "Frequency Bands (2.4GHz vs 5GHz)", "Channel Bonding", "MIMO and MU-MIMO", "Throughput vs Range"]},
                    {"title": "WiFi Configuration and Planning", "subtopics": ["SSID and BSSID", "Beacon Frames", "Channel Selection", "Transmit Power", "Antenna Types"]},
                    {"title": "Wireless Security Protocols", "subtopics": ["WEP (Wired Equivalent Privacy)", "WPA (Wi-Fi Protected Access)", "WPA2 (AES/CCMP)", "WPA3 (SAE)", "Enterprise Authentication (802.1X)"]},
                    {"title": "Wireless Authentication Methods", "subtopics": ["Open System", "Pre-Shared Key (PSK)", "EAP Methods", "RADIUS Server", "Captive Portal"]},
                    {"title": "Wireless Network Types", "subtopics": ["Infrastructure Mode", "Ad-hoc Mode", "Mesh Networks", "Hotspot Networks", "Bridging (WDS)"]},
                    {"title": "Site Surveys and Planning", "subtopics": ["RF Site Survey Tools", "Heat Map Generation", "AP Placement", "Coverage Analysis", "Capacity Planning"]},
                    {"title": "Wireless Troubleshooting", "subtopics": ["Signal Strength Issues", "Interference Sources", "Roaming Problems", "Authentication Failures", "Speed/Performance Issues"]},
                    {"title": "Wireless Performance Optimization", "subtopics": ["Channel Optimization", "Load Balancing", "Band Steering", "Airtime Fairness", "Client Isolation"]},
                    {"title": "Guest Networks and Isolation", "subtopics": ["Guest SSID Configuration", "VLAN Isolation", "Captive Portal Setup", "Rate Limiting", "Access Policies"]},
                    {"title": "Wireless Mesh and Controller", "subtopics": ["Mesh Network Architecture", "Controller-based WiFi", "CAPWAP Protocol", "Zero-touch Provisioning", "RF Planning Tools"]}
                ]
            },
            {
                "heading": "Module 5: Network Security",
                "description": "Network security fundamentals and implementation",
                "items": [
                    {"title": "Network Security Fundamentals", "subtopics": ["Security Goals (CIA Triad)", "Threat Landscape", "Vulnerability Assessment", "Risk Management", "Security Policies"]},
                    {"title": "Zero Trust Architecture", "subtopics": ["Zero Trust Principles", "Micro-segmentation", "Identity-based Access", "Least Privilege", "Continuous Verification"]},
                    {"title": "Authentication and Authorization", "subtopics": ["AAA (Authentication, Authorization, Accounting)", "RADIUS Protocol", "TACACS+ Protocol", "LDAP Integration", "Multi-factor Authentication"]},
                    {"title": "VPN Technologies", "subtopics": ["Site-to-Site VPN", "Remote Access VPN", "SSL VPN", "IPsec Protocol Suite", "VPN Tunnel Modes"]},
                    {"title": "Access Control Methods", "subtopics": ["Role-based Access Control (RBAC)", "Attribute-based Access Control (ABAC)", "Network Access Control (NAC)", "Port-based Network Access Control (PNAC)", "802.1X"]},
                    {"title": "Firewall Implementation", "subtopics": ["Firewall Rule Configuration", "Zone-based Firewalls", "Application Filtering", "Content Inspection", "Zone-policy Configuration"]},
                    {"title": "Network Hardening", "subtopics": ["Disable Unused Services", "Port Security", "Switch Port Hardening", "BPDU Guard/Root Guard", "DHCP Snooping"]},
                    {"title": "Network Threats and Attack Types", "subtopics": ["DoS/DDoS Attacks", "Man-in-the-Middle", "ARP Spoofing", "DNS Spoofing", "Port Scanning"]},
                    {"title": "Intrusion Detection and Prevention", "subtopics": ["IDS vs IPS", "Signature-based Detection", "Anomaly-based Detection", "Snort Rules", "SIEM Integration"]},
                    {"title": "Security Monitoring and Logging", "subtopics": ["Log Types and Levels", "Syslog Configuration", "Security Information and Event Management (SIEM)", "Correlation Rules", "Alerting and Escalation"]}
                ]
            },
            {
                "heading": "Module 6: Cloud and Virtualization",
                "description": "Modern cloud and virtualization technologies",
                "items": [
                    {"title": "Cloud Computing Concepts", "subtopics": ["Cloud Service Models (IaaS, PaaS, SaaS)", "Deployment Models (Public, Private, Hybrid)", "Cloud Providers Overview", "Cloud Billing Models", "Cloud Migration Strategies"]},
                    {"title": "Virtualization Technologies", "subtopics": ["Hypervisor Types (Type 1 vs Type 2)", "Virtual Machines", "Virtual Networking", "Virtual Storage", "Virtual Machine Lifecycle"]},
                    {"title": "Software-Defined Networking (SDN)", "subtopics": ["SDN Architecture", "Control Plane vs Data Plane", "OpenFlow Protocol", "SDN Controllers (OpenDaylight, ONOS)", "Network Function Virtualization (NFV)"]},
                    {"title": "Software-Defined Wide Area Network (SD-WAN)", "subtopics": ["SD-WAN Architecture", "WAN Edge Devices", "Application-based Routing", "Zero-trust WAN", "SD-WAN Providers"]},
                    {"title": "Network Virtualization", "subtopics": ["VXLAN (Virtual Extensible LAN)", "NVGRE (Network Virtualization using GRE)", "VRF (Virtual Routing and Forwarding)", "VLAN vs VXLAN", "Virtual Network Overlay"]},
                    {"title": "High Availability Concepts", "subtopics": ["HA Cluster Configuration", "Load Balancing Algorithms", "Failover Mechanisms", "Active-Active vs Active-Passive", "Heartbeat and Health Checks"]},
                    {"title": "Container Networking", "subtopics": ["Docker Networking", "Kubernetes Networking", "Pod-to-Pod Communication", "Service Discovery", "Ingress Controllers"]},
                    {"title": "Infrastructure as Code", "subtopics": ["Ansible for Network Automation", "Terraform Basics", "Configuration Management", "Network Device Templates", "Version Control for Network Config"]},
                    {"title": "Network Automation Tools", "subtopics": ["REST APIs for Network Devices", "NETCONF/YANG", "gNMI (gRPC Network Management Interface)", "Python for Network Automation", "CI/CD for Network"]},
                    {"title": "Hybrid Cloud Networking", "subtopics": ["Cloud Connectivity Options", "Direct Connect/ExpressRoute", "VPN over Internet", "Cloud DNS", "CDN (Content Delivery Network)"]}
                ]
            },
            {
                "heading": "Module 7: Network Operations",
                "description": "Network management and operational practices",
                "items": [
                    {"title": "Network Monitoring Tools", "subtopics": ["SNMP (Simple Network Management Protocol)", "NetFlow/sFlow/IPFIX", "Packet Capture (Wireshark)", "Graphite/Grafana for Monitoring", "PRTG and SolarWinds"]},
                    {"title": "Network Documentation", "subtopics": ["Network Diagrams (Logical/Physical)", "IP Address Management (IPAM)", "Configuration Documentation", "Change Management Process", "Asset Management"]},
                    {"title": "Network Policies and Compliance", "subtopics": ["Security Policies", "Acceptable Use Policy", "Data Retention Policy", "Compliance Standards (PCI-DSS, HIPAA)", "Policy Implementation"]},
                    {"title": "Disaster Recovery and Backup", "subtopics": ["DR Planning and Strategy", "RTO and RPO", "Backup Types (Full/Incremental/Differential)", "Site Replication", "Failover Testing"]},
                    {"title": "Network Performance Optimization", "subtopics": ["Bandwidth Monitoring", "QoS Implementation", "Traffic Shaping", "Performance Baselines", "Bottleneck Analysis"]},
                    {"title": "Business Continuity", "subtopics": ["BCP (Business Continuity Planning)", "Single Point of Failure Identification", "Redundancy Design", "Alternative Routing", "Communication Plans"]},
                    {"title": "Change Management", "subtopics": ["RFC (Request for Change) Process", "Change Advisory Board (CAB)", "Implementation and Rollback", "Change Documentation", "Post-implementation Review"]},
                    {"title": "Incident Management", "subtopics": ["Incident Response Process", "Escalation Matrix", "Root Cause Analysis (RCA)", "Incident Reporting", "Lessons Learned"]},
                    {"title": "Capacity Planning", "subtopics": ["Growth Forecasting", "Bandwidth Utilization Analysis", "Hardware Capacity", "Cloud Resource Planning", "Cost Optimization"]},
                    {"title": "Network Team and Operations", "subtopics": ["NOC (Network Operations Center)", "On-call Rotation", "SLA Management", "Vendor Management", "Outsourcing Considerations"]}
                ]
            },
            {
                "heading": "Module 8: Network Troubleshooting",
                "description": "Systematic approach to network problem solving",
                "items": [
                    {"title": "Troubleshooting Methodology", "subtopics": ["Structured Troubleshooting Approach", "Gather Information", "Establish Theory", "Test Hypothesis", "Document Findings"]},
                    {"title": "Common Network Issues", "subtopics": ["IP Configuration Problems", "DNS Resolution Issues", "Gateway Connectivity", "Duplex/Speed Mismatches", "VLAN Misconfigurations"]},
                    {"title": "Connectivity Troubleshooting", "subtopics": ["Ping and Traceroute", "PathPing and MTR", "Packet Loss Analysis", "Latency Issues", "Jitter and Bandwidth Testing"]},
                    {"title": "Cable and Port Issues", "subtopics": ["Cable Tester Tools", "Fiber Optic Testing", "Port Flapping Issues", "Transceiver Problems", "Link Status Errors"]},
                    {"title": "Command-line Utilities", "subtopics": ["ipconfig/ifconfig", "netstat and ss", "nslookup/dig", "arp -a", "route print"]},
                    {"title": "Wireless Troubleshooting", "subtopics": ["Signal Strength Analysis", "Channel Interference", "Authentication Issues", "Roaming Failures", "Client Connection Problems"]},
                    {"title": "Performance Troubleshooting", "subtopics": ["CPU/Memory Utilization", "Interface Errors", "Queue Depth", "Buffer Overflows", "QoS Violations"]},
                    {"title": "DNS and DHCP Troubleshooting", "subtopics": ["DHCP Pool Exhaustion", "DNS Resolution Failures", "DNS Cache Issues", "DHCP Relay Problems", "Dynamic Update Failures"]},
                    {"title": "Advanced Troubleshooting Tools", "subtopics": ["Wireshark Packet Analysis", "Network Sniffers", "Protocol Analyzers", "Network Taps", "SPAN/Port Mirroring"]},
                    {"title": "Troubleshooting Documentation", "subtopics": ["Issue Logging", "Troubleshooting Log Templates", "Knowledge Base Articles", "Post-mortem Analysis", "Process Improvement"]}
                ]
            },
            {
                "heading": "Module 9: Hands-On Labs and Practice",
                "description": "Practical lab exercises and real-world scenarios",
                "items": [
                    {"title": "Router Configuration Lab", "subtopics": ["Basic Router Setup", "Interface Configuration", "Static Route Configuration", "Default Gateway", "NAT Configuration"]},
                    {"title": "Switch Configuration Lab", "subtopics": ["VLAN Creation", "VLAN Trunking", "VLAN Inter Routing", "Port Security", "STP Configuration"]},
                    {"title": "IP Addressing Lab", "subtopics": ["Subnetting Practice", "VLSM Implementation", "IP Address Planning", "DHCP Server Setup", "IP Addressing Troubleshooting"]},
                    {"title": "Wireless Configuration Lab", "subtopics": ["AP Setup and Configuration", "Security Implementation", "Channel Planning", "Client Connectivity", "Guest Network Setup"]},
                    {"title": "VPN Setup Lab", "subtopics": ["Site-to-Site VPN", "Remote Access VPN", "IPsec Configuration", "SSL VPN Setup", "VPN Troubleshooting"]},
                    {"title": "Firewall Configuration Lab", "subtopics": ["Firewall Rule Creation", "Zone-based Policy", "NAT Configuration", "IDS/IPS Setup", "Logging and Monitoring"]},
                    {"title": "Network Design Project", "subtopics": ["Enterprise Network Design", "Subnetting Scheme", "Redundancy Implementation", "Security Hardening", "Documentation"]},
                    {"title": "Packet Analysis Lab", "subtopics": ["Wireshark Basics", "Protocol Analysis", "Traffic Capture", "Performance Issues", "Security Analysis"]},
                    {"title": "Troubleshooting Scenarios", "subtopics": ["Network Down Scenario", "Slow Connectivity", "Security Breach Simulation", "VLAN Issues", "VPN Problems"]},
                    {"title": "Final Comprehensive Lab", "subtopics": ["Complete Network Setup", "Multi-vendor Integration", "Performance Optimization", "Security Implementation", "Documentation"]}
                ]
            },
            {
                "heading": "Module 10: Certification Exam Preparation",
                "description": "Prepare for CompTIA Network+ N10-009 exam",
                "items": [
                    {"title": "Exam Overview and Objectives", "subtopics": ["Exam Format", "Question Types", "Passing Score", "Exam Domains", "Time Management"]},
                    {"title": "Domain 1: Networking Fundamentals", "subtopics": ["Network Models", "Ports and Protocols", "IP Addressing", "OSI Model", "Topology Types"]},
                    {"title": "Domain 2: Network Implementations", "subtopics": ["Network Devices", "Fiber Optics", "Wireless Technologies", "Cloud Concepts", "Physical Installations"]},
                    {"title": "Domain 3: Network Operations", "subtopics": ["Device Management", "Monitoring Tools", "High Availability", "API Integration", "Configuration Management"]},
                    {"title": "Domain 4: Network Security", "subtopics": ["Security Concepts", "Authentication Methods", "Network Segmentation", "Device Hardening", "Incident Response"]},
                    {"title": "Domain 5: Network Troubleshooting", "subtopics": ["Troubleshooting Methodology", "Tools and Utilities", "Cable Issues", "Configuration Issues", "Performance Issues"]},
                    {"title": "Practice Tests - Set 1", "subtopics": ["Multiple Choice Questions", "Performance-based Questions", "Scenario-based Questions", "Time-bound Practice", "Score Analysis"]},
                    {"title": "Practice Tests - Set 2", "subtopics": ["Full-length Mock Test", "PBQ Practice", "Weak Area Identification", "Review and Remediation", "Final Preparation"]},
                    {"title": "Exam Tips and Strategies", "subtopics": ["Question Reading Tips", "Elimination Method", "Time Allocation", "Flagging Questions", "Exam Day Preparation"]},
                    {"title": "Last Minute Revision", "subtopics": ["Key Concepts Review", "Acronyms and Formulas", "Quick Reference Guide", "Stress Management", "Confidence Building"]}
                ]
            }
        ])
        
        # =========================================================================
        # 4. TOPIC-WISE CONTENT DISTRIBUTION (Detailed)
        # =========================================================================
        course.topic_wise_content = json.dumps([
            {
                "heading": "Networking Fundamentals",
                "items": [
                    {
                        "title": "Introduction to Networking",
                        "description": "Basic networking concepts and models",
                        "subtopics": [
                            "Basic networking concepts and models",
                            "Need for computer networks",
                            "Network components and devices",
                            "Network communication fundamentals"
                        ]
                    },
                    {
                        "title": "OSI Model and TCP/IP",
                        "description": "Understanding network layers",
                        "subtopics": [
                            "Seven layers of OSI model",
                            "TCP/IP four-layer model",
                            "Encapsulation and decapsulation",
                            "Protocol interaction between layers"
                        ]
                    },
                    {
                        "title": "Network Types and Topologies",
                        "description": "Types of networks and physical/logical layouts",
                        "subtopics": [
                            "LAN, WAN, MAN, PAN, and VPN",
                            "Physical and logical topologies",
                            "Bus, Star, Ring, Mesh, and Hybrid",
                            "Network scale and scope"
                        ]
                    },
                    {
                        "title": "IP Addressing",
                        "description": "IPv4 and IPv6 addressing schemes",
                        "subtopics": [
                            "IPv4 address classes (A, B, C, D, E)",
                            "Private and public IP addresses",
                            "Subnet masks and CIDR notation",
                            "IPv6 addressing and types"
                        ]
                    }
                ]
            },
            {
                "heading": "Network Security",
                "items": [
                    {
                        "title": "Security Fundamentals",
                        "description": "Core security concepts and principles",
                        "subtopics": [
                            "CIA Triad (Confidentiality, Integrity, Availability)",
                            "Security threats and vulnerabilities",
                            "Security policies and procedures",
                            "Risk assessment and mitigation"
                        ]
                    },
                    {
                        "title": "Firewalls and VPNs",
                        "description": "Protection mechanisms for network security",
                        "subtopics": [
                            "Firewall types and implementations",
                            "Stateful packet inspection",
                            "VPN technologies (IPsec, SSL)",
                            "NAT and PAT configuration"
                        ]
                    },
                    {
                        "title": "Wireless Security",
                        "description": "WiFi protection and authentication",
                        "subtopics": [
                            "WPA2/WPA3 security protocols",
                            "Enterprise authentication (802.1X)",
                            "RADIUS integration",
                            "Wireless intrusion prevention"
                        ]
                    }
                ]
            }
        ])
        
        # =========================================================================
        # 5. INDUSTRY PROJECTS
        # =========================================================================
        course.projects_list = json.dumps([
            {
                "title": "Network Design Project",
                "description": "Design a complete enterprise network topology with VLANs, routing, and security. Create comprehensive network documentation including IP addressing scheme, VLAN structure, router and switch configurations, firewall rules, and security policies for a mid-sized organization."
            },
            {
                "title": "Troubleshooting Lab",
                "description": "Diagnose and fix common network issues in a simulated environment. Use systematic troubleshooting methodology to identify and resolve connectivity problems, performance issues, security breaches, and configuration errors in a multi-site enterprise network."
            },
            {
                "title": "Security Implementation",
                "description": "Configure firewalls, VPNs, and access controls for a small business. Implement a complete security solution including perimeter firewall, internal segmentation, site-to-site VPN, remote access VPN, 802.1X network access control, and security monitoring."
            },
            {
                "title": "Wireless Network Setup",
                "description": "Plan and deploy a secure wireless network for an office. Conduct site survey, design RF coverage, configure multiple access points, implement wireless security, set up guest network, and validate performance with thorough testing."
            }
        ])
        
        # =========================================================================
        # 6. CAREER BENEFITS
        # =========================================================================
        course.benefits_list = json.dumps([
            {"icon": "FaBriefcase", "title": "Job Ready", "description": "Get ready for network administrator roles"},
            {"icon": "FaCertificate", "title": "Certification Prep", "description": "Clear CompTIA Network+ exam"},
            {"icon": "FaLaptopCode", "title": "Hands-on Skills", "description": "Practical lab experience"},
            {"icon": "FaChartLine", "title": "Career Growth", "description": "Average 40% salary increase"}
        ])
        
        # =========================================================================
        # 7. COURSE ADVISORS
        # =========================================================================
        course.advisor_list = json.dumps([
            {
                "name": "Mr. Rajesh Kumar",
                "role": "Lead Instructor | CCIE Security",
                "bio": "Rajesh Kumar is a network security expert with over 15 years of experience in enterprise networking. He has trained thousands of students for CompTIA certifications and has worked with Fortune 500 companies on network security implementations.",
                "image_url": "https://trainingprotec.com/images/advisors/rajesh-kumar.jpg"
            },
            {
                "name": "Ms. Priya Sharma",
                "role": "Senior Network Architect",
                "bio": "Priya Sharma is a certified network architect with expertise in cloud networking and SDN. She has designed and implemented networks for major telecom companies and data centers.",
                "image_url": "https://trainingprotec.com/images/advisors/priya-sharma.jpg"
            }
        ])
        
        # =========================================================================
        # 8. STUDENT REVIEWS
        # =========================================================================
        course.reviews_list = json.dumps([
            {
                "name": "Ankit Patel",
                "role": "Network Admin at TechCorp",
                "text": "Excellent course! Cleared Network+ on first attempt. The hands-on labs were incredibly helpful and the instructor explained complex topics in a very easy way."
            },
            {
                "name": "Priya Singh",
                "role": "IT Support Specialist",
                "text": "Great hands-on labs. Very practical content. The troubleshooting section helped me a lot in my job. Highly recommended for anyone starting in networking."
            },
            {
                "name": "Vikram Kumar",
                "role": "Junior Network Engineer",
                "text": "Best course for beginners. The curriculum is well-structured and covers all exam objectives. The practice tests were very similar to actual exam questions."
            },
            {
                "name": "Saurabh Mishra",
                "role": "System Administrator",
                "text": "The instructor's real-world experience really shows in the teaching. I learned things that I directly apply at work. Worth every penny!"
            },
            {
                "name": "Aishwarya Reddy",
                "role": "Help Desk Technician",
                "text": "Started with zero knowledge in networking. Now I feel confident handling network issues at my job. The step-by-step approach made learning easy."
            }
        ])
        
        # =========================================================================
        # 9. WHY JOIN THIS PROGRAM
        # =========================================================================
        course.why_join = json.dumps([
            {"icon": "FaUserTie", "title": "Expert Trainers", "description": "Learn from industry professionals with 10+ years experience"},
            {"icon": "FaLaptopCode", "title": "Hands-on Labs", "description": "Practice on real equipment and simulations"},
            {"icon": "FaCertificate", "title": "Certification Focus", "description": "Specifically designed for exam success"},
            {"icon": "FaHeadset", "title": "24/7 Support", "description": "Round-the-clock doubt resolution"}
        ])
        
        # =========================================================================
        # 10. FAQ SECTION
        # =========================================================================
        course.faq = json.dumps([
            {
                "question": "What is CompTIA Network+ certification?",
                "answer": "CompTIA Network+ is a globally recognized certification that validates foundational networking skills required to configure, manage, troubleshoot, and secure enterprise networks. It is one of the most sought-after entry-level networking certifications in the industry."
            },
            {
                "question": "Which exam is covered in this training?",
                "answer": "This training covers the latest CompTIA Network+ N10-009 certification exam objectives. The N10-009 exam was released in 2024 and covers modern networking technologies including cloud, virtualization, and network security."
            },
            {
                "question": "Who should join the CompTIA Network+ course?",
                "answer": "This course is ideal for beginners, IT support professionals, help desk technicians, system administrators, and anyone looking to start a career in networking. No prior networking experience is required."
            },
            {
                "question": "Are there any prerequisites for CompTIA Network+?",
                "answer": "There are no mandatory prerequisites, but basic computer knowledge and understanding of IT fundamentals are recommended. The course is designed to take you from basics to advanced networking concepts."
            },
            {
                "question": "What skills will I learn in this course?",
                "answer": "You will learn networking fundamentals, IP addressing, subnetting, routing, switching, wireless networking, network security, troubleshooting, cloud networking concepts, and virtualization technologies."
            },
            {
                "question": "Does the training include practical labs?",
                "answer": "Yes, the training includes hands-on practical labs, real-world networking scenarios, and troubleshooting exercises. You will get access to virtual lab environments to practice all concepts."
            },
            {
                "question": "Is this training suitable for beginners?",
                "answer": "Yes, the course is designed for both beginners and working professionals. The curriculum starts from basic concepts and gradually progresses to advanced topics."
            },
            {
                "question": "Do you provide one-to-one training sessions?",
                "answer": "Yes, both one-to-one and group instructor-led training options are available. You can choose the mode that best suits your learning style and schedule."
            },
            {
                "question": "What job roles can I apply for after completing CompTIA Network+?",
                "answer": "You can apply for roles such as Network Support Technician, Network Administrator, IT Support Specialist, Help Desk Technician, Junior Network Engineer, and Field Service Technician."
            },
            {
                "question": "Is certification exam support provided?",
                "answer": "Yes, we provide complete guidance for certification exam preparation including practice tests, exam tips, scheduling assistance, and post-exam support."
            },
            {
                "question": "Why choose Training Protec for CompTIA Network+ training?",
                "answer": "Training Protec provides experienced trainers with real-world industry experience, practical lab sessions, flexible schedules, personalized support, interview preparation, and certification-focused training with high pass rates."
            },
            {
                "question": "How long does it take to complete this course?",
                "answer": "The course is designed for 40 hours of instructor-led training. However, the total time including labs, practice tests, and self-study is approximately 60-80 hours depending on your pace."
            },
            {
                "question": "Do you provide course materials and resources?",
                "answer": "Yes, you will receive comprehensive course materials including presentations, lab guides, practice questions, and access to our online learning portal with additional resources."
            },
            {
                "question": "What is the passing score for CompTIA Network+ exam?",
                "answer": "The passing score for CompTIA Network+ N10-009 exam is 720 out of 900 (on a scale of 100-900). The exam consists of 90 questions and you have 90 minutes to complete it."
            },
            {
                "question": "Can I retake the exam if I fail?",
                "answer": "Yes, if you fail the exam, you can retake it after a 30-day waiting period. We recommend using your practice test results to identify weak areas before retaking."
            }
        ])
        
        # =========================================================================
        # 11. ELIGIBILITY/PREREQUISITES
        # =========================================================================
        course.eligibility = """This course is ideal for:
- Beginners looking to start a career in networking
- IT support professionals wanting to advance their career
- Help desk technicians and system administrators
- Anyone seeking CompTIA Network+ certification

No mandatory prerequisites - basic computer knowledge is sufficient."""
        
        # =========================================================================
        # 12. CERTIFICATION
        # =========================================================================
        course.certification = json.dumps({
            "title": "CompTIA Network+ Certification",
            "description": "Complete your CompTIA Network+ N10-009 certification exam and become a certified network professional.",
            "details": [
                "Globally recognized certification",
                "Validates networking fundamentals",
                "Industry-standard credential",
                "Enhanced career opportunities"
            ]
        })
        
        # Save changes
        db.session.commit()
        
        print("=" * 60)
        print("SUCCESS! CompTIA Network+ Course Updated Successfully!")
        print("=" * 60)
        print(f"\nCourse ID: {course.id}")
        print(f"Course Title: {course.title}")
        print(f"Slug: {course.slug}")
        print(f"Sale Price: ${course.sale_price}")
        print(f"Original Price: ${course.original_price}")
        print(f"Duration: {course.duration}")
        print(f"Level: {course.level}")
        print(f"Modules: 10")
        print(f"Projects: 4")
        print("\nUpdated Sections:")
        print("  ✓ Basic Information")
        print("  ✓ Overview & Key Benefits")
        print("  ✓ Full Curriculum (10 Modules)")
        print("  ✓ Topic-wise Content")
        print("  ✓ Industry Projects (4)")
        print("  ✓ Career Benefits (4)")
        print("  ✓ Course Advisors (2)")
        print("  ✓ Student Reviews (5)")
        print("  ✓ Why Join (4 points)")
        print("  ✓ FAQ (15 questions)")
        print("  ✓ Eligibility/Prerequisites")
        print("  ✓ Certification Details")
        print("=" * 60)
        
        return True

if __name__ == "__main__":
    try:
        update_comptia_network_course()
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)