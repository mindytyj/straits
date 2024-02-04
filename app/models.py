# from . import db
#
# class Staff(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     courses = db.relationship('Course', backref='staff', lazy=True)
#
# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=True)
