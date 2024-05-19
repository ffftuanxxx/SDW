from flask import render_template, request, redirect, url_for, flash, session
from new_control.Course import Course1
from app_pre import db,app
from co_ import Course, AssignQ,Topic
# 其他代码...
from sqlalchemy import or_
@app.route('/searchcourse', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_name_num = request.form.get('search_name_num')
        search_category = request.form.get('search_category')
        search_score = request.form.get('search_score')

        assign_qs = []
        topics = []

        if search_name_num:
            if any(char in search_name_num for char in '#@!$%^&*()'):
                flash('输入包含非法字符,请重新输入。', 'warning')
            else:
                courses = db.session.query(Course).filter(
                    or_(Course.CName == search_name_num, Course.CNumber == search_name_num)).all()

                if not courses:
                    flash('没有找到相关的课程,请尝试其他关键词。', 'warning')
                else:
                    for course in courses:
                        assign_qs += db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all()
                        topics += db.session.query(Topic).filter_by(CNumber=course.CNumber).all()

                    if not assign_qs and not topics:
                        flash('没有找到相关的分配查询或主题,请检查输入。', 'warning')

        if search_category:
            courses = db.session.query(Course).filter_by(Ccategory=search_category).all()

            for course in courses:
                assign_qs += db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all()
                topics += db.session.query(Topic).filter_by(CNumber=course.CNumber).all()

        if search_score:
            try:
                valid_score = float(search_score)
                if not (0 <= valid_score <= 100):
                    flash('输入的分数无效,请输入0到100之间的数值。', 'warning')
                else:
                    assign_qs += db.session.query(AssignQ).filter_by(score=valid_score).all()

                    if not assign_qs:
                        flash('没有找到匹配的分数记录,请尝试其他分数。', 'warning')
            except ValueError:
                flash('请输入一个有效的数字作为分数。', 'warning')

        return render_template('searchresult.html', assign_qs=assign_qs, topics=topics)
    else:
        return render_template('searchcourse.html')

@app.route('/searchresult')
def courseresult():
    assign_qs = []  # 存储所有的AssignQ内容

    # 获取所有的AssignQ内容
    assign_qs = db.session.query(AssignQ).all()

    return render_template('searchresult.html', assign_qs=assign_qs)

@app.route('/question_details/<qid>')
def qDetail(qid):
    details = db.session.query(AssignQ).filter_by(qid=qid).first()
    return render_template('quesetion_details.html', details=details)