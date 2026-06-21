import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import {
  FaDatabase,
  FaCloud,
  FaShieldAlt,
  FaCode,
  FaBullhorn,
  FaChartBar,
  FaPaintBrush,
  FaMobileAlt,
  FaArrowRight,
  FaStar,
  FaClock,
  FaBookOpen,
  FaLaptopCode,
  FaRobot,
  FaSearch,
  FaTimes,
  FaFilter,
  FaSpinner
} from 'react-icons/fa';

const iconMap = {
  FaDatabase: <FaDatabase />,
  FaCloud: <FaCloud />,
  FaShieldAlt: <FaShieldAlt />,
  FaCode: <FaCode />,
  FaBullhorn: <FaBullhorn />,
  FaChartBar: <FaChartBar />,
  FaPaintBrush: <FaPaintBrush />,
  FaMobileAlt: <FaMobileAlt />,
  FaBookOpen: <FaBookOpen />,
  FaLaptopCode: <FaLaptopCode />,
  FaRobot: <FaRobot />
};

const Courses = () => {
  const [showAll, setShowAll] = useState(false);
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [activeFilter, setActiveFilter] = useState('all');
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL ? `${process.env.REACT_APP_API_URL}/api/courses` : '/api/courses';
    fetch(apiUrl)
      .then(res => {
        if (!res.ok) throw new Error('API not available');
        return res.json();
      })
      .then(data => {
        if (data && data.length > 0) {
          const mapped = data.map(c => ({
            icon: iconMap[c.icon] || <FaBookOpen />,
            title: c.title,
            description: c.description,
            description_html: c.description_html || '',
            image: c.image,
            slug: c.slug,
            price: c.price ? `$${c.price}` : '$0',
            originalPrice: c.originalPrice ? `$${c.originalPrice}` : '$0',
            rating: c.rating || 4.5,
            reviews: c.reviews || 0,
            learners: c.learners || '0',
            duration: c.duration || '',
            level: c.level || 'Beginner',
            tag: c.tag || '',
            category: c.category || '',
            modules: c.modules || 0,
            projects: c.projects || 0,
            instructor: c.instructor || {},
            curriculum: c.curriculum || []
          }));
          setCourses(mapped);
          const cats = [...new Set(mapped.filter(c => c.category).map(c => c.category))];
          setCategories(cats);
        }
        setLoading(false);
      })
      .catch(err => {
        console.log('API error:', err.message);
        setLoading(false);
      });
  }, []);

  // Filter and search logic
  const filteredCourses = courses.filter(course => {
    const matchesSearch = !searchQuery.trim() ||
      course.title?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.description?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.level?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.tag?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.duration?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.category?.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesFilter = activeFilter === 'all' ||
      course.level?.toLowerCase().includes(activeFilter.toLowerCase()) ||
      course.category?.toLowerCase() === activeFilter.toLowerCase();

    return matchesSearch && matchesFilter;
  });

  const displayedCourses = showAll ? filteredCourses : filteredCourses.slice(0, 12);

  const allFilterOptions = [
    { key: 'all', label: 'All Courses' },
    { key: 'Beginner', label: 'Beginner' },
    { key: 'Intermediate', label: 'Intermediate' },
    { key: 'Advanced', label: 'Advanced' },
    ...categories.map(cat => ({ key: cat, label: cat })),
  ];

  const getDiscount = (price, original) => {
    const p = parseInt(price.replace(/[₹$,]/g, ''));
    const o = parseInt(original.replace(/[₹$,]/g, ''));
    return Math.round(((o - p) / o) * 100);
  };

  return (
    <section className="tp-courses" id="courses">
      <div className="section-header">
        <span className="section-badge">Professional Certification Courses</span>
        <h2 className="section-title">
          Explore Our <span>Courses</span>
        </h2>
        <p className="section-description">
          Industry-designed courses with placement assistance, live sessions, and
          certifications recognized worldwide.
        </p>
      </div>

      {/* Search & Filter Bar */}
      <div className="tp-courses-search-bar">
        <div className="tp-search-input-wrap">
          <FaSearch className="tp-search-icon" />
          <input
            type="text"
            placeholder="Search courses by name, topic, or level..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="tp-search-input"
          />
          {searchQuery && (
            <button className="tp-search-clear" onClick={() => setSearchQuery('')}>
              <FaTimes />
            </button>
          )}
        </div>
        <div className="tp-filter-buttons">
          <FaFilter className="tp-filter-icon" />
          {allFilterOptions.map(opt => (
            <button
              key={opt.key}
              className={`tp-filter-btn ${activeFilter === opt.key ? 'active' : ''}`}
              onClick={() => setActiveFilter(opt.key)}
            >
              {opt.label}
            </button>
          ))}
        </div>
      </div>

      {/* Results count */}
      {searchQuery && (
        <div className="tp-search-results-count">
          {filteredCourses.length} course{filteredCourses.length !== 1 ? 's' : ''} found
          {searchQuery && <> for "<strong>{searchQuery}</strong>"</>}
        </div>
      )}

      {loading ? (
        <div style={{ textAlign: 'center', padding: '3rem', color: '#94a3b8' }}>
          <FaSpinner style={{ fontSize: '2rem', animation: 'spin 1s linear infinite' }} />
          <p style={{ marginTop: '1rem' }}>Loading courses...</p>
        </div>
      ) : filteredCourses.length > 0 ? (
        <div className="tp-courses-grid">
          {displayedCourses.map((course, index) => (
            <Link to={`/courses/${course.slug}`} className="tp-course-card" key={index}>
              <div className="tp-course-img">
                <img src={course.image} alt={course.title} />
                {course.tag && <span className="tp-course-badge" data-tag={course.tag}>{course.tag}</span>}
                {course.category && <span className="tp-course-badge" style={{background:'#0066cc',right: course.tag ? '90px' : '12px'}}>{course.category}</span>}
                <span className="tp-course-discount">{getDiscount(course.price, course.originalPrice)}% OFF</span>
              </div>
              <div className="tp-course-body">
                <div className="tp-course-top">
                  <span className="tp-course-level">{course.level}</span>
                  <span className="tp-course-duration"><FaClock /> {course.duration}</span>
                </div>
                <h3 className="tp-course-title">{course.title}</h3>
                <p className="tp-course-desc">{(course.description_html || course.description).replace(/<[^>]*>/g, '')}</p>
                
                <div className="tp-course-bottom">
                  <div className="tp-course-rating">
                    <FaStar className="tp-star" />
                    <strong>{course.rating}</strong>
                    <span>({course.reviews.toLocaleString()})</span>
                  </div>
                  <div className="tp-course-pricing">
                    <span className="tp-course-price">{course.price}</span>
                    <span className="tp-course-original">{course.originalPrice}</span>
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      ) : (
        <div className="tp-no-courses">
          <FaSearch style={{fontSize: '2.5rem', color: '#ccc', marginBottom: '1rem'}} />
          <h3>No courses found</h3>
          <p>Try adjusting your search or filter to find what you're looking for.</p>
          <button className="btn-primary" onClick={() => { setSearchQuery(''); setActiveFilter('all'); }}>
            Clear Filters <FaTimes />
          </button>
        </div>
      )}

      {!showAll && filteredCourses.length > 4 && (
        <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
          <button className="btn-primary" onClick={() => setShowAll(true)}>
            View All Courses <FaArrowRight />
          </button>
        </div>
      )}

      {showAll && filteredCourses.length > 4 && (
        <div style={{ textAlign: 'center', marginTop: '2.5rem' }}>
          <button className="btn-primary" onClick={() => setShowAll(false)}>
            Show Less
          </button>
        </div>
      )}
    </section>
  );
};

export default Courses;
