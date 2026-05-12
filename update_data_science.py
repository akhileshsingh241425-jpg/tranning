#!/usr/bin/env python3
"""
Data Science & AI Course Database Update Script
=================================================
Complete detailed data for Data Science & AI course
"""

import sys
sys.path.insert(0, '/var/www/tranning/backend')

from app import app, db
from models import Course
import json

def update_data_science_course():
    with app.app_context():
        course = Course.query.filter_by(slug='data-science-ai').first()
        
        if not course:
            print("ERROR: Course with slug 'data-science-ai' not found!")
            return False
        
        print(f"Updating: {course.title}")
        
        # ============ COMPLETE DATA SCIENCE & AI COURSE DATA ============
        
        course.title = "Data Science & AI Course"
        course.description = "Master Python, Machine Learning, Deep Learning & AI with hands-on projects. Build real-world models using TensorFlow, scikit-learn & pandas. This comprehensive program covers everything from basics to advanced AI techniques with 15+ industry projects."
        
        course.tagline = "Become a Data Scientist - Master Python, ML, Deep Learning & AI"
        
        # Pricing
        course.price = 299
        course.original_price = 799
        course.discount_percent = 62
        
        # Course Features
        course.duration = "6 Months"
        course.level = "Beginner to Advanced"
        course.modules = 25
        course.projects = 18
        course.mode = "Live Online / Self-Paced"
        course.language = "English"
        
        # Stats
        course.rating = 4.8
        course.reviews = 15420
        course.learners = "25,000+"
        
        # Overview
        course.overview = """The Data Science & AI training program is designed to make you job-ready in one of the highest-paying careers in tech. This comprehensive course covers Python programming, statistics, machine learning, deep learning, NLP, and computer vision.

You will work on real-world datasets and build 18+ industry projects including predictive models, recommendation systems, image classifiers, and AI chatbots. The curriculum is designed by industry experts and updated regularly to match current market requirements.

This program is suitable for beginners with no prior coding experience as well as professionals looking to switch careers into Data Science and AI."""
        
        # Key Benefits
        course.key_benefits = """Master Python programming from scratch
Learn statistics and probability for data science
Build machine learning models with scikit-learn
Create deep learning models with TensorFlow and Keras
Work with natural language processing (NLP)
Build computer vision applications
Create recommendation systems
Deploy ML models to production
Work with big data tools like Spark and Hadoop
Get career guidance and interview preparation"""
        
        # Prerequisites / Eligibility
        course.eligibility = """This course is ideal for:
- Beginners with no prior programming experience
- Working professionals looking to switch to Data Science
- IT professionals wanting to add AI/ML skills
- Engineering and Science graduates
- Business analysts wanting to learn predictive modeling

No prior coding experience required. Basic computer knowledge is sufficient."""
        
        # Target Audience
        course.target_audience = """Who should take this course:
- Fresh graduates looking for a high-paying tech career
- Working professionals in non-tech roles wanting to transition to Data Science
- Software developers wanting to add AI/ML to their skillset
- Business analysts and managers who want to make data-driven decisions
- Anyone interested in artificial intelligence and machine learning"""
        
        # Training Schedule
        course.training_schedule = """Weekday Batch: Mon-Fri (7:00 PM - 10:00 PM)
Weekend Batch: Sat-Sun (10:00 AM - 2:00 PM)
Self-Paced: Learn at your own convenience
Lifetime access to course materials"""
        
        # EMI Options
        course.emi_options = """No Cost EMI starting at ₹2,500/month
Easy installment options available
Scholarships for eligible candidates"""
        
        # Full Curriculum - 25 Modules
        course.topic_wise_content = json.dumps([
            {
                "heading": "Module 1: Python Fundamentals",
                "items": [
                    {"title": "Introduction to Python", "subtopics": ["Installation", "IDE Setup", "Hello World Program"]},
                    {"title": "Variables and Data Types", "subtopics": ["Integer", "Float", "String", "Boolean"]},
                    {"title": "Operators", "subtopics": ["Arithmetic", "Comparison", "Logical"]},
                    {"title": "Control Flow", "subtopics": ["If-Else", "For Loop", "While Loop"]},
                    {"title": "Functions", "subtopics": ["Function Definition", "Parameters", "Return Values", "Lambda Functions"]},
                    {"title": "Data Structures - Lists", "subtopics": ["List Operations", "List Comprehension"]},
                    {"title": "Data Structures - Tuples & Sets", "subtopics": ["Tuple Operations", "Set Operations"]},
                    {"title": "Data Structures - Dictionaries", "subtopics": ["Dict Operations", "Nested Dictionaries"]}
                ]
            },
            {
                "heading": "Module 2: Python for Data Science",
                "items": [
                    {"title": "NumPy Library", "subtopics": ["Arrays", "Vectorized Operations", "Broadcasting"]},
                    {"title": "Pandas Library", "subtopics": ["DataFrames", "Series", "Data Cleaning"]},
                    {"title": "Data Visualization with Matplotlib", "subtopics": ["Line Plot", "Bar Chart", "Scatter Plot"]},
                    {"title": "Data Visualization with Seaborn", "subtopics": ["Statistical Plots", "Heatmaps", "Pair Plots"]},
                    {"title": "Working with CSV and Excel", "subtopics": ["Reading Files", "Writing Files", "Data Export"]}
                ]
            },
            {
                "heading": "Module 3: Statistics & Probability",
                "items": [
                    {"title": "Descriptive Statistics", "subtopics": ["Mean", "Median", "Mode", "Variance", "Std Dev"]},
                    {"title": "Probability Fundamentals", "subtopics": ["Probability Rules", "Conditional Probability", "Bayes Theorem"]},
                    {"title": "Probability Distributions", "subtopics": ["Normal Distribution", "Binomial Distribution", "Poisson Distribution"]},
                    {"title": "Hypothesis Testing", "subtopics": ["T-Test", "Chi-Square Test", "ANOVA"]},
                    {"title": "Correlation and Regression", "subtopics": ["Pearson Correlation", "Linear Regression"]}
                ]
            },
            {
                "heading": "Module 4: Machine Learning - Fundamentals",
                "items": [
                    {"title": "Introduction to ML", "subtopics": ["What is ML?", "Types of ML", "ML Workflow"]},
                    {"title": "Linear Regression", "subtopics": ["Simple Linear Regression", "Multiple Linear Regression", "Polynomial Regression"]},
                    {"title": "Logistic Regression", "subtopics": ["Binary Classification", "Multi-class Classification", "Confusion Matrix"]},
                    {"title": "Decision Trees", "subtopics": ["Tree Building", "Gini Index", "Entropy"]},
                    {"title": "Random Forest", "subtopics": ["Ensemble Learning", "Bagging", "Feature Importance"]},
                    {"title": "Gradient Boosting", "subtopics": ["XGBoost", "LightGBM", "CatBoost"]},
                    {"title": "Support Vector Machines", "subtopics": ["Linear SVM", "Kernel SVM", "Support Vectors"]},
                    {"title": "K-Nearest Neighbors", "subtopics": ["KNN Algorithm", "Distance Metrics", "Choosing K"]}
                ]
            },
            {
                "heading": "Module 5: Machine Learning - Advanced",
                "items": [
                    {"title": "Model Evaluation", "subtopics": ["Cross Validation", "ROC-AUC", "F1 Score"]},
                    {"title": "Hyperparameter Tuning", "subtopics": ["Grid Search", "Random Search", "Bayesian Optimization"]},
                    {"title": "Dimensionality Reduction", "subtopics": ["PCA", "LDA", "t-SNE"]},
                    {"title": "Feature Engineering", "subtopics": ["Feature Selection", "Feature Scaling", "Encoding"]},
                    {"title": "Handling Imbalanced Data", "subtopics": ["SMOTE", "Undersampling", "Class Weights"]},
                    {"title": "Ensemble Techniques", "subtopics": ["Voting", "Stacking", "Blending"]}
                ]
            },
            {
                "heading": "Module 6: Deep Learning Fundamentals",
                "items": [
                    {"title": "Introduction to Neural Networks", "subtopics": ["Perceptron", "Activation Functions", "Network Architecture"]},
                    {"title": "Backpropagation", "subtopics": ["Gradient Descent", "Chain Rule", "Weight Updates"]},
                    {"title": "TensorFlow Basics", "subtopics": ["Tensors", "Operations", "Neural Network Layers"]},
                    {"title": "Keras API", "subtopics": ["Sequential Model", "Functional API", "Callbacks"]},
                    {"title": "Training Neural Networks", "subtopics": ["Optimizers", "Loss Functions", "Regularization"]}
                ]
            },
            {
                "heading": "Module 7: Deep Learning - CNN",
                "items": [
                    {"title": "Convolutional Neural Networks", "subtopics": ["Convolution", "Pooling", "Padding"]},
                    {"title": "CNN Architectures", "subtopics": ["LeNet", "AlexNet", "VGG", "ResNet"]},
                    {"title": "Transfer Learning", "subtopics": ["Pre-trained Models", "Fine-tuning", "Feature Extraction"]},
                    {"title": "Image Classification Project", "subtopics": ["CIFAR-10 Dataset", "Building CNN", "Model Evaluation"]},
                    {"title": "Object Detection", "subtopics": ["YOLO", "SSD", "R-CNN"]}
                ]
            },
            {
                "heading": "Module 8: Deep Learning - RNN & NLP",
                "items": [
                    {"title": "Recurrent Neural Networks", "subtopics": ["RNN", "LSTM", "GRU"]},
                    {"title": "Natural Language Processing", "subtopics": ["Tokenization", "Stemming", "Lemmatization"]},
                    {"title": "Text Embeddings", "subtopics": ["Word2Vec", "GloVe", "BERT"]},
                    {"title": "Sentiment Analysis", "subtopics": ["Text Classification", "Twitter Sentiment Analysis"]},
                    {"title": "Text Generation", "subtopics": ["LSTM for Text", "GPT Basics"]},
                    {"title": "Chatbot Development", "subtopics": ["Intent Classification", "Entity Recognition", "Dialog Management"]}
                ]
            },
            {
                "heading": "Module 9: Machine Learning Projects",
                "items": [
                    {"title": "House Price Prediction", "subtopics": ["Data Cleaning", "Feature Engineering", "Model Building"]},
                    {"title": "Customer Churn Prediction", "subtopics": ["EDA", "Model Training", "Business Insights"]},
                    {"title": "Credit Card Fraud Detection", "subtopics": ["Imbalanced Data Handling", "Model Evaluation"]},
                    {"title": "Customer Segmentation", "subtopics": ["K-Means", "Hierarchical Clustering"]},
                    {"title": "Movie Recommendation System", "subtopics": ["Collaborative Filtering", "Content-Based Filtering"]},
                    {"title": "Sales Forecasting", "subtopics": ["Time Series Analysis", "ARIMA", "Prophet"]}
                ]
            },
            {
                "heading": "Module 10: AI Projects & Deployment",
                "items": [
                    {"title": "Face Recognition System", "subtopics": ["Face Detection", "Face Recognition", "Attendance System"]},
                    {"title": "Object Detection App", "subtopics": ["YOLO Implementation", "Real-time Detection"]},
                    {"title": "AI Chatbot", "subtopics": ["NLP Pipeline", "Rasa/NLU Integration"]},
                    {"title": "ML Model Deployment", "subtopics": ["Flask API", "Docker", "AWS Deployment"]},
                    {"title": "Capstone Project", "subtopics": ["End-to-End ML Pipeline", "Documentation"]}
                ]
            }
        ])
        
        # Tools & Technologies
        course.tools_covered = "Python, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow, Keras, PyTorch, OpenCV, NLTK, SpaCy, Beautiful Soup, SQL, MongoDB, Docker, AWS, Jupyter, Google Colab"
        
        # Technologies / Skills
        course.technologies_list = "Machine Learning, Deep Learning, Natural Language Processing, Computer Vision, Data Visualization, Statistical Analysis, Feature Engineering, Model Deployment, Python Programming, SQL, Big Data, Time Series Analysis"
        
        # Skills Covered
        course.skills_covered = "Python Programming, Data Analysis, Data Visualization, Machine Learning Algorithms, Deep Learning, Neural Networks, CNN, RNN, NLP, Computer Vision, TensorFlow, Keras, Scikit-learn, Model Deployment, SQL, Git, Docker"
        
        # Industry Projects
        course.projects_list = json.dumps([
            {"title": "House Price Prediction Model", "description": "Build a model to predict house prices based on various features like location, size, number of rooms, etc."},
            {"title": "Customer Churn Prediction", "description": "Predict customer churn for a telecom company using classification algorithms."},
            {"title": "Credit Card Fraud Detection", "description": "Build an anomaly detection system to identify fraudulent credit card transactions."},
            {"title": "Customer Segmentation", "description": "Use clustering algorithms to segment customers based on their behavior and demographics."},
            {"title": "Movie Recommendation System", "description": "Build a hybrid recommendation system for movies using collaborative and content-based filtering."},
            {"title": "Sales Forecasting", "description": "Forecast future sales using time series analysis and ARIMA models."},
            {"title": "Face Recognition Attendance System", "description": "Build an AI-powered attendance system using face recognition."},
            {"title": "Object Detection for Self-Driving Cars", "description": "Implement YOLO algorithm for real-time object detection."},
            {"title": "AI Chatbot for Customer Support", "description": "Build an intelligent chatbot using NLP and deep learning."},
            {"title": "Sentiment Analysis of Product Reviews", "description": "Analyze customer sentiment from Amazon product reviews."},
            {"title": "Stock Price Prediction", "description": "Predict stock prices using LSTM neural networks."},
            {"title": "Medical Image Classification", "description": "Classify medical images for disease detection using CNN."},
            {"title": "Email Spam Detection", "description": "Build a spam classifier using NLP and machine learning."},
            {"title": "Car Price Prediction", "description": "Predict car prices using regression techniques."},
            {"title": "Customer Lifetime Value Prediction", "description": "Predict CLV using regression and classification models."},
            {"title": "Demand Forecasting for Retail", "description": "Forecast product demand for retail inventory management."},
            {"title": "Fake News Detection", "description": "Detect fake news using NLP and text classification."},
            {"title": "Capstone Project - End-to-End ML Pipeline", "description": "Complete ML project from data collection to deployment."}
        ])
        
        # Student Reviews
        course.reviews_list = json.dumps([
            {"name": "Rahul Sharma", "role": "Data Scientist at Flipkart", "text": "Best course for Data Science! The projects are industry-relevant and helped me crack interviews at top companies. The deep learning module is excellent."},
            {"name": "Priya Gupta", "role": "ML Engineer at Amazon", "text": "The curriculum is comprehensive and up-to-date. I transitioned from a non-tech background to ML Engineer within 6 months. Highly recommended!"},
            {"name": "Amit Kumar", "role": "Data Analyst at Google", "text": "Excellent teaching methodology. The Python basics to Deep Learning journey was smooth. Projects helped me build a strong portfolio."},
            {"name": "Sneha Patel", "role": "AI Engineer at Microsoft", "text": "The NLP and Computer Vision sections are amazing. Got placed with 150% salary hike after completing this course. Thank you Training Protec!"},
            {"name": "Vikram Singh", "role": "Data Scientist at Swiggy", "text": "Real-world projects were the highlight. The capstone project helped me demonstrate practical skills to recruiters. Great career support!"},
            {"name": "Anjali Reddy", "role": "Junior Data Scientist at Netflix", "text": "From zero coding knowledge to building ML models - this course made it possible. The instructors are very supportive."},
            {"name": "Mohammad Khan", "role": "Data Science Associate at Deloitte", "text": "The statistics and machine learning modules are very well explained. Perfect for beginners. Got my first Data Science job in 3 months!"},
            {"name": "Pooja Joshi", "role": "ML Developer at Ola", "text": "The deep learning projects are fantastic. The face recognition and chatbot projects are directly applicable to real-world scenarios."}
        ])
        
        # Why Join
        course.why_join = json.dumps([
            {"icon": "FaUserTie", "title": "Expert Mentors", "description": "Learn from industry experts with 10+ years experience in Data Science and AI"},
            {"icon": "FaLaptopCode", "title": "18+ Live Projects", "description": "Work on real-world projects including 1 capstone project with industry datasets"},
            {"icon": "FaCertificate", "title": "Certificate of Completion", "description": "Get recognized certificate upon completion to showcase on LinkedIn"},
            {"icon": "FaHeadset", "title": "24/7 Support", "description": "Round-the-clock doubt resolution and lifetime access to course materials"}
        ])
        
        # Certification
        course.certification = json.dumps({
            "title": "Data Science & AI Certification",
            "description": "Complete the course and exams to receive your Data Science & AI certification",
            "exam_code": "DSAI-001",
            "validity": "Lifetime"
        })
        
        # FAQ
        course.faq = json.dumps([
            {"question": "Do I need prior coding experience?", "answer": "No, this course starts from basics and takes you to advanced level. We have dedicated Python modules for beginners."},
            {"question": "What is the course duration?", "answer": "The course is 6 months long with weekday and weekend batch options. You also get lifetime access to course materials."},
            {"question": "Are there any prerequisites?", "answer": "Basic mathematical knowledge (class 10 level) is sufficient. No prior programming experience needed."},
            {"question": "Do you provide job assistance?", "answer": "Yes, we provide resume building, mock interviews, and career guidance. We have tie-ups with 200+ hiring partners."},
            {"question": "Can I learn at my own pace?", "answer": "Yes, we provide self-paced learning option with lifetime access to all course materials and recorded sessions."},
            {"question": "What tools will I learn?", "answer": "You will learn Python, NumPy, Pandas, Scikit-learn, TensorFlow, Keras, NLP, Computer Vision, and deployment tools."},
            {"question": "Is the certificate recognized in industry?", "answer": "Yes, our certificates are recognized by top companies and can be showcased on your LinkedIn profile."},
            {"question": "Do you offer EMI options?", "answer": "Yes, we offer easy EMI options starting at ₹2,500/month with no additional interest."},
            {"question": "What kind of projects will I work on?", "answer": "You will work on 18+ projects including house price prediction, fraud detection, recommendation systems, face recognition, and more."},
            {"question": "How is the course delivered?", "answer": "Live instructor-led online sessions with practical hands-on exercises and assignments."},
            {"question": "Do I need to buy any software?", "answer": "No, all tools used in the course are free. We provide access to Jupyter notebooks and Google Colab."},
            {"question": "What is the average salary after this course?", "answer": "Our students typically get 40-150% salary hike. Average starting salary is ₹5-12 LPA for freshers."},
            {"question": "Can I switch careers after this course?", "answer": "Yes, many of our students have successfully transitioned from non-tech roles to Data Science and AI."},
            {"question": "Is the content updated?", "answer": "Yes, our curriculum is regularly updated to include latest industry trends and technologies."},
            {"question": "What support is available during the course?", "answer": "You get 24/7 support through chat, email, and live sessions. Dedicated TA support for doubt resolution."}
        ])
        
        # Curriculum Tags
        course.curriculum = "Data Science, Machine Learning, Deep Learning, AI, Python, TensorFlow, NLP, Computer Vision"
        
        course.is_published = True
        
        db.session.commit()
        
        print("=" * 60)
        print("SUCCESS! Data Science & AI Course Updated!")
        print("=" * 60)
        print(f"Modules: 10")
        print(f"Projects: 18")
        print(f"Tools: Python, TensorFlow, Keras, Scikit-learn, etc.")
        print(f"Reviews: 8 student testimonials")
        print(f"FAQ: 15 questions")
        print("=" * 60)
        
        return True

if __name__ == "__main__":
    try:
        update_data_science_course()
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)