from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# إعداد العرض المتداخل (Inline) للدروس والخيارات والأسئلة
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# تخصيص عرض الكورسات لتشمل الدروس
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# تخصيص عرض الأسئلة لتشمل الخيارات (ChoiceInline)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# تسجيل جميع الموديلات السبعة في لوحة التحكم
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)