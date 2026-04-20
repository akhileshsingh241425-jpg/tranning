import { 
  FaCode, FaPaintBrush, FaChartLine, FaBullhorn, FaMobileAlt, FaShieldAlt, FaCloud, FaChartBar,
  FaHtml5, FaCss3Alt, FaReact, FaNodeJs, FaPython, FaDatabase,
  FaFigma, FaPalette, FaLayerGroup, FaBezierCurve, FaPenFancy,
  FaBrain, FaRobot, FaProjectDiagram, FaFlask,
  FaSearchPlus, FaHashtag, FaEnvelope, FaShareAlt, FaBullseye, FaChartLine as FaChartLine2,
  FaAppStore, FaLock, FaBug, FaNetworkWired, FaUserShield, FaTerminal,
  FaDocker, FaServer, FaTools, FaSitemap, FaCogs, FaFileCode,
  FaGraduationCap, FaCertificate, FaBookOpen, FaChalkboardTeacher, FaUsers, FaAward
} from 'react-icons/fa';
import courseDataAnalytics from '../assets/images/courses/data-analytics.jpg';
import courseNetworkSecurity from '../assets/images/courses/network-security.jpg';
import courseCybersecurity from '../assets/images/courses/cybersecurity.jpg';
import courseWebDev from '../assets/images/courses/web-development.jpg';
import courseDigitalMarketing from '../assets/images/courses/digital-marketing.jpg';
import courseGraphicDesign from '../assets/images/courses/graphic-design.jpg';
import courseMobileApp from '../assets/images/courses/mobile-app.jpg';

const coursesDetailData = [
  {
    slug: 'data-science-ai',
    title: 'Data Science & AI Master\'s Program',
    tagline: 'Become a Data Scientist — Learn Python, ML, Deep Learning & AI',
    heroImage: courseDataAnalytics,
    icon: FaChartLine,
    price: '₹16,999',
    duration: '6 Months',
    level: 'Beginner to Advanced',
    overview: `Transform your career with our comprehensive Data Science & AI Master's Program designed in collaboration with industry experts. This program covers everything from Python programming and statistics to advanced machine learning, deep learning, and natural language processing. Work on 15+ industry-grade projects, get placement assistance, and earn a certificate recognized by 200+ hiring partners.`,
    keyBenefits: [
      'Master Python, Pandas, NumPy & data visualization',
      'Build ML models with scikit-learn & TensorFlow',
      '15+ real-world projects including capstone',
      'Placement assistance with 200+ hiring partners',
      'Live instructor-led classes with doubt resolution',
      'Industry-recognized certification'
    ],
    subServices: [
      { icon: FaPython, title: 'Python for Data Science', description: 'Master Python programming, Pandas, NumPy, Matplotlib & Seaborn for data manipulation, analysis and visualization.' },
      { icon: FaBrain, title: 'Machine Learning', description: 'Learn supervised & unsupervised algorithms — regression, classification, clustering, ensemble methods & model evaluation.' },
      { icon: FaRobot, title: 'Deep Learning & Neural Networks', description: 'Build CNNs, RNNs & transformers with TensorFlow/Keras for image recognition, NLP & generative AI applications.' },
      { icon: FaChartBar, title: 'Data Analysis & Visualization', description: 'Transform raw data into insights using EDA, statistical methods, interactive dashboards with Plotly & Tableau.' },
      { icon: FaProjectDiagram, title: 'Natural Language Processing', description: 'Process text data using NLP techniques — sentiment analysis, text classification, chatbots & LLM applications.' },
      { icon: FaFlask, title: 'ML Model Deployment', description: 'Deploy models using Flask, FastAPI & cloud platforms. Build end-to-end ML pipelines for production.' }
    ],
    process: [
      { step: 1, title: 'Python & Statistics', description: 'Master Python, statistics & probability — the foundation for all data science work.' },
      { step: 2, title: 'Data Analysis & SQL', description: 'Learn SQL, data wrangling, EDA & visualization techniques with real datasets.' },
      { step: 3, title: 'Machine Learning', description: 'Build predictive models — regression, classification, clustering & recommendation systems.' },
      { step: 4, title: 'Deep Learning & AI', description: 'Master neural networks, computer vision, NLP & generative AI technologies.' },
      { step: 5, title: 'Capstone Projects', description: 'Build 3 end-to-end projects solving real business problems for your portfolio.' },
      { step: 6, title: 'Interview & Placement Prep', description: 'Resume building, mock interviews, coding challenges & placement assistance.' }
    ],
    technologies: ['Python', 'Pandas', 'NumPy', 'scikit-learn', 'TensorFlow', 'Keras', 'SQL', 'Tableau', 'Power BI', 'Spark', 'AWS', 'Git'],
    stats: [
      { number: '12,500+', label: 'Learners' },
      { number: '4.8', label: 'Rating' },
      { number: '180+', label: 'Hours Content' },
      { number: '15+', label: 'Projects' }
    ],
    faq: [
      { question: 'Do I need prior programming experience?', answer: 'No! We start from Python basics and build up. Complete beginners are welcome — many of our successful graduates started with zero coding experience.' },
      { question: 'Is there placement assistance?', answer: 'Yes! We provide dedicated placement assistance including resume reviews, mock interviews, and direct referrals to 200+ hiring partners worldwide.' },
      { question: 'What salary can I expect after completion?', answer: 'Our graduates see an average 70% salary hike. Entry-level data science roles start at $60,000-$90,000/year, with experienced roles going up to $150,000+/year.' },
      { question: 'Are classes live or recorded?', answer: 'Both! You get live instructor-led sessions plus recordings for revision. Live sessions include real-time doubt resolution and hands-on coding.' }
    ]
  },
  {
    slug: 'cloud-computing-devops',
    title: 'Cloud Computing & DevOps Engineer',
    tagline: 'Master AWS, Azure, Docker, Kubernetes & CI/CD Pipelines',
    heroImage: courseNetworkSecurity,
    icon: FaCloud,
    price: '₹14,999',
    duration: '5 Months',
    level: 'Intermediate',
    overview: `Become a certified Cloud & DevOps engineer with our industry-designed program. Learn AWS, Azure, Docker, Kubernetes, Terraform, and CI/CD pipeline automation. This hands-on program prepares you for top cloud certifications (AWS Solutions Architect, Azure Administrator) and equips you with skills demanded by 90% of Fortune 500 companies.`,
    keyBenefits: [
      'Master AWS, Azure & GCP cloud platforms',
      'Learn Docker, Kubernetes & container orchestration',
      'Build CI/CD pipelines with Jenkins, GitHub Actions',
      'AWS Solutions Architect certification prep included',
      'Infrastructure as Code with Terraform & Ansible',
      'Placement support with cloud-focused companies'
    ],
    subServices: [
      { icon: FaCloud, title: 'AWS Cloud Services', description: 'Master EC2, S3, Lambda, RDS, VPC, IAM & 30+ AWS services. Build scalable, secure cloud architectures.' },
      { icon: FaServer, title: 'Azure & Multi-Cloud', description: 'Learn Azure VMs, App Service, AKS & multi-cloud strategies. Understand cloud cost optimization & governance.' },
      { icon: FaDocker, title: 'Docker & Containerization', description: 'Build, ship & run containerized applications. Learn Docker Compose, networking, volumes & registry management.' },
      { icon: FaCogs, title: 'Kubernetes Orchestration', description: 'Deploy & manage containers at scale with K8s — pods, services, deployments, Helm charts & monitoring.' },
      { icon: FaTools, title: 'CI/CD & Automation', description: 'Build automated pipelines with Jenkins, GitHub Actions, ArgoCD. Implement GitOps & Infrastructure as Code.' },
      { icon: FaTerminal, title: 'Linux & Scripting', description: 'Master Linux administration, Bash scripting, Python automation & configuration management with Ansible.' }
    ],
    process: [
      { step: 1, title: 'Linux & Networking', description: 'Master Linux commands, networking fundamentals, and shell scripting basics.' },
      { step: 2, title: 'AWS Cloud Mastery', description: 'Learn 30+ AWS services, cloud architecture patterns, and security best practices.' },
      { step: 3, title: 'Containers & Docker', description: 'Containerize applications with Docker, understand microservices architecture.' },
      { step: 4, title: 'Kubernetes & Orchestration', description: 'Deploy, scale & manage containerized apps with Kubernetes in production.' },
      { step: 5, title: 'CI/CD & IaC', description: 'Build end-to-end automated pipelines and manage infrastructure with Terraform.' },
      { step: 6, title: 'Certification & Placement', description: 'Prepare for AWS/Azure certifications and get dedicated placement support.' }
    ],
    technologies: ['AWS', 'Azure', 'Docker', 'Kubernetes', 'Terraform', 'Jenkins', 'Ansible', 'Linux', 'Python', 'Git', 'Prometheus', 'Grafana'],
    stats: [
      { number: '9,800+', label: 'Learners' },
      { number: '4.7', label: 'Rating' },
      { number: '150+', label: 'Hours Content' },
      { number: '12+', label: 'Projects' }
    ],
    faq: [
      { question: 'Do I need coding experience?', answer: 'Basic programming knowledge helps, but we cover Linux and scripting from scratch. Familiarity with any programming language is sufficient.' },
      { question: 'Which cloud certification is included?', answer: 'We prepare you for AWS Solutions Architect Associate and Azure Administrator certifications with practice tests and exam strategies.' },
{ question: 'What job roles can I target?', answer: 'Cloud Engineer, DevOps Engineer, SRE, Cloud Architect, Platform Engineer - all among the highest-paid roles in IT with salaries of $70,000-$180,000/year.' },
      { question: 'Is hands-on lab access provided?', answer: 'Yes! You get free AWS/Azure lab credits to practice on real cloud environments throughout the course.' }
    ]
  },
  {
    slug: 'cyber-security',
    title: 'Cyber Security Professional',
    tagline: 'Learn Ethical Hacking, Penetration Testing & Security Operations',
    heroImage: courseCybersecurity,
    icon: FaShieldAlt,
    price: '₹15,999',
    duration: '5 Months',
    level: 'Beginner to Advanced',
    overview: `Enter the critical field of cybersecurity with our comprehensive professional program. Learn ethical hacking, penetration testing, network security, incident response, and security operations. This program aligns with CEH and CompTIA Security+ certifications and prepares you for one of the fastest-growing career paths in technology.`,
    keyBenefits: [
      'Learn ethical hacking & penetration testing',
      'Master network security & firewall management',
      'CEH & CompTIA Security+ certification prep',
      'Hands-on labs with real attack/defense scenarios',
      'Learn SIEM, SOC operations & incident response',
      'Placement assistance in cybersecurity roles'
    ],
    subServices: [
      { icon: FaBug, title: 'Ethical Hacking & Pen Testing', description: 'Learn reconnaissance, scanning, exploitation & reporting using Kali Linux, Metasploit, Burp Suite & Nmap.' },
      { icon: FaNetworkWired, title: 'Network Security', description: 'Master firewalls, IDS/IPS, VPNs, network monitoring & defense against DDoS, MITM & other attacks.' },
      { icon: FaLock, title: 'Application Security', description: 'Understand OWASP Top 10, web app vulnerabilities, API security, secure coding & security testing tools.' },
      { icon: FaUserShield, title: 'Security Operations (SOC)', description: 'Learn SIEM tools (Splunk, ELK), log analysis, threat hunting, incident detection & response workflows.' },
      { icon: FaShieldAlt, title: 'Compliance & Governance', description: 'Understand ISO 27001, GDPR, PCI-DSS, risk assessment frameworks & security audit procedures.' },
      { icon: FaTerminal, title: 'Digital Forensics', description: 'Investigate security incidents — disk forensics, memory analysis, malware analysis & evidence preservation.' }
    ],
    process: [
      { step: 1, title: 'Security Fundamentals', description: 'Learn networking basics, operating system security & cryptography foundations.' },
      { step: 2, title: 'Ethical Hacking', description: 'Master reconnaissance, scanning, exploitation with hands-on Kali Linux labs.' },
      { step: 3, title: 'Network & App Security', description: 'Defend networks and applications against common attack vectors.' },
      { step: 4, title: 'SOC & Incident Response', description: 'Operate SIEM tools, analyze threats, and respond to security incidents.' },
      { step: 5, title: 'Advanced Topics', description: 'Cloud security, mobile security, IoT security & emerging threat landscape.' },
      { step: 6, title: 'Certification & Career', description: 'CEH/Security+ exam preparation and dedicated placement support.' }
    ],
    technologies: ['Kali Linux', 'Metasploit', 'Burp Suite', 'Wireshark', 'Nmap', 'Splunk', 'Nessus', 'Snort', 'Python', 'PowerShell', 'AWS Security', 'OWASP'],
    stats: [
      { number: '7,200+', label: 'Learners' },
      { number: '4.8', label: 'Rating' },
      { number: '160+', label: 'Hours Content' },
      { number: '20+', label: 'Lab Exercises' }
    ],
    faq: [
      { question: 'Is this legal to learn?', answer: 'Absolutely! Ethical hacking is a legitimate and highly sought-after skill. We teach responsible security testing in controlled lab environments.' },
      { question: 'What certifications does this prepare for?', answer: 'CEH (Certified Ethical Hacker), CompTIA Security+, and foundational knowledge for CISSP and OSCP.' },
      { question: 'What salary can cybersecurity professionals expect?', answer: 'Entry-level cybersecurity roles start at $55,000-$80,000/year, with experienced professionals earning $100,000-$200,000+/year.' },
      { question: 'Do I need a technical background?', answer: 'Basic computer knowledge is enough. We cover networking and OS fundamentals before diving into security topics.' }
    ]
  },
  {
    slug: 'web-development',
    title: 'Full Stack Web Development',
    tagline: 'Master MERN Stack — React, Node.js, MongoDB & Express',
    heroImage: courseWebDev,
    icon: FaCode,
    price: '₹12,999',
    duration: '6 Months',
    level: 'Beginner to Advanced',
    overview: `Become a job-ready Full Stack Developer with our comprehensive MERN Stack program. Master HTML, CSS, JavaScript, React.js, Node.js, Express, and MongoDB. Build 10+ production-ready projects, learn deployment, testing, and industry best practices. Our graduates work at companies like TCS, Infosys, Wipro, startups and as freelancers.`,
    keyBenefits: [
      'Build 10+ real-world projects for your portfolio',
      'Master React, Node.js, Express & MongoDB (MERN)',
      'Learn responsive design & mobile-first development',
      'Deploy projects on AWS, Vercel & Netlify',
      'Git, GitHub & collaboration workflows',
      'Job-ready with resume building & mock interviews'
    ],
    subServices: [
      { icon: FaHtml5, title: 'HTML5, CSS3 & JavaScript', description: 'Build responsive, accessible websites with semantic HTML, modern CSS (Flexbox, Grid, animations) & ES6+ JavaScript.' },
      { icon: FaReact, title: 'React.js & Frontend', description: 'Master React components, hooks, state management (Redux/Context), React Router & Next.js for SSR applications.' },
      { icon: FaNodeJs, title: 'Node.js & Express Backend', description: 'Build RESTful APIs, middleware, authentication, file uploads & real-time features with Socket.io.' },
      { icon: FaDatabase, title: 'MongoDB & SQL Databases', description: 'Design schemas, write queries, implement CRUD operations, aggregation pipelines & database optimization.' },
      { icon: FaCss3Alt, title: 'Advanced CSS & Frameworks', description: 'Master Tailwind CSS, Bootstrap, CSS-in-JS, Sass preprocessors & design system implementation.' },
      { icon: FaCode, title: 'Deployment & DevOps Basics', description: 'Deploy on Vercel, Netlify, AWS. Learn Docker basics, CI/CD with GitHub Actions & production monitoring.' }
    ],
    process: [
      { step: 1, title: 'Web Foundations', description: 'Master HTML, CSS & JavaScript fundamentals with 5+ mini-projects.' },
      { step: 2, title: 'Frontend with React', description: 'Build interactive SPAs with React, routing, state management & API integration.' },
      { step: 3, title: 'Backend with Node.js', description: 'Create server-side applications, REST APIs & database integrations.' },
      { step: 4, title: 'Full Stack Projects', description: 'Build e-commerce, social media & dashboard apps combining all technologies.' },
      { step: 5, title: 'Advanced & Testing', description: 'Learn TypeScript, testing, performance optimization & security practices.' },
      { step: 6, title: 'Portfolio & Placement', description: 'Build your portfolio website, prepare for interviews & apply to jobs.' }
    ],
    technologies: ['HTML5', 'CSS3', 'JavaScript', 'React', 'Next.js', 'Node.js', 'Express', 'MongoDB', 'PostgreSQL', 'Git', 'Docker', 'Tailwind CSS', 'TypeScript'],
    stats: [
      { number: '15,000+', label: 'Learners' },
      { number: '4.9', label: 'Rating' },
      { number: '200+', label: 'Hours Content' },
      { number: '10+', label: 'Projects' }
    ],
    faq: [
      { question: 'Can a complete beginner join?', answer: 'Yes! This course starts from HTML basics. Many of our top-performing graduates had zero coding experience when they started.' },
{ question: 'What job roles can I get after this?', answer: 'Frontend Developer, Backend Developer, Full Stack Developer, MERN Stack Developer - with salaries of $50,000-$120,000/year.' },
      { question: 'How are classes conducted?', answer: 'Live instructor-led sessions on weekdays/weekends with recordings available. Includes code-along exercises and doubt resolution.' },
      { question: 'Do you provide internship/job support?', answer: 'Yes! We offer 100% placement assistance with resume preparation, portfolio review, mock technical interviews, and direct referrals.' }
    ]
  },
  {
    slug: 'digital-marketing',
    title: 'Digital Marketing Specialist',
    tagline: 'Master SEO, Google Ads, Social Media & Analytics — Get Certified',
    heroImage: courseDigitalMarketing,
    icon: FaBullhorn,
    price: '₹9,999',
    duration: '4 Months',
    level: 'Beginner',
    overview: `Become a certified Digital Marketing specialist with our all-in-one program. Master SEO, SEM, social media marketing, Google Ads, content marketing, email automation, and analytics. Work on live campaigns, get Google & HubSpot certified, and learn to generate measurable ROI for any business — whether you want a corporate career or want to grow your own business.`,
    keyBenefits: [
      'Google Ads & Google Analytics certification prep',
      'Work on live campaigns with real budgets',
      'Master SEO, SEM, SMM & content marketing',
      'Learn marketing automation & email marketing',
      'Build data-driven strategies with analytics',
      'Freelance-ready with client management skills'
    ],
    subServices: [
      { icon: FaSearchPlus, title: 'SEO & Content Strategy', description: 'Learn keyword research, on-page/off-page SEO, technical SEO, content planning & link building for organic growth.' },
      { icon: FaBullseye, title: 'Google Ads & PPC', description: 'Master campaign setup, audience targeting, ad copywriting, bidding strategies, conversion tracking & ROAS optimization.' },
      { icon: FaShareAlt, title: 'Social Media Marketing', description: 'Build strategies for Instagram, LinkedIn, Facebook & YouTube. Learn content creation, ads, analytics & influencer marketing.' },
      { icon: FaEnvelope, title: 'Email Marketing & CRM', description: 'Create automated sequences, drip campaigns, segmentation & A/B testing with Mailchimp, HubSpot & ConvertKit.' },
      { icon: FaChartLine2, title: 'Analytics & Performance', description: 'Master Google Analytics 4, Meta Pixel, UTM tracking, attribution modeling & campaign performance reporting.' },
      { icon: FaHashtag, title: 'Content & Brand Strategy', description: 'Develop content calendars, write compelling copy, create video content plans & build brand authority online.' }
    ],
    process: [
      { step: 1, title: 'Marketing Fundamentals', description: 'Learn digital marketing landscape, customer journey & funnel strategies.' },
      { step: 2, title: 'SEO & Content', description: 'Master organic growth through search engine optimization & content marketing.' },
      { step: 3, title: 'Paid Advertising', description: 'Run Google Ads & social media advertising campaigns with live budgets.' },
      { step: 4, title: 'Social & Email', description: 'Build social media presence & automated email marketing systems.' },
      { step: 5, title: 'Analytics & Optimization', description: 'Measure, analyze & optimize campaigns using data-driven approaches.' },
      { step: 6, title: 'Portfolio & Freelancing', description: 'Build case studies, prepare for certifications & learn freelance business skills.' }
    ],
    technologies: ['Google Analytics 4', 'Google Ads', 'SEMrush', 'Ahrefs', 'Mailchimp', 'HubSpot', 'Meta Ads Manager', 'Canva', 'WordPress', 'Hootsuite'],
    stats: [
      { number: '18,000+', label: 'Learners' },
      { number: '4.7', label: 'Rating' },
      { number: '120+', label: 'Hours Content' },
      { number: '10+', label: 'Live Projects' }
    ],
    faq: [
      { question: 'Do I need a marketing background?', answer: 'Not at all! This program is designed for complete beginners. We teach everything from basics to advanced strategies step-by-step.' },
      { question: 'Will I get Google certified?', answer: 'Yes! We prepare you for Google Analytics and Google Ads certifications — both industry-recognized credentials that boost your resume.' },
      { question: 'Can I use this for my own business?', answer: 'Absolutely! Many students take this to market their own businesses. Every technique is immediately applicable to real businesses.' },
      { question: 'What is the earning potential?', answer: 'Digital marketing managers earn $50,000-$120,000/year. Freelancers can earn $3,000-$15,000/month depending on clients and expertise.' }
    ]
  },
  {
    slug: 'business-analytics',
    title: 'Business Analytics & Intelligence',
    tagline: 'Master Excel, SQL, Tableau, Power BI & Statistical Analysis',
    heroImage: courseDigitalMarketing,
    icon: FaChartBar,
    price: '₹11,999',
    duration: '4 Months',
    level: 'Beginner to Intermediate',
    overview: `Bridge the gap between data and business decisions with our Business Analytics program. Learn advanced Excel, SQL, Python for analytics, Tableau, Power BI, and statistical analysis. This program is ideal for professionals in any domain who want to become data-driven decision makers — from marketing and finance to operations and HR.`,
    keyBenefits: [
      'Master Excel, SQL, Tableau & Power BI',
      'Learn Python for business analytics',
      'Build interactive dashboards & reports',
      'Understand statistics & data storytelling',
      'Industry case studies from real companies',
      'Certification valued by consulting & analytics firms'
    ],
    subServices: [
      { icon: FaChartBar, title: 'Advanced Excel & VBA', description: 'Master pivot tables, VLOOKUP, Power Query, macros & VBA automation for business data analysis & reporting.' },
      { icon: FaDatabase, title: 'SQL for Business', description: 'Write complex queries, join tables, aggregate data, create views & stored procedures for business intelligence.' },
      { icon: FaChartLine, title: 'Tableau & Power BI', description: 'Build interactive dashboards, data visualizations & automated reports for executive-level business insights.' },
      { icon: FaPython, title: 'Python for Analytics', description: 'Use Python with Pandas & Matplotlib for data analysis, automation & advanced statistical modeling.' },
      { icon: FaSitemap, title: 'Statistical Analysis', description: 'Learn hypothesis testing, regression analysis, A/B testing, forecasting & predictive analytics for business.' },
      { icon: FaProjectDiagram, title: 'Business Case Studies', description: 'Solve real-world problems from e-commerce, banking, healthcare & marketing using analytics frameworks & tools.' }
    ],
    process: [
      { step: 1, title: 'Excel & Data Basics', description: 'Master advanced Excel, data cleaning & fundamental analytics concepts.' },
      { step: 2, title: 'SQL & Databases', description: 'Query relational databases & extract business insights from large datasets.' },
      { step: 3, title: 'Visualization Tools', description: 'Build dashboards with Tableau & Power BI for business stakeholders.' },
      { step: 4, title: 'Statistics & Python', description: 'Apply statistical methods & Python for deeper business analysis.' },
      { step: 5, title: 'Industry Projects', description: 'Solve real business problems across different domains & industries.' },
      { step: 6, title: 'Career Preparation', description: 'Build analytics portfolio, practice case interviews & get placement support.' }
    ],
    technologies: ['Excel', 'SQL', 'Tableau', 'Power BI', 'Python', 'Pandas', 'R', 'SPSS', 'Google Sheets', 'Looker'],
    stats: [
      { number: '8,500+', label: 'Learners' },
      { number: '4.6', label: 'Rating' },
      { number: '100+', label: 'Hours Content' },
      { number: '8+', label: 'Case Studies' }
    ],
    faq: [
      { question: 'Who is this course for?', answer: 'Anyone wanting to make data-driven decisions — MBA students, marketing professionals, managers, finance analysts, or career changers entering analytics.' },
      { question: 'Do I need programming skills?', answer: 'No! We start with Excel and SQL which require no programming background. Python is taught from basics for analytics-specific use cases.' },
      { question: 'How is this different from Data Science?', answer: 'Business Analytics focuses on business understanding, dashboards & decision-making. Data Science goes deeper into ML/AI algorithms. Many start here then move to data science.' },
      { question: 'What tools will I master?', answer: 'Excel (advanced), SQL, Tableau, Power BI, and Python for analytics. These are the most in-demand tools in business analytics job postings.' }
    ]
  },
  {
    slug: 'ui-ux-design',
    title: 'UI/UX Design Professional',
    tagline: 'Master Figma, User Research, Wireframing & Prototyping',
    heroImage: courseGraphicDesign,
    icon: FaPaintBrush,
    price: '₹10,999',
    duration: '4 Months',
    level: 'Beginner',
    overview: `Launch your design career with our industry-aligned UI/UX Design program. Learn user research, wireframing, prototyping, visual design, and design systems using Figma — the industry's #1 design tool. Build a portfolio of 8+ projects and get placement-ready for product design roles at top tech companies and startups.`,
    keyBenefits: [
      'Master Figma — the industry standard design tool',
      'Learn user research, personas & journey mapping',
      'Build interactive prototypes & design systems',
      'Create 8+ portfolio projects',
      'Understand accessibility & responsive design',
      'Placement assistance for product design roles'
    ],
    subServices: [
      { icon: FaFigma, title: 'Figma Mastery', description: 'Learn auto-layout, components, variants, design tokens, prototyping & collaboration features for professional design workflows.' },
      { icon: FaUsers, title: 'User Research & Testing', description: 'Conduct user interviews, surveys, usability testing, create personas & journey maps to design user-centered products.' },
      { icon: FaBezierCurve, title: 'Wireframing & Prototyping', description: 'Create low-fidelity wireframes, high-fidelity mockups & interactive prototypes with micro-interactions & animations.' },
      { icon: FaPalette, title: 'Visual Design', description: 'Master color theory, typography, spacing, iconography & visual hierarchy for beautiful, functional interfaces.' },
      { icon: FaLayerGroup, title: 'Design Systems', description: 'Build scalable component libraries, style guides & design tokens for consistent product experiences across platforms.' },
      { icon: FaPenFancy, title: 'Portfolio & Case Studies', description: 'Document your design process in compelling case studies that showcase your thinking, process & impact to employers.' }
    ],
    process: [
      { step: 1, title: 'Design Fundamentals', description: 'Learn core design principles — balance, contrast, hierarchy, alignment & spacing.' },
      { step: 2, title: 'Figma & Tools', description: 'Get hands-on with Figma through guided exercises & component building.' },
      { step: 3, title: 'UX Research', description: 'Conduct user research, create personas, journey maps & information architecture.' },
      { step: 4, title: 'UI Design', description: 'Design beautiful interfaces for web & mobile with proper design systems.' },
      { step: 5, title: 'Prototyping & Testing', description: 'Build interactive prototypes, conduct usability tests & iterate designs.' },
      { step: 6, title: 'Portfolio Building', description: 'Create 3+ detailed case studies & a portfolio website for job applications.' }
    ],
    technologies: ['Figma', 'Adobe XD', 'Sketch', 'InVision', 'Maze', 'Hotjar', 'Miro', 'Notion', 'Framer'],
    stats: [
      { number: '6,200+', label: 'Learners' },
      { number: '4.8', label: 'Rating' },
      { number: '100+', label: 'Hours Content' },
      { number: '8+', label: 'Projects' }
    ],
    faq: [
      { question: 'Do I need artistic skills?', answer: 'No! UI/UX design is about problem-solving, not drawing. We teach you the frameworks and tools to create professional designs regardless of artistic background.' },
      { question: 'What tools do I need?', answer: 'Just a laptop and internet! Figma is free. We provide access to all premium resources, templates, and design assets needed for the course.' },
      { question: 'What is the career outlook for UX designers?', answer: 'Product/UX designers are in massive demand. Entry-level salaries start at $55,000-$80,000/year, with senior designers earning $120,000-$200,000/year at top companies.' },
      { question: 'Is this only for mobile/web design?', answer: 'We focus primarily on digital product design (web & mobile), but the principles apply to any design discipline — AR/VR, voice UI, automotive, etc.' }
    ]
  },
  {
    slug: 'mobile-app-development',
    title: 'Mobile App Development',
    tagline: 'Build Professional iOS & Android Apps with React Native & Flutter',
    heroImage: courseMobileApp,
    icon: FaMobileAlt,
    price: '₹14,999',
    duration: '5 Months',
    level: 'Intermediate',
    overview: `Build professional mobile applications for iOS and Android using React Native and Flutter. This program teaches cross-platform development, allowing you to create beautiful, performant apps from a single codebase. From UI implementation to API integration, push notifications to app store deployment — learn the complete mobile development lifecycle.`,
    keyBenefits: [
      'Build cross-platform apps with React Native & Flutter',
      'Learn mobile UI/UX patterns & navigation',
      'Integrate APIs, Firebase & push notifications',
      'Publish apps to App Store & Google Play',
      'Build 5+ portfolio-ready mobile apps',
      'Placement support for mobile developer roles'
    ],
    subServices: [
      { icon: FaReact, title: 'React Native Development', description: 'Build cross-platform apps with React Native — components, navigation, Redux state management & native module integration.' },
      { icon: FaMobileAlt, title: 'Flutter & Dart', description: 'Create beautiful apps with Flutter — widget composition, Provider/Riverpod state management & platform-specific customizations.' },
      { icon: FaDatabase, title: 'Backend & Firebase', description: 'Integrate REST/GraphQL APIs, Firebase Auth, Firestore, Cloud Functions & real-time database for mobile backends.' },
      { icon: FaPaintBrush, title: 'Mobile UI/UX Patterns', description: 'Implement iOS Human Interface Guidelines & Material Design. Create smooth animations, transitions & responsive layouts.' },
      { icon: FaFileCode, title: 'Advanced Features', description: 'Add push notifications, camera, geolocation, maps, payments& social login using native device capabilities.' },
      { icon: FaAppStore, title: 'App Store Deployment', description: 'Complete deployment process — app signing, store listings, screenshots, review guidelines & post-launch analytics.' }
    ],
    process: [
      { step: 1, title: 'Mobile Fundamentals', description: 'Understand mobile development concepts, React Native or Flutter setup & basics.' },
      { step: 2, title: 'UI Development', description: 'Build mobile interfaces with navigation, layouts & responsive design patterns.' },
      { step: 3, title: 'State & API Integration', description: 'Master state management, REST APIs, Firebase & local storage.' },
      { step: 4, title: 'Native Features', description: 'Access camera, location, notifications & other device capabilities.' },
      { step: 5, title: 'Testing & Optimization', description: 'Test, debug & optimize app performance across devices.' },
      { step: 6, title: 'Publishing & Career', description: 'Deploy to stores, build portfolio & prepare for mobile dev interviews.' }
    ],
    technologies: ['React Native', 'Flutter', 'Dart', 'Firebase', 'Redux', 'TypeScript', 'Expo', 'SQLite', 'GraphQL', 'Xcode', 'Android Studio'],
    stats: [
      { number: '5,400+', label: 'Learners' },
      { number: '4.7', label: 'Rating' },
      { number: '140+', label: 'Hours Content' },
      { number: '5+', label: 'App Projects' }
    ],
    faq: [
      { question: 'React Native or Flutter — which is better?', answer: 'We cover both! React Native is great if you know JavaScript, Flutter offers best performance. Most companies use one or the other — knowing both makes you versatile.' },
      { question: 'Do I need a Mac for iOS development?', answer: 'For React Native with Expo, you can develop on Windows. For final iOS builds, a Mac is needed — we help with cloud Mac solutions for Windows users.' },
      { question: 'What prior knowledge is needed?', answer: 'JavaScript knowledge is recommended for React Native, general programming for Flutter. Our Web Development course is a great precursor.' },
      { question: 'Can I publish my projects?', answer: 'Absolutely! Your projects are yours to keep, modify & monetize. We guide you through the complete app store submission for both platforms.' }
    ]
  }
];

export default coursesDetailData;
