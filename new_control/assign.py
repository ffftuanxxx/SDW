"""
修改AssignQ
"""
from co_ import AssignQ, session, Course

class assignq():
    def __init__(self):
        self.session = session


    def create(CNumber, qtext, category, picturename, score):
        """
        在AssignQ表中为指定课程创建新问题
        """
        course = session.query(Course).filter_by(CNumber=CNumber).first()
        if not course:
            print(f"错误: 课程编号 '{CNumber}' 不存在!")
            return None

        new_question = AssignQ(CNumber=CNumber, qtext=qtext, category=category, picturename=picturename, score=score)
        session.add(new_question)
        session.commit()
        print(f"新问题创建成功, qid: {new_question.qid}")
        return new_question.qid


    def get(qid):
        """
        查询AssignQ表中的问题
        """
        # 查找问题
        question = session.query(AssignQ).filter_by(qid=qid).first()

        # 如果问题不存在
        if not question:
            print(f"错误: 问题ID {qid} 不存在!")
            return None

        return question

