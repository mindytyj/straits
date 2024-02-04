# from flask import render_template, redirect, url_for, flash, request
# from . import db, create_app
# from .models import Staff, Course
# from .forms import CourseSelectionForm, ClockInForm
#
# app = create_app()
#
# @app.route('/')
# def index():
#     return render_template('dashboard.html')
#
# @app.route('/select_course', methods=['GET', 'POST'])
# def select_course():
#     form = CourseSelectionForm()
#     form.course.choices = [(c.id, c.title) for c in Course.query.all()]
#     if form.validate_on_submit():
#         course_id = form.course.data
#         # Example action: assign course to staff (you need to handle staff identification)
#         flash('Course selected successfully.')
#         return redirect(url_for('index'))
#     return render_template('select_courses.html', form=form)
#
# # Implement the clock_in route similarly
