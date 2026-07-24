from django.contrib import admin
from .excel_export import export_as_excel
from .admin_export import ExportExcelAdmin

# Register your models here.
from django.contrib import admin
from .models import Course, Service, ServiceDemoLink, Contact
from .models import ClientProject, StudentReview,JobApplication
from .models import WorkshopPhoto, Certificate, ServiceFeature, ServiceFAQ, ProcessStep
from .models import Module
from .models import Internship
from .models import SiteOffer
from .models import UpcomingWorkshop
from .models import DemoCategory, DemoRequest
from .models import DemoBooking, CourseBooking, ServiceBooking, WorkshopRegistration

admin.site.register(ClientProject)
admin.site.register(StudentReview)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(UpcomingWorkshop)

class ServiceDemoLinkInline(admin.TabularInline):
    model = ServiceDemoLink
    extra = 1
    fields = ('title', 'image', 'url', 'category', 'technologies', 'description', 'is_featured', 'order')

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

class ServiceFAQInline(admin.TabularInline):
    model = ServiceFAQ
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [ServiceDemoLinkInline, ServiceFeatureInline, ServiceFAQInline]

@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    ordering = ('order',) 

admin.site.register(Contact)
from django.contrib import admin
from .models import Career

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('role', 'employment_type', 'salary', 'posted_on')
    list_filter = ('employment_type',)
    search_fields = ('role',)


@admin.register(JobApplication)
class JobApplicationAdmin(ExportExcelAdmin, admin.ModelAdmin):

    list_display = (
        "full_name",
        "career",
        "email",
        "mobile",
        "education",
        "year_passed_out",
        "applied_on",
    )

    search_fields = (
        "full_name",
        "email",
        "mobile",
    )

    list_filter = (
        "career",
        "applied_on",
    )

    ordering = ("-applied_on",)

    actions = [export_as_excel]


@admin.register(CourseBooking)
class CourseBookingAdmin(ExportExcelAdmin, admin.ModelAdmin):

    list_display = (
        "name",
        "course",
        "email",
        "mobile",
        "education",
        "year_passed",
        "amount",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "mobile",
        "course",
    )

    list_filter = (
        "course",
        "education",
        "created_at",
    )

    ordering = ("-created_at",)

    actions = [export_as_excel]


@admin.register(WorkshopRegistration)
class WorkshopRegistrationAdmin(ExportExcelAdmin, admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "mobile",
        "gender",
        "participation_mode",
        "present_address",
        "year_of_study",
        "college_name",
        "degree",
        "department",
        "passed_out_year",
        "interested_domains",
        "technical_skill",
        "technical_skill_other",
        "demo_interest",
        "demo_interest_other",
        "demo_mode",
        "preferred_demo_time",
        "consent",
        "queries",
        "referred_by",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "mobile",
        "college_name",
        "department",
        "degree",
        "interested_domains",
        "referred_by",
    )

    list_filter = (
        "gender",
        "participation_mode",
        "technical_skill",
        "demo_interest",
        "demo_mode",
        "consent",
        "created_at",
    )

    readonly_fields = ("created_at",)

    ordering = ("-created_at",)

    actions = [export_as_excel]


@admin.register(ServiceBooking)
class ServiceBookingAdmin(ExportExcelAdmin, admin.ModelAdmin):
    list_display = (
        "full_name",
        "service_name",
        "email",
        "mobile",
        "preferred_date",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "mobile",
        "service_name",
    )

    list_filter = (
        "service_name",
        "created_at",
    )

    readonly_fields = ("created_at",)

    ordering = ("-created_at",)

    actions = [export_as_excel]


# from .models import Course, CourseBooking

@admin.register(WorkshopPhoto)
class WorkshopPhotoAdmin(admin.ModelAdmin):
    list_display  = ('title', 'event_date', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    list_filter   = ('event_date',)
    ordering      = ('order', '-created_at')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display  = ('course_name', 'cert_type', 'order', 'created_at')
    list_editable = ('order',)
    list_filter   = ('cert_type',)
    search_fields = ('course_name',)
    ordering      = ('order', '-created_at')

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'price', 'duration')
  
    search_fields = ('title',)


@admin.register(SiteOffer)
class SiteOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')

@admin.register(DemoCategory)
class DemoCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "demo_link", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(DemoRequest)
class DemoRequestAdmin(ExportExcelAdmin, admin.ModelAdmin):
    list_display = (
        "organization_name",
        "email",
        "mobile",
        "category",
        "status",
        "created_at",
    )

    list_filter = ("status", "category")
    search_fields = (
        "organization_name",
        "email",
        "mobile",
        "custom_requirement",
    )

    readonly_fields = ("created_at",)

    actions = [export_as_excel]


@admin.register(DemoBooking)
class DemoBookingAdmin(ExportExcelAdmin, admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "mobile",
        "education",
        "source",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "mobile",
    )

    list_filter = (
        "education",
        "created_at",
    )

    ordering = ("-created_at",)

    actions = [export_as_excel]

