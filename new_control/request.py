from co_ import Request, session


class Requestment123():
    def create_request(qid, explanation, scoreupdate, email, session):
        new_request = Request(qid=qid, explanation=explanation,
                              scoreupdate=scoreupdate, approved=0,email=email)
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

    def update_request(qid, explanation, scoreupdate, session):
        """
        更新Request表中的请求记录
        """
        request = session.query(Request).filter_by(requestid=requestid).first()
        if not request:
            print(f"错误: 请求ID {requestid} 不存在!")
            return

        request.qid = qid
        request.explanation = explanation
        request.scoreupdate = scoreupdate
        session.commit()
        print(f"请求ID {requestid} 更新成功!")

    def approve_request_(requestid, approve, session):
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



