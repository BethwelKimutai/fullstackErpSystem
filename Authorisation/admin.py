from django.contrib import admin
from django.core.mail import send_mail

from .models import Company, User


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_approved']
    actions = ['approve_companies']

    def approve_companies(self, request, queryset):
        for company in queryset:
            if not company.is_approved:
                company.is_approved = True
                company.save()

                # Create an admin user for the approved company
                admin_user = User.objects.create(
                    username='admin',
                    email=company.email,
                    company=company,
                    is_manager=True,
                    is_superuser=False,
                    is_staff=True
                )
                admin_user.set_password('jikoTrack@2024')
                admin_user.save()

                send_mail(
                    'Registration Approved',
                    'Your registration has been approved. Here are your admin credentials:\n\nUsername: '
                    'admin\nPassword: jikoTrack@2024',
                    'from@example.com',
                    [company.email],
                    fail_silently=False,
                )

    approve_companies.short_description = "Approve selected companies and create admin user"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'company', 'is_manager', 'is_accounting_manager', 'is_inventory_manager',
                    'is_purchase_manager']
