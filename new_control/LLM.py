from co_ import LLM, session
def create_llm(answerid, answerimage, llmscore, comments, session):
    """
    在LLM表中创建新记录
    """
    new_llm = LLM(answerid=answerid, answerimage=answerimage, llmscore=llmscore, comments=comments)
    session.add(new_llm)
    session.commit()
    print(f"新LLM记录创建成功, llm_id: {new_llm.llm_id}")
    return new_llm.llm_id

def get_llm(llm_id, session):
    """
    查询LLM表中的记录
    """
    llm = session.query(LLM).filter_by(llm_id=llm_id).first()
    if not llm:
        print(f"错误: LLM ID {llm_id} 不存在!")
        return None
    return llm

def update_llm(llm_id, answerid, answerimage, llmscore, comments, session):
    """
    更新LLM表中的记录
    """
    llm = session.query(LLM).filter_by(llm_id=llm_id).first()
    if not llm:
        print(f"错误: LLM ID {llm_id} 不存在!")
        return

    llm.answerid = answerid
    llm.answerimage = answerimage
    llm.llmscore = llmscore
    llm.comments = comments

    session.commit()
    print(f"LLM ID {llm_id} 更新成功!")

def delete_llm(llm_id, session):
    """
    从LLM表中删除记录
    """
    llm = session.query(LLM).filter_by(llm_id=llm_id).first()
    if not llm:
        print(f"错误: LLM ID {llm_id} 不存在!")
        return

    session.delete(llm)
    session.commit()
    print(f"LLM ID {llm_id} 删除成功!")

def get_all_llms(session):
    """
    从数据库中获取所有LLM记录
    """
    return session.query(LLM).all()

if __name__ == "__main__":
    # 创建新记录
    new_id = create_llm(1, "answer.jpg", 4, "很好的回答", session)
    print(f"新记录ID: {new_id}")

    # 获取记录信息
    llm = get_llm(new_id, session)
    print(f"记录: {llm.answerid}, {llm.answerimage}, {llm.llmscore}, {llm.comments}")

    # 更新记录
    update_llm(new_id, 2, "new.png", 5, "非常棒的回答", session)

    # 删除记录
    delete_llm(new_id, session)