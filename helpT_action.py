from flask import render_template, request, redirect, url_for, flash
from app_pre import db, app
from new_control.HelpTopic import create_helptopic, get_helptopic, update_helptopic, delete_helptopic, get_all_helptopics

@app.route('/helptopics')
def helptopics():
    all_topics = get_all_helptopics(session=db.session)
    return render_template('helptopics.html', topics=all_topics)

@app.route('/create_helptopic', methods=['GET', 'POST'])
def create_helptopic_view():
    cnumber = request.args.get('CNumber')  # 从 URL 参数获取 CNumber
    if request.method == 'POST':
        title = request.form.get('title')
        topicq = request.form.get('topicq')
        topica = request.form.get('topica')
        # 将 CNumber 传递给创建函数
        create_helptopic(title=title, topicq=topicq, topica=topica, cnumber=cnumber, session=db.session)
        flash('Help topic created successfully!', 'success')
        return redirect(url_for('courses'))
    # 将 CNumber 传递到模板，以便在需要时使用
    return render_template('create_helptopic.html', CNumber=cnumber)


@app.route('/update_helptopic/<int:topic_id>', methods=['GET', 'POST'])
def update_helptopic_view(topic_id):
    topic = get_helptopic(topic_id=topic_id, session=db.session)
    if request.method == 'POST':
        title = request.form.get('title')
        topicq = request.form.get('topicq')
        topica = request.form.get('topica')
        update_helptopic(topic_id=topic_id, title=title, topicq=topicq, topica=topica, session=db.session)
        flash('Help topic updated successfully!', 'success')
        return redirect(url_for('helptopics'))
    return render_template('update_helptopic.html', topic=topic)

@app.route('/delete_helptopic/<int:topic_id>', methods=['POST'])
def delete_helptopic_view(topic_id):
    delete_helptopic(topic_id=topic_id, session=db.session)
    flash('Help topic deleted successfully!', 'success')
    return redirect(url_for('helptopics'))
