from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    enrollment = Enrollment.objects.get(user=user, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    selected_ids = request.POST.getlist('choice')

    for choice_id in selected_ids:
        choice = Choice.objects.get(pk=int(choice_id))
        submission.choices.add(choice)

    return redirect(
        reverse(
            'onlinecourse:show_exam_result',
            args=(course.id, submission.id)
        )
    )


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    selected_ids = submission.choices.values_list('id', flat=True)

    total_grade = 0
    score = 0

    for question in course.question_set.all():
        total_grade += question.grade
        if question.is_get_score(selected_ids):
            score += question.grade

    context = {
        'course': course,
        'submission': submission,
        'choices': submission.choices.all(),
        'score': score,
        'total_grade': total_grade,
        'passed': score >= total_grade * 0.5
    }

    return render(
        request,
        'onlinecourse/exam_result_bootstrap.html',
        context
    )