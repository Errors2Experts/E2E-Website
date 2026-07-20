from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.conf import settings

from .models import (
    Course,
    Service,
    Internship,
    UpcomingWorkshop,
    CourseBooking,
    WorkshopRegistration,
    ServiceBooking,
    Contact,
)


def get_registered_emails():
    """Collect all registered user emails and remove duplicates."""

    emails = set()

    emails.update(
        CourseBooking.objects.exclude(email="").values_list("email", flat=True)
    )

    emails.update(
        WorkshopRegistration.objects.exclude(email="").values_list("email", flat=True)
    )

    emails.update(
        ServiceBooking.objects.exclude(email="").values_list("email", flat=True)
    )

    emails.update(
        Contact.objects.exclude(email="").values_list("email", flat=True)
    )

    return list(emails)


def send_update_email(update_type, title):

    recipients = get_registered_emails()

    if not recipients:
        return

    # ---------------- COURSE ----------------

    if update_type == "Course":

        subject = "🚀 New Course Available | Errors2Experts"

        body = f"""
Hello,

We're excited to announce a new course at Errors2Experts!

📘 Course: {title}

Build industry-ready skills through expert-led training and real-time projects.

🌐 Explore the Course:
https://website.com/courses/

📸 Stay Connected:
https://www.instagram.com/errors2experts_2026/

Thank you for choosing Errors2Experts.

Best Regards,
Errors2Experts Team
"""

    # ---------------- SERVICE ----------------

    elif update_type == "Service":

        subject = "💼 New Service Available | Errors2Experts"

        body = f"""
Hello,

We're excited to introduce a new service at Errors2Experts!

💼 Service: {title}

Explore our latest service and discover how we can help bring your ideas to life with innovative digital solutions.

🌐 Learn More:
https://website.com/services/

📸 Stay Connected:
https://www.instagram.com/errors2experts_2026/

Thank you for choosing Errors2Experts.

Best Regards,
Errors2Experts Team
"""

    # ---------------- INTERNSHIP ----------------

    elif update_type == "Internship":

        subject = "🎓 New Internship Opportunity | Errors2Experts"

        body = f"""
Hello,

We're happy to announce a new internship opportunity at Errors2Experts!

🎓 Internship: {title}

Gain practical experience, work on real-time projects, and build your career with expert guidance.

🌐 Learn More:
https://website.com/internships/

📸 Stay Connected:
https://www.instagram.com/errors2experts_2026/

Thank you for choosing Errors2Experts.

Best Regards,
Errors2Experts Team
"""

    # ---------------- WORKSHOP ----------------

    elif update_type == "Workshop":

        subject = "🎯 New Workshop Open for Registration | Errors2Experts"

        body = f"""
Hello,

We're excited to announce a new workshop at Errors2Experts!

🎯 Workshop: {title}

Join our hands-on workshop to learn from industry experts and enhance your practical skills.

🌐 Register Now:
https://website.com/workshops/

📸 Stay Connected:
https://www.instagram.com/errors2experts_2026/

Thank you for choosing Errors2Experts.

Best Regards,
Errors2Experts Team
"""

    else:
        return

    # Send mail individually to each registered user
    for recipient in recipients:

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient],
        )

        email.send(fail_silently=False)


# ---------------- COURSE ----------------

@receiver(post_save, sender=Course)
def course_created(sender, instance, created, **kwargs):
    if created:
        send_update_email("Course", instance.title)


# ---------------- SERVICE ----------------

@receiver(post_save, sender=Service)
def service_created(sender, instance, created, **kwargs):
    if created:
        send_update_email("Service", instance.title)


# ---------------- INTERNSHIP ----------------

@receiver(post_save, sender=Internship)
def internship_created(sender, instance, created, **kwargs):
    if created:
        send_update_email("Internship", instance.title)


# ---------------- UPCOMING WORKSHOP ----------------

@receiver(post_save, sender=UpcomingWorkshop)
def workshop_created(sender, instance, created, **kwargs):
    if created:
        send_update_email("Workshop", instance.title)