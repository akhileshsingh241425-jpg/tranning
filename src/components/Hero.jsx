import React, { useState, useEffect } from 'react';
import { FaArrowRight, FaPlay, FaCheckCircle, FaChevronLeft, FaChevronRight, FaStar } from 'react-icons/fa';

const defaultSlides = [
  { url: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1920&q=80', title: 'Data Science' },
  { url: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80', title: 'Cloud & DevOps' },
  { url: 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1920&q=80', title: 'AI & ML' },
  { url: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1920&q=80', title: 'Cyber Security' },
  { url: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1920&q=80', title: 'Full Stack Dev' }
];

const Hero = () => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [slides, setSlides] = useState(defaultSlides);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL ? `${process.env.REACT_APP_API_URL}/api/hero-settings` : '/api/hero-settings';
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        if (data.slides && data.slides.length > 0) {
          setSlides(data.slides);
        }
      })
      .catch(err => console.log('Using default hero slides:', err.message));
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 5000);
    return () => clearInterval(timer);
  }, [slides]);

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % slides.length);
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + slides.length) % slides.length);
  };

  return (
    <section className="hero" id="home">
      {/* Background Slider */}
      <div className="hero-slider-bg">
        {slides.map((slide, index) => (
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

        </div>
      </div>

      {/* Slider Dots */}
      <div className="hero-slider-dots">
        {slides.map((slide, index) => (
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
