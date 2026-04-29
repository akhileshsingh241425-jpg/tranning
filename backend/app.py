from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, session, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import json
import uuid
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

# Load environment variables from .env file (in same directory as app.py)
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'trainingprotec-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eduhub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

# ==================== EMAIL CONFIGURATION ====================
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
SMTP_USERNAME = os.environ.get('SMTP_USERNAME', '')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', '')
SMTP_USE_TLS = os.environ.get('SMTP_USE_TLS', 'true').lower() == 'true'
NOTIFICATION_EMAIL = os.environ.get('NOTIFICATION_EMAIL', 'contact@trainingprotec.com')
SENDER_EMAIL = os.environ.get('SENDER_EMAIL', SMTP_USERNAME)
REMINDER_DAYS = int(os.environ.get('REMINDER_DAYS', '10'))
CRON_SECRET = os.environ.get('CRON_SECRET', '')

# SMTP configuration status (available in all templates)
SMTP_CONFIGURED = bool(SMTP_USERNAME and SMTP_PASSWORD)

@app.context_processor
def inject_smtp_status():
    return {'smtp_configured': SMTP_CONFIGURED}

def send_enquiry_email(data):
    """Send email notification when a new enquiry is submitted."""
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        logger.warning('SMTP credentials not configured. Email notification skipped.')
        return False

    try:
        service_type = data.get('service', 'General Enquiry')

        # Build HTML email body based on enquiry type
        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
            <div style="background: linear-gradient(135deg, #4f46e5, #7c3aed); padding: 20px 30px; border-radius: 10px 10px 0 0;">
                <h2 style="color: #fff; margin: 0;">New {service_type}</h2>
                <p style="color: #e0e7ff; margin: 5px 0 0 0;">TrainingProtec Website Enquiry</p>
            </div>
            <div style="border: 1px solid #e5e7eb; border-top: none; padding: 25px 30px; border-radius: 0 0 10px 10px;">
                <table style="width: 100%; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5; width: 140px;">Name:</td>
                        <td style="padding: 8px 0;">{data.get('name', 'N/A')}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Email:</td>
                        <td style="padding: 8px 0;"><a href="mailto:{data.get('email', '')}" style="color: #4f46e5;">{data.get('email', 'N/A')}</a></td>
                    </tr>
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Phone:</td>
                        <td style="padding: 8px 0;">{data.get('phone', 'N/A')}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Enquiry Type:</td>
                        <td style="padding: 8px 0;">{service_type}</td>
                    </tr>"""

        # Add extra fields based on enquiry type
        if data.get('organization'):
            html_body += f"""
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Organization:</td>
                        <td style="padding: 8px 0;">{data.get('organization')}</td>
                    </tr>"""
        if data.get('partnershipType'):
            html_body += f"""
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Partnership Type:</td>
                        <td style="padding: 8px 0;">{data.get('partnershipType')}</td>
                    </tr>"""
        if data.get('position'):
            html_body += f"""
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Position:</td>
                        <td style="padding: 8px 0;">{data.get('position')}</td>
                    </tr>"""
        if data.get('experience'):
            html_body += f"""
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Experience:</td>
                        <td style="padding: 8px 0;">{data.get('experience')}</td>
                    </tr>"""
        if data.get('expertise'):
            html_body += f"""
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Expertise:</td>
                        <td style="padding: 8px 0;">{data.get('expertise')}</td>
                    </tr>"""
        if data.get('linkedin'):
            html_body += f"""
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">LinkedIn:</td>
                        <td style="padding: 8px 0;"><a href="{data.get('linkedin')}" style="color: #4f46e5;">{data.get('linkedin')}</a></td>
                    </tr>"""
        if data.get('resumeLink'):
            html_body += f"""
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5;">Resume Link:</td>
                        <td style="padding: 8px 0;"><a href="{data.get('resumeLink')}" style="color: #4f46e5;">{data.get('resumeLink')}</a></td>
                    </tr>"""

        html_body += f"""
                    <tr>
                        <td style="padding: 8px 0; font-weight: bold; color: #4f46e5; vertical-align: top;">Message:</td>
                        <td style="padding: 8px 0;">{data.get('message', 'N/A')}</td>
                    </tr>
                </table>
                <div style="margin-top: 20px; padding-top: 15px; border-top: 1px solid #e5e7eb; color: #6b7280; font-size: 12px;">
                    <p>This enquiry was submitted on {datetime.now().strftime('%B %d, %Y at %I:%M %p')} via the TrainingProtec website.</p>
                </div>
            </div>
        </body>
        </html>"""

        # Build plain text fallback
        text_body = f"""New {service_type}

Name: {data.get('name', 'N/A')}
Email: {data.get('email', 'N/A')}
Phone: {data.get('phone', 'N/A')}
Enquiry Type: {service_type}"""
        if data.get('organization'):
            text_body += f"\nOrganization: {data.get('organization')}"
        if data.get('partnershipType'):
            text_body += f"\nPartnership Type: {data.get('partnershipType')}"
        if data.get('position'):
            text_body += f"\nPosition: {data.get('position')}"
        if data.get('experience'):
            text_body += f"\nExperience: {data.get('experience')}"
        if data.get('expertise'):
            text_body += f"\nExpertise: {data.get('expertise')}"
        if data.get('linkedin'):
            text_body += f"\nLinkedIn: {data.get('linkedin')}"
        if data.get('resumeLink'):
            text_body += f"\nResume Link: {data.get('resumeLink')}"
        text_body += f"\nMessage: {data.get('message', 'N/A')}"
        text_body += f"\n\nSubmitted on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"

        msg = MIMEMultipart('alternative')
        msg['From'] = f'TrainingProtec Website <{SENDER_EMAIL}>'
        msg['To'] = NOTIFICATION_EMAIL
        msg['Subject'] = f'New {service_type} - {data.get("name", "Unknown")}'

        msg.attach(MIMEText(text_body, 'plain'))
        msg.attach(MIMEText(html_body, 'html'))

        # Send email
        if SMTP_USE_TLS:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.ehlo()
        else:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, NOTIFICATION_EMAIL, msg.as_string())
        server.quit()

        logger.info(f'Email notification sent to {NOTIFICATION_EMAIL} for {service_type}')
        return True

    except Exception as e:
        logger.error(f'Failed to send email notification: {str(e)}')
        return False

def send_auto_reply_email(data):
    """Send an automatic confirmation email to the person who submitted the enquiry."""
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        logger.warning('SMTP credentials not configured. Auto-reply email skipped.')
        return False

    try:
        service_type = data.get('service', 'General Enquiry')
        customer_name = data.get('name', 'there')

        # Customize message based on enquiry type
        if service_type == 'Become an Instructor':
            subject_line = 'Thank You for Your Instructor Application'
            hero_text = 'We Received Your Instructor Application!'
            intro_text = f"Dear {customer_name}, thank you for your interest in becoming an instructor at TrainingProtec. We have received your application and our team will review it carefully."
            cta_text = 'Explore Our Courses'
            cta_url = 'https://trainingprotec.com/courses'
        elif service_type == 'Partnership Enquiry':
            subject_line = 'Thank You for Your Partnership Interest'
            hero_text = 'Partnership Enquiry Received!'
            intro_text = f"Dear {customer_name}, thank you for your interest in partnering with TrainingProtec. We are excited about the possibility of working together and will review your proposal promptly."
            cta_text = 'Learn About Us'
            cta_url = 'https://trainingprotec.com/about'
        elif service_type == 'Career Enquiry':
            subject_line = 'Thank You for Your Career Enquiry'
            hero_text = 'Career Enquiry Received!'
            intro_text = f"Dear {customer_name}, thank you for your interest in career opportunities at TrainingProtec. We have received your enquiry and will get back to you soon."
            cta_text = 'View Open Positions'
            cta_url = 'https://trainingprotec.com/careers'
        else:
            subject_line = 'Thank You for Your Enquiry'
            hero_text = 'We Received Your Enquiry!'
            intro_text = f"Dear {customer_name}, thank you for reaching out to TrainingProtec. We have received your enquiry and our team will get back to you shortly."
            cta_text = 'Explore Our Courses'
            cta_url = 'https://trainingprotec.com/courses'

        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
            <div style="background: linear-gradient(135deg, #4f46e5, #7c3aed); padding: 30px; border-radius: 10px 10px 0 0; text-align: center;">
                <h1 style="color: #fff; margin: 0; font-size: 24px;">{hero_text}</h1>
                <p style="color: #e0e7ff; margin: 10px 0 0 0; font-size: 14px;">TrainingProtec - Cyber Security Training Institute</p>
            </div>
            <div style="border: 1px solid #e5e7eb; border-top: none; padding: 30px; border-radius: 0 0 10px 10px;">
                <p style="font-size: 16px;">{intro_text}</p>

                <div style="background: #f3f4f6; border-radius: 8px; padding: 15px 20px; margin: 20px 0;">
                    <p style="margin: 0; font-size: 14px; color: #4b5563;"><strong>Your Enquiry Details:</strong></p>
                    <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
                        <tr>
                            <td style="padding: 5px 0; color: #6b7280; width: 120px;">Name:</td>
                            <td style="padding: 5px 0; font-weight: 600;">{data.get('name', 'N/A')}</td>
                        </tr>
                        <tr>
                            <td style="padding: 5px 0; color: #6b7280;">Enquiry Type:</td>
                            <td style="padding: 5px 0; font-weight: 600;">{service_type}</td>
                        </tr>
                    </table>
                </div>

                <div style="text-align: center; margin: 25px 0;">
                    <a href="{cta_url}" style="background: linear-gradient(135deg, #4f46e5, #7c3aed); color: #fff; padding: 12px 30px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block;">{cta_text}</a>
                </div>

                <p style="font-size: 14px; color: #6b7280;">Our team typically responds within <strong>24-48 hours</strong>. If your enquiry is urgent, feel free to call us at <strong>+91-XXXXXXXXXX</strong>.</p>

                <div style="margin-top: 20px; padding-top: 15px; border-top: 1px solid #e5e7eb;">
                    <p style="margin: 0; font-size: 14px; color: #4b5563;">Best regards,</p>
                    <p style="margin: 5px 0 0 0; font-size: 14px; font-weight: 600; color: #4f46e5;">TrainingProtec Team</p>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #9ca3af;">contact@trainingprotec.com | https://trainingprotec.com</p>
                </div>
            </div>
            <div style="text-align: center; padding: 15px; color: #9ca3af; font-size: 11px;">
                <p style="margin: 0;">This is an automated message. Please do not reply directly to this email.</p>
                <p style="margin: 5px 0 0 0;">© {datetime.now().year} TrainingProtec. All rights reserved.</p>
            </div>
        </body>
        </html>"""

        text_body = f"""{hero_text}

Dear {customer_name},

{intro_text}

Your Enquiry Details:
- Name: {data.get('name', 'N/A')}
- Enquiry Type: {service_type}

Our team typically responds within 24-48 hours.

Best regards,
TrainingProtec Team
contact@trainingprotec.com | https://trainingprotec.com

This is an automated message. Please do not reply directly to this email.
© {datetime.now().year} TrainingProtec. All rights reserved."""

        msg = MIMEMultipart('alternative')
        msg['From'] = f'TrainingProtec <{SENDER_EMAIL}>'
        msg['To'] = data.get('email', '')
        msg['Subject'] = subject_line

        msg.attach(MIMEText(text_body, 'plain'))
        msg.attach(MIMEText(html_body, 'html'))

        # Send email
        if SMTP_USE_TLS:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.ehlo()
        else:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, data.get('email', ''), msg.as_string())
        server.quit()

        logger.info(f'Auto-reply email sent to {data.get("email")} for {service_type}')
        return True

    except Exception as e:
        logger.error(f'Failed to send auto-reply email: {str(e)}')
        return False

def send_reminder_email(contact):
    """Send a follow-up reminder email to the enquirer after REMINDER_DAYS."""
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        logger.warning('SMTP credentials not configured. Reminder email skipped.')
        return False

    try:
        service_type = contact.service or 'General Enquiry'
        customer_name = contact.name or 'there'

        # Customize reminder based on enquiry type
        if service_type == 'Become an Instructor':
            subject_line = f'Still Interested in Teaching at TrainingProtec?'
            reminder_text = f"Dear {customer_name}, we noticed you applied to become an instructor at TrainingProtec a while ago. We'd love to hear from you again and discuss how your expertise can help shape the next generation of cybersecurity professionals."
            cta_text = 'Continue Your Application'
            cta_url = 'https://trainingprotec.com/courses'
        elif service_type == 'Partnership Enquiry':
            subject_line = f'Let\'s Continue Our Partnership Discussion'
            reminder_text = f"Dear {customer_name}, we're still very interested in exploring a partnership with you. Let's reconnect and discuss how we can create value together."
            cta_text = 'Reconnect With Us'
            cta_url = 'https://trainingprotec.com/contact'
        elif service_type == 'Career Enquiry':
            subject_line = f'Still Looking for Career Opportunities?'
            reminder_text = f"Dear {customer_name}, we wanted to follow up on your career enquiry at TrainingProtec. New opportunities may have opened up since we last heard from you."
            cta_text = 'Explore Opportunities'
            cta_url = 'https://trainingprotec.com/courses'
        else:
            subject_line = f'Still Interested in {service_type}?'
            reminder_text = f"Dear {customer_name}, we noticed you enquired about our services at TrainingProtec a while ago. We wanted to check in and see if you still need assistance or have any questions we can help with."
            cta_text = 'Get in Touch'
            cta_url = 'https://trainingprotec.com/contact'

        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
            <div style="background: linear-gradient(135deg, #f59e0b, #ef4444); padding: 30px; border-radius: 10px 10px 0 0; text-align: center;">
                <h1 style="color: #fff; margin: 0; font-size: 22px;">We'd Love to Hear From You!</h1>
                <p style="color: #fef3c7; margin: 10px 0 0 0; font-size: 14px;">TrainingProtec - Follow Up</p>
            </div>
            <div style="border: 1px solid #e5e7eb; border-top: none; padding: 30px; border-radius: 0 0 10px 10px;">
                <p style="font-size: 16px;">{reminder_text}</p>

                <div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px 20px; margin: 20px 0; border-radius: 0 8px 8px 0;">
                    <p style="margin: 0; font-size: 14px; color: #92400e;"><strong>💡 Did you know?</strong> TrainingProtec has helped 1000+ professionals advance their careers in cybersecurity with industry-recognized certifications and hands-on training.</p>
                </div>

                <div style="text-align: center; margin: 25px 0;">
                    <a href="{cta_url}" style="background: linear-gradient(135deg, #4f46e5, #7c3aed); color: #fff; padding: 12px 30px; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block;">{cta_text}</a>
                </div>

                <p style="font-size: 14px; color: #6b7280;">If you have any questions or would like to discuss your options, don't hesitate to reach out. You can reply to this email or call us at <strong>+91-XXXXXXXXXX</strong>.</p>

                <div style="margin-top: 20px; padding-top: 15px; border-top: 1px solid #e5e7eb;">
                    <p style="margin: 0; font-size: 14px; color: #4b5563;">Best regards,</p>
                    <p style="margin: 5px 0 0 0; font-size: 14px; font-weight: 600; color: #4f46e5;">TrainingProtec Team</p>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #9ca3af;">contact@trainingprotec.com | https://trainingprotec.com</p>
                </div>
            </div>
            <div style="text-align: center; padding: 15px; color: #9ca3af; font-size: 11px;">
                <p style="margin: 0;">This is a follow-up to your enquiry submitted on {contact.created_at.strftime('%B %d, %Y')}.</p>
                <p style="margin: 5px 0 0 0;">© {datetime.now().year} TrainingProtec. All rights reserved.</p>
            </div>
        </body>
        </html>"""

        text_body = f"""We'd Love to Hear From You!

Dear {customer_name},

{reminder_text}

Did you know? TrainingProtec has helped 1000+ professionals advance their careers in cybersecurity.

{cta_text}: {cta_url}

If you have any questions, don't hesitate to reach out.
Email: contact@trainingprotec.com

Best regards,
TrainingProtec Team

This is a follow-up to your enquiry submitted on {contact.created_at.strftime('%B %d, %Y')}.
© {datetime.now().year} TrainingProtec. All rights reserved."""

        msg = MIMEMultipart('alternative')
        msg['From'] = f'TrainingProtec <{SENDER_EMAIL}>'
        msg['To'] = contact.email
        msg['Subject'] = subject_line

        msg.attach(MIMEText(text_body, 'plain'))
        msg.attach(MIMEText(html_body, 'html'))

        # Send email
        if SMTP_USE_TLS:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.ehlo()
        else:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, contact.email, msg.as_string())
        server.quit()

        logger.info(f'Reminder email sent to {contact.email} for {service_type} (enquiry #{contact.id})')
        return True

    except Exception as e:
        logger.error(f'Failed to send reminder email to {contact.email}: {str(e)}')
        return False

def check_and_send_reminders():
    """Check for enquiries older than REMINDER_DAYS that haven't received a reminder yet."""
    with app.app_context():
        try:
            reminder_cutoff = datetime.utcnow() - timedelta(days=REMINDER_DAYS)
            contacts = Contact.query.filter(
                Contact.created_at <= reminder_cutoff,
                Contact.reminder_sent == False
            ).all()

            if not contacts:
                logger.info('No pending reminders to send.')
                return

            sent_count = 0
            for contact in contacts:
                if send_reminder_email(contact):
                    contact.reminder_sent = True
                    contact.reminder_sent_at = datetime.utcnow()
                    db.session.commit()
                    sent_count += 1
                else:
                    logger.warning(f'Reminder email failed for enquiry #{contact.id}')

            logger.info(f'Reminder check complete: {sent_count}/{len(contacts)} reminders sent.')

        except Exception as e:
            logger.error(f'Error in reminder check: {str(e)}')

def send_welcome_email(email):
    """Send a welcome email to a new newsletter subscriber."""
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        logger.warning('SMTP not configured. Skipping welcome email.')
        return False
    
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = SMTP_USERNAME
        msg['To'] = email
        msg['Subject'] = 'Welcome to TrainingProtec Newsletter!'
        
        html_content = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background: #0a0e17; color: #e2e8f0; padding: 30px; border-radius: 10px;">
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="color: #00d4ff; margin: 0;">Welcome to TrainingProtec!</h1>
            </div>
            <div style="background: rgba(0, 212, 255, 0.05); padding: 20px; border-radius: 8px; border: 1px solid rgba(0, 212, 255, 0.1); margin-bottom: 20px;">
                <p style="color: #e2e8f0; font-size: 16px; line-height: 1.6;">Thank you for subscribing to our newsletter! 🎉</p>
                <p style="color: #94a3b8; font-size: 14px; line-height: 1.6;">You'll now receive:</p>
                <ul style="color: #94a3b8; font-size: 14px; line-height: 1.8;">
                    <li>Free career guides and industry insights</li>
                    <li>Course updates and exclusive offers</li>
                    <li>Expert tips for professional growth</li>
                </ul>
            </div>
            <div style="text-align: center; margin-top: 20px;">
                <a href="https://trainingprotec.com" style="background: linear-gradient(135deg, #4f46e5, #00d4ff); color: white; padding: 12px 30px; text-decoration: none; border-radius: 6px; font-weight: bold;">Explore Our Courses</a>
            </div>
            <p style="color: #64748b; font-size: 12px; text-align: center; margin-top: 30px;">TrainingProtec - Global Professional Training Platform</p>
        </div>
        """
        
        text_content = f"""Welcome to TrainingProtec Newsletter!

Thank you for subscribing! You'll now receive:
- Free career guides and industry insights
- Course updates and exclusive offers
- Expert tips for professional growth

Visit us at https://trainingprotec.com"""
        
        part1 = MIMEText(text_content, 'plain')
        part2 = MIMEText(html_content, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, email, msg.as_string())
        
        logger.info(f'Welcome email sent to {email}')
        return True
    except Exception as e:
        logger.error(f'Failed to send welcome email to {email}: {str(e)}')
        return False

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

CORS(app, origins=[
    'http://localhost:3000', 'http://localhost:3005',
    'http://147.93.19.87', 'http://147.93.19.87:5050',
    'https://trainingprotec.com', 'https://www.trainingprotec.com',
    'http://trainingprotec.com', 'http://www.trainingprotec.com'
], supports_credentials=True)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'

# ==================== MODELS ====================

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default='admin')  # 'superadmin' or 'admin'
    is_active = db.Column(db.Boolean, default=True)
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
    reminder_sent = db.Column(db.Boolean, default=False)
    reminder_sent_at = db.Column(db.DateTime, nullable=True)
    auto_reply_sent = db.Column(db.Boolean, default=False)
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
            'reminder_sent': self.reminder_sent,
            'reminder_sent_at': self.reminder_sent_at.strftime('%Y-%m-%d %H:%M:%S') if self.reminder_sent_at else None,
            'auto_reply_sent': self.auto_reply_sent,
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
    title = db.Column(db.String(200), nullable=True, default='')
    slug = db.Column(db.String(200), unique=True, nullable=True, default='')
    description = db.Column(db.Text, nullable=True, default='')
    image = db.Column(db.String(500), nullable=True, default='')
    icon = db.Column(db.String(50), default='FaBookOpen')
    price = db.Column(db.Integer, nullable=True, default=0)
    original_price = db.Column(db.Integer, nullable=True, default=0)
    rating = db.Column(db.Float, default=4.5)
    reviews = db.Column(db.Integer, default=0)
    learners = db.Column(db.String(50), default='0')
    duration = db.Column(db.String(50), nullable=True, default='')
    level = db.Column(db.String(50), default='Beginner')
    tag = db.Column(db.String(50))
    modules = db.Column(db.Integer, default=0)
    projects = db.Column(db.Integer, default=0)
    instructor_name = db.Column(db.String(100), nullable=True, default='')
    instructor_role = db.Column(db.String(200), nullable=True, default='')
    instructor_image = db.Column(db.String(500), nullable=True, default='')
    instructor_experience = db.Column(db.String(50), nullable=True, default='')
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

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    welcome_email_sent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'is_active': self.is_active,
            'welcome_email_sent': self.welcome_email_sent,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

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

    # Send admin notification email (non-blocking - won't fail the request if email fails)
    try:
        email_sent = send_enquiry_email(data)
        if email_sent:
            logger.info(f'Admin notification sent for enquiry from {data.get("email")}')
        else:
            logger.warning(f'Admin notification skipped for enquiry from {data.get("email")}')
    except Exception as e:
        logger.error(f'Admin notification error (enquiry still saved): {str(e)}')

    # Send auto-reply email to the enquirer (non-blocking)
    try:
        auto_reply_sent = send_auto_reply_email(data)
        if auto_reply_sent:
            contact.auto_reply_sent = True
            db.session.commit()
            logger.info(f'Auto-reply sent to {data.get("email")}')
        else:
            logger.warning(f'Auto-reply skipped for {data.get("email")}')
    except Exception as e:
        logger.error(f'Auto-reply error (enquiry still saved): {str(e)}')

    return jsonify({'success': True, 'message': 'Message sent successfully!'})

@app.route('/api/subscribe', methods=['POST'])
def subscribe_newsletter():
    """Subscribe an email to the newsletter."""
    data = request.json
    email = data.get('email', '').strip().lower() if data.get('email') else ''
    
    if not email:
        return jsonify({'success': False, 'message': 'Email is required.'}), 400
    
    # Basic email validation
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return jsonify({'success': False, 'message': 'Please enter a valid email address.'}), 400
    
    # Check if already subscribed
    existing = Subscriber.query.filter_by(email=email).first()
    if existing:
        if existing.is_active:
            return jsonify({'success': False, 'message': 'This email is already subscribed!'})
        else:
            # Reactivate unsubscribed email
            existing.is_active = True
            db.session.commit()
            return jsonify({'success': True, 'message': 'Welcome back! You have been re-subscribed.'})
    
    # Create new subscriber
    subscriber = Subscriber(email=email, is_active=True)
    db.session.add(subscriber)
    db.session.commit()
    
    # Send welcome email (non-blocking)
    try:
        welcome_sent = send_welcome_email(email)
        if welcome_sent:
            subscriber.welcome_email_sent = True
            db.session.commit()
            logger.info(f'Welcome email sent to subscriber {email}')
        else:
            logger.warning(f'Welcome email skipped for subscriber {email}')
    except Exception as e:
        logger.error(f'Welcome email error (subscription still saved): {str(e)}')
    
    return jsonify({'success': True, 'message': 'Thank you for subscribing! You will receive our latest updates.'})

@app.route('/api/cron/reminders', methods=['POST'])
def trigger_reminders():
    """Cron endpoint to trigger reminder emails. Secured with CRON_SECRET."""
    provided_secret = request.headers.get('X-Cron-Secret', '') or request.args.get('secret', '')
    if CRON_SECRET and provided_secret != CRON_SECRET:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        check_and_send_reminders()
        return jsonify({'success': True, 'message': 'Reminder check completed'})
    except Exception as e:
        logger.error(f'Cron reminder error: {str(e)}')
        return jsonify({'error': 'Internal error'}), 500

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
    try:
        logger.info(f"Upload request received. Files: {list(request.files.keys())}, Content-Type: {request.content_type}")
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        if not allowed_file(file.filename):
            return jsonify({'error': f'File type not allowed. Allowed types: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
        
        # Ensure upload folder exists and is writable
        upload_folder = app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)
        if not os.access(upload_folder, os.W_OK):
            logger.error(f"Upload folder not writable: {upload_folder}")
            # Try to fix permissions
            try:
                os.chmod(upload_folder, 0o755)
            except Exception as e:
                logger.error(f"Cannot fix upload folder permissions: {e}")
            return jsonify({'error': 'Server upload directory not writable. Contact admin.'}), 500
        
        # Generate unique filename using secure_filename
        original_filename = secure_filename(file.filename)
        ext = original_filename.rsplit('.', 1)[1].lower() if '.' in original_filename else 'png'
        unique_name = f"{uuid.uuid4().hex[:12]}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
        
        filepath = os.path.join(upload_folder, unique_name)
        logger.info(f"Saving upload to: {filepath}")
        file.save(filepath)
        
        # Verify file was saved
        if not os.path.exists(filepath):
            logger.error(f"File was not saved: {filepath}")
            return jsonify({'error': 'Failed to save file'}), 500
        
        file_size = os.path.getsize(filepath)
        logger.info(f"Upload successful: {unique_name} ({file_size} bytes)")
        
        # Return the URL path that can be used as the image value
        image_url = f"/static/uploads/{unique_name}"
        return jsonify({'url': image_url, 'filename': unique_name})
    
    except Exception as e:
        logger.error(f"Upload error: {str(e)}", exc_info=True)
        return jsonify({'error': f'Upload failed: {str(e)}'}), 500

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
    subscribers_count = Subscriber.query.filter_by(is_active=True).count()
    total_views = db.session.query(db.func.sum(Blog.views)).scalar() or 0
    recent_blogs = Blog.query.order_by(Blog.created_at.desc()).limit(5).all()
    recent_contacts = Contact.query.order_by(Contact.created_at.desc()).limit(5).all()
    recent_courses = Course.query.order_by(Course.created_at.desc()).limit(5).all()
    recent_subscribers = Subscriber.query.filter_by(is_active=True).order_by(Subscriber.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html',
                         blogs_count=blogs_count,
                         contacts_count=contacts_count,
                         courses_count=courses_count,
                         testimonials_count=testimonials_count,
                         subscribers_count=subscribers_count,
                         total_views=total_views,
                         recent_blogs=recent_blogs,
                         recent_contacts=recent_contacts,
                         recent_courses=recent_courses,
                         recent_subscribers=recent_subscribers)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password):
            if not admin.is_active:
                flash('Your account has been deactivated. Contact superadmin.', 'error')
                return render_template('admin/login.html')
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

@app.route('/admin/contacts/send-auto-reply/<int:id>', methods=['POST'])
@login_required
def admin_send_auto_reply(id):
    contact = Contact.query.get_or_404(id)
    if contact.auto_reply_sent:
        flash('Auto-reply already sent to this contact.', 'warning')
        return redirect(url_for('admin_contact_view', id=id))
    data = {
        'name': contact.name,
        'email': contact.email,
        'phone': contact.phone or '',
        'service': contact.service or 'General',
        'message': contact.message or '',
        'enquiry_type': contact.service or 'General'
    }
    if send_auto_reply_email(data):
        contact.auto_reply_sent = True
        db.session.commit()
        flash('Auto-reply email sent successfully!', 'success')
    else:
        flash('Failed to send auto-reply email. Check SMTP settings.', 'danger')
    return redirect(url_for('admin_contact_view', id=id))

@app.route('/admin/contacts/send-reminder/<int:id>', methods=['POST'])
@login_required
def admin_send_reminder(id):
    contact = Contact.query.get_or_404(id)
    if contact.reminder_sent:
        flash('Reminder already sent to this contact.', 'warning')
        return redirect(url_for('admin_contact_view', id=id))
    if send_reminder_email(contact):
        contact.reminder_sent = True
        contact.reminder_sent_at = datetime.utcnow()
        db.session.commit()
        flash('Reminder email sent successfully!', 'success')
    else:
        flash('Failed to send reminder email. Check SMTP settings.', 'danger')
    return redirect(url_for('admin_contact_view', id=id))

# Course Management
@app.route('/admin/courses')
@login_required
def admin_courses():
    courses = Course.query.order_by(Course.sort_order, Course.created_at.desc()).all()
    return render_template('admin/courses.html', courses=courses)

def safe_int(value, default=0):
    """Safely convert form value to int, returning default for empty/invalid values."""
    try:
        return int(value) if value and value.strip() else default
    except (ValueError, TypeError, AttributeError):
        return default

def safe_float(value, default=4.5):
    """Safely convert form value to float, returning default for empty/invalid values."""
    try:
        return float(value) if value and value.strip() else default
    except (ValueError, TypeError, AttributeError):
        return default

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
            price=safe_int(request.form.get('price', ''), 0),
            original_price=safe_int(request.form.get('original_price', ''), 0),
            rating=safe_float(request.form.get('rating', ''), 4.5),
            reviews=safe_int(request.form.get('reviews', ''), 0),
            learners=request.form.get('learners', '0'),
            duration=request.form.get('duration', ''),
            level=request.form.get('level', 'Beginner'),
            tag=request.form.get('tag', ''),
            modules=safe_int(request.form.get('modules', ''), 0),
            projects=safe_int(request.form.get('projects', ''), 0),
            instructor_name=request.form.get('instructor_name', ''),
            instructor_role=request.form.get('instructor_role', ''),
            instructor_image=request.form.get('instructor_image', ''),
            instructor_experience=request.form.get('instructor_experience', ''),
            curriculum=request.form.get('curriculum', ''),
            is_published=request.form.get('is_published') == 'on',
            sort_order=safe_int(request.form.get('sort_order', ''), 0),
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
        try:
            db.session.add(course)
            db.session.commit()
            flash('Course created successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating course: {str(e)}', 'error')
            return render_template('admin/course_form.html', course=course)
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
        course.price = safe_int(request.form.get('price', ''), 0)
        course.original_price = safe_int(request.form.get('original_price', ''), 0)
        course.rating = safe_float(request.form.get('rating', ''), 4.5)
        course.reviews = safe_int(request.form.get('reviews', ''), 0)
        course.learners = request.form.get('learners', '0')
        course.duration = request.form.get('duration', '')
        course.level = request.form.get('level', 'Beginner')
        course.tag = request.form.get('tag', '')
        course.modules = safe_int(request.form.get('modules', ''), 0)
        course.projects = safe_int(request.form.get('projects', ''), 0)
        course.instructor_name = request.form.get('instructor_name', '')
        course.instructor_role = request.form.get('instructor_role', '')
        course.instructor_image = request.form.get('instructor_image', '')
        course.instructor_experience = request.form.get('instructor_experience', '')
        course.curriculum = request.form.get('curriculum', '')
        course.is_published = request.form.get('is_published') == 'on'
        course.sort_order = safe_int(request.form.get('sort_order', ''), 0)
        course.tagline = request.form.get('tagline', '')
        course.hero_image = request.form.get('hero_image', '')
        course.overview = request.form.get('overview', '')
        course.key_benefits = request.form.get('key_benefits', '')
        course.modules_detail = request.form.get('modules_detail', '')
        course.learning_path = request.form.get('learning_path', '')
        course.technologies_list = request.form.get('technologies_list', '')
        course.faq = request.form.get('faq', '')
        course.detail_stats = request.form.get('detail_stats', '')
        try:
            db.session.commit()
            flash('Course updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating course: {str(e)}', 'error')
            return render_template('admin/course_form.html', course=course)
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

# ==================== USER MANAGEMENT ====================

@app.route('/admin/users')
@login_required
def admin_users():
    if current_user.role != 'superadmin':
        flash('Only superadmins can manage users.', 'error')
        return redirect(url_for('admin_dashboard'))
    users = Admin.query.order_by(Admin.created_at.desc()).all()
    return render_template('admin/users.html', users=users)

@app.route('/admin/users/new', methods=['GET', 'POST'])
@login_required
def admin_user_new():
    if current_user.role != 'superadmin':
        flash('Only superadmins can manage users.', 'error')
        return redirect(url_for('admin_dashboard'))
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        role = request.form.get('role', 'admin')
        is_active = 'is_active' in request.form

        if not username or not email or not password:
            flash('Username, email, and password are required.', 'error')
            return render_template('admin/user_form.html', user=None)

        if Admin.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return render_template('admin/user_form.html', user=None)

        if Admin.query.filter_by(email=email).first():
            flash('Email already exists.', 'error')
            return render_template('admin/user_form.html', user=None)

        user = Admin(username=username, email=email, role=role, is_active=is_active)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('User created successfully!', 'success')
        return redirect(url_for('admin_users'))

    return render_template('admin/user_form.html', user=None)

@app.route('/admin/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_user_edit(id):
    if current_user.role != 'superadmin':
        flash('Only superadmins can manage users.', 'error')
        return redirect(url_for('admin_dashboard'))
    user = Admin.query.get_or_404(id)

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        role = request.form.get('role', 'admin')
        is_active = 'is_active' in request.form

        if not username or not email:
            flash('Username and email are required.', 'error')
            return render_template('admin/user_form.html', user=user)

        # Check uniqueness (exclude current user)
        existing = Admin.query.filter_by(username=username).first()
        if existing and existing.id != id:
            flash('Username already exists.', 'error')
            return render_template('admin/user_form.html', user=user)

        existing = Admin.query.filter_by(email=email).first()
        if existing and existing.id != id:
            flash('Email already exists.', 'error')
            return render_template('admin/user_form.html', user=user)

        user.username = username
        user.email = email
        user.role = role
        user.is_active = is_active
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('admin_users'))

    return render_template('admin/user_form.html', user=user)

@app.route('/admin/users/delete/<int:id>', methods=['POST'])
@login_required
def admin_user_delete(id):
    if current_user.role != 'superadmin':
        flash('Only superadmins can manage users.', 'error')
        return redirect(url_for('admin_dashboard'))
    if id == current_user.id:
        flash('You cannot delete your own account.', 'error')
        return redirect(url_for('admin_users'))
    user = Admin.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin_users'))

@app.route('/admin/users/change-password/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_user_change_password(id):
    if current_user.role != 'superadmin' and id != current_user.id:
        flash('You do not have permission to change this password.', 'error')
        return redirect(url_for('admin_users'))
    user = Admin.query.get_or_404(id)

    if request.method == 'POST':
        new_password = request.form.get('new_password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not new_password or len(new_password) < 6:
            flash('Password must be at least 6 characters.', 'error')
            return render_template('admin/change_password.html', target_user=user)

        if new_password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('admin/change_password.html', target_user=user)

        user.set_password(new_password)
        db.session.commit()
        flash('Password changed successfully!', 'success')
        return redirect(url_for('admin_users'))

    return render_template('admin/change_password.html', target_user=user)

@app.route('/admin/users/toggle-active/<int:id>', methods=['POST'])
@login_required
def admin_user_toggle_active(id):
    if current_user.role != 'superadmin':
        flash('Only superadmins can manage users.', 'error')
        return redirect(url_for('admin_dashboard'))
    if id == current_user.id:
        flash('You cannot deactivate your own account.', 'error')
        return redirect(url_for('admin_users'))
    user = Admin.query.get_or_404(id)
    user.is_active = not user.is_active
    db.session.commit()
    status = 'activated' if user.is_active else 'deactivated'
    flash(f'User {status} successfully!', 'success')
    return redirect(url_for('admin_users'))

# ==================== SUBSCRIBER MANAGEMENT ====================

@app.route('/admin/subscribers')
@login_required
def admin_subscribers():
    subscribers = Subscriber.query.order_by(Subscriber.created_at.desc()).all()
    active_count = Subscriber.query.filter_by(is_active=True).count()
    total_count = Subscriber.query.count()
    return render_template('admin/subscribers.html',
                         subscribers=subscribers,
                         active_count=active_count,
                         total_count=total_count)

@app.route('/admin/subscribers/delete/<int:id>', methods=['POST'])
@login_required
def admin_subscriber_delete(id):
    subscriber = Subscriber.query.get_or_404(id)
    db.session.delete(subscriber)
    db.session.commit()
    flash('Subscriber deleted successfully!', 'success')
    return redirect(url_for('admin_subscribers'))

@app.route('/admin/subscribers/toggle-active/<int:id>', methods=['POST'])
@login_required
def admin_subscriber_toggle_active(id):
    subscriber = Subscriber.query.get_or_404(id)
    subscriber.is_active = not subscriber.is_active
    db.session.commit()
    status = 'activated' if subscriber.is_active else 'deactivated'
    flash(f'Subscriber {status} successfully!', 'success')
    return redirect(url_for('admin_subscribers'))

@app.route('/admin/subscribers/export')
@login_required
def admin_subscribers_export():
    """Export all active subscriber emails as CSV."""
    subscribers = Subscriber.query.filter_by(is_active=True).order_by(Subscriber.created_at.desc()).all()
    
    import io
    output = io.StringIO()
    output.write('Email,Subscribed Date,Welcome Email Sent\n')
    for sub in subscribers:
        welcome_status = 'Yes' if sub.welcome_email_sent else 'No'
        output.write(f'{sub.email},{sub.created_at.strftime("%Y-%m-%d %H:%M")},{welcome_status}\n')
    
    from flask import make_response
    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=newsletter_subscribers.csv'
    return response

# ==================== INITIALIZE ====================

def create_admin():
    admin = Admin.query.first()
    if not admin:
        admin = Admin(username='vishalsharma1104@gmail.com', email='vishalsharma1104@gmail.com', role='superadmin')
        admin.set_password('Vishal@1*sharma')
        db.session.add(admin)
        db.session.commit()
        print('Admin user created: vishalsharma1104@gmail.com / Vishal@1*sharma')
    else:
        # Update existing admin credentials and ensure superadmin role
        admin.username = 'vishalsharma1104@gmail.com'
        admin.email = 'vishalsharma1104@gmail.com'
        admin.set_password('Vishal@1*sharma')
        admin.role = 'superadmin'
        db.session.commit()
        print('Admin credentials updated: vishalsharma1104@gmail.com / Vishal@1*sharma')

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
                price=199,
                original_price=569,
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
                price=179,
                original_price=499,
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
                price=189,
                original_price=549,
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
                price=149,
                original_price=449,
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
                description='Master SEO, Google Ads, Social Media Marketing, Analytics & Content Strategy. Run real campaigns with $100 Google Ad credits. Google certified program.',
                image='https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
                icon='FaBullhorn',
                price=119,
                original_price=349,
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
                price=139,
                original_price=399,
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
                price=129,
                original_price=389,
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
                price=179,
                original_price=499,
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

def migrate_db():
    """Add missing columns to existing database tables."""
    with app.app_context():
        # Get existing columns for each table
        inspector = db.inspect(db.engine)
        
        # Migrate Course table
        course_columns = [col['name'] for col in inspector.get_columns('course')]
        course_new_columns = {
            'tagline': "ALTER TABLE course ADD COLUMN tagline VARCHAR(300) DEFAULT ''",
            'hero_image': "ALTER TABLE course ADD COLUMN hero_image VARCHAR(500) DEFAULT ''",
            'overview': "ALTER TABLE course ADD COLUMN overview TEXT DEFAULT ''",
            'key_benefits': "ALTER TABLE course ADD COLUMN key_benefits TEXT DEFAULT ''",
            'modules_detail': "ALTER TABLE course ADD COLUMN modules_detail TEXT DEFAULT ''",
            'learning_path': "ALTER TABLE course ADD COLUMN learning_path TEXT DEFAULT ''",
            'technologies_list': "ALTER TABLE course ADD COLUMN technologies_list TEXT DEFAULT ''",
            'faq': "ALTER TABLE course ADD COLUMN faq TEXT DEFAULT ''",
            'detail_stats': "ALTER TABLE course ADD COLUMN detail_stats TEXT DEFAULT ''",
        }
        for col_name, sql in course_new_columns.items():
            if col_name not in course_columns:
                try:
                    db.session.execute(db.text(sql))
                    db.session.commit()
                    print(f'Added column "{col_name}" to course table')
                except Exception as e:
                    db.session.rollback()
                    print(f'Column "{col_name}" may already exist: {e}')

        # Migrate Testimonial table
        testimonial_columns = [col['name'] for col in inspector.get_columns('testimonial')]
        testimonial_new_columns = {
            'prev_role': "ALTER TABLE testimonial ADD COLUMN prev_role VARCHAR(200) DEFAULT ''",
            'image': "ALTER TABLE testimonial ADD COLUMN image VARCHAR(500) DEFAULT ''",
            'rating': "ALTER TABLE testimonial ADD COLUMN rating INTEGER DEFAULT 5",
            'salary_hike': "ALTER TABLE testimonial ADD COLUMN salary_hike VARCHAR(50) DEFAULT ''",
            'course': "ALTER TABLE testimonial ADD COLUMN course VARCHAR(200) DEFAULT ''",
            'is_published': "ALTER TABLE testimonial ADD COLUMN is_published BOOLEAN DEFAULT 1",
            'sort_order': "ALTER TABLE testimonial ADD COLUMN sort_order INTEGER DEFAULT 0",
        }
        for col_name, sql in testimonial_new_columns.items():
            if col_name not in testimonial_columns:
                try:
                    db.session.execute(db.text(sql))
                    db.session.commit()
                    print(f'Added column "{col_name}" to testimonial table')
                except Exception as e:
                    db.session.rollback()
                    print(f'Column "{col_name}" may already exist: {e}')

        # Migrate Blog table
        blog_columns = [col['name'] for col in inspector.get_columns('blog')]
        blog_new_columns = {
            'category': "ALTER TABLE blog ADD COLUMN category VARCHAR(100) DEFAULT ''",
            'tags': "ALTER TABLE blog ADD COLUMN tags VARCHAR(500) DEFAULT ''",
            'is_published': "ALTER TABLE blog ADD COLUMN is_published BOOLEAN DEFAULT 1",
        }
        for col_name, sql in blog_new_columns.items():
            if col_name not in blog_columns:
                try:
                    db.session.execute(db.text(sql))
                    db.session.commit()
                    print(f'Added column "{col_name}" to blog table')
                except Exception as e:
                    db.session.rollback()
                    print(f'Column "{col_name}" may already exist: {e}')

        # Migrate Contact table (email tracking fields)
        contact_columns = [col['name'] for col in inspector.get_columns('contact')]
        contact_new_columns = {
            'reminder_sent': "ALTER TABLE contact ADD COLUMN reminder_sent BOOLEAN DEFAULT 0",
            'reminder_sent_at': "ALTER TABLE contact ADD COLUMN reminder_sent_at DATETIME DEFAULT NULL",
            'auto_reply_sent': "ALTER TABLE contact ADD COLUMN auto_reply_sent BOOLEAN DEFAULT 0",
        }
        for col_name, sql in contact_new_columns.items():
            if col_name not in contact_columns:
                try:
                    db.session.execute(db.text(sql))
                    db.session.commit()
                    print(f'Added column "{col_name}" to contact table')
                except Exception as e:
                    db.session.rollback()
                    print(f'Column "{col_name}" may already exist: {e}')

        # Migrate Admin table (role & is_active fields)
        admin_columns = [col['name'] for col in inspector.get_columns('admin')]
        admin_new_columns = {
            'role': "ALTER TABLE admin ADD COLUMN role VARCHAR(20) DEFAULT 'admin'",
            'is_active': "ALTER TABLE admin ADD COLUMN is_active BOOLEAN DEFAULT 1",
        }
        for col_name, sql in admin_new_columns.items():
            if col_name not in admin_columns:
                try:
                    db.session.execute(db.text(sql))
                    db.session.commit()
                    print(f'Added column "{col_name}" to admin table')
                except Exception as e:
                    db.session.rollback()
                    print(f'Column "{col_name}" may already exist: {e}')

        # Migrate course prices from INR to USD (one-time update)
        # Only update if prices are still in INR range (>1000)
        usd_prices = {
            'data-science-ai': (199, 569),
            'cloud-computing-devops': (179, 499),
            'cyber-security': (189, 549),
            'web-development': (149, 449),
            'digital-marketing': (119, 349),
            'business-analytics': (139, 399),
            'ui-ux-design': (129, 389),
            'mobile-app-development': (179, 499),
        }
        courses_to_update = Course.query.filter(Course.price > 1000).all()
        if courses_to_update:
            for course in courses_to_update:
                if course.slug in usd_prices:
                    course.price, course.original_price = usd_prices[course.slug]
                else:
                    # Fallback: rough INR→USD conversion for custom courses
                    course.price = round(course.price / 80)
                    course.original_price = round(course.original_price / 80)
            db.session.commit()
            print(f'Updated {len(courses_to_update)} course prices from INR to USD')

        print('Database migration completed!')

# Error handler for file too large
@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({'error': 'File too large. Maximum size is 5MB.'}), 413

# Global error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(error):
    logger.error(f"Internal server error: {str(error)}", exc_info=True)
    return jsonify({'error': 'Internal server error. Please try again.'}), 500

# ==================== APSCHEDULER SETUP ====================
# Only start scheduler when running directly (not under Gunicorn).
# In production, use system cron to hit /api/cron/reminders instead:
#   0 9 * * * curl -s -X POST https://trainingprotec.com/api/cron/reminders -H "X-Cron-Secret: YOUR_SECRET"
scheduler = None

def start_scheduler():
    """Start the APScheduler (only for direct `python app.py` usage)."""
    global scheduler
    if scheduler is not None:
        return
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=check_and_send_reminders,
        trigger='cron',
        hour=9,
        minute=0,
        id='reminder_check',
        name='Send 10-day reminder emails',
        replace_existing=True
    )
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))

# ==================== APP INITIALIZATION ====================
# Initialize database and seed data when the app is loaded (works with both
# `python app.py` and Gunicorn `gunicorn app:app`).
with app.app_context():
    db.create_all()
    migrate_db()
    create_admin()
    create_sample_blogs()
    create_sample_courses()
    create_sample_testimonials()

if __name__ == '__main__':
    start_scheduler()
    app.run(debug=False, host='0.0.0.0', port=5050)
