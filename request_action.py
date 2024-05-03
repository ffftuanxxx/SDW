from flask import render_template, request, redirect, url_for, flash
from new_control.register import create_user
from app_pre import db,app
from new_control.request import create_request,get_all_requests,approve_request_

@app.route('/submit_request', methods=['GET', 'POST'])
def submit_request():
    if request.method == 'POST':
        qid = request.form.get('qid')
        courseid = request.form.get('courseid')
        explanation = request.form.get('explanation')
        scoreupdate = request.form.get('scoreupdate')
        requesttype = request.form.get('requesttype')

        try:
            qid = int(qid)
            courseid = int(courseid)
            scoreupdate = int(scoreupdate)

            new_request = create_request(qid=qid, courseid=courseid, explanation=explanation,
                                  scoreupdate=scoreupdate, requesttype=requesttype,session=db.session)
            #print(1)
            flash('Request submitted successfully!', 'success')
            return redirect(url_for('submit_request'))
        except ValueError:
            flash('Invalid input values. Please enter valid integers for qid, courseid, and scoreupdate.', 'error')
        except Exception as e:
            flash(str(e), 'error')

    return render_template('request.html')

@app.route('/approve_request', methods=['GET', 'POST'])
def approve_request():
    requests = get_all_requests(db.session)
    return render_template('approve_request.html', requests=requests)

@app.route('/approve_request_action/<int:request_id>', methods=['GET', 'POST'])
def approve_request_action(request_id):
    request = approve_request_(request_id,1,db.session)
    if request:
        # 处理批准请求的逻辑
        return redirect(url_for('approve_request'))
    else:
        return 'Request not found'

@app.route('/reject_request_action/<int:request_id>', methods=['GET', 'POST'])
def reject_request_action(request_id):
    request = approve_request_(request_id,2,db.session)
    print(request)
    if request:
        # 处理拒绝请求的逻辑
        return redirect(url_for('approve_request'))
    else:
        return 'Request not found'
