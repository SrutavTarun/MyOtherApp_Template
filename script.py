import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get email credentials from .env file
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Load HTML template
with open("index.html", "r", encoding="utf-8") as file:
    template_content = file.read()

# Define data
data = {
    "participant_name": "John Doe",
    "event_name": "Tech Conference 2025",
    "event_date": "March 15, 2025",
    "event_time": "10:00 AM - 3:00 PM",
    "event_location": "Online (Zoom Link)",
    "event_prizes": "Exciting prizes for top participants!",
    "organizer_name": "Tech Org",
    "contact_email": "support@techorg.com",
    "contact_phone": "+1234567890",
    "sender_name": "Event Team",
    "organization_name": "Tech Org",
    "website_link": "https://techorg.com",
    "social_media_link": "https://twitter.com/techorg"
}

# Render email content
jinja_template = Template(template_content)
html_content = jinja_template.render(data)

# Email details
receiver_email = "cedricaltis@gmail.com"
subject = "Your Ticket is Cooked! - Tech Conference 2025"

# Create email message
msg = MIMEMultipart()
msg["From"] = EMAIL_USER
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(html_content, "html"))

# Send email via SMTP
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, receiver_email, msg.as_string())
        print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)
