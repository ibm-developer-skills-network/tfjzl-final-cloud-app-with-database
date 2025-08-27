## Online Course — Assessment Feature (My Contribution)

This repository contains an online course application built with Django. I was responsible for designing and implementing the course assessment feature end-to-end: modeling exam data, rendering questions in the UI, capturing submissions, and evaluating results.

## What I built

- Data model

- Question with a configurable grade

- Choice with is_correct flag (supports single and multiple correct answers)

- Submission that stores selected choices per attempt (M2M → Choice)

- Admin authoring

- Created/registered admin forms so instructors can build exams: Course → Questions → Choices

- Views & URLs

- Course detail view that renders the exam form

- Submission view that validates and persists selected choices

- Result view that evaluates the attempt and displays per-question feedback + total score

- Scoring logic

## Tech stack

Python 3.10+

Django 4.x/5.x

SQLite 

Django Templates + Bootstrap for styling
