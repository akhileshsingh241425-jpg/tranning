import { 
  FaShieldAlt, FaClipboardCheck, FaCode, FaGraduationCap, FaBug, FaBullhorn,
  FaLock, FaNetworkWired, FaServer, FaUserShield, FaSearch, FaExclamationTriangle,
  FaFileContract, FaBalanceScale, FaCertificate, FaDatabase, FaCheckCircle, FaGlobe,
  FaLaptopCode, FaMobileAlt, FaCloud, FaCogs, FaRocket, FaPaintBrush,
  FaChalkboardTeacher, FaUsers, FaAward, FaBookOpen, FaHandsHelping, FaBrain,
  FaVial, FaClipboardList, FaTachometerAlt, FaSyncAlt, FaToolbox, FaEye,
  FaChartLine, FaHashtag, FaEnvelope, FaSearchPlus, FaBullseye, FaShareAlt
} from 'react-icons/fa';
import socMonitoring from '../assets/images/services/soc-monitoring.jpg';
import penetrationTesting from '../assets/images/services/penetration-testing.jpg';
import cloudSecurity from '../assets/images/services/cloud-security.jpg';
import securityConsulting from '../assets/images/services/security-consulting.jpg';
import incidentResponse from '../assets/images/services/incident-response.jpg';
import securityTraining from '../assets/images/services/security-training.jpg';

const servicesDetailData = [
  {
    slug: 'cybersecurity-services',
    title: 'Cybersecurity Services',
    tagline: 'Protect Your Digital Assets with Advanced Threat Defense',
    heroImage: socMonitoring,
    icon: FaShieldAlt,
    overview: `In today's rapidly evolving digital landscape, cybersecurity is no longer optional — it's essential. Our Cybersecurity Services provide comprehensive protection against sophisticated cyber threats, ensuring your business remains secure, compliant, and resilient. We employ cutting-edge tools, proven methodologies, and industry-certified professionals to safeguard your critical infrastructure, sensitive data, and digital operations from ever-evolving attack vectors.`,
    keyBenefits: [
      'Proactive identification and remediation of security vulnerabilities',
      'Reduced risk of data breaches and financial losses',
      '24/7 security monitoring and real-time threat detection',
      'Compliance with industry regulations (ISO 27001, SOC 2, GDPR)',
      'Improved customer trust and business reputation',
      'Customized security strategies tailored to your industry'
    ],
    subServices: [
      {
        icon: FaSearch,
        title: 'Penetration Testing',
        description: 'Our certified ethical hackers simulate real-world attacks on your network, web applications, APIs, and mobile apps to uncover vulnerabilities before malicious actors do. We deliver detailed reports with risk ratings and actionable remediation steps.'
      },
      {
        icon: FaNetworkWired,
        title: 'Network Security Assessment',
        description: 'Comprehensive evaluation of your network architecture, firewall configurations, access controls, and intrusion detection systems. We identify weak points in your infrastructure and recommend hardening measures to prevent unauthorized access.'
      },
      {
        icon: FaServer,
        title: 'Cloud Security',
        description: 'Secure your AWS, Azure, or GCP environments with thorough cloud configuration audits, identity & access management reviews, data encryption verification, and compliance checks to protect your cloud-based assets.'
      },
      {
        icon: FaExclamationTriangle,
        title: 'Incident Response & Forensics',
        description: 'When a breach occurs, every second counts. Our rapid incident response team contains threats, investigates root causes through digital forensics, recovers compromised systems, and implements measures to prevent recurrence.'
      },
      {
        icon: FaUserShield,
        title: 'Security Operations Center (SOC)',
        description: 'Round-the-clock security monitoring with our managed SOC service. We use SIEM tools, threat intelligence feeds, and advanced analytics to detect, analyze, and respond to security incidents in real-time.'
      },
      {
        icon: FaLock,
        title: 'Data Protection & Encryption',
        description: 'Implement robust data-at-rest and data-in-transit encryption, DLP (Data Loss Prevention) solutions, secure key management, and access controls to protect your most sensitive business information.'
      }
    ],
    process: [
      { step: 1, title: 'Discovery & Scoping', description: 'We assess your current security posture, understand your business requirements, and define the scope of engagement.' },
      { step: 2, title: 'Vulnerability Assessment', description: 'Using automated scanners and manual techniques, we identify vulnerabilities across your infrastructure.' },
      { step: 3, title: 'Exploitation & Testing', description: 'Our ethical hackers attempt to exploit identified vulnerabilities to determine real-world impact.' },
      { step: 4, title: 'Analysis & Reporting', description: 'We compile comprehensive reports with risk ratings, proof-of-concept findings, and prioritized remediation guidance.' },
      { step: 5, title: 'Remediation Support', description: 'Our team works alongside your IT staff to fix vulnerabilities and strengthen your defenses.' },
      { step: 6, title: 'Ongoing Monitoring', description: 'Continuous security monitoring and periodic reassessments ensure your security posture stays strong.' }
    ],
    technologies: ['Burp Suite', 'Metasploit', 'Nessus', 'Wireshark', 'Splunk SIEM', 'CrowdStrike', 'Nmap', 'OWASP ZAP', 'Qualys', 'Carbon Black'],
    stats: [
      { number: '500+', label: 'Security Assessments' },
      { number: '99.9%', label: 'Threat Detection Rate' },
      { number: '24/7', label: 'Security Monitoring' },
      { number: '50+', label: 'Certified Experts' }
    ],
    faq: [
      { question: 'How often should we conduct penetration testing?', answer: 'We recommend penetration testing at least annually, or after any significant infrastructure changes, new application deployments, or regulatory requirements. High-risk industries may benefit from quarterly testing.' },
      { question: 'What is the difference between vulnerability assessment and penetration testing?', answer: 'A vulnerability assessment identifies and catalogs security weaknesses, while penetration testing goes further by actively exploiting those vulnerabilities to determine the actual business impact and risk level.' },
      { question: 'Do you provide post-assessment support?', answer: 'Absolutely. We provide detailed remediation guidance and work with your team to fix identified vulnerabilities. We also offer retesting to verify that fixes have been properly implemented.' },
      { question: 'What certifications do your security experts hold?', answer: 'Our team holds industry-leading certifications including CEH, OSCP, CISSP, CISA, CompTIA Security+, and AWS Security Specialty, ensuring you get expert-level assessments.' }
    ]
  },
  {
    slug: 'compliance-regulatory-audits',
    title: 'Compliance & Regulatory Audits',
    tagline: 'Navigate Complex Regulations with Confidence',
    heroImage: penetrationTesting,
    icon: FaClipboardCheck,
    overview: `Regulatory compliance isn't just about avoiding penalties — it's about building trust with your customers, partners, and stakeholders. Our Compliance & Regulatory Audit services help organizations navigate the complex landscape of industry regulations, data protection laws, and security standards. From gap analysis to full certification support, we ensure your organization meets and exceeds compliance requirements while strengthening your overall security posture.`,
    keyBenefits: [
      'Avoid hefty fines and legal penalties from non-compliance',
      'Build customer trust through demonstrated compliance',
      'Streamlined audit preparation reducing time and effort',
      'Clear roadmap for achieving and maintaining compliance',
      'Expert guidance through complex regulatory requirements',
      'Continuous compliance monitoring and reporting'
    ],
    subServices: [
      {
        icon: FaCertificate,
        title: 'ISO 27001 Implementation',
        description: 'Complete Information Security Management System (ISMS) implementation and certification support. We guide you through every step — from risk assessment and policy development to internal audits and certification body coordination.'
      },
      {
        icon: FaBalanceScale,
        title: 'GDPR Compliance',
        description: 'Comprehensive General Data Protection Regulation assessment covering data mapping, consent management, privacy impact assessments, Data Protection Officer (DPO) support, and ongoing compliance monitoring for EU data processing.'
      },
      {
        icon: FaFileContract,
        title: 'SOC 2 Type I & II Audits',
        description: 'End-to-end SOC 2 readiness assessment and audit support. We help design controls around Trust Service Criteria — security, availability, processing integrity, confidentiality, and privacy — and prepare you for external auditor reviews.'
      },
      {
        icon: FaDatabase,
        title: 'PCI DSS Compliance',
        description: 'Payment Card Industry Data Security Standard compliance for organizations handling cardholder data. We assess your Cardholder Data Environment (CDE), identify compliance gaps, and implement required security controls.'
      },
      {
        icon: FaCheckCircle,
        title: 'HIPAA Compliance',
        description: 'Healthcare data protection compliance services including risk analysis, policy development, employee training, and technical safeguard implementation to protect Protected Health Information (PHI).'
      },
      {
        icon: FaGlobe,
        title: 'Custom Compliance Frameworks',
        description: 'Tailored compliance programs for industry-specific regulations including NIST Cybersecurity Framework, CIS Controls, SWIFT CSP, and regional data protection laws, customized to your business needs.'
      }
    ],
    process: [
      { step: 1, title: 'Compliance Gap Analysis', description: 'We evaluate your current security controls against the required compliance framework to identify gaps.' },
      { step: 2, title: 'Risk Assessment', description: 'Thorough risk assessment to understand threats, vulnerabilities, and potential impacts on your organization.' },
      { step: 3, title: 'Policy & Procedure Development', description: 'We create or update policies, procedures, and documentation required for compliance.' },
      { step: 4, title: 'Control Implementation', description: 'Technical and administrative controls are designed and implemented to meet compliance requirements.' },
      { step: 5, title: 'Internal Audit & Testing', description: 'Pre-certification internal audits to verify all controls are operating effectively.' },
      { step: 6, title: 'Certification & Maintenance', description: 'Support during external audits and ongoing monitoring to maintain continuous compliance.' }
    ],
    technologies: ['OneTrust', 'Vanta', 'Drata', 'ServiceNow GRC', 'RSA Archer', 'Qualys Policy Compliance', 'Tenable.io', 'Rapid7 InsightConnect'],
    stats: [
      { number: '200+', label: 'Successful Audits' },
      { number: '100%', label: 'Certification Rate' },
      { number: '15+', label: 'Compliance Frameworks' },
      { number: '50+', label: 'Industries Served' }
    ],
    faq: [
      { question: 'How long does ISO 27001 certification take?', answer: 'Typically 3-6 months depending on your organization\'s size, complexity, and current security maturity level. We accelerate the process with proven templates and frameworks.' },
      { question: 'What happens if we fail an audit?', answer: 'We conduct thorough pre-assessment audits to identify and fix gaps before the formal audit. Our preparation process significantly reduces the risk of non-conformities during certification audits.' },
      { question: 'Do you help with ongoing compliance maintenance?', answer: 'Yes, we offer continuous compliance monitoring services including periodic reviews, control testing, policy updates, and preparation for surveillance audits.' },
      { question: 'Can you handle multiple compliance frameworks simultaneously?', answer: 'Absolutely. We specialize in integrated compliance programs that map controls across multiple frameworks (e.g., ISO 27001 + SOC 2 + GDPR), reducing duplication and cost.' }
    ]
  },
  {
    slug: 'software-web-development',
    title: 'Software & Web Development',
    tagline: 'Build Secure, Scalable Solutions for the Digital Age',
    heroImage: cloudSecurity,
    icon: FaCode,
    overview: `Transform your business with custom software solutions built with security at their core. Our development team combines cutting-edge technologies with secure coding practices to deliver robust, scalable applications that drive business growth. From enterprise web applications to mobile apps and APIs, we build solutions that are not only feature-rich but also resilient against modern cyber threats, ensuring your digital products are secure from day one.`,
    keyBenefits: [
      'Security-first development approach (DevSecOps)',
      'Scalable architecture designed for growth',
      'Modern tech stack with latest frameworks',
      'Agile development with transparent communication',
      'Comprehensive testing and quality assurance',
      'Post-launch support and maintenance'
    ],
    subServices: [
      {
        icon: FaLaptopCode,
        title: 'Enterprise Web Applications',
        description: 'Full-stack web application development using React, Angular, Vue.js, Node.js, Python, and .NET. We build responsive, secure, and high-performance web applications with modern UI/UX design and robust backend architectures.'
      },
      {
        icon: FaMobileAlt,
        title: 'Mobile App Development',
        description: 'Native and cross-platform mobile applications for iOS and Android using React Native, Flutter, and Swift. Every app includes end-to-end encryption, secure authentication, and compliance with app store security requirements.'
      },
      {
        icon: FaCloud,
        title: 'Cloud-Native Solutions',
        description: 'Microservices architecture, serverless computing, containerized deployments with Docker and Kubernetes, and cloud infrastructure setup on AWS, Azure, or GCP — all built for maximum scalability and reliability.'
      },
      {
        icon: FaCogs,
        title: 'API Development & Integration',
        description: 'Secure RESTful and GraphQL API design and development with OAuth 2.0 authentication, rate limiting, input validation, and comprehensive API documentation. We also integrate third-party services seamlessly.'
      },
      {
        icon: FaRocket,
        title: 'E-Commerce Solutions',
        description: 'Custom e-commerce platforms with PCI-compliant payment processing, inventory management, customer analytics, and multi-channel selling capabilities. We build shopping experiences that convert.'
      },
      {
        icon: FaPaintBrush,
        title: 'UI/UX Design',
        description: 'User-centered design with wireframing, prototyping, and usability testing. Our designers create intuitive interfaces that enhance user engagement while maintaining accessibility standards (WCAG 2.1).'
      }
    ],
    process: [
      { step: 1, title: 'Requirements Analysis', description: 'Deep-dive into your business requirements, user stories, and technical specifications to define the project scope.' },
      { step: 2, title: 'Architecture & Design', description: 'System architecture design, database modeling, UI/UX wireframes, and technology stack selection.' },
      { step: 3, title: 'Agile Development', description: 'Iterative development in 2-week sprints with regular demos, code reviews, and stakeholder feedback.' },
      { step: 4, title: 'Security Integration', description: 'SAST/DAST scanning, code security reviews, and vulnerability testing integrated into the CI/CD pipeline.' },
      { step: 5, title: 'QA & Testing', description: 'Comprehensive functional, integration, performance, and security testing before deployment.' },
      { step: 6, title: 'Deployment & Support', description: 'Production deployment with monitoring setup, documentation, and ongoing maintenance and support.' }
    ],
    technologies: ['React', 'Node.js', 'Python', 'TypeScript', 'PostgreSQL', 'MongoDB', 'Docker', 'Kubernetes', 'AWS', 'Azure', 'GraphQL', 'Redis'],
    stats: [
      { number: '300+', label: 'Projects Delivered' },
      { number: '99.5%', label: 'Client Satisfaction' },
      { number: '40+', label: 'Technologies' },
      { number: '100+', label: 'Developers' }
    ],
    faq: [
      { question: 'What technologies do you specialize in?', answer: 'We work with modern tech stacks including React, Angular, Vue.js, Node.js, Python/Django, .NET, React Native, Flutter, and cloud platforms like AWS, Azure, and GCP. We choose the best technology for your specific needs.' },
      { question: 'How do you ensure security in development?', answer: 'We follow DevSecOps practices — security is integrated into every stage of development through secure coding guidelines, automated SAST/DAST scanning, dependency vulnerability checks, and manual code reviews.' },
      { question: 'What is your development methodology?', answer: 'We use Agile/Scrum methodology with 2-week sprints, daily standups, sprint reviews, and retrospectives. You have full visibility into progress through project management tools and regular updates.' },
      { question: 'Do you provide post-launch support?', answer: 'Yes, we offer comprehensive post-launch support including bug fixes, performance optimization, security patches, feature enhancements, and 24/7 monitoring for critical applications.' }
    ]
  },
  {
    slug: 'training-skill-development',
    title: 'Training & Skill Development',
    tagline: 'Build Future-Ready Talent for the Digital World',
    heroImage: securityConsulting,
    icon: FaGraduationCap,
    overview: `Empower your workforce with industry-aligned training programs designed to build real-world skills. Our comprehensive training solutions cover cybersecurity, cloud computing, software development, and digital transformation — delivered by certified instructors with hands-on lab environments. Whether you're upskilling existing employees or building new talent pipelines, our programs are tailored to meet your organization's specific learning objectives and career development goals.`,
    keyBenefits: [
      'Hands-on practical training with real-world scenarios',
      'Industry-recognized certifications and credentials',
      'Customized training programs for your organization',
      'Expert instructors with real industry experience',
      'Flexible delivery — online, in-person, or hybrid',
      'Post-training assessment and skill validation'
    ],
    subServices: [
      {
        icon: FaShieldAlt,
        title: 'Cybersecurity Training',
        description: 'Comprehensive cybersecurity courses covering ethical hacking, penetration testing, threat analysis, incident response, and security operations. Prepare for CEH, OSCP, CISSP, and CompTIA Security+ certifications with hands-on lab exercises.'
      },
      {
        icon: FaCloud,
        title: 'Cloud Computing Certification',
        description: 'AWS, Azure, and Google Cloud certification training programs from foundational to professional level. Includes hands-on labs with real cloud environments, practice exams, and expert-led sessions to accelerate your cloud career.'
      },
      {
        icon: FaChalkboardTeacher,
        title: 'Corporate Security Awareness',
        description: 'Organization-wide security awareness training covering phishing prevention, social engineering defense, password security, data handling, and incident reporting. Reduce human error — the #1 cause of security breaches.'
      },
      {
        icon: FaCode,
        title: 'DevSecOps Workshop',
        description: 'Hands-on workshops integrating security into CI/CD pipelines. Learn secure coding practices, automated security testing, container security, infrastructure-as-code security, and shift-left security strategies.'
      },
      {
        icon: FaUsers,
        title: 'Leadership & Management',
        description: 'IT leadership development programs covering security governance, risk management, compliance leadership, and strategic technology planning for managers and C-level executives.'
      },
      {
        icon: FaBookOpen,
        title: 'Custom Training Programs',
        description: 'Tailored training solutions designed around your organization\'s specific technology stack, security challenges, and skill gaps. We create custom curricula with relevant case studies and hands-on exercises.'
      }
    ],
    process: [
      { step: 1, title: 'Training Needs Analysis', description: 'We assess your team\'s current skill levels, identify gaps, and understand your learning objectives.' },
      { step: 2, title: 'Curriculum Design', description: 'Custom training curriculum developed with hands-on labs, case studies, and real-world scenarios.' },
      { step: 3, title: 'Environment Setup', description: 'Dedicated lab environments provisioned with necessary tools and infrastructure for practical exercises.' },
      { step: 4, title: 'Training Delivery', description: 'Expert-led sessions with interactive learning, group exercises, and individual hands-on practice.' },
      { step: 5, title: 'Assessment & Certification', description: 'Skills assessment through practical exams, projects, and certification preparation support.' },
      { step: 6, title: 'Continuous Learning', description: 'Post-training resources, refresher sessions, and advanced learning paths for continuous development.' }
    ],
    technologies: ['Kali Linux', 'AWS Academy', 'Azure Learn', 'Hack The Box', 'TryHackMe', 'Splunk', 'Docker', 'Kubernetes', 'OWASP', 'Burp Suite'],
    stats: [
      { number: '5000+', label: 'Professionals Trained' },
      { number: '95%', label: 'Certification Pass Rate' },
      { number: '50+', label: 'Training Programs' },
      { number: '100+', label: 'Corporate Clients' }
    ],
    faq: [
      { question: 'Do you provide certification preparation?', answer: 'Yes, our training programs are aligned with major industry certifications. We provide practice exams, study materials, and exam preparation support. Our students have a 95%+ first-attempt pass rate.' },
      { question: 'Can training be customized for our organization?', answer: 'Absolutely. We design custom training programs based on your specific technology stack, security challenges, compliance requirements, and employee skill levels. We can also incorporate your own case studies and scenarios.' },
      { question: 'What formats do you offer?', answer: 'We offer flexible delivery options including instructor-led classroom training, virtual live sessions, self-paced e-learning, hybrid models, and on-site bootcamps at your facility.' },
      { question: 'Do you provide hands-on lab access?', answer: 'Yes, every participant gets access to dedicated lab environments with real tools and infrastructure for hands-on practice during and after the training period.' }
    ]
  },
  {
    slug: 'quality-assurance-testing',
    title: 'Quality & Assurance Testing',
    tagline: 'Deliver Flawless Software with Rigorous Testing',
    heroImage: incidentResponse,
    icon: FaBug,
    overview: `Quality isn't negotiable — it's the foundation of user trust and business success. Our Quality Assurance & Testing services ensure your software applications perform flawlessly under all conditions. From automated testing frameworks to manual exploratory testing, performance benchmarking to security validation, we provide comprehensive quality assurance that catches bugs before your users do. Our rigorous testing methodology ensures your products are reliable, secure, and ready for the market.`,
    keyBenefits: [
      'Early bug detection reducing fix costs by up to 10x',
      'Faster time-to-market with automated testing pipelines',
      'Improved application reliability and user experience',
      'Comprehensive test coverage across all platforms',
      'Security validation integrated into QA process',
      'Detailed reporting with actionable insights'
    ],
    subServices: [
      {
        icon: FaVial,
        title: 'Automated Testing',
        description: 'End-to-end test automation using Selenium, Cypress, Playwright, and Jest. We build scalable test frameworks integrated into CI/CD pipelines for continuous testing — covering unit, integration, regression, and E2E tests.'
      },
      {
        icon: FaTachometerAlt,
        title: 'Performance & Load Testing',
        description: 'Stress testing, load testing, and endurance testing using JMeter, Gatling, and k6. We simulate thousands of concurrent users to ensure your application handles peak traffic without degradation or crashes.'
      },
      {
        icon: FaShieldAlt,
        title: 'Security Testing (VAPT)',
        description: 'Vulnerability Assessment and Penetration Testing specifically for applications. We identify security flaws including SQL injection, XSS, CSRF, authentication bypasses, and business logic vulnerabilities.'
      },
      {
        icon: FaMobileAlt,
        title: 'Mobile App Testing',
        description: 'Comprehensive testing across iOS and Android devices covering functional, UI/UX, compatibility, performance, and security testing. We test on real devices across multiple OS versions and screen sizes.'
      },
      {
        icon: FaClipboardList,
        title: 'Manual & Exploratory Testing',
        description: 'Expert QA analysts perform manual testing, exploratory testing, and usability reviews that automated tests can miss. We think like end-users to uncover edge cases and user experience issues.'
      },
      {
        icon: FaSyncAlt,
        title: 'API & Integration Testing',
        description: 'Thorough API testing using Postman, REST Assured, and custom frameworks. We validate API responses, error handling, data integrity, authentication, and integration between microservices.'
      }
    ],
    process: [
      { step: 1, title: 'Test Strategy & Planning', description: 'We define test scope, objectives, test types, tools, and resource requirements based on your application and risk profile.' },
      { step: 2, title: 'Test Environment Setup', description: 'Configuration of test environments mirroring production, with test data generation and tool setup.' },
      { step: 3, title: 'Test Case Development', description: 'Detailed test cases and automated test scripts created covering all functional and non-functional requirements.' },
      { step: 4, title: 'Test Execution', description: 'Systematic test execution with defect logging, severity classification, and real-time progress tracking.' },
      { step: 5, title: 'Defect Management', description: 'Comprehensive bug reporting with reproduction steps, root cause analysis, and fix verification through retesting.' },
      { step: 6, title: 'Reporting & Sign-off', description: 'Detailed test summary reports with metrics, coverage analysis, risk assessment, and go/no-go recommendations.' }
    ],
    technologies: ['Selenium', 'Cypress', 'JMeter', 'Postman', 'Jest', 'Playwright', 'Appium', 'BrowserStack', 'JIRA', 'TestRail', 'k6', 'Gatling'],
    stats: [
      { number: '1M+', label: 'Test Cases Executed' },
      { number: '99.8%', label: 'Defect Detection Rate' },
      { number: '60%', label: 'Faster Release Cycles' },
      { number: '200+', label: 'Applications Tested' }
    ],
    faq: [
      { question: 'How much of the testing can be automated?', answer: 'Typically 60-80% of regression and functional tests can be automated. We analyze your application to identify the optimal automation coverage while keeping manual testing for exploratory and usability scenarios.' },
      { question: 'Do you integrate testing into CI/CD pipelines?', answer: 'Yes, we set up automated test suites that run on every code commit, pull request, and deployment — providing continuous quality feedback throughout the development lifecycle.' },
      { question: 'What types of applications can you test?', answer: 'We test web applications, mobile apps (iOS & Android), APIs, desktop applications, IoT solutions, and enterprise software across all major technology stacks.' },
      { question: 'How do you handle test data and environments?', answer: 'We set up dedicated test environments mirroring production and use synthetic test data generation to ensure realistic testing without compromising production data security.' }
    ]
  },
  {
    slug: 'digital-marketing',
    title: 'Digital Marketing',
    tagline: 'Accelerate Growth with Data-Driven Marketing',
    heroImage: securityTraining,
    icon: FaBullhorn,
    overview: `In the digital-first world, effective marketing is the engine that drives business growth. Our Digital Marketing services combine creative strategy with data analytics to deliver measurable results. From SEO and content marketing to paid advertising and social media management, we craft comprehensive digital campaigns that increase brand visibility, generate qualified leads, and convert prospects into loyal customers. Every strategy is backed by analytics and optimized for maximum ROI.`,
    keyBenefits: [
      'Data-driven strategies with measurable KPIs',
      'Increased organic traffic and search rankings',
      'Higher conversion rates and lead generation',
      'Cost-effective advertising with optimized ROI',
      'Consistent brand presence across all channels',
      'Transparent reporting and real-time analytics'
    ],
    subServices: [
      {
        icon: FaSearchPlus,
        title: 'Search Engine Optimization (SEO)',
        description: 'Comprehensive SEO services including technical SEO audits, keyword research, on-page optimization, content strategy, backlink building, and local SEO. We improve your organic search rankings and drive sustainable traffic growth.'
      },
      {
        icon: FaBullseye,
        title: 'Pay-Per-Click Advertising (PPC)',
        description: 'High-ROI Google Ads, Bing Ads, and social media advertising campaigns with advanced audience targeting, A/B testing, bid optimization, and conversion tracking. We maximize every advertising dollar spent.'
      },
      {
        icon: FaShareAlt,
        title: 'Social Media Marketing',
        description: 'Strategic social media management across LinkedIn, Instagram, Twitter, and Facebook. We create engaging content, build brand communities, run targeted campaigns, and provide social listening and reputation management.'
      },
      {
        icon: FaEnvelope,
        title: 'Email Marketing & Automation',
        description: 'Automated email campaigns with personalization, segmentation, A/B testing, drip sequences, and detailed analytics. We nurture leads through the sales funnel and re-engage existing customers for repeat business.'
      },
      {
        icon: FaChartLine,
        title: 'Content Marketing',
        description: 'Strategic content creation including blog posts, whitepapers, case studies, infographics, and video content. We develop thought leadership content that educates, engages, and converts your target audience.'
      },
      {
        icon: FaHashtag,
        title: 'Brand Strategy & Identity',
        description: 'Complete brand positioning, visual identity design, messaging framework, and brand guidelines. We help you differentiate in the market with a compelling brand story that resonates with your audience.'
      }
    ],
    process: [
      { step: 1, title: 'Market Research & Audit', description: 'We analyze your market, competitors, current digital presence, and target audience to identify opportunities.' },
      { step: 2, title: 'Strategy Development', description: 'Data-driven marketing strategy with defined goals, KPIs, channel selection, and budget allocation.' },
      { step: 3, title: 'Campaign Creation', description: 'Creative development of ad copy, content, landing pages, and marketing assets optimized for each channel.' },
      { step: 4, title: 'Campaign Launch', description: 'Strategic campaign rollout with proper tracking, attribution, and real-time monitoring setup.' },
      { step: 5, title: 'Optimization & A/B Testing', description: 'Continuous performance optimization through A/B testing, bid adjustments, and content refinement.' },
      { step: 6, title: 'Reporting & Scaling', description: 'Comprehensive analytics reporting with insights and recommendations for scaling successful campaigns.' }
    ],
    technologies: ['Google Analytics', 'Google Ads', 'SEMrush', 'Ahrefs', 'HubSpot', 'Mailchimp', 'Hootsuite', 'Canva', 'Facebook Ads Manager', 'LinkedIn Campaign Manager'],
    stats: [
      { number: '300%', label: 'Avg Traffic Increase' },
      { number: '150+', label: 'Campaigns Managed' },
      { number: '10M+', label: 'Leads Generated' },
      { number: '50+', label: 'Industries Served' }
    ],
    faq: [
      { question: 'How long does it take to see SEO results?', answer: 'SEO is a long-term strategy. Initial improvements are typically visible within 3-4 months, with significant ranking and traffic increases in 6-12 months. PPC campaigns can deliver immediate results while SEO builds momentum.' },
      { question: 'What is your approach to measuring ROI?', answer: 'We set clear KPIs from day one — traffic, leads, conversions, cost-per-acquisition, and revenue attribution. Monthly reports provide transparent insights into campaign performance and ROI.' },
      { question: 'Do you create the content or do we need to provide it?', answer: 'Our team includes experienced content writers, designers, and videographers who create all marketing content. We also collaborate with your team for industry-specific insights and brand voice consistency.' },
      { question: 'Which social media platforms should we focus on?', answer: 'Platform selection depends on your target audience and industry. We analyze where your audience is most active and engaged, then develop platform-specific strategies rather than a one-size-fits-all approach.' }
    ]
  }
];

export default servicesDetailData;
