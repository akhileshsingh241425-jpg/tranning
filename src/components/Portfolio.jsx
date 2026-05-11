import React, { useState } from 'react';
import { FaExternalLinkAlt, FaCode, FaPaintBrush, FaChartLine, FaCamera, FaBullhorn, FaLaptopCode, FaImage, FaExpand, FaTimes, FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import portfolioDigitalMarketing from '../assets/images/portfolio/digital-marketing.jpg';
import portfolioCoding from '../assets/images/portfolio/coding.jpg';
import portfolioDataAnalytics from '../assets/images/portfolio/data-analytics.jpg';
import portfolioContentWriting from '../assets/images/portfolio/content-writing.jpg';
import portfolioGraphicDesign from '../assets/images/portfolio/graphic-design.jpg';
import portfolioSocialMedia from '../assets/images/portfolio/social-media.jpg';
import portfolioCamera from '../assets/images/portfolio/camera.jpg';
import portfolioMobileApp from '../assets/images/portfolio/mobile-app.jpg';
import portfolioAi from '../assets/images/portfolio/ai.jpg';
import portfolioPhotography from '../assets/images/portfolio/photography.jpg';
import portfolioProduct from '../assets/images/portfolio/product.jpg';
import portfolioVideo from '../assets/images/portfolio/video.jpg';
import portfolioSeo from '../assets/images/portfolio/seo.jpg';
import portfolioFood from '../assets/images/portfolio/food.jpg';

const portfolioItems = [
  // Web Development
  {
    id: 1,
    category: 'web-dev',
    title: 'E-Commerce Platform',
    description: 'Full-stack React + Node.js e-commerce site with payment integration built by a student.',
    image: portfolioDigitalMarketing
  },
  {
    id: 2,
    category: 'web-dev',
    title: 'Portfolio Website',
    description: 'A responsive personal portfolio built with React and modern CSS animations.',
    image: portfolioCoding
  },
  {
    id: 3,
    category: 'web-dev',
    title: 'Social Media Dashboard',
    description: 'Real-time analytics dashboard built with React, Chart.js, and REST APIs.',
    image: portfolioDataAnalytics
  },
  {
    id: 4,
    category: 'web-dev',
    title: 'Blog Platform',
    description: 'Full-stack blogging platform with CMS, authentication, and markdown support.',
    image: portfolioContentWriting
  },
  // Graphic Design
  {
    id: 5,
    category: 'design',
    title: 'Brand Identity Package',
    description: 'Complete brand system with logo, color palette, and guidelines for a startup.',
    image: portfolioGraphicDesign
  },
  {
    id: 6,
    category: 'design',
    title: 'Social Media Campaign',
    description: 'Visually cohesive Instagram campaign graphics for a fitness brand.',
    image: portfolioSocialMedia
  },
  {
    id: 7,
    category: 'design',
    title: 'Magazine Layout',
    description: 'Professional magazine spread designed in InDesign with custom typography.',
    image: portfolioCamera
  },
  {
    id: 8,
    category: 'design',
    title: 'Mobile App UI Design',
    description: 'Clean and modern mobile app interface designed in Figma for a health app.',
    image: portfolioMobileApp
  },
  // Data Science
  {
    id: 9,
    category: 'data-science',
    title: 'Predictive Analytics Model',
    description: 'Machine learning model predicting customer churn with 92% accuracy.',
    image: portfolioDataAnalytics
  },
  {
    id: 10,
    category: 'data-science',
    title: 'NLP Sentiment Analyzer',
    description: 'Natural language processing tool analyzing social media sentiment in real-time.',
    image: portfolioAi
  },
  {
    id: 11,
    category: 'data-science',
    title: 'Sales Forecasting Dashboard',
    description: 'Interactive data visualization dashboard with Python and Plotly for sales prediction.',
    image: portfolioDigitalMarketing
  },
  // Photography & Video
  {
    id: 12,
    category: 'photo-video',
    title: 'Portrait Series',
    description: 'Professional portrait photography series with creative lighting and editing.',
    image: portfolioPhotography
  },
  {
    id: 13,
    category: 'photo-video',
    title: 'Product Photography',
    description: 'E-commerce product photography with clean backgrounds and lifestyle shots.',
    image: portfolioProduct
  },
  {
    id: 14,
    category: 'photo-video',
    title: 'Short Film Project',
    description: 'Cinematic short film produced and edited by a student as capstone project.',
    image: portfolioVideo
  },
  // Digital Marketing
  {
    id: 15,
    category: 'marketing',
    title: 'SEO Case Study',
    description: 'Increased organic traffic by 300% in 6 months using SEO strategies learned in course.',
    image: portfolioSeo
  },
  {
    id: 16,
    category: 'marketing',
    title: 'PPC Ad Campaign',
    description: 'Google Ads campaign achieving 5x ROAS for a local business.',
    image: portfolioDigitalMarketing
  },
  // Mobile Development
  {
    id: 17,
    category: 'mobile',
    title: 'Fitness Tracker App',
    description: 'React Native fitness app with workout tracking, stats, and social features.',
    image: portfolioMobileApp
  },
  {
    id: 18,
    category: 'mobile',
    title: 'Food Delivery App',
    description: 'Flutter-based food delivery app with real-time order tracking and payments.',
    image: portfolioFood
  }
];

const categories = [
  { id: 'all', label: 'All Projects', icon: FaImage },
  { id: 'web-dev', label: 'Web Development', icon: FaCode },
  { id: 'design', label: 'Graphic Design', icon: FaPaintBrush },
  { id: 'data-science', label: 'Data Science', icon: FaChartLine },
  { id: 'photo-video', label: 'Photo & Video', icon: FaCamera },
  { id: 'marketing', label: 'Marketing', icon: FaBullhorn },
  { id: 'mobile', label: 'Mobile Apps', icon: FaLaptopCode }
];

const Portfolio = () => {
  const [activeCategory, setActiveCategory] = useState('all');
  const [lightbox, setLightbox] = useState({ isOpen: false, currentIndex: 0 });
  const [visibleCount, setVisibleCount] = useState(12);

  const filteredItems = activeCategory === 'all' 
    ? portfolioItems 
    : portfolioItems.filter(item => item.category === activeCategory);

  const displayedItems = filteredItems.slice(0, visibleCount);

  const openLightbox = (index) => {
    setLightbox({ isOpen: true, currentIndex: index });
    document.body.style.overflow = 'hidden';
  };

  const closeLightbox = () => {
    setLightbox({ isOpen: false, currentIndex: 0 });
    document.body.style.overflow = 'auto';
  };

  const nextImage = () => {
    setLightbox(prev => ({
      ...prev,
      currentIndex: (prev.currentIndex + 1) % filteredItems.length
    }));
  };

  const prevImage = () => {
    setLightbox(prev => ({
      ...prev,
      currentIndex: (prev.currentIndex - 1 + filteredItems.length) % filteredItems.length
    }));
  };

  const loadMore = () => {
    setVisibleCount(prev => prev + 8);
  };

  const handleCategoryChange = (catId) => {
    setActiveCategory(catId);
    setVisibleCount(12);
  };

  return (
    <section className="portfolio" id="portfolio">
      <div className="section-header">
        <span className="section-badge">Portfolio</span>
        <h2 className="section-title">Student <span>Projects</span></h2>
        <p className="section-description">
          Explore {portfolioItems.length}+ amazing projects built by our students across web development, design, data science, and more
        </p>
      </div>

      <div className="portfolio-filters">
        {categories.map(cat => (
          <button
            key={cat.id}
            className={`filter-btn ${activeCategory === cat.id ? 'active' : ''}`}
            onClick={() => handleCategoryChange(cat.id)}
          >
            <cat.icon />
            {cat.label}
            <span className="filter-count">
              {cat.id === 'all' ? portfolioItems.length : portfolioItems.filter(i => i.category === cat.id).length}
            </span>
          </button>
        ))}
      </div>

      <div className="portfolio-grid">
        {displayedItems.map((item, index) => (
          <div className="portfolio-item" key={item.id}>
            <div className="portfolio-image">
              <img src={item.image} alt={item.title} loading="lazy" />
              <div className="portfolio-overlay">
                <span className="portfolio-category">{item.category}</span>
                <h3>{item.title}</h3>
                <p>{item.description}</p>
                <button 
                  className="portfolio-expand"
                  onClick={() => openLightbox(index)}
                >
                  <FaExpand /> View Full
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {visibleCount < filteredItems.length && (
        <div className="portfolio-load-more">
          <button className="btn-load-more" onClick={loadMore}>
            Load More Projects
            <span>({filteredItems.length - visibleCount} remaining)</span>
          </button>
        </div>
      )}

      <div className="portfolio-cta">
        <p>Want to see more of our work?</p>
        <div className="cta-buttons">
          <a 
            href="https://www.behance.net/pbdigitalartwork" 
            target="_blank" 
            rel="noopener noreferrer"
            className="btn-primary"
          >
            Behance Portfolio <FaExternalLinkAlt />
          </a>
          <a 
            href="https://instagram.com/pb.portraits" 
            target="_blank" 
            rel="noopener noreferrer"
            className="btn-secondary"
          >
            Instagram <FaExternalLinkAlt />
          </a>
        </div>
      </div>

      {/* Lightbox Modal */}
      {lightbox.isOpen && (
        <div className="lightbox-overlay" onClick={closeLightbox}>
          <div className="lightbox-content" onClick={e => e.stopPropagation()}>
            <button className="lightbox-close" onClick={closeLightbox}>
              <FaTimes />
            </button>
            <button className="lightbox-nav prev" onClick={prevImage}>
              <FaChevronLeft />
            </button>
            <div className="lightbox-image-container">
              <img 
                src={filteredItems[lightbox.currentIndex]?.image} 
                alt={filteredItems[lightbox.currentIndex]?.title}
              />
              <div className="lightbox-info">
                <span className="lightbox-category">{filteredItems[lightbox.currentIndex]?.category}</span>
                <h3>{filteredItems[lightbox.currentIndex]?.title}</h3>
                <p>{filteredItems[lightbox.currentIndex]?.description}</p>
              </div>
            </div>
            <button className="lightbox-nav next" onClick={nextImage}>
              <FaChevronRight />
            </button>
            <div className="lightbox-counter">
              {lightbox.currentIndex + 1} / {filteredItems.length}
            </div>
          </div>
        </div>
      )}
    </section>
  );
};

export default Portfolio;
