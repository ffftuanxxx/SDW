from flask import render_template, request, redirect, url_for, flash,session
from new_control.register import Register123
from app_pre import db,app
from new_control.request import Requestment123
from co_ import Request
from co_ import AssignQ, Variation, HelpTopic,Topic
@app.route('/submit_request', methods=['GET', 'POST'])
def submit_request():
    qid = request.args.get('qid', default=None, type=int)
    if request.method == 'POST':
        explanation = request.form.get('explanation')
        scoreupdate = request.form.get('scoreupdate')
        try:
            qid = int(qid)
            scoreupdate = int(scoreupdate)

            Requestment123.create_request(qid=qid, explanation=explanation,
                                  scoreupdate=scoreupdate,email=session.get('email'),session=db.session)
            print(1)
            flash('Request submitted successfully!', 'success')
            return redirect(url_for('teacher'))
        except ValueError:
            flash('Invalid input values. Please enter valid integers for qid, courseid, and scoreupdate.', 'error')
            print(e)
        except Exception as e:
            flash(str(e), 'error')
            print(e)

    return render_template('request.html')


@app.route('/approve_request0', methods=['GET'])
def approve_request0():
    requests = Requestment123.get_all_requests(db.session)
    return render_template('approve_request0.html', requests=requests)


@app.route('/approve_request/<int:request_id>', methods=['POST'])
def approve_request(request_id):
    # 查询请求
    req = db.session.query(Request).filter_by(requestid=request_id).first()
    if req:
        req.approved = 1  # 标记请求为已批准
        db.session.commit()

        # 从AssignQ获取与Request相关的条目
        assign_q = db.session.query(AssignQ).filter_by(qid=req.qid).first()
        if assign_q:
            # 更新AssignQ中的分数
            z = assign_q.score
            assign_q.score = req.scoreupdate  # 假设scoreupdate是要增加的分数
            db.session.commit()

            # 检查并更新或创建Variation记录
            variation = db.session.query(Variation).filter_by(qid=req.qid).first()
            if variation:
                # 如果已存在记录，更新之
                variation.vtext = assign_q.qtext  # 假设AssignQ有qtext字段
                variation.vcode = z
            else:
                # 如果不存在，创建新记录
                new_variation = Variation(
                    vcode=z,  # 根据需要设置合适的vcode
                    vtext=assign_q.qtext,  # 假设AssignQ有qtext字段
                    qid=req.qid
                )
                db.session.add(new_variation)
            db.session.commit()
            flash('Request has been approved, score updated, and variation handled successfully!', 'success')
        else:
            flash('No related record found in AssignQ.', 'error')
    else:
        flash('Request not found.', 'error')

    return redirect(url_for('approve_request0'))


@app.route('/approve_request1')
def helptopics_view():
    helptopics = db.session.query(Topic).all()  # 假设 HelpTopic 是你的模型名称
    return render_template('approve_request1.html', helptopics=helptopics)


@app.route('/approve_topic/<int:topicid>', methods=['POST'])
def approve_topic(topicid):
    # 在数据库中查找对应的主题
    topics = db.session.query(Topic).all()
    topic = None
    for t in topics:
        if t.topicid == topicid:
            topic = t
            break

    if topic:
        # 将主题的 approved 字段设为 1
        topic.approved = 1
        db.session.commit()
        flash('Subject approved', 'success')
    else:
        flash('No corresponding topic found', 'error')

    return redirect(url_for('back'))