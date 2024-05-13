from flask import render_template, request, redirect, url_for, flash
from new_control.assign import assignq
from app_pre import db,app
from co_ import AssignQ, session, Course

@app.route('/create_assignment/<cnumber>', methods=['GET', 'POST'])
def create_assignq_route(cnumber):
    error_message = None  # 初始化错误信息变量
    if request.method == 'POST':
        qtext = request.form.get('qtext')
        category = request.form.get('category')
        picturename = request.form.get('picturename')
        score = request.form.get('score')  # 从表单获取分数
        try:
            score = float(score)  # 确保分数是浮点数
            if score < 5:
                error_message = '分数最低为5。'  # 设置错误消息
                return render_template('create_assignment.html', error_message=error_message)
            new_question = assignq.create(cnumber, qtext, category, picturename, score)
            flash('新问题创建成功', 'success')
            return redirect(url_for('courses'))  # 假设 courses_list 是课程列表的路由
        except ValueError:
            error_message = '请输入有效的数字。'
        except Exception as e:
            error_message = str(e)
            print(e)

    return render_template('create_assignment.html', error_message=error_message)

