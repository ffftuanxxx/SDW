from flask import render_template, request, redirect, url_for, flash, session
from new_control.Course import Course1
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
            # 检查输入是否包含特殊字符
            if any(char in search_name_num for char in '#@!$%^&*()'):
                flash('输入包含非法字符，请重新输入。', 'warning')
            else:
                # 在Course表中根据CName和CNumber进行搜索
                courses = db.session.query(Course).filter(
                    or_(Course.CName == search_name_num, Course.CNumber == search_name_num)).all()

                if not courses:  # 如果没有找到任何课程
                    flash('没有找到相关的课程，请尝试其他关键词。', 'warning')
                else:
                    # 遍历搜索到的课程列表
                    for course in courses:
                        # 在AssignQ表中根据CNumber属性搜索行，并将结果添加到assign_qs列表中
                        assign_qs += db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all()

                    if not assign_qs:  # 如果没有相关的AssignQ记录
                        flash('没有找到相关的分配查询，请检查输入。', 'warning')
                    # 如果需要，可以在这里处理assign_qs
        if search_category:  # 如果课程类别搜索栏有输入值
            # 在Course表中根据Category进行搜索
            courses = db.session.query(Course).filter_by(Ccategory=search_category).all()

            # 遍历搜索到的课程列表
            for course in courses:

                assign_qs += db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all()
                #print(assign_qs, course.CNumber,db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all())

        if search_score:  # 如果分数搜索栏有输入值
            # 检查输入是否为合法的分数
            try:
                valid_score = float(search_score)  # 尝试将输入转换为浮点数
                if not (0 <= valid_score <= 100):  # 检查分数是否在0到100之间
                    flash('输入的分数无效，请输入0到100之间的数值。', 'warning')
                else:
                    # 在AssignQ表中根据Score进行搜索
                    assign_qs += db.session.query(AssignQ).filter_by(score=valid_score).all()

                    if not assign_qs:  # 如果没有找到任何相关的记录
                        flash('没有找到匹配的分数记录，请尝试其他分数。', 'warning')
            except ValueError:  # 如果转换失败，说明输入不是一个合法的数字
                flash('请输入一个有效的数字作为分数。', 'warning')

        return render_template('searchresult.html', assign_qs=assign_qs)
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