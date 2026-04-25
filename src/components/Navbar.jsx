import React, { useState, useEffect, useRef } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { FaChevronDown, FaEnvelope, FaSearch, FaTimes, FaClock, FaStar, FaArrowRight } from 'react-icons/fa';
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
  const [searchOpen, setSearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [allCourses, setAllCourses] = useState([]);
  const searchInputRef = useRef(null);
  const searchOverlayRef = useRef(null);
  const location = useLocation();
  const isHome = location.pathname === '/';
  const navigate = useNavigate();

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Fetch courses for search
  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL || 'http://147.93.19.87'}/api/courses`)
      .then(res => res.ok ? res.json() : Promise.reject())
      .then(data => {
        if (data && data.length > 0) {
          setAllCourses(data);
        }
      })
      .catch(() => {});
  }, []);

  // Focus input when search opens
  useEffect(() => {
    if (searchOpen && searchInputRef.current) {
      searchInputRef.current.focus();
    }
  }, [searchOpen]);

  // Close search on Escape key
  useEffect(() => {
    const handleEsc = (e) => {
      if (e.key === 'Escape') {
        setSearchOpen(false);
        setSearchQuery('');
        setSearchResults([]);
      }
    };
    window.addEventListener('keydown', handleEsc);
    return () => window.removeEventListener('keydown', handleEsc);
  }, []);

  // Search logic
  useEffect(() => {
    if (!searchQuery.trim()) {
      setSearchResults([]);
      return;
    }
    const q = searchQuery.toLowerCase();
    const filtered = allCourses.filter(c =>
      c.title?.toLowerCase().includes(q) ||
      c.description?.toLowerCase().includes(q) ||
      c.level?.toLowerCase().includes(q) ||
      c.tag?.toLowerCase().includes(q) ||
      c.duration?.toLowerCase().includes(q)
    );
    setSearchResults(filtered.slice(0, 6));
  }, [searchQuery, allCourses]);

  const handleSearchClick = (slug) => {
    setSearchOpen(false);
    setSearchQuery('');
    setSearchResults([]);
    navigate(`/courses/${slug}`);
  };

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
          <span className="nav-top-text">Upskill with industry-recognized certifications</span>
          <div className="nav-top-right">
            <a href="mailto:support@trainingprotec.com" className="nav-top-phone"><FaEnvelope /> support@trainingprotec.com</a>
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
          <button className="nav-search-btn" onClick={() => setSearchOpen(true)} aria-label="Search courses">
            <FaSearch />
          </button>
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

      {/* Search Overlay */}
      {searchOpen && (
        <div className="nav-search-overlay" ref={searchOverlayRef} onClick={(e) => {
          if (e.target === searchOverlayRef.current) {
            setSearchOpen(false);
            setSearchQuery('');
            setSearchResults([]);
          }
        }}>
          <div className="nav-search-modal">
            <div className="nav-search-header">
              <div className="nav-search-input-wrap">
                <FaSearch className="nav-search-input-icon" />
                <input
                  ref={searchInputRef}
                  type="text"
                  placeholder="Search courses... (e.g. Data Science, Cyber Security, Web Dev)"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="nav-search-input"
                />
                {searchQuery && (
                  <button className="nav-search-clear" onClick={() => { setSearchQuery(''); setSearchResults([]); }}>
                    <FaTimes />
                  </button>
                )}
              </div>
              <button className="nav-search-close" onClick={() => { setSearchOpen(false); setSearchQuery(''); setSearchResults([]); }}>
                <FaTimes /> <span>ESC</span>
              </button>
            </div>

            {searchQuery && searchResults.length > 0 && (
              <div className="nav-search-results">
                {searchResults.map((course) => (
                  <div key={course.slug} className="nav-search-result-item" onClick={() => handleSearchClick(course.slug)}>
                    <img src={course.image} alt={course.title} className="nav-search-result-img" />
                    <div className="nav-search-result-info">
                      <h4>{course.title}</h4>
                      <p>{course.description?.substring(0, 80)}...</p>
                      <div className="nav-search-result-meta">
                        {course.level && <span className="nav-search-result-level">{course.level}</span>}
                        {course.duration && <span><FaClock /> {course.duration}</span>}
                        {course.rating && <span><FaStar className="nav-search-star" /> {course.rating}</span>}
                        {course.tag && <span className="nav-search-result-tag">{course.tag}</span>}
                      </div>
                    </div>
                    <FaArrowRight className="nav-search-result-arrow" />
                  </div>
                ))}
              </div>
            )}

            {searchQuery && searchResults.length === 0 && (
              <div className="nav-search-no-results">
                <FaSearch style={{fontSize: '2rem', color: '#ccc', marginBottom: '0.75rem'}} />
                <h4>No courses found</h4>
                <p>Try searching with different keywords like "Data Science", "Cyber Security", or "Web Development"</p>
              </div>
            )}

            {!searchQuery && (
              <div className="nav-search-suggestions">
                <h4>Popular Courses</h4>
                <div className="nav-search-suggestion-chips">
                  {courseCategories.map((cat) => (
                    <Link
                      key={cat.slug}
                      to={`/courses/${cat.slug}`}
                      className="nav-search-chip"
                      onClick={() => { setSearchOpen(false); setSearchQuery(''); setSearchResults([]); }}
                    >
                      {cat.name}
                    </Link>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </>
  );
};

export default Navbar;
