from co_ import Request, session
def create_request(qid, courseid, explanation, scoreupdate, requesttype, session):
    """
    在Request表中创建新请求记录
    """
    new_request = Request(qid=qid, courseid=courseid, explanation=explanation,
                          scoreupdate=scoreupdate, requesttype=requesttype)
    session.add(new_request)
    session.commit()
    print(f"新请求创建成功, requestid: {new_request.requestid}")
    return new_request.requestid

def get_request(requestid, session):
    """
    查询Request表中的请求记录
    """
    request = session.query(Request).filter_by(requestid=requestid).first()
    if not request:
        print(f"错误: 请求ID {requestid} 不存在!")
        return None
    return request
def get_all_requests(session):
    """
    查询Request表中的所有请求记录
    """
    requests = session.query(Request).all()
    if not requests:
        print("错误: Request表中没有任何记录!")
        return None
    return requests
def update_request(requestid, qid, courseid, explanation, scoreupdate, requesttype, session):
    """
    更新Request表中的请求记录
    """
    request = session.query(Request).filter_by(requestid=requestid).first()
    if not request:
        print(f"错误: 请求ID {requestid} 不存在!")
        return

    request.qid = qid
    request.courseid = courseid
    request.explanation = explanation
    request.scoreupdate = scoreupdate
    request.requesttype = requesttype

    session.commit()
    print(f"请求ID {requestid} 更新成功!")

def approve_request_(requestid,approve, session):
    """
    更新Request表中的请求记录
    """
    request = session.query(Request).filter_by(requestid=requestid).first()
    if not request:
        print(f"错误: 请求ID {requestid} 不存在!")
        return

    request.approved = approve

    session.commit()
    print(f"请求ID {requestid} 更新成功!")
    return requestid

def delete_request(requestid, session):
    """
    从Request表中删除请求记录
    """
    request = session.query(Request).filter_by(requestid=requestid).first()
    if not request:
        print(f"错误: 请求ID {requestid} 不存在!")
        return

    session.delete(request)
    session.commit()
    print(f"请求ID {requestid} 删除成功!")

if __name__ == "__main__":
    # 创建新请求
    new_id = create_request(1, 101, "需要帮助解答", 0, "学习请求", session)
    print(f"新请求ID: {new_id}")

    # 获取请求信息
    request = get_request(new_id, session)
    print(f"请求: {request.qid}, {request.courseid}, {request.explanation}, {request.scoreupdate}, {request.requesttype}")

    # 更新请求
    update_request(new_id, 2, 102, "修改后的说明", 1, "考试申请", session)

    # 删除请求
    delete_request(new_id, session)