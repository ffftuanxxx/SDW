from co_ import LLM, session,comment


class LLM222:
    def create_llm(homeproblem, usedanswer, answerimage, llmscore, comments, CNumber, qid, session):
        """
        在LLM表中创建新记录
        """
        print("new llm")
        new_llm = LLM(homeproblem=homeproblem, usedanswer=usedanswer, answerimage=answerimage, llmscore=llmscore,
                      comments=comments, CNumber=CNumber, qid=qid)
        session.add(new_llm)
        session.commit()
        return new_llm.llm_id
    def create_comment(llm_id, com, session):
        """
        在LLM表中创建新记录
        """
        new_c = comment(llm_id=llm_id,comments=com)
        session.add(new_c)
        session.commit()
        return new_c.commentid

    def get_comment(llm_id, session):
        """
        查询com表中的记录
        """
        com = session.query(comment).filter_by(llm_id=llm_id).all()
        if not com:
            return None
        return com
    def get_llm(llm_id, session):
        """
        查询LLM表中的记录
        """
        llm = session.query(LLM).filter_by(llm_id=llm_id).first()
        if not llm:
            return None
        return llm

    def update_llm(llm_id, llmscore, comments, session):
        """
        更新LLM表中的记录
        """
        llm = session.query(LLM).filter_by(llm_id=llm_id).first()
        if not llm:
            return

        llm.llmscore = llmscore
        llm.comments = comments

        session.commit()

    def delete_llm(llm_id, session):
        """
        从LLM表中删除记录
        """
        llm = session.query(LLM).filter_by(llm_id=llm_id).first()
        if not llm:
            return

        session.delete(llm)
        session.commit()

    def get_all_llms(session):
        """
        从数据库中获取所有LLM记录
        """
        return session.query(LLM).all()

