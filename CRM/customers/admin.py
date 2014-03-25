from django.contrib import admin
from customers.models import Customer, Project, Income, Outcome


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Customer Information', {'fields': ('name',
                                             'phone_number',
                                             'website',
                                             'email',
                                             'tasks',
                                             'contact_date')}),
    ]
    inlines = [ProjectInline]
admin.site.register(Customer, CustomerAdmin)


class IncomeInline(admin.TabularInline):
    model = Income
    extra = 2


class OutcomeInline(admin.TabularInline):
    model = Outcome
    extra = 2


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project Information', {'fields': ('customer_name',
                                            'name')}),
    ]
    inlines = [IncomeInline, OutcomeInline]
    list_display = ('customer_name', 'name')
admin.site.register(Project, ProjectAdmin)


class IncomeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Income Information', {'fields': ('project_name',
                                           'date',
                                           'type',
                                           'value',
                                           'work_time',
                                           'Receipt',
                                           'note')}),
    ]
admin.site.register(Income, IncomeAdmin)


class OutcomeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Outcome Information', {'fields': ('project_name',
                                            'date',
                                            'type',
                                            'value',
                                            'note')}),
    ]
admin.site.register(Outcome, OutcomeAdmin)
