from flask import render_template, request, redirect, url_for, flash
from app_pre import db, app
from new_control.topic import TopicManager
from sqlalchemy.exc import PendingRollbackError

@app.route('/topics/<string:CNumber>', methods=['GET', 'POST'])
def topic_list(CNumber):
    if request.method == 'POST':
        topictxt = request.form['topictxt']
        topic_id = TopicManager().create_topic(CNumber, topictxt)
        return redirect(url_for('topic_list', CNumber=CNumber))

    topics = TopicManager().get_topics_by_course(CNumber)
    return render_template('topic_list.html', topics=topics, CNumber=CNumber)


@app.route('/subtopics/<int:topicid>', methods=['GET', 'POST'])
def subtopic_list(topicid):
    if request.method == 'POST':
        subtxt = request.form['subtxt']
        subtopic_id = TopicManager().create_subtopic(topicid, subtxt)
        return redirect(url_for('subtopic_list', topicid=topicid))

    session = None  # 确保 session 变量被定义
    try:
        session = db.session
        session.autocommit = True
        subtopics = TopicManager().get_subtopics_by_topic(topicid)
    except PendingRollbackError:
        session.rollback()
        subtopics = TopicManager().get_subtopics_by_topic(topicid)
    finally:
        if session is not None:  # 检查 session 是否为 None
            session.close()

    CNumber = TopicManager().get_cnumber_by_topicid(topicid)
    return render_template('subtopic_list.html', subtopics=subtopics, topicid=topicid, CNumber=CNumber)


@app.route('/subqs/<int:subid>', methods=['GET', 'POST'])
def subq_list(subid):
    if request.method == 'POST':
        subqtext = request.form['subqtext']
        qanswer = request.form['qanswer']
        subq_id = TopicManager().create_subtopic_question(subid, subqtext, qanswer)
        return redirect(url_for('subq_list', subid=subid))

    subqs = TopicManager().get_subqs_by_subtopic(subid)
    subtopic = TopicManager().get_subtopic_by_id(subid)  # 获取子主题对象
    return render_template('subq_list.html', subqs=subqs, subtopic=subtopic)