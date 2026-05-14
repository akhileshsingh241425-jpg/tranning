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
    title: 'Data Science & AI Course',
    tagline: 'Become a Data Scientist - Master Python, ML, Deep Learning & AI',
    heroImage: courseDataAnalytics,
    icon: FaChartLine,
    price: '$299',
    originalPrice: '$799',
    rating: 4.8,
    reviews: 15420,
    learners: '25,000+',
    duration: '6 Months',
    level: 'Beginner to Advanced',
    modules: 25,
    projects: 18,
    mode: 'Live Online / Self-Paced',
    trainingSchedule: 'Weekdays: Mon-Fri (7-10 PM IST)\nWeekends: Sat-Sun (10 AM-2 PM IST)',
    start_date: 'Every Monday',
    next_batch: 'Starting 1st June 2026',
    overview: `The Data Science & AI training program is designed to make you job-ready in one of the highest-paying careers in tech. This comprehensive course covers Python programming, statistics, machine learning, deep learning, NLP, and computer vision.

You will work on real-world datasets and build 18+ industry projects including predictive models, recommendation systems, image classifiers, and AI chatbots. The curriculum is designed by industry experts and updated regularly to match current market requirements.

This program is suitable for beginners with no prior coding experience as well as professionals looking to switch careers into Data Science and AI.`,
    keyBenefits: [
      'Master Python programming from scratch',
      'Learn statistics and probability for data science',
      'Build machine learning models with scikit-learn',
      'Create deep learning models with TensorFlow and Keras',
      'Work with natural language processing (NLP)',
      'Build computer vision applications',
      'Create recommendation systems',
      'Deploy ML models to production',
      'Work with big data tools like Spark and Hadoop',
      'Get career guidance and interview preparation'
    ],
    technologies: [
      'Python', 'NumPy', 'Pandas', 'Matplotlib', 'Seaborn', 'Scikit-learn', 
      'TensorFlow', 'Keras', 'PyTorch', 'OpenCV', 'NLTK', 'SQL', 'MongoDB'
    ],
    topicWiseContent: [
      {
        heading: 'Module 1: Python Fundamentals',
        items: [
          {title: 'Introduction to Python', subtopics: ['Installation', 'IDE Setup', 'Hello World']},
          {title: 'Variables and Data Types', subtopics: ['Integer', 'Float', 'String', 'Boolean']},
          {title: 'Control Flow', subtopics: ['If-Else', 'For Loop', 'While Loop']},
          {title: 'Functions', subtopics: ['Function Definition', 'Parameters', 'Return Values']},
          {title: 'Data Structures', subtopics: ['Lists', 'Tuples', 'Dictionaries', 'Sets']}
        ]
      },
      {
        heading: 'Module 2: Python for Data Science',
        items: [
          {title: 'NumPy Library', subtopics: ['Arrays', 'Vectorized Operations']},
          {title: 'Pandas Library', subtopics: ['DataFrames', 'Data Cleaning']},
          {title: 'Data Visualization', subtopics: ['Matplotlib', 'Seaborn', 'Plotly']},
          {title: 'Working with Files', subtopics: ['CSV', 'Excel', 'JSON']}
        ]
      },
      {
        heading: 'Module 3: Statistics & Probability',
        items: [
          {title: 'Descriptive Statistics', subtopics: ['Mean', 'Median', 'Mode', 'Variance']},
          {title: 'Probability', subtopics: ['Probability Rules', 'Bayes Theorem']},
          {title: 'Hypothesis Testing', subtopics: ['T-Test', 'Chi-Square', 'ANOVA']},
          {title: 'Correlation', subtopics: ['Pearson', 'Linear Regression']}
        ]
      },
      {
        heading: 'Module 4: Machine Learning Fundamentals',
        items: [
          {title: 'Linear Regression', subtopics: ['Simple', 'Multiple', 'Polynomial']},
          {title: 'Logistic Regression', subtopics: ['Binary Classification', 'Confusion Matrix']},
          {title: 'Decision Trees', subtopics: ['Tree Building', 'Gini Index']},
          {title: 'Random Forest', subtopics: ['Ensemble Learning', 'Bagging']},
          {title: 'SVM and KNN', subtopics: ['Support Vectors', 'Distance Metrics']}
        ]
      },
      {
        heading: 'Module 5: Deep Learning',
        items: [
          {title: 'Neural Networks', subtopics: ['Perceptron', 'Activation Functions']},
          {title: 'CNN', subtopics: ['Convolution', 'Pooling', 'Transfer Learning']},
          {title: 'RNN & LSTM', subtopics: ['Sequential Data', 'Time Series']},
          {title: 'TensorFlow & Keras', subtopics: ['Model Building', 'Training']}
        ]
      },
      {
        heading: 'Module 6: NLP & Computer Vision',
        items: [
          {title: 'NLP Basics', subtopics: ['Tokenization', 'Stemming', 'Lemmatization']},
          {title: 'Text Embeddings', subtopics: ['Word2Vec', 'BERT']},
          {title: 'Sentiment Analysis', subtopics: ['Text Classification']},
          {title: 'Computer Vision', subtopics: ['Image Processing', 'Object Detection']}
        ]
      },
      {
        heading: 'Module 7-10: Projects',
        items: [
          {title: 'House Price Prediction', subtopics: ['Regression', 'Feature Engineering']},
          {title: 'Customer Churn Prediction', subtopics: ['Classification', 'EDA']},
          {title: 'Fraud Detection', subtopics: ['Anomaly Detection', 'Imbalanced Data']},
          {title: 'Recommendation System', subtopics: ['Collaborative Filtering']},
          {title: 'Face Recognition', subtopics: ['CNN', 'OpenCV']},
          {title: 'AI Chatbot', subtopics: ['NLP', 'Rasa']}
        ]
      }
    ],
    projectsList: [
      {title: 'House Price Prediction Model', description: 'Build a model to predict house prices based on various features'},
      {title: 'Customer Churn Prediction', description: 'Predict customer churn using classification algorithms'},
      {title: 'Credit Card Fraud Detection', description: 'Build anomaly detection system for fraud detection'},
      {title: 'Customer Segmentation', description: 'Use clustering to segment customers based on behavior'},
      {title: 'Movie Recommendation System', description: 'Build hybrid recommendation system for movies'},
      {title: 'Sales Forecasting', description: 'Forecast future sales using time series analysis'},
      {title: 'Face Recognition System', description: 'Build AI-powered attendance system using face recognition'},
      {title: 'Object Detection', description: 'Implement YOLO for real-time object detection'},
      {title: 'AI Chatbot', description: 'Build intelligent chatbot using NLP and deep learning'},
      {title: 'Sentiment Analysis', description: 'Analyze customer sentiment from product reviews'},
      {title: 'Stock Price Prediction', description: 'Predict stock prices using LSTM neural networks'},
      {title: 'Medical Image Classification', description: 'Classify medical images using CNN'},
      {title: 'Email Spam Detection', description: 'Build spam classifier using NLP'},
      {title: 'Fake News Detection', description: 'Detect fake news using text classification'},
      {title: 'Capstone Project', description: 'Complete end-to-end ML pipeline from data to deployment'}
    ],
    reviewsList: [
      {name: 'Rahul Sharma', role: 'Data Scientist at Flipkart', text: 'Best course for Data Science! The projects are industry-relevant and helped me crack interviews at top companies.'},
      {name: 'Priya Gupta', role: 'ML Engineer at Amazon', text: 'The curriculum is comprehensive. I transitioned from a non-tech background to ML Engineer within 6 months. Highly recommended!'},
      {name: 'Amit Kumar', role: 'Data Analyst at Google', text: 'Excellent teaching methodology. The Python to Deep Learning journey was smooth. Projects helped build strong portfolio.'},
      {name: 'Sneha Patel', role: 'AI Engineer at Microsoft', text: 'The NLP and Computer Vision sections are amazing. Got placed with 150% salary hike after completing this course!'},
      {name: 'Vikram Singh', role: 'Data Scientist at Swiggy', text: 'Real-world projects were the highlight. The capstone project helped demonstrate practical skills to recruiters.'},
      {name: 'Anjali Reddy', role: 'Junior Data Scientist at Netflix', text: 'From zero coding knowledge to building ML models - this course made it possible. Great instructors!'},
      {name: 'Mohammad Khan', role: 'Data Science Associate at Deloitte', text: 'The statistics and ML modules are very well explained. Perfect for beginners. Got my first job in 3 months!'},
      {name: 'Pooja Joshi', role: 'ML Developer at Ola', text: 'The deep learning projects are fantastic. Face recognition and chatbot projects are directly applicable to real scenarios.'}
    ],
    why_join: [
      {icon: 'FaUserTie', title: 'Expert Mentors', description: 'Learn from industry experts with 10+ years experience'},
      {icon: 'FaLaptopCode', title: '18+ Live Projects', description: 'Work on real-world projects with industry datasets'},
      {icon: 'FaCertificate', title: 'Certificate', description: 'Get recognized certificate upon completion'},
      {icon: 'FaHeadset', title: '24/7 Support', description: 'Round-the-clock doubt resolution'}
    ],
    eligibility: `This course is ideal for:
- Beginners with no prior programming experience
- Working professionals looking to switch to Data Science
- IT professionals wanting to add AI/ML skills
- Engineering and Science graduates
- Business analysts wanting to learn predictive modeling

No prior coding experience required. Basic computer knowledge is sufficient.`,
    target_audience: `Who should take this course:
- Fresh graduates looking for a high-paying tech career
- Working professionals in non-tech roles wanting to transition to Data Science
- Software developers wanting to add AI/ML skills
- Business analysts who want to make data-driven decisions
- Anyone interested in artificial intelligence and machine learning`,
    faq: [
      {question: 'Do I need prior coding experience?', answer: 'No, this course starts from basics. We have dedicated Python modules for beginners.'},
      {question: 'What is the course duration?', answer: '6 months with weekday and weekend batch options. Lifetime access to course materials.'},
      {question: 'Are there any prerequisites?', answer: 'Basic mathematical knowledge (class 10 level) is sufficient. No prior programming needed.'},
      {question: 'Do you provide job assistance?', answer: 'Yes, we provide resume building, mock interviews, and have tie-ups with 200+ hiring partners.'},
      {question: 'Can I learn at my own pace?', answer: 'Yes, we provide self-paced learning option with lifetime access to all course materials.'},
      {question: 'What tools will I learn?', answer: 'Python, NumPy, Pandas, Scikit-learn, TensorFlow, Keras, NLP, Computer Vision, SQL, and deployment tools.'},
      {question: 'Is the certificate recognized?', answer: 'Yes, our certificates are recognized by top companies and can be showcased on LinkedIn.'},
      {question: 'Do you offer EMI options?', answer: 'Yes, we offer easy EMI options starting at affordable monthly installments.'},
      {question: 'What kind of projects will I work on?', answer: '18+ projects including house price prediction, fraud detection, recommendation systems, face recognition, and more.'},
      {question: 'How is the course delivered?', answer: 'Live instructor-led online sessions with practical hands-on exercises and assignments.'},
      {question: 'What is the average salary after this course?', answer: 'Our students typically get 40-150% salary hike. Average starting salary is ₹5-12 LPA for freshers.'},
      {question: 'Can I switch careers after this course?', answer: 'Yes, many students have successfully transitioned from non-tech roles to Data Science and AI.'},
      {question: 'Is the content updated?', answer: 'Yes, our curriculum is regularly updated to include latest industry trends and technologies.'},
      {question: 'What support is available?', answer: '24/7 support through chat, email, and live sessions. Dedicated TA support for doubt resolution.'},
      {question: 'Do I need to buy any software?', answer: 'No, all tools used are free. We provide access to Jupyter notebooks and Google Colab.'}
    ],
    exam_code: 'DS-001',
    exam_questions: 'Maximum 90 Questions',
    exam_format: 'Multiple Choice and Performance-Based',
    exam_duration: '90 Minutes',
    exam_passing_score: '750 (on a scale of 100-900)',
    exam_languages: 'English, Japanese, Portuguese, Spanish',
    courseObjectives: [
      'Develop a comprehensive understanding of foundational security concepts and principles that serve as the cornerstone of cybersecurity.',
      'Learn to identify, assess, and mitigate various threats, vulnerabilities, and risks that can compromise the security of digital environments.',
      'Master the principles and practices of designing, implementing, and managing a robust security architecture that can withstand diverse cyber threats.',
      'Gain expertise in day-to-day security operations, including incident response, monitoring, and safeguarding critical assets.',
      'Acquire the knowledge and skills required to oversee and manage a security program effectively, ensuring compliance, governance, and the protection of valuable data.'
    ]
  },
  // ... other courses
];

export default coursesDetailData;