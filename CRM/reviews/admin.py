from django.contrib import admin
from reviews.models import Review, Question


class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Information', {'fields': ('review',
                                             'date',
                                             'text')}),
    ]


admin.site.register(Question, QuestionsAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Review Information', {'fields': ('name',
                                           'customer_name',
                                           'date',
                                           'rate',
                                           'note')}),
    ]


admin.site.register(Review, ReviewsAdmin)