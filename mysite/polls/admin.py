from django.contrib import admin

# Register your models here.
from .models import Question, Choices

admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls Admin Area"
admin.site.index_title = "Welcome to Polls admin area"


# admin.site.register(Question)
# admin.site.register(Choices)

class ChoicesInline(admin.TabularInline):
    model = Choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': 
    ['collapse']}),]
    inlines = [ChoicesInline]


admin.site.register(Question, QuestionAdmin)    
