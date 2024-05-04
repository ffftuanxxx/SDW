from flask import render_template, request, redirect, url_for, flash
from app_pre import db, app
from new_control.assign import create_assignq, get_assignq, update_assignq, delete_assignq, get_all_assignqs

@app.route('/assignqs')
def assignqs():
    all_questions = get_all_assignqs(session=db.session)
    return render_template('assignqs.html', questions=all_questions)

@app.route('/create_assignq', methods=['GET', 'POST'])
def create_assignq_view():
    if request.method == 'POST':
        aid = request.form.get('aid')
        qtext = request.form.get('qtext')
        category = request.form.get('category')
        picturename = request.form.get('picturename')
        create_assignq(aid=aid, qtext=qtext, category=category, picturename=picturename, session=db.session)
        flash('Question created successfully!', 'success')
        return redirect(url_for('assignqs'))
    return render_template('create_assignq.html')

@app.route('/update_assignq/<int:qid>', methods=['GET', 'POST'])
def update_assignq_view(qid):
    question = get_assignq(qid=qid, session=db.session)
    if request.method == 'POST':
        aid = request.form.get('aid')
        qtext = request.form.get('qtext')
        category = request.form.get('category')
        picturename = request.form.get('picturename')
        update_assignq(qid=qid, aid=aid, qtext=qtext, category=category, picturename=picturename, session=db.session)
        flash('Question updated successfully!', 'success')
        return redirect(url_for('assignqs'))
    return render_template('update_assignq.html', question=question)

@app.route('/delete_assignq/<int:qid>', methods=['POST'])
def delete_assignq_view(qid):
    delete_assignq(qid=qid, session=db.session)
    flash('Question deleted successfully!', 'success')
    return redirect(url_for('assignqs'))
