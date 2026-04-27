import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import SEO from './components/SEO';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Courses from './components/Courses';
import CourseDetail from './components/CourseDetail';
import About from './components/About';
import Features from './components/Features';
import Stats from './components/Stats';
import Blog from './components/Blog';
import Testimonials from './components/Testimonials';
import Contact from './components/Contact';
import Footer from './components/Footer';
import Chatbot from './components/Chatbot';
import TermsAndConditions from './components/TermsAndConditions';
import EnquiryInstructor from './components/EnquiryInstructor';
import EnquiryPartnership from './components/EnquiryPartnership';
import EnquiryCareer from './components/EnquiryCareer';
import './App.css';

function HomePage() {
  return (
    <>
      <SEO
        title="IT Certification Training – Data Science, Cloud, Cyber Security & More"
        description="TrainingProtec offers live instructor-led courses in Data Science, Cloud Computing, Cyber Security, Full Stack Development, Digital Marketing & more. Expert trainers, real projects, job assistance."
        keywords="IT training, data science course, cloud computing, cyber security, full stack development, digital marketing, business analytics, UI UX design, mobile app development, online training India"
        canonical="/"
      />
      <Hero />
      <Courses />
      <About />
      <Features />
      <Stats />
      <Testimonials />
      <Blog />
      <Contact />
    </>
  );
}

function App() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  }, []);

  if (loading) {
    return (
      <div className="loader-container">
        <div className="cyber-loader">
          <div className="loader-ring"></div>
          <div className="loader-ring"></div>
          <div className="loader-ring"></div>
          <span className="loader-text">TrainingProtec</span>
        </div>
      </div>
    );
  }

  return (
    <HelmetProvider>
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/courses/:slug" element={<CourseDetail />} />
          <Route path="/terms" element={<TermsAndConditions />} />
          <Route path="/enquiry/instructor" element={<EnquiryInstructor />} />
          <Route path="/enquiry/partnership" element={<EnquiryPartnership />} />
          <Route path="/enquiry/career" element={<EnquiryCareer />} />
        </Routes>
        <Footer />
        <Chatbot />
      </div>
    </Router>
    </HelmetProvider>
  );
}

export default App;
