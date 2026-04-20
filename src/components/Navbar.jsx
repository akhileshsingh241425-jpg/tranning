import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaChevronDown, FaPhone } from 'react-icons/fa';
import logo from '../assets/fevicon.png';

const courseCategories = [
  { name: 'Data Science & AI', slug: 'data-science-ai' },
  { name: 'Cloud Computing & DevOps', slug: 'cloud-computing-devops' },
  { name: 'Cyber Security', slug: 'cyber-security' },
  { name: 'Web Development', slug: 'web-development' },
  { name: 'Digital Marketing', slug: 'digital-marketing' },
  { name: 'Business Analytics', slug: 'business-analytics' },
  { name: 'UI/UX Design', slug: 'ui-ux-design' },
  { name: 'Mobile App Development', slug: 'mobile-app-development' },
];

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [coursesDropdown, setCoursesDropdown] = useState(false);
  const location = useLocation();
  const isHome = location.pathname === '/';

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleNavClick = (hash) => {
    setMobileMenuOpen(false);
    setCoursesDropdown(false);
    if (!isHome) {
      window.location.href = '/' + hash;
    }
  };

  return (
    <>
      {/* Top Bar */}
      <div className="nav-top-bar">
        <div className="nav-top-content">
          <span className="nav-top-text">Upskill with industry-recognized certifications | <strong>Placement Assistance</strong> included</span>
          <div className="nav-top-right">
            <a href="tel:+919773983859" className="nav-top-phone"><FaPhone /> +91 97739 83859</a>
          </div>
        </div>
      </div>

      <nav className={`navbar ${scrolled ? 'scrolled' : ''}`}>
        <Link to="/" className="nav-logo">
          <img src={logo} alt="TrainingProtec" className="logo-img" />
          <span className="logo-text">TrainingProtec</span>
        </Link>

        <ul className={`nav-links ${mobileMenuOpen ? 'active' : ''}`}>
          <li><a href={isHome ? '#home' : '/#home'} onClick={() => handleNavClick('#home')}>Home</a></li>
          <li 
            className="nav-dropdown-container"
            onMouseEnter={() => setCoursesDropdown(true)}
            onMouseLeave={() => setCoursesDropdown(false)}
          >
            <a href={isHome ? '#courses' : '/#courses'} onClick={() => handleNavClick('#courses')}>
              Courses <FaChevronDown className="dropdown-arrow" />
            </a>
            {coursesDropdown && (
              <div className="nav-dropdown">
                <div className="nav-dropdown-grid">
                  {courseCategories.map((cat, index) => (
                    <Link 
                      key={index} 
                      to={`/courses/${cat.slug}`} 
                      className="nav-dropdown-item"
                      onClick={() => { setCoursesDropdown(false); setMobileMenuOpen(false); }}
                    >
                      {cat.name}
                    </Link>
                  ))}
                </div>
                <div className="nav-dropdown-footer">
                  <a href={isHome ? '#courses' : '/#courses'} onClick={() => { setCoursesDropdown(false); handleNavClick('#courses'); }}>
                    View All Courses →
                  </a>
                </div>
              </div>
            )}
          </li>
          <li><a href={isHome ? '#about' : '/#about'} onClick={() => handleNavClick('#about')}>About</a></li>
          <li><a href={isHome ? '#blog' : '/#blog'} onClick={() => handleNavClick('#blog')}>Blog</a></li>
          <li><a href={isHome ? '#contact' : '/#contact'} onClick={() => handleNavClick('#contact')}>Contact</a></li>
        </ul>

        <div className="nav-right">
          <a href={isHome ? '#courses' : '/#courses'} style={{textDecoration:'none'}}>
            <button className="nav-cta">Explore Courses</button>
          </a>
        </div>

        <div 
          className="mobile-menu-btn" 
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          <span></span>
          <span></span>
          <span></span>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
