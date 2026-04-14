import React, { useState, useEffect } from 'react';
import { FaArrowRight, FaPlay, FaCheckCircle, FaChevronLeft, FaChevronRight, FaStar } from 'react-icons/fa';
import hero1 from '../assets/images/hero/hero-1.jpg';
import hero2 from '../assets/images/hero/hero-2.jpg';
import hero3 from '../assets/images/hero/hero-3.jpg';
import hero4 from '../assets/images/hero/hero-4.jpg';
import hero5 from '../assets/images/hero/hero-5.jpg';

const heroSlides = [
  {
    url: hero1,
    title: "Data Science"
  },
  {
    url: hero2,
    title: "Cloud & DevOps"
  },
  {
    url: hero3,
    title: "AI & ML"
  },
  {
    url: hero4,
    title: "Cyber Security"
  },
  {
    url: hero5,
    title: "Full Stack Dev"
  }
];

const partnerLogos = [
  'IBM', 'Microsoft', 'Google', 'AWS', 'Meta', 'Coursera'
];

const Hero = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % heroSlides.length);
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % heroSlides.length);
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + heroSlides.length) % heroSlides.length);
  };

  return (
    <section className="hero" id="home">
      {/* Background Slider */}
      <div className="hero-slider-bg">
        {heroSlides.map((slide, index) => (
          <div 
            key={index}
            className={`hero-slide ${index === currentSlide ? 'active' : ''}`}
            style={{ backgroundImage: `url(${slide.url})` }}
          />
        ))}
        <div className="hero-overlay"></div>
      </div>

      {/* Slider Controls */}
      <button className="hero-slider-btn prev" onClick={prevSlide}>
        <FaChevronLeft />
      </button>
      <button className="hero-slider-btn next" onClick={nextSlide}>
        <FaChevronRight />
      </button>

      {/* Main Content */}
      <div className="hero-content">
        <div className="hero-text">
          <span className="hero-tagline">
            <FaStar style={{color: '#f59e0b', marginRight: '6px'}} />
            Global Professional Certification Training Platform
          </span>
          
          <h1 className="hero-title">
            Launch Your
            <span className="hero-title-highlight"> Tech Career </span>
            <br/>With Globally Recognized Certifications
          </h1>
          
          <p className="hero-description">
            Master in-demand skills with courses designed by industry experts. 
            Get certified in <strong>Cybersecurity, Cloud, Data Science, Project Management & more</strong>. 
            Flexible learning with personalized training options.
          </p>

          <div className="hero-highlights">
            <span><FaCheckCircle /> Certification Support</span>
            <span><FaCheckCircle /> Live Instructor-Led</span>
            <span><FaCheckCircle /> 1-on-1 Training</span>
          </div>
          
          <div className="hero-buttons">
            <a href="#courses" className="btn-primary">
              Explore Courses <FaArrowRight />
            </a>
            <a href="#contact" className="btn-secondary">
              <FaPlay /> Request Callback
            </a>
          </div>

          <div className="hero-stats">
            <div className="hero-stat">
              <span className="stat-number">150+</span>
              <span className="stat-label">Certifications</span>
            </div>
            <div className="hero-stat">
              <span className="stat-number">50+</span>
              <span className="stat-label">Expert Trainers</span>
            </div>
            <div className="hero-stat">
              <span className="stat-number">10+</span>
              <span className="stat-label">Countries</span>
            </div>
            <div className="hero-stat">
              <span className="stat-number">95%</span>
              <span className="stat-label">Satisfaction Rate</span>
            </div>
          </div>

          <div className="hero-partners">
            <span className="partner-label">Trusted by learners at:</span>
            <div className="partner-logos">
              {partnerLogos.map((logo, index) => (
                <span key={index} className="partner-logo-text">{logo}</span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Slider Dots */}
      <div className="hero-slider-dots">
        {heroSlides.map((slide, index) => (
          <button 
            key={index}
            className={`hero-dot ${index === currentSlide ? 'active' : ''}`}
            onClick={() => setCurrentSlide(index)}
          >
            <span className="dot-label">{slide.title}</span>
          </button>
        ))}
      </div>
    </section>
  );
};

export default Hero;
