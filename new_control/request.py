from co_ import Request, session


class Requestment123():
    def create_request(qid, explanation, scoreupdate, email, session):
        new_request = Request(qid=qid, explanation=explanation,
                              scoreupdate=scoreupdate, approved=0,email=email)
        session.add(new_request)
        return new_request.requestid

    def get_request(requestid, session):
        """
        查询Request表中的请求记录
        """
        request = session.query(Request).filter_by(requestid=requestid).first()
        if not request:
            return None
        return request

    def get_all_requests(session):
        """
        查询Request表中的所有请求记录
        """
        requests = session.query(Request).all()
        if not requests:
            return None
        return requests

    def update_request(qid, explanation, scoreupdate, session):
        """
        更新Request表中的请求记录
        """
        request = session.query(Request).filter_by(requestid=requestid).first()
        if not request:
            return

        request.qid = qid
        request.explanation = explanation
        request.scoreupdate = scoreupdate
        session.commit()

    def approve_request_(requestid, approve, session):
        """
        更新Request表中的请求记录
        """
        request = session.query(Request).filter_by(requestid=requestid).first()
        if not request:
            return

        request.approved = approve

        session.commit()
        return requestid



