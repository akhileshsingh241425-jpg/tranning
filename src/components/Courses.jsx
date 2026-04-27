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
  FaUsers,
  FaClock,
  FaBookOpen,
  FaChalkboardTeacher,
  FaPercent,
  FaLaptopCode,
  FaCertificate,
  FaRobot,
  FaSearch,
  FaTimes,
  FaFilter
} from 'react-icons/fa';
import courseDataAnalytics from '../assets/images/courses/data-analytics.jpg';
import courseNetworkSecurity from '../assets/images/courses/network-security.jpg';
import courseCybersecurity from '../assets/images/courses/cybersecurity.jpg';
import courseWebDev from '../assets/images/courses/web-development.jpg';
import courseDigitalMarketing from '../assets/images/courses/digital-marketing.jpg';
import courseGraphicDesign from '../assets/images/courses/graphic-design.jpg';
import courseMobileApp from '../assets/images/courses/mobile-app.jpg';
import person1 from '../assets/images/testimonials/person-1.jpg';
import person2 from '../assets/images/testimonials/person-2.jpg';
import person3 from '../assets/images/testimonials/person-3.jpg';
import person4 from '../assets/images/testimonials/person-4.jpg';
import person5 from '../assets/images/testimonials/person-5.jpg';
import person6 from '../assets/images/testimonials/person-6.jpg';

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

const fallbackCourses = [
  {
    icon: <FaDatabase />,
    title: "Data Science & AI",
    description: "Master Python, Machine Learning, Deep Learning & AI with hands-on projects. Build real-world models using TensorFlow, scikit-learn & pandas. Includes capstone project with industry dataset.",
    image: courseDataAnalytics,
    slug: "data-science-ai",
    price: "₹16,999",
    originalPrice: "₹49,999",
    rating: 4.8,
    reviews: 2840,
    learners: "12,500+",
    duration: "6 Months",
    level: "Beginner to Advanced",
    tag: "Bestseller",
    modules: 12,
    projects: 15,
    instructor: {
      name: "Dr. Amit Sharma",
      role: "Ex-Google AI Engineer | IIT Delhi",
      image: person2,
      experience: "14+ years"
    },
    curriculum: ["Python & Statistics", "Machine Learning", "Deep Learning & NLP", "AI with TensorFlow"]
  },
  {
    icon: <FaCloud />,
    title: "Cloud Computing & DevOps",
    description: "Learn AWS, Azure, Docker, Kubernetes & CI/CD pipelines. Deploy real applications to the cloud. Includes AWS Solutions Architect certification prep.",
    image: courseNetworkSecurity,
    slug: "cloud-computing-devops",
    price: "₹14,999",
    originalPrice: "₹39,999",
    rating: 4.7,
    reviews: 1950,
    learners: "9,800+",
    duration: "5 Months",
    level: "Intermediate",
    tag: "Trending",
    modules: 10,
    projects: 12,
    instructor: {
      name: "Rajesh Menon",
      role: "AWS Certified Solutions Architect | Ex-Amazon",
      image: person4,
      experience: "12+ years"
    },
    curriculum: ["AWS Core Services", "Docker & Kubernetes", "CI/CD Pipelines", "Infrastructure as Code"]
  },
  {
    icon: <FaShieldAlt />,
    title: "Cyber Security",
    description: "Learn ethical hacking, penetration testing, network security & compliance. Hands-on labs with Kali Linux, Metasploit & Burp Suite. CEH certification prep included.",
    image: courseCybersecurity,
    slug: "cyber-security",
    price: "₹15,999",
    originalPrice: "₹44,999",
    rating: 4.8,
    reviews: 1620,
    learners: "7,200+",
    duration: "5 Months",
    level: "Beginner to Advanced",
    tag: "Hot",
    modules: 11,
    projects: 10,
    instructor: {
      name: "Vikash Kumar",
      role: "CISO | CEH, OSCP Certified | IIT Bombay",
      image: person6,
      experience: "16+ years"
    },
    curriculum: ["Network Security Basics", "Ethical Hacking", "Penetration Testing", "Compliance & Forensics"]
  },
  {
    icon: <FaCode />,
    title: "Full Stack Web Development",
    description: "Master MERN Stack — React, Node.js, MongoDB, Express. Build 10+ real-world projects including an e-commerce platform, social media app & REST APIs.",
    image: courseWebDev,
    slug: "web-development",
    price: "₹12,999",
    originalPrice: "₹39,999",
    rating: 4.9,
    reviews: 3200,
    learners: "15,000+",
    duration: "6 Months",
    level: "Beginner to Advanced",
    tag: "Bestseller",
    modules: 14,
    projects: 12,
    instructor: {
      name: "Priya Nair",
      role: "Senior Developer | Ex-Flipkart | NIT Trichy",
      image: person1,
      experience: "10+ years"
    },
    curriculum: ["HTML, CSS & JavaScript", "React & Redux", "Node.js & Express", "MongoDB & Deployment"]
  },
  {
    icon: <FaBullhorn />,
    title: "Digital Marketing",
    description: "Master SEO, Google Ads, Social Media Marketing, Analytics & Content Strategy. Run real campaigns with Google Ad credits. Google certified program.",
    image: courseDigitalMarketing,
    slug: "digital-marketing",
    price: "₹9,999",
    originalPrice: "₹29,999",
    rating: 4.7,
    reviews: 2100,
    learners: "18,000+",
    duration: "4 Months",
    level: "Beginner",
    tag: "Popular",
    modules: 8,
    projects: 6,
    instructor: {
      name: "Sneha Patel",
      role: "CMO | Ex-HubSpot | Google Certified Trainer",
      image: person5,
      experience: "11+ years"
    },
    curriculum: ["SEO & Content Marketing", "Google Ads & PPC", "Social Media Strategy", "Analytics & Reporting"]
  },
  {
    icon: <FaChartBar />,
    title: "Business Analytics",
    description: "Learn Excel, SQL, Tableau, Power BI & statistical analysis. Work on real business datasets from top companies. Make data-driven decisions like a pro.",
    image: courseDataAnalytics,
    slug: "business-analytics",
    price: "₹11,999",
    originalPrice: "₹34,999",
    rating: 4.6,
    reviews: 1450,
    learners: "8,500+",
    duration: "4 Months",
    level: "Beginner to Intermediate",
    tag: "New",
    modules: 9,
    projects: 8,
    instructor: {
      name: "Dr. Sanjay Mehta",
      role: "Analytics Lead | Ex-Deloitte | ISB Hyderabad",
      image: person2,
      experience: "15+ years"
    },
    curriculum: ["Excel Advanced", "SQL for Analytics", "Tableau & Power BI", "Statistical Modeling"]
  },
  {
    icon: <FaPaintBrush />,
    title: "UI/UX Design",
    description: "Master Figma, wireframing, prototyping & user research. Build a professional 10+ piece design portfolio. Includes real client projects & design sprints.",
    image: courseGraphicDesign,
    slug: "ui-ux-design",
    price: "₹10,999",
    originalPrice: "₹32,999",
    rating: 4.8,
    reviews: 1180,
    learners: "6,200+",
    duration: "4 Months",
    level: "Beginner",
    tag: "Trending",
    modules: 8,
    projects: 10,
    instructor: {
      name: "Anita Desai",
      role: "Design Lead | Ex-Swiggy | NID Ahmedabad",
      image: person3,
      experience: "9+ years"
    },
    curriculum: ["Design Thinking", "Figma & Prototyping", "User Research", "Design Systems"]
  },
  {
    icon: <FaMobileAlt />,
    title: "Mobile App Development",
    description: "Build iOS & Android apps with React Native & Flutter. Publish to App Store & Google Play. Includes backend integration with Firebase & real-time features.",
    image: courseMobileApp,
    slug: "mobile-app-development",
    price: "₹14,999",
    originalPrice: "₹39,999",
    rating: 4.7,
    reviews: 980,
    learners: "5,400+",
    duration: "5 Months",
    level: "Intermediate",
    tag: "Popular",
    modules: 10,
    projects: 8,
    instructor: {
      name: "Karan Singh",
      role: "Mobile Lead | Ex-Paytm | BITS Pilani",
      image: person4,
      experience: "10+ years"
    },
    curriculum: ["React Native Basics", "Flutter Development", "Firebase & APIs", "App Store Deployment"]
  }
];

const Courses = () => {
  const [showAll, setShowAll] = useState(false);
  const [courses, setCourses] = useState(fallbackCourses);
  const [searchQuery, setSearchQuery] = useState('');
  const [activeFilter, setActiveFilter] = useState('all');

  const filterOptions = [
    { key: 'all', label: 'All Courses' },
    { key: 'Beginner', label: 'Beginner' },
    { key: 'Intermediate', label: 'Intermediate' },
    { key: 'Advanced', label: 'Advanced' },
  ];

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL || ''}/api/courses`)
      .then(res => res.ok ? res.json() : Promise.reject())
      .then(data => {
        if (data && data.length > 0) {
          const mapped = data.map(c => ({
            icon: iconMap[c.icon] || <FaBookOpen />,
            title: c.title,
            description: c.description,
            image: c.image,
            slug: c.slug,
            price: `₹${c.price}`,
            originalPrice: `₹${c.originalPrice}`,
            rating: c.rating,
            reviews: c.reviews,
            learners: c.learners,
            duration: c.duration,
            level: c.level,
            tag: c.tag,
            modules: c.modules,
            projects: c.projects,
            instructor: c.instructor,
            curriculum: c.curriculum
          }));
          setCourses(mapped);
        }
      })
      .catch(() => {});
  }, []);

  // Filter and search logic
  const filteredCourses = courses.filter(course => {
    const matchesSearch = !searchQuery.trim() ||
      course.title?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.description?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.level?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.tag?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.duration?.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesFilter = activeFilter === 'all' ||
      course.level?.toLowerCase().includes(activeFilter.toLowerCase());

    return matchesSearch && matchesFilter;
  });

  const displayedCourses = showAll ? filteredCourses : filteredCourses.slice(0, 4);

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
          {filterOptions.map(opt => (
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

      {filteredCourses.length > 0 ? (
        <div className="tp-courses-grid">
          {displayedCourses.map((course, index) => (
            <Link to={`/courses/${course.slug}`} className="tp-course-card" key={index}>
              <div className="tp-course-img">
                <img src={course.image} alt={course.title} />
                {course.tag && <span className="tp-course-badge" data-tag={course.tag}>{course.tag}</span>}
                <span className="tp-course-discount">{getDiscount(course.price, course.originalPrice)}% OFF</span>
              </div>
              <div className="tp-course-body">
                <div className="tp-course-top">
                  <span className="tp-course-level">{course.level}</span>
                  <span className="tp-course-duration"><FaClock /> {course.duration}</span>
                </div>
                <h3 className="tp-course-title">{course.title}</h3>
                <p className="tp-course-desc">{course.description}</p>
                
                <div className="tp-course-instructor">
                  <img src={course.instructor.image} alt={course.instructor.name} />
                  <span>{course.instructor.name}</span>
                </div>

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
