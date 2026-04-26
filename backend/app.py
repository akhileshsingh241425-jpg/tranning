from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, session, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import json
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'trainingprotec-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduhub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

CORS(app, origins=['http://localhost:3000', 'http://localhost:3005', 'http://147.93.19.87', 'http://147.93.19.87:5050'], supports_credentials=True)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'

# ==================== MODELS ====================

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.String(200))
    is_published = db.Column(db.Boolean, default=True)
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'excerpt': self.excerpt,
            'image_url': self.image_url,
            'author': self.author,
            'category': self.category,
            'tags': self.tags.split(',') if self.tags else [],
            'is_published': self.is_published,
            'views': self.views,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    service = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'service': self.service,
            'message': self.message,
            'is_read': self.is_read,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(200), nullable=False)
    prev_role = db.Column(db.String(200), default='')
    image = db.Column(db.String(500), default='')
    rating = db.Column(db.Integer, default=5)
    salary_hike = db.Column(db.String(50), default='')
    course = db.Column(db.String(200), default='')
    is_published = db.Column(db.Boolean, default=True)
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'author': self.author,
            'position': self.position,
            'prevRole': self.prev_role,
            'image': self.image,
            'rating': self.rating,
            'salaryHike': self.salary_hike,
            'course': self.course,
            'is_published': self.is_published,
            'sort_order': self.sort_order,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(500), nullable=False)
    icon = db.Column(db.String(50), default='FaBookOpen')
    price = db.Column(db.Integer, nullable=False)
    original_price = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, default=4.5)
    reviews = db.Column(db.Integer, default=0)
    learners = db.Column(db.String(50), default='0')
    duration = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(50), default='Beginner')
    tag = db.Column(db.String(50))
    modules = db.Column(db.Integer, default=0)
    projects = db.Column(db.Integer, default=0)
    instructor_name = db.Column(db.String(100), nullable=False)
    instructor_role = db.Column(db.String(200), nullable=False)
    instructor_image = db.Column(db.String(500))
    instructor_experience = db.Column(db.String(50))
    curriculum = db.Column(db.Text)  # comma-separated
    is_published = db.Column(db.Boolean, default=True)
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # ---- Course Detail Page fields ----
    tagline = db.Column(db.String(300), default='')
    hero_image = db.Column(db.String(500), default='')
    overview = db.Column(db.Text, default='')
    key_benefits = db.Column(db.Text, default='')          # newline-separated
    modules_detail = db.Column(db.Text, default='')        # JSON: [{title, description}]
    learning_path = db.Column(db.Text, default='')         # JSON: [{step, title, description}]
    technologies_list = db.Column(db.Text, default='')     # comma-separated
    faq = db.Column(db.Text, default='')                   # JSON: [{question, answer}]
    detail_stats = db.Column(db.Text, default='')          # JSON: [{number, label}]

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'image': self.image,
            'icon': self.icon,
            'price': self.price,
            'originalPrice': self.original_price,
            'rating': self.rating,
            'reviews': self.reviews,
            'learners': self.learners,
            'duration': self.duration,
            'level': self.level,
            'tag': self.tag,
            'modules': self.modules,
            'projects': self.projects,
            'instructor': {
                'name': self.instructor_name,
                'role': self.instructor_role,
                'image': self.instructor_image or '',
                'experience': self.instructor_experience or ''
            },
            'curriculum': [c.strip() for c in self.curriculum.split(',')] if self.curriculum else [],
            'is_published': self.is_published,
            'sort_order': self.sort_order,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    def to_detail_dict(self):
        """Full course details for the detail page"""
        base = self.to_dict()
        base['tagline'] = self.tagline or ''
        base['heroImage'] = self.hero_image or self.image
        base['overview'] = self.overview or ''
        base['keyBenefits'] = [b.strip() for b in self.key_benefits.split('\n') if b.strip()] if self.key_benefits else []
        base['modulesDetail'] = json.loads(self.modules_detail) if self.modules_detail else []
        base['learningPath'] = json.loads(self.learning_path) if self.learning_path else []
        base['technologies'] = [t.strip() for t in self.technologies_list.split(',')] if self.technologies_list else []
        base['faq'] = json.loads(self.faq) if self.faq else []
        base['detailStats'] = json.loads(self.detail_stats) if self.detail_stats else []
        return base

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

# ==================== API ROUTES ====================

@app.route('/api/blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.filter_by(is_published=True).order_by(Blog.created_at.desc()).all()
    return jsonify([blog.to_dict() for blog in blogs])

@app.route('/api/blogs/<slug>', methods=['GET'])
def get_blog(slug):
    blog = Blog.query.filter_by(slug=slug, is_published=True).first_or_404()
    blog.views += 1
    db.session.commit()
    return jsonify(blog.to_dict())

@app.route('/api/blogs/category/<category>', methods=['GET'])
def get_blogs_by_category(category):
    blogs = Blog.query.filter_by(category=category, is_published=True).order_by(Blog.created_at.desc()).all()
    return jsonify([blog.to_dict() for blog in blogs])

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.json
    contact = Contact(
        name=data.get('name'),
        email=data.get('email'),
        phone=data.get('phone'),
        service=data.get('service'),
        message=data.get('message')
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Message sent successfully!'})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    total_blogs = Blog.query.filter_by(is_published=True).count()
    total_views = db.session.query(db.func.sum(Blog.views)).scalar() or 0
    return jsonify({
        'total_blogs': total_blogs,
        'total_views': total_views
    })

# ==================== COURSE API ROUTES ====================

@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = Course.query.filter_by(is_published=True).order_by(Course.sort_order, Course.created_at.desc()).all()
    return jsonify([course.to_dict() for course in courses])

@app.route('/api/courses/<slug>', methods=['GET'])
def get_course(slug):
    course = Course.query.filter_by(slug=slug, is_published=True).first_or_404()
    return jsonify(course.to_detail_dict())

@app.route('/api/courses/search', methods=['GET'])
def search_courses():
    """Search courses by query string and/or filter by level"""
    query = request.args.get('q', '').strip()
    level = request.args.get('level', '').strip()
    
    courses_query = Course.query.filter_by(is_published=True)
    
    if query:
        search_term = f'%{query}%'
        courses_query = courses_query.filter(
            db.or_(
                Course.title.ilike(search_term),
                Course.description.ilike(search_term),
                Course.level.ilike(search_term),
                Course.tag.ilike(search_term),
                Course.duration.ilike(search_term)
            )
        )
    
    if level:
        courses_query = courses_query.filter(Course.level.ilike(f'%{level}%'))
    
    courses = courses_query.order_by(Course.sort_order, Course.created_at.desc()).all()
    return jsonify([course.to_dict() for course in courses])

# ==================== TESTIMONIAL API ROUTES ====================

@app.route('/api/testimonials', methods=['GET'])
def get_testimonials():
    testimonials = Testimonial.query.filter_by(is_published=True).order_by(Testimonial.sort_order, Testimonial.created_at.desc()).all()
    return jsonify([t.to_dict() for t in testimonials])

# ==================== IMAGE UPLOAD ====================

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
@login_required
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': f'File type not allowed. Allowed types: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
    
    # Generate unique filename
    ext = file.filename.rsplit('.', 1)[1].lower()
    unique_name = f"{uuid.uuid4().hex[:12]}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
    file.save(filepath)
    
    # Return the URL path that can be used as the image value
    image_url = f"/static/uploads/{unique_name}"
    return jsonify({'url': image_url, 'filename': unique_name})

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# ==================== ADMIN PANEL ROUTES ====================

@app.route('/admin')
@login_required
def admin_dashboard():
    blogs_count = Blog.query.count()
    contacts_count = Contact.query.filter_by(is_read=False).count()
    courses_count = Course.query.count()
    testimonials_count = Testimonial.query.count()
    total_views = db.session.query(db.func.sum(Blog.views)).scalar() or 0
    recent_blogs = Blog.query.order_by(Blog.created_at.desc()).limit(5).all()
    recent_contacts = Contact.query.order_by(Contact.created_at.desc()).limit(5).all()
    recent_courses = Course.query.order_by(Course.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html',
                         blogs_count=blogs_count,
                         contacts_count=contacts_count,
                         courses_count=courses_count,
                         testimonials_count=testimonials_count,
                         total_views=total_views,
                         recent_blogs=recent_blogs,
                         recent_contacts=recent_contacts,
                         recent_courses=recent_courses)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('admin_dashboard'))
        flash('Invalid username or password', 'error')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

# Blog Management
@app.route('/admin/blogs')
@login_required
def admin_blogs():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('admin/blogs.html', blogs=blogs)

@app.route('/admin/blogs/new', methods=['GET', 'POST'])
@login_required
def admin_blog_new():
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug') or title.lower().replace(' ', '-')
        blog = Blog(
            title=title,
            slug=slug,
            content=request.form.get('content'),
            excerpt=request.form.get('excerpt'),
            image_url=request.form.get('image_url'),
            author=request.form.get('author'),
            category=request.form.get('category'),
            tags=request.form.get('tags'),
            is_published=request.form.get('is_published') == 'on'
        )
        db.session.add(blog)
        db.session.commit()
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('admin_blogs'))
    
    return render_template('admin/blog_form.html', blog=None)

@app.route('/admin/blogs/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_blog_edit(id):
    blog = Blog.query.get_or_404(id)
    
    if request.method == 'POST':
        blog.title = request.form.get('title')
        blog.slug = request.form.get('slug') or blog.title.lower().replace(' ', '-')
        blog.content = request.form.get('content')
        blog.excerpt = request.form.get('excerpt')
        blog.image_url = request.form.get('image_url')
        blog.author = request.form.get('author')
        blog.category = request.form.get('category')
        blog.tags = request.form.get('tags')
        blog.is_published = request.form.get('is_published') == 'on'
        db.session.commit()
        flash('Blog post updated successfully!', 'success')
        return redirect(url_for('admin_blogs'))
    
    return render_template('admin/blog_form.html', blog=blog)

@app.route('/admin/blogs/delete/<int:id>')
@login_required
def admin_blog_delete(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    flash('Blog post deleted successfully!', 'success')
    return redirect(url_for('admin_blogs'))

# Contact Management
@app.route('/admin/contacts')
@login_required
def admin_contacts():
    contacts = Contact.query.order_by(Contact.created_at.desc()).all()
    return render_template('admin/contacts.html', contacts=contacts)

@app.route('/admin/contacts/view/<int:id>')
@login_required
def admin_contact_view(id):
    contact = Contact.query.get_or_404(id)
    contact.is_read = True
    db.session.commit()
    return render_template('admin/contact_view.html', contact=contact)

@app.route('/admin/contacts/delete/<int:id>')
@login_required
def admin_contact_delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!', 'success')
    return redirect(url_for('admin_contacts'))

# Course Management
@app.route('/admin/courses')
@login_required
def admin_courses():
    courses = Course.query.order_by(Course.sort_order, Course.created_at.desc()).all()
    return render_template('admin/courses.html', courses=courses)

@app.route('/admin/courses/new', methods=['GET', 'POST'])
@login_required
def admin_course_new():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        slug = request.form.get('slug', '').strip() or title.lower().replace(' ', '-').replace('&', 'and')
        course = Course(
            title=title,
            slug=slug,
            description=request.form.get('description', ''),
            image=request.form.get('image', ''),
            icon=request.form.get('icon', 'FaBookOpen'),
            price=int(request.form.get('price', 0)),
            original_price=int(request.form.get('original_price', 0)),
            rating=float(request.form.get('rating', 4.5)),
            reviews=int(request.form.get('reviews', 0)),
            learners=request.form.get('learners', '0'),
            duration=request.form.get('duration', ''),
            level=request.form.get('level', 'Beginner'),
            tag=request.form.get('tag', ''),
            modules=int(request.form.get('modules', 0)),
            projects=int(request.form.get('projects', 0)),
            instructor_name=request.form.get('instructor_name', ''),
            instructor_role=request.form.get('instructor_role', ''),
            instructor_image=request.form.get('instructor_image', ''),
            instructor_experience=request.form.get('instructor_experience', ''),
            curriculum=request.form.get('curriculum', ''),
            is_published=request.form.get('is_published') == 'on',
            sort_order=int(request.form.get('sort_order', 0)),
            tagline=request.form.get('tagline', ''),
            hero_image=request.form.get('hero_image', ''),
            overview=request.form.get('overview', ''),
            key_benefits=request.form.get('key_benefits', ''),
            modules_detail=request.form.get('modules_detail', ''),
            learning_path=request.form.get('learning_path', ''),
            technologies_list=request.form.get('technologies_list', ''),
            faq=request.form.get('faq', ''),
            detail_stats=request.form.get('detail_stats', '')
        )
        db.session.add(course)
        db.session.commit()
        flash('Course created successfully!', 'success')
        return redirect(url_for('admin_courses'))

    return render_template('admin/course_form.html', course=None)

@app.route('/admin/courses/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_course_edit(id):
    course = Course.query.get_or_404(id)

    if request.method == 'POST':
        course.title = request.form.get('title', '').strip()
        course.slug = request.form.get('slug', '').strip() or course.title.lower().replace(' ', '-').replace('&', 'and')
        course.description = request.form.get('description', '')
        course.image = request.form.get('image', '')
        course.icon = request.form.get('icon', 'FaBookOpen')
        course.price = int(request.form.get('price', 0))
        course.original_price = int(request.form.get('original_price', 0))
        course.rating = float(request.form.get('rating', 4.5))
        course.reviews = int(request.form.get('reviews', 0))
        course.learners = request.form.get('learners', '0')
        course.duration = request.form.get('duration', '')
        course.level = request.form.get('level', 'Beginner')
        course.tag = request.form.get('tag', '')
        course.modules = int(request.form.get('modules', 0))
        course.projects = int(request.form.get('projects', 0))
        course.instructor_name = request.form.get('instructor_name', '')
        course.instructor_role = request.form.get('instructor_role', '')
        course.instructor_image = request.form.get('instructor_image', '')
        course.instructor_experience = request.form.get('instructor_experience', '')
        course.curriculum = request.form.get('curriculum', '')
        course.is_published = request.form.get('is_published') == 'on'
        course.sort_order = int(request.form.get('sort_order', 0))
        course.tagline = request.form.get('tagline', '')
        course.hero_image = request.form.get('hero_image', '')
        course.overview = request.form.get('overview', '')
        course.key_benefits = request.form.get('key_benefits', '')
        course.modules_detail = request.form.get('modules_detail', '')
        course.learning_path = request.form.get('learning_path', '')
        course.technologies_list = request.form.get('technologies_list', '')
        course.faq = request.form.get('faq', '')
        course.detail_stats = request.form.get('detail_stats', '')
        db.session.commit()
        flash('Course updated successfully!', 'success')
        return redirect(url_for('admin_courses'))

    return render_template('admin/course_form.html', course=course)

@app.route('/admin/courses/delete/<int:id>')
@login_required
def admin_course_delete(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash('Course deleted successfully!', 'success')
    return redirect(url_for('admin_courses'))

# ==================== TESTIMONIAL ADMIN ROUTES ====================

@app.route('/admin/testimonials')
@login_required
def admin_testimonials():
    testimonials = Testimonial.query.order_by(Testimonial.sort_order, Testimonial.created_at.desc()).all()
    return render_template('admin/testimonials.html', testimonials=testimonials)

@app.route('/admin/testimonials/new', methods=['GET', 'POST'])
@login_required
def admin_testimonial_new():
    if request.method == 'POST':
        testimonial = Testimonial(
            content=request.form.get('content', ''),
            author=request.form.get('author', ''),
            position=request.form.get('position', ''),
            prev_role=request.form.get('prev_role', ''),
            image=request.form.get('image', ''),
            rating=int(request.form.get('rating', 5)),
            salary_hike=request.form.get('salary_hike', ''),
            course=request.form.get('course', ''),
            is_published='is_published' in request.form,
            sort_order=int(request.form.get('sort_order', 0))
        )
        db.session.add(testimonial)
        db.session.commit()
        flash('Testimonial created successfully!', 'success')
        return redirect(url_for('admin_testimonials'))
    return render_template('admin/testimonial_form.html', testimonial=None)

@app.route('/admin/testimonials/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_testimonial_edit(id):
    testimonial = Testimonial.query.get_or_404(id)
    if request.method == 'POST':
        testimonial.content = request.form.get('content', '')
        testimonial.author = request.form.get('author', '')
        testimonial.position = request.form.get('position', '')
        testimonial.prev_role = request.form.get('prev_role', '')
        testimonial.image = request.form.get('image', '')
        testimonial.rating = int(request.form.get('rating', 5))
        testimonial.salary_hike = request.form.get('salary_hike', '')
        testimonial.course = request.form.get('course', '')
        testimonial.is_published = 'is_published' in request.form
        testimonial.sort_order = int(request.form.get('sort_order', 0))
        db.session.commit()
        flash('Testimonial updated successfully!', 'success')
        return redirect(url_for('admin_testimonials'))
    return render_template('admin/testimonial_form.html', testimonial=testimonial)

@app.route('/admin/testimonials/delete/<int:id>')
@login_required
def admin_testimonial_delete(id):
    testimonial = Testimonial.query.get_or_404(id)
    db.session.delete(testimonial)
    db.session.commit()
    flash('Testimonial deleted successfully!', 'success')
    return redirect(url_for('admin_testimonials'))

# ==================== INITIALIZE ====================

def create_admin():
    admin = Admin.query.filter_by(username='admin').first()
    if not admin:
        admin = Admin(username='admin', email='admin@eduhub.com')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print('Admin user created: admin / admin123')

def create_sample_blogs():
    if Blog.query.count() == 0:
        blogs = [
            Blog(
                title='10 Best Programming Languages to Learn in 2026',
                slug='best-programming-languages-2026',
                content='''<p>The tech landscape in 2026 continues to evolve rapidly, making it crucial to choose the right programming languages for your career.</p>
                <h3>1. Python</h3>
                <p>Python remains the top choice for beginners and professionals alike, dominating data science, AI, and web development.</p>
                <h3>2. JavaScript</h3>
                <p>JavaScript powers the web and continues to grow with frameworks like React, Vue, and Node.js making it indispensable.</p>
                <h3>3. TypeScript</h3>
                <p>TypeScript adoption has exploded, offering type safety and better tooling for large-scale applications.</p>
                <h3>4. Rust</h3>
                <p>Rust is gaining momentum for systems programming, offering memory safety without a garbage collector.</p>
                <h3>5. Go</h3>
                <p>Go is perfect for cloud services and microservices, valued for its simplicity and excellent concurrency support.</p>''',
                excerpt='Discover the most in-demand programming languages that can boost your career and open new opportunities in tech.',
                image_url='https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80',
                author='Prof. Amit Kumar',
                category='Programming',
                tags='programming,career,2026,languages',
                is_published=True
            ),
            Blog(
                title='How to Build a Learning Routine That Sticks',
                slug='build-learning-routine',
                content='''<p>Building a consistent learning routine is the key to mastering new skills. Here are science-backed strategies.</p>
                <h3>The 20-Minute Rule</h3>
                <p>Research shows that just 20 minutes of focused daily practice is more effective than hours of sporadic study.</p>
                <h3>Active Recall</h3>
                <p>Instead of re-reading notes, test yourself. Active recall strengthens neural pathways and improves long-term retention.</p>
                <h3>Spaced Repetition</h3>
                <p>Review material at increasing intervals to move knowledge from short-term to long-term memory.</p>
                <h3>Project-Based Learning</h3>
                <p>Apply what you learn by building real projects. This contextualizes knowledge and builds your portfolio.</p>''',
                excerpt='Science-backed strategies to create a consistent study habit and maximize your learning retention.',
                image_url='https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80',
                author='Dr. Meera Joshi',
                category='Study Tips',
                tags='study-tips,productivity,habits,learning',
                is_published=True
            ),
            Blog(
                title='The Rise of AI in Education',
                slug='ai-in-education',
                content='''<p>AI is revolutionizing education in ways we never imagined, personalized learning to intelligent tutoring.</p>
                <h3>Personalized Learning Paths</h3>
                <p>AI algorithms can adapt course content to each student's pace and learning style.</p>
                <h3>AI Tutors</h3>
                <p>Virtual AI tutors provide 24/7 support, answering questions and explaining concepts in real-time.</p>
                <h3>Automated Assessment</h3>
                <p>AI-powered grading saves time and provides instant feedback to students.</p>
                <h3>The Future</h3>
                <p>As AI continues to evolve, education will become more accessible and effective for everyone.</p>''',
                excerpt='Explore how artificial intelligence is transforming the way we learn and teach in 2026 and beyond.',
                image_url='https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80',
                author='Raj Patel',
                category='EdTech',
                tags='AI,edtech,future,education',
                is_published=True
            ),
            Blog(
                title='From Zero to Developer: A Complete Roadmap',
                slug='zero-to-developer-roadmap',
                content='''<p>Starting a career in development can feel overwhelming. This roadmap breaks it down into manageable steps.</p>
                <h3>Month 1-2: Foundations</h3>
                <p>Learn HTML, CSS, and JavaScript basics. Build simple static websites to practice.</p>
                <h3>Month 3-4: Frontend Framework</h3>
                <p>Pick React or Vue and build interactive applications. Learn Git and version control.</p>
                <h3>Month 5-6: Backend & Databases</h3>
                <p>Learn Node.js or Python, understand REST APIs, and work with databases.</p>
                <h3>Month 7-8: Projects & Portfolio</h3>
                <p>Build 3-5 portfolio projects and start applying for junior developer positions.</p>''',
                excerpt='A step-by-step guide to becoming a professional developer, even if you have no prior experience.',
                image_url='https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80',
                author='Vikash Singh',
                category='Career Guide',
                tags='career,development,roadmap,beginner',
                is_published=True
            ),
            Blog(
                title='Top Freelancing Skills to Learn in 2026',
                slug='top-freelancing-skills-2026',
                content='''<p>Freelancing continues to grow as a career choice. Here are the most profitable skills in 2026.</p>
                <h3>Web Development</h3>
                <p>Full-stack development remains the highest-paying freelance skill with rates ranging from $50-150/hour.</p>
                <h3>UI/UX Design</h3>
                <p>Businesses need great design more than ever, making this a lucrative freelancing niche.</p>
                <h3>Data Analysis</h3>
                <p>Companies are willing to pay premium rates for freelancers who can turn data into insights.</p>
                <h3>Digital Marketing</h3>
                <p>SEO, social media, and PPC specialists are in constant demand from businesses of all sizes.</p>''',
                excerpt='The most profitable freelancing skills you can learn online and start earning from home.',
                image_url='https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80',
                author='Neha Gupta',
                category='Freelancing',
                tags='freelancing,skills,remote-work,career',
                is_published=True
            ),
            Blog(
                title='Why Data Science Is the Hottest Career in 2026',
                slug='data-science-career-2026',
                content='''<p>Data science has become one of the most sought-after careers globally.</p>
                <h3>Growing Demand</h3>
                <p>Every industry needs data professionals, from healthcare to finance to e-commerce.</p>
                <h3>High Salaries</h3>
                <p>Data scientists earn an average of $120K+ annually, with senior roles exceeding $200K.</p>
                <h3>Diverse Roles</h3>
                <p>Data analyst, ML engineer, AI researcher — the field offers multiple career paths.</p>
                <h3>Getting Started</h3>
                <p>Learn Python, statistics, and machine learning. Online courses make it accessible to anyone.</p>''',
                excerpt='Data science continues to dominate job markets. Here is why you should consider it and how to get started.',
                image_url='https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80',
                author='Dr. Sanjay Mehta',
                category='Data Science',
                tags='data-science,career,AI,machine-learning',
                is_published=True
            )
        ]
        for blog in blogs:
            db.session.add(blog)
        db.session.commit()
        print('Sample blog posts created!')

def create_sample_courses():
    if Course.query.count() == 0:
        courses = [
            Course(
                title='Data Science & AI',
                slug='data-science-ai',
                description='Master Python, Machine Learning, Deep Learning & AI with hands-on projects. Build real-world models using TensorFlow, scikit-learn & pandas. Includes capstone project with industry dataset.',
                image='https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaDatabase',
                price=15999,
                original_price=45999,
                rating=4.8,
                reviews=2840,
                learners='12,500+',
                duration='6 Months',
                level='Beginner to Advanced',
                tag='Bestseller',
                modules=12,
                projects=15,
                instructor_name='Dr. Amit Sharma',
                instructor_role='Ex-Google AI Engineer | IIT Delhi',
                instructor_image='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                instructor_experience='14+ years',
                curriculum='Python & Statistics, Machine Learning, Deep Learning & NLP, AI with TensorFlow',
                is_published=True,
                sort_order=1
            ),
            Course(
                title='Cloud Computing & DevOps',
                slug='cloud-computing-devops',
                description='Learn AWS, Azure, Docker, Kubernetes & CI/CD pipelines. Deploy real applications to the cloud. Includes AWS Solutions Architect certification prep.',
                image='https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaCloud',
                price=13999,
                original_price=39999,
                rating=4.7,
                reviews=1950,
                learners='9,800+',
                duration='5 Months',
                level='Intermediate',
                tag='Trending',
                modules=10,
                projects=12,
                instructor_name='Rajesh Menon',
                instructor_role='AWS Certified Solutions Architect | Ex-Amazon',
                instructor_image='https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                instructor_experience='12+ years',
                curriculum='AWS Core Services, Docker & Kubernetes, CI/CD Pipelines, Infrastructure as Code',
                is_published=True,
                sort_order=2
            ),
            Course(
                title='Cyber Security',
                slug='cyber-security',
                description='Learn ethical hacking, penetration testing, network security & compliance. Hands-on labs with Kali Linux, Metasploit & Burp Suite. CEH certification prep included.',
                image='https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaShieldAlt',
                price=14999,
                original_price=42999,
                rating=4.8,
                reviews=1620,
                learners='7,200+',
                duration='5 Months',
                level='Beginner to Advanced',
                tag='Hot',
                modules=11,
                projects=10,
                instructor_name='Vikash Kumar',
                instructor_role='CISO | CEH, OSCP Certified | IIT Bombay',
                instructor_image='https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                instructor_experience='16+ years',
                curriculum='Network Security Basics, Ethical Hacking, Penetration Testing, Compliance & Forensics',
                is_published=True,
                sort_order=3
            ),
            Course(
                title='Full Stack Web Development',
                slug='web-development',
                description='Master MERN Stack — React, Node.js, MongoDB, Express. Build 10+ real-world projects including an e-commerce platform, social media app & REST APIs.',
                image='https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaCode',
                price=12999,
                original_price=37999,
                rating=4.9,
                reviews=3200,
                learners='15,000+',
                duration='6 Months',
                level='Beginner to Advanced',
                tag='Bestseller',
                modules=14,
                projects=12,
                instructor_name='Priya Nair',
                instructor_role='Senior Developer | Ex-Flipkart | NIT Trichy',
                instructor_image='https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                instructor_experience='10+ years',
                curriculum='HTML CSS & JavaScript, React & Redux, Node.js & Express, MongoDB & Deployment',
                is_published=True,
                sort_order=4
            ),
            Course(
                title='Digital Marketing',
                slug='digital-marketing',
                description='Master SEO, Google Ads, Social Media Marketing, Analytics & Content Strategy. Run real campaigns with Rs 10000 Google Ad credits. Google certified program.',
                image='https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaBullhorn',
                price=9999,
                original_price=29999,
                rating=4.7,
                reviews=2100,
                learners='18,000+',
                duration='4 Months',
                level='Beginner',
                tag='Popular',
                modules=8,
                projects=6,
                instructor_name='Sneha Patel',
                instructor_role='CMO | Ex-HubSpot | Google Certified Trainer',
                instructor_image='https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                instructor_experience='11+ years',
                curriculum='SEO & Content Marketing, Google Ads & PPC, Social Media Strategy, Analytics & Reporting',
                is_published=True,
                sort_order=5
            ),
            Course(
                title='Business Analytics',
                slug='business-analytics',
                description='Learn Excel, SQL, Tableau, Power BI & statistical analysis. Work on real business datasets from top companies. Make data-driven decisions like a pro.',
                image='https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaChartBar',
                price=11999,
                original_price=34999,
                rating=4.6,
                reviews=1450,
                learners='8,500+',
                duration='4 Months',
                level='Beginner to Intermediate',
                tag='New',
                modules=9,
                projects=8,
                instructor_name='Dr. Sanjay Mehta',
                instructor_role='Analytics Lead | Ex-Deloitte | ISB Hyderabad',
                instructor_image='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                instructor_experience='15+ years',
                curriculum='Excel Advanced, SQL for Analytics, Tableau & Power BI, Statistical Modeling',
                is_published=True,
                sort_order=6
            ),
            Course(
                title='UI/UX Design',
                slug='ui-ux-design',
                description='Master Figma, wireframing, prototyping & user research. Build a professional 10+ piece design portfolio. Includes real client projects & design sprints.',
                image='https://images.unsplash.com/photo-1626785774573-4b799315345d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaPaintBrush',
                price=10999,
                original_price=32999,
                rating=4.8,
                reviews=1180,
                learners='6,200+',
                duration='4 Months',
                level='Beginner',
                tag='Trending',
                modules=8,
                projects=10,
                instructor_name='Anita Desai',
                instructor_role='Design Lead | Ex-Swiggy | NID Ahmedabad',
                instructor_image='https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                instructor_experience='9+ years',
                curriculum='Design Thinking, Figma & Prototyping, User Research, Design Systems',
                is_published=True,
                sort_order=7
            ),
            Course(
                title='Mobile App Development',
                slug='mobile-app-development',
                description='Build iOS & Android apps with React Native & Flutter. Publish to App Store & Google Play. Includes backend integration with Firebase & real-time features.',
                image='https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaMobileAlt',
                price=13999,
                original_price=38999,
                rating=4.7,
                reviews=980,
                learners='5,400+',
                duration='5 Months',
                level='Intermediate',
                tag='Popular',
                modules=10,
                projects=8,
                instructor_name='Karan Singh',
                instructor_role='Mobile Lead | Ex-Paytm | BITS Pilani',
                instructor_image='https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80',
                instructor_experience='10+ years',
                curriculum='React Native Basics, Flutter Development, Firebase & APIs, App Store Deployment',
                is_published=True,
                sort_order=8
            )
        ]
        for course in courses:
            db.session.add(course)
        db.session.commit()
        print('Sample courses created!')

def create_sample_testimonials():
    if Testimonial.query.count() == 0:
        testimonials = [
            Testimonial(
                content="After completing the Data Science & AI program, I transitioned from a manual testing role to a Data Analyst position at Deloitte. The placement team was incredibly supportive throughout.",
                author="Priya Sharma",
                position="Data Analyst, Deloitte",
                prev_role="Manual Tester",
                image="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80",
                rating=5,
                salary_hike="120%",
                course="Data Science & AI",
                is_published=True,
                sort_order=1
            ),
            Testimonial(
                content="The Cloud Computing & DevOps course gave me hands-on experience with AWS and Kubernetes. Within 2 months of completion, I received 3 job offers. Now working as a DevOps Engineer at Infosys.",
                author="Rahul Verma",
                position="DevOps Engineer, Infosys",
                prev_role="System Administrator",
                image="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80",
                rating=5,
                salary_hike="95%",
                course="Cloud Computing & DevOps",
                is_published=True,
                sort_order=2
            ),
            Testimonial(
                content="As a non-tech graduate, I was skeptical about learning web development. TrainingProtec's structured approach and live classes made it so easy. Got placed at a startup in Bangalore within a month!",
                author="Anita Desai",
                position="Full Stack Developer, TechStartup",
                prev_role="BBA Graduate (Fresher)",
                image="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80",
                rating=5,
                salary_hike="First Job",
                course="Full Stack Web Development",
                is_published=True,
                sort_order=3
            ),
            Testimonial(
                content="The Cyber Security course is world-class. The hands-on labs with real attack scenarios prepared me better than any theory course. Cleared CEH certification on the first attempt!",
                author="Vikash Kumar",
                position="Security Analyst, TCS",
                prev_role="IT Support Engineer",
                image="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80",
                rating=5,
                salary_hike="85%",
                course="Cyber Security Professional",
                is_published=True,
                sort_order=4
            ),
            Testimonial(
                content="I took the Digital Marketing course to grow my own e-commerce business. Within 3 months, my online revenue tripled. The Google Ads and SEO modules were game-changers.",
                author="Sneha Patel",
                position="Founder, ShopEasy.in",
                prev_role="Offline Retailer",
                image="https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80",
                rating=5,
                salary_hike="3x Revenue",
                course="Digital Marketing",
                is_published=True,
                sort_order=5
            ),
            Testimonial(
                content="At age 35, I thought career switching was impossible. TrainingProtec proved me wrong. The Business Analytics course helped me move from operations to a data-driven analytics role at Wipro.",
                author="Deepak Joshi",
                position="Business Analyst, Wipro",
                prev_role="Operations Manager",
                image="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80",
                rating=5,
                salary_hike="70%",
                course="Business Analytics",
                is_published=True,
                sort_order=6
            )
        ]
        for testimonial in testimonials:
            db.session.add(testimonial)
        db.session.commit()
        print('Sample testimonials created!')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin()
        create_sample_blogs()
        create_sample_courses()
        create_sample_testimonials()
    app.run(debug=False, host='0.0.0.0', port=5050)
