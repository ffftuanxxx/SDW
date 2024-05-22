from co_ import session, Topic, Subtopic, SubtopicQ

class TopicManager:
    def __init__(self):
        self.session = session

    def create_topic(self, CNumber, topictxt):
        """
        在Topic表中为指定课程创建新主题
        """
        new_topic = Topic(CNumber=CNumber, topictxt=topictxt)
        session.add(new_topic)
        session.commit()
        return new_topic.topicid

    def get_all_topics(self):
        """
        查询Topic表中的所有主题
        """
        topics = session.query(Topic).all()
        return topics

    def create_subtopic(self, topicid, subtxt):
        """
        在Subtopic表中为指定主题创建新子主题
        """
        new_subtopic = Subtopic(topicid=topicid, subtxt=subtxt)
        session.add(new_subtopic)
        session.commit()
        return new_subtopic.subid

    def get_all_subtopics(self):
        """
        查询Subtopic表中的所有子主题
        """
        subtopics = session.query(Subtopic).all()
        return subtopics

    def create_subtopic_question(self, subid, subqtext, qanswer):
        """
        在SubtopicQ表中为指定子主题创建新问题
        """
        new_question = SubtopicQ(subid=subid, subqtext=subqtext, qanswer=qanswer)
        session.add(new_question)
        session.commit()
        return new_question.subqid

    def get_all_subtopic_questions(self):
        """
        查询SubtopicQ表中的所有子主题问题
        """
        questions = session.query(SubtopicQ).all()
        return questions

    def get_topics_by_course(self, CNumber):
        topics = session.query(Topic).filter_by(CNumber=CNumber).all()
        return topics

    def get_subtopics_by_topic(self, topicid):
        subtopics = session.query(Subtopic).filter_by(topicid=topicid).all()
        return subtopics

    def get_subqs_by_subtopic(self, subid):
        subqs = session.query(SubtopicQ).filter_by(subid=subid).all()
        return subqs

    def get_cnumber_by_topicid(self, topicid):
        topic = session.query(Topic).filter_by(topicid=topicid).first()
        if topic:
            return topic.CNumber
        return None

    def get_subtopic_by_id(self, subid):
        subtopic = session.query(Subtopic).filter_by(subid=subid).first()
        return subtopic