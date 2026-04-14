import React from 'react';
import { FaStar, FaArrowUp, FaQuoteLeft } from 'react-icons/fa';
import person1 from '../assets/images/testimonials/person-1.jpg';
import person2 from '../assets/images/testimonials/person-2.jpg';
import person3 from '../assets/images/testimonials/person-3.jpg';
import person4 from '../assets/images/testimonials/person-4.jpg';
import person5 from '../assets/images/testimonials/person-5.jpg';
import person6 from '../assets/images/testimonials/person-6.jpg';

const testimonialsData = [
  {
    content: "After completing the Data Science & AI program, I transitioned from a manual testing role to a Data Analyst position at Deloitte. The placement team was incredibly supportive throughout.",
    author: "Priya Sharma",
    position: "Data Analyst, Deloitte",
    prevRole: "Manual Tester",
    image: person1,
    rating: 5,
    salaryHike: "120%",
    course: "Data Science & AI"
  },
  {
    content: "The Cloud Computing & DevOps course gave me hands-on experience with AWS and Kubernetes. Within 2 months of completion, I received 3 job offers. Now working as a DevOps Engineer at Infosys.",
    author: "Rahul Verma",
    position: "DevOps Engineer, Infosys",
    prevRole: "System Administrator",
    image: person2,
    rating: 5,
    salaryHike: "95%",
    course: "Cloud Computing & DevOps"
  },
  {
    content: "As a non-tech graduate, I was skeptical about learning web development. TrainingProtec's structured approach and live classes made it so easy. Got placed at a startup in Bangalore within a month!",
    author: "Anita Desai",
    position: "Full Stack Developer, TechStartup",
    prevRole: "BBA Graduate (Fresher)",
    image: person3,
    rating: 5,
    salaryHike: "First Job",
    course: "Full Stack Web Development"
  },
  {
    content: "The Cyber Security course is world-class. The hands-on labs with real attack scenarios prepared me better than any theory course. Cleared CEH certification on the first attempt!",
    author: "Vikash Kumar",
    position: "Security Analyst, TCS",
    prevRole: "IT Support Engineer",
    image: person4,
    rating: 5,
    salaryHike: "85%",
    course: "Cyber Security Professional"
  },
  {
    content: "I took the Digital Marketing course to grow my own e-commerce business. Within 3 months, my online revenue tripled. The Google Ads and SEO modules were game-changers.",
    author: "Sneha Patel",
    position: "Founder, ShopEasy.in",
    prevRole: "Offline Retailer",
    image: person5,
    rating: 5,
    salaryHike: "3x Revenue",
    course: "Digital Marketing"
  },
  {
    content: "At age 35, I thought career switching was impossible. TrainingProtec proved me wrong. The Business Analytics course helped me move from operations to a data-driven analytics role at Wipro.",
    author: "Deepak Joshi",
    position: "Business Analyst, Wipro",
    prevRole: "Operations Manager",
    image: person6,
    rating: 5,
    salaryHike: "70%",
    course: "Business Analytics"
  }
];

const Testimonials = () => {
  return (
    <section className="testimonials" id="testimonials">
      <div className="section-header">
        <span className="section-badge">Success Stories</span>
        <h2 className="section-title">
          Career Transformations That <span>Inspire</span>
        </h2>
        <p className="section-description">
          Real stories from real learners who transformed their careers with TrainingProtec.
        </p>
      </div>

      <div className="testimonials-grid">
        {testimonialsData.map((testimonial, index) => (
          <div className="testimonial-card" key={index}>
            <div className="testimonial-hike-badge">
              <FaArrowUp /> {testimonial.salaryHike} {testimonial.salaryHike.includes('%') ? 'Salary Hike' : ''}
            </div>
            <div className="testimonial-course-tag">{testimonial.course}</div>
            <div className="testimonial-content">
              <FaQuoteLeft className="quote-icon" />
              <p>{testimonial.content}</p>
            </div>
            <div className="testimonial-career-path">
              <span className="prev-role">{testimonial.prevRole}</span>
              <FaArrowUp className="career-arrow" />
              <span className="new-role">{testimonial.position}</span>
            </div>
            <div className="testimonial-author">
              <img 
                src={testimonial.image} 
                alt={testimonial.author} 
                className="author-image"
              />
              <div className="author-info">
                <h4>{testimonial.author}</h4>
                <p>{testimonial.position}</p>
              </div>
            </div>
            <div className="testimonial-rating">
              {[...Array(testimonial.rating)].map((_, i) => (
                <FaStar key={i} />
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Testimonials;
