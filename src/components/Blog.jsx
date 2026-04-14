import React, { useState, useEffect } from 'react';
import { FaCalendarAlt, FaUser, FaEye, FaArrowRight, FaTag } from 'react-icons/fa';
import blogCoding from '../assets/images/blog/coding.jpg';
import blogStudy from '../assets/images/blog/study.jpg';
import blogAi from '../assets/images/blog/ai.jpg';
import blogLaptopCode from '../assets/images/blog/laptop-code.jpg';
import teamImg from '../assets/images/about/team.jpg';
import blogDataAnalytics from '../assets/images/blog/data-analytics.jpg';

const Blog = () => {
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedBlog, setSelectedBlog] = useState(null);

  // Sample blogs data (will be replaced by API data when backend is running)
  const sampleBlogs = [
    {
      id: 1,
      title: '10 Best Programming Languages to Learn in 2026',
      slug: 'best-programming-languages-2026',
      excerpt: 'Discover the most in-demand programming languages that can boost your career and open new opportunities in tech.',
      content: '<p>The tech landscape in 2026 continues to evolve rapidly...</p>',
      image_url: blogCoding,
      author: 'Prof. Amit Kumar',
      category: 'Programming',
      tags: ['programming', 'career', '2026'],
      views: 2847,
      created_at: '2026-02-10 10:00:00'
    },
    {
      id: 2,
      title: 'How to Build a Learning Routine That Sticks',
      slug: 'build-learning-routine',
      excerpt: 'Science-backed strategies to create a consistent study habit and maximize your learning retention.',
      content: '<p>Building a consistent learning routine is the key to success...</p>',
      image_url: blogStudy,
      author: 'Dr. Meera Joshi',
      category: 'Study Tips',
      tags: ['study-tips', 'productivity', 'habits'],
      views: 1892,
      created_at: '2026-02-08 14:30:00'
    },
    {
      id: 3,
      title: 'The Rise of AI in Education',
      slug: 'ai-in-education',
      excerpt: 'Explore how artificial intelligence is transforming the way we learn and teach in 2026 and beyond.',
      content: '<p>AI is revolutionizing education in ways we never imagined...</p>',
      image_url: blogAi,
      author: 'Raj Patel',
      category: 'EdTech',
      tags: ['AI', 'edtech', 'future'],
      views: 1654,
      created_at: '2026-02-05 09:15:00'
    },
    {
      id: 4,
      title: 'From Zero to Developer: A Complete Roadmap',
      slug: 'zero-to-developer-roadmap',
      excerpt: 'A step-by-step guide to becoming a professional developer, even if you have no prior experience.',
      content: '<p>Starting a career in development can feel overwhelming...</p>',
      image_url: blogLaptopCode,
      author: 'Vikash Singh',
      category: 'Career Guide',
      tags: ['career', 'development', 'roadmap'],
      views: 2521,
      created_at: '2026-02-01 16:45:00'
    },
    {
      id: 5,
      title: 'Top Freelancing Skills to Learn in 2026',
      slug: 'top-freelancing-skills-2026',
      excerpt: 'The most profitable freelancing skills you can learn online and start earning from home.',
      content: '<p>Freelancing continues to grow as a career choice...</p>',
      image_url: teamImg,
      author: 'Neha Gupta',
      category: 'Freelancing',
      tags: ['freelancing', 'skills', 'remote-work'],
      views: 1789,
      created_at: '2026-01-28 11:20:00'
    },
    {
      id: 6,
      title: 'Why Data Science Is the Hottest Career in 2026',
      slug: 'data-science-career-2026',
      excerpt: 'Data science continues to dominate job markets. Here\'s why you should consider it and how to get started.',
      content: '<p>Data science has become one of the most sought-after careers...</p>',
      image_url: blogDataAnalytics,
      author: 'Dr. Sanjay Mehta',
      category: 'Data Science',
      tags: ['data-science', 'career', 'AI'],
      views: 2023,
      created_at: '2026-01-25 08:00:00'
    }
  ];

  useEffect(() => {
    fetchBlogs();
  }, []);

  const fetchBlogs = async () => {
    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL || 'http://147.93.19.87'}/api/blogs`);
      if (response.ok) {
        const data = await response.json();
        setBlogs(data);
      } else {
        setBlogs(sampleBlogs);
      }
    } catch (error) {
      console.log('Using sample blogs data');
      setBlogs(sampleBlogs);
    }
    setLoading(false);
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'short', 
      day: 'numeric' 
    });
  };

  const openBlogModal = (blog) => {
    setSelectedBlog(blog);
    document.body.style.overflow = 'hidden';
  };

  const closeBlogModal = () => {
    setSelectedBlog(null);
    document.body.style.overflow = 'auto';
  };

  return (
    <section className="blog-section" id="blog">
      <div className="section-header">
        <span className="section-badge">Our Blog</span>
        <h2 className="section-title">
          Latest <span>Articles & Tips</span>
        </h2>
        <p className="section-description">
          Stay updated with the latest learning tips, career advice, and industry insights from our experts.
        </p>
      </div>

      {loading ? (
        <div className="blog-loading">
          <div className="loader-ring"></div>
          <p>Loading articles...</p>
        </div>
      ) : (
        <div className="blog-grid">
          {blogs.map((blog) => (
            <article className="blog-card" key={blog.id}>
              <div className="blog-image">
                <img src={blog.image_url} alt={blog.title} />
                <div className="blog-category">{blog.category}</div>
              </div>
              <div className="blog-content">
                <div className="blog-meta">
                  <span><FaCalendarAlt /> {formatDate(blog.created_at)}</span>
                  <span><FaEye /> {blog.views} views</span>
                </div>
                <h3 className="blog-title">{blog.title}</h3>
                <p className="blog-excerpt">{blog.excerpt}</p>
                <div className="blog-footer">
                  <div className="blog-author">
                    <FaUser />
                    <span>{blog.author}</span>
                  </div>
                  <button 
                    className="blog-read-more"
                    onClick={() => openBlogModal(blog)}
                  >
                    Read More <FaArrowRight />
                  </button>
                </div>
              </div>
            </article>
          ))}
        </div>
      )}

      {/* Blog Modal */}
      {selectedBlog && (
        <div className="blog-modal-overlay" onClick={closeBlogModal}>
          <div className="blog-modal" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={closeBlogModal}>×</button>
            <div className="modal-image">
              <img src={selectedBlog.image_url} alt={selectedBlog.title} />
            </div>
            <div className="modal-content">
              <span className="modal-category">{selectedBlog.category}</span>
              <h2>{selectedBlog.title}</h2>
              <div className="modal-meta">
                <span><FaUser /> {selectedBlog.author}</span>
                <span><FaCalendarAlt /> {formatDate(selectedBlog.created_at)}</span>
                <span><FaEye /> {selectedBlog.views} views</span>
              </div>
              <div className="modal-tags">
                {selectedBlog.tags && selectedBlog.tags.map((tag, index) => (
                  <span key={index} className="tag"><FaTag /> {tag}</span>
                ))}
              </div>
              <div 
                className="modal-body"
                dangerouslySetInnerHTML={{ __html: selectedBlog.content }}
              />
            </div>
          </div>
        </div>
      )}
    </section>
  );
};

export default Blog;
