from co_ import Variation,session
def create_variation(vtext, session):
    """
    在Variation表中创建新记录
    """
    new_variation = Variation(vtext=vtext)
    session.add(new_variation)
    session.commit()
    print(f"新变体记录创建成功, vcode: {new_variation.vcode}")
    return new_variation.vcode

def get_variation(vcode, session):
    """
    查询Variation表中的记录
    """
    variation = session.query(Variation).filter_by(vcode=vcode).first()
    if not variation:
        print(f"错误: 变体ID {vcode} 不存在!")
        return None
    return variation

def update_variation(vcode, vtext, session):
    """
    更新Variation表中的记录
    """
    variation = session.query(Variation).filter_by(vcode=vcode).first()
    if not variation:
        print(f"错误: 变体ID {vcode} 不存在!")
        return

    variation.vtext = vtext
    session.commit()
    print(f"变体ID {vcode} 更新成功!")

def delete_variation(vcode, session):
    """
    从Variation表中删除记录
    """
    variation = session.query(Variation).filter_by(vcode=vcode).first()
    if not variation:
        print(f"错误: 变体ID {vcode} 不存在!")
        return

    session.delete(variation)
    session.commit()
    print(f"变体ID {vcode} 删除成功!")


def get_all_variations(session):
    return session.query(Variation).all()



if __name__ == "__main__":
    # 创建新变体
    new_code = create_variation("这是一个测试变体", session)
    print(f"新变体码: {new_code}")

    # 获取变体信息
    variation = get_variation(new_code, session)
    print(f"变体内容: {variation.vtext}")

    # 更新变体
    update_variation(new_code, "已更新的变体内容", session)

    # 删除变体
    delete_variation(new_code, session)