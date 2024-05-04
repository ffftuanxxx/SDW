from co_ import HelpTopic, session
def create_helptopic(title, topicq, topica, session):
    """
    在HelpTopic表中创建新帮助主题
    """
    new_topic = HelpTopic(title=title, topicq=topicq, topica=topica)
    session.add(new_topic)
    session.commit()
    print(f"新帮助主题创建成功, topic_id: {new_topic.topic_id}")
    return new_topic.topic_id

def get_helptopic(topic_id, session):
    """
    查询HelpTopic表中的帮助主题
    """
    topic = session.query(HelpTopic).filter_by(topic_id=topic_id).first()
    if not topic:
        print(f"错误: 主题ID {topic_id} 不存在!")
        return None
    return topic

def update_helptopic(topic_id, title, topicq, topica, session):
    """
    更新HelpTopic表中的帮助主题
    """
    topic = session.query(HelpTopic).filter_by(topic_id=topic_id).first()
    if not topic:
        print(f"错误: 主题ID {topic_id} 不存在!")
        return

    topic.title = title
    topic.topicq = topicq
    topic.topica = topica

    session.commit()
    print(f"主题ID {topic_id} 更新成功!")

def delete_helptopic(topic_id, session):
    """
    从HelpTopic表中删除帮助主题
    """
    topic = session.query(HelpTopic).filter_by(topic_id=topic_id).first()
    if not topic:
        print(f"错误: 主题ID {topic_id} 不存在!")
        return

    session.delete(topic)
    session.commit()
    print(f"主题ID {topic_id} 删除成功!")

if __name__ == "__main__":
    # 创建新主题
    new_id = create_helptopic("Python基础", "什么是变量?", "变量用于存储值...", session)
    print(f"新主题ID: {new_id}")

    # 获取主题信息
    topic = get_helptopic(new_id, session)
    print(f"主题: {topic.title}, {topic.topicq}, {topic.topica}")

    # 更新主题
    update_helptopic(new_id, "Python高级", "什么是装饰器?", "装饰器用于修改函数...", session)

    # 删除主题
    delete_helptopic(new_id, session)