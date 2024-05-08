from flask import render_template, request, redirect, url_for, flash, session
from new_control.Course import get_course_name,get_course_num
from app_pre import db,app
from co_ import Course, AssignQ
# 其他代码...
from sqlalchemy import or_
@app.route('/searchcourse', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_name_num = request.form.get('search_name_num')  # 获取名称/编号搜索栏的输入值
        search_category = request.form.get('search_category')  # 获取课程类别搜索栏的输入值
        search_score = request.form.get('search_score')  # 获取分数搜索栏的输入值

        assign_qs = []  # 存储匹配的AssignQ内容

        if search_name_num:  # 如果名称/编号搜索栏有输入值
            # 在Course表中根据CName和CNumber进行搜索
            courses = db.session.query(Course).filter(or_(Course.CName == search_name_num, Course.CNumber == search_name_num)).all()

            # 遍历搜索到的课程列表
            for course in courses:
                # 在AssignQ表中根据CNumber属性搜索行，并将结果添加到assign_qs列表中
                assign_qs += db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all()
                #print(assign_qs, course.CNumber, db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all())

        if search_category:  # 如果课程类别搜索栏有输入值
            # 在Course表中根据Category进行搜索
            courses = db.session.query(Course).filter_by(Ccategory=search_category).all()

            # 遍历搜索到的课程列表
            for course in courses:

                assign_qs += db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all()
                #print(assign_qs, course.CNumber,db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all())

        if search_score:  # 如果分数搜索栏有输入值
            # 在AssignQ表中根据Score进行搜索
            assign_qs += db.session.query(AssignQ).filter_by(score=search_score).all()

        return render_template('searchresult.html', assign_qs=assign_qs)
    else:
        return render_template('searchcourse.html')

@app.route('/searchresult')
def courseresult():
    assign_qs = []  # 存储所有的AssignQ内容

    # 获取所有的AssignQ内容
    assign_qs = db.session.query(AssignQ).all()

    return render_template('searchresult.html', assign_qs=assign_qs)
# @app.route('/searchcourse', methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         search_type = request.form.get('search_type')
#         search_info = request.form.get('search_info')
#
#         if search_type == 'course_name':
#             courses = get_course_name(search_info, db.session)
#         else:
#             course = get_course_num(search_info, db.session)
#             courses = [course] if course else []
#
#         return render_template('courseresult.html', courses=courses)
#     else:
#         return render_template('searchcourse.html')

# @app.route('/courseresult', methods=['POST'])
# def search_results():
#     search_type = request.form.get('search_type')
#     search_info = request.form.get('search_info')
#
#     if search_type == 'course_name':
#         course = get_course_name(search_info, db.session)
#         courses = [course] if course else []
#     else:
#         course = get_course_num(search_info, db.session)
#         courses = [course] if course else []
#
#     return render_template('courseresult.html', courses=courses)




# @app.route('/course/<course_number>/assignments')
# def course_assignments(course_number):
#     course = db.session.query(Course).filter_by(CNumber=course_number).first_or_404()
#     assignments = db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all()
#     return render_template('course_assignments.html', course=course, assignments=assignments)

@app.route('/question_details/<qid>')
def qDetail(qid):
    details = db.session.query(AssignQ).filter_by(qid=qid).first()
    return render_template('quesetion_details.html', details=details)