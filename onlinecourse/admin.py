from django.contrib import admin
from .models import (
    Course, Lesson, Instructor, Learner,
    Question, Choice, Submission
)

# Inline pour les choix d'une question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1  # nombre de champs vides affichés par défaut

# Inline pour les questions d'un cours
class QuestionInline(admin.StackedInline):
    model = Question
    inlines = [ChoiceInline]  # permet d'afficher les choix dans la question
    extra = 1

# Inline pour les leçons dans un cours
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Admin pour les cours
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]  # Leçons et questions dans la page cours
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Admin pour les leçons
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Admin pour les questions
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # Choix visibles directement dans la question
    list_display = ['question_text', 'course', 'grade_point']

# Admin pour les choix
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'question', 'is_correct']

# Admin pour les submissions
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['enrollment']

# Enregistrement des modèles dans l'admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
