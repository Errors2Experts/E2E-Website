from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    discount=models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    


class Placement(models.Model):
    student_name = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='placements/')
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    job_role = models.CharField(max_length=100)
    package = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True)
    placed_year = models.PositiveIntegerField()
    course = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.company_name}"

class Module(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='modules'
    )
    module_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.module_name


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    technologies = models.CharField(
        max_length=400,
        blank=True,
        help_text="Comma-separated, e.g. 'Django, Bootstrap, PostgreSQL, REST API'"
    )
 
    def __str__(self):
        return self.title
 
    def tech_list(self):
        """Returns technologies as a clean list for templates: service.tech_list"""
        return [t.strip() for t in self.technologies.split(',') if t.strip()]
 
 
class ServiceDemoLink(models.Model):

    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='demo_links'
    )
    title = models.CharField(
        max_length=150,
        help_text="e.g. 'E-commerce Demo', 'Portfolio Demo'"
    )
    image = models.FileField(upload_to='service_images/', blank=True, null=True)
    url = models.URLField(help_text="Full link to the live demo site",blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower number = shown first")
    description = models.CharField(
        max_length=300, blank=True,
        help_text="Short one-line description shown on the Live Demo card"
    )
    category = models.CharField(
        max_length=100, blank=True,
        help_text="e.g. 'Education', 'CRM', 'Hotel', 'Portfolio' — used for Live Demo filters"
    )
    technologies = models.CharField(
        max_length=300, blank=True,
        help_text="Comma-separated, e.g. 'HTML, CSS, JS'"
    )
    is_featured = models.BooleanField(
        default=True,
        help_text="Show this on its Service's detail page (uncheck to keep it Live-Demo-page-only)"
    )
 
    class Meta:
        ordering = ['order']
 
    def __str__(self):
        return f"{self.service.title} — {self.title}"
    
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]
# models.py — add below Service / ServiceDemoLink

class ServiceFeature(models.Model):
    """3-6 per service — powers the 'Why Choose This Service' cards."""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    icon = models.CharField(
        max_length=50, default='bi-check-circle',
        help_text="Bootstrap Icon class, e.g. 'bi-rocket-takeoff' — browse icons.getbootstrap.com"
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.service.title} — {self.title}"


class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=250)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Service FAQ'
        verbose_name_plural = 'Service FAQs'

    def __str__(self):
        return f"{self.service.title} — {self.question}"


class ProcessStep(models.Model):
    """Global — same development process shown on every service page."""
    icon = models.CharField(max_length=50, default='bi-search', help_text="Bootstrap Icon class")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class ClientProject(models.Model):
    client_name = models.CharField(max_length=150)
    project_type = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.client_name} - {self.project_type}"


# Students Reviews Model
class StudentReview(models.Model):
    GENDER_CHOICES = (('M','Male'),('F','Female'),('O','Other/Prefer not to say'))
    student_name = models.CharField(max_length=120)
    course_name = models.CharField(max_length=150)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(default=5) 
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M',help_text="Used for default anime avatar if no custom image is uploaded")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student_name} - {self.course_name}"
    
from django.db import models

class Career(models.Model):

    EMPLOYMENT_TYPES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    )

    role = models.CharField(max_length=200)
    job_description = models.TextField()
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES)
    salary = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='careers/', blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role
    
class JobApplication(models.Model):
    career = models.ForeignKey('Career', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    education = models.CharField(max_length=200)
    year_passed_out = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.career.role}"
    
class CourseBooking(models.Model):
    PAYMENT_CHOICES = (
        ('full', 'Full Amount'),
        ('emi', 'Installment EMI'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    education = models.CharField(max_length=200)
    year_passed = models.CharField(max_length=10)
    course = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ServiceBooking(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    service_name = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    preferred_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service_name}"

class WorkshopPhoto(models.Model):
    """
    Stores photos from workshops / events conducted by Errors2Experts.
    Upload images via Django admin → they appear in the Workshop Gallery section.
    """
    title       = models.CharField(max_length=200, help_text="e.g. 'Python Bootcamp – March 2025'")
    description = models.TextField(blank=True, help_text="Short caption shown under the photo (optional)")
    image       = models.ImageField(upload_to='workshop_photos/', help_text="Upload workshop photo")
    event_date  = models.DateField(blank=True, null=True, help_text="Date the workshop was held (optional)")
    order       = models.PositiveIntegerField(default=0, help_text="Lower number = shown first")
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name        = 'Workshop Photo'
        verbose_name_plural = 'Workshop Photos'

    def __str__(self):
        return self.title

class WorkshopRegistration(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    education = models.CharField(max_length=150)
    workshop = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class UpcomingWorkshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    event_date = models.DateField()
    event_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    registration_info = models.CharField(max_length=200, blank=True)

    image = models.ImageField(upload_to="upcoming_workshops/")

    def __str__(self):
        return self.title
    
    
class Certificate(models.Model):
    """
    Stores certificate images that E2E issues to students.
    Each certificate can have a name, course name, and an image (scan/design).
    Upload via Django admin → they appear in the Certificates section.
    """
    CERT_TYPES = (
        ('course',      'Course Completion'),
        ('internship',  'Internship'),
        ('workshop',    'Workshop'),
        ('project',     'Live Project'),
    )

    cert_type   = models.CharField(max_length=20, choices=CERT_TYPES, default='course', verbose_name='Certificate Type')
    course_name = models.CharField(max_length=200, help_text="e.g. 'Python Full Stack Development'")
    image       = models.ImageField(upload_to='certificates/', help_text="Upload certificate image/scan")
    description = models.TextField(blank=True, help_text="Optional tagline shown under the certificate")
    order       = models.PositiveIntegerField(default=0, help_text="Lower number = shown first")
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name        = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return f"{self.course_name} ({self.get_cert_type_display()})"

from django.db import models

class Internship(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    # Storing syllabus as a JSON list for easy iteration
    syllabus = models.JSONField(help_text="Enter syllabus items as a list")


    # Image Field
    image = models.ImageField(upload_to='internships/', blank=True, null=True)

    def __str__(self):
        return self.title
    from django.db import models

class SiteOffer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='site_offers/', blank=True, null=True)
    link_url = models.CharField(max_length=200, help_text="e.g., /internships/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models


class DemoCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    demo_link = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class DemoRequest(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    ]

    organization_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

    category = models.ForeignKey(
        DemoCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    custom_requirement = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.category:
            return f"{self.organization_name} - {self.category.name}"
        return f"{self.organization_name} - Custom Request"
