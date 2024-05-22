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
        course_numbers = set()

        # 合并查询条件，减少数据库查询次数
        if search_name_num:
            if any(char in search_name_num for char in '#@!$%^&*()'):
                flash('输入包含非法字符,请重新输入。', 'warning')
                return render_template('searchcourse.html')
            else:
                name_num_courses = db.session.query(Course).filter(
                    or_(Course.CName == search_name_num, Course.CNumber == search_name_num)).all()
                course_numbers.update([course.CNumber for course in name_num_courses])

        if search_category:
            category_courses = db.session.query(Course).filter_by(Ccategory=search_category).all()
            course_numbers.update([course.CNumber for course in category_courses])

        if search_score:
            try:
                valid_score = float(search_score)
                if not (0 <= valid_score <= 100):
                    flash('输入的分数无效,请输入0到100之间的数值。', 'warning')
                else:
                    score_assign_qs = db.session.query(AssignQ).filter_by(score=valid_score).all()
                    assign_qs.extend(score_assign_qs)
                    course_numbers.update([assign_q.CNumber for assign_q in score_assign_qs])
            except ValueError:
                flash('请输入一个有效的数字作为分数。', 'warning')

        # 查询相关课程的分配查询和主题
        if course_numbers:
            assign_qs.extend(db.session.query(AssignQ).filter(AssignQ.CNumber.in_(course_numbers)).all())
            topics.extend(db.session.query(Topic).filter(Topic.CNumber.in_(course_numbers)).all())

        if not assign_qs and not topics:
            flash('没有找到相关的分配查询或主题,请检查输入。', 'warning')

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