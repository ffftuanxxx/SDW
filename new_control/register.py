"""
密码必须要大写小写和数字，邮箱不能重复
"""
import re
from co_ import User, session

class Register123():
    def create_user(uclass, email, pd, session):
        # 验证 uclass 是否为 0、1 或 2
        if uclass not in [0, 1, 2]:
            print("错误: uclass 必须为 0、1 或 2")
            return

        # 验证 email 格式
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            print("错误: 无效的 email 格式")
            return

        # 验证 pd 包含大小写和数字
        if not any(char.isdigit() for char in pd) or not any(char.isupper() for char in pd) or not any(
                char.islower() for char in pd):
            print("错误: pd 必须包含大小写和数字")
            return

        # 检查 email 是否已存在
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            print("错误: email 已存在")
            return

        # 创建新用户
        new_user = User(uclass=uclass, email=email, pd=pd)
        session.add(new_user)
        session.commit()
        print(f"新用户创建成功! uid: {new_user.uid}")
        return new_user.uid

    def delete_user(email, session):
        """
        删除用户
        """
        # 查找要删除的用户
        user = session.query(User).filter_by(email=email).first()

        # 如果用户不存在
        if not user:
            print(f"错误: 用户ID {email} 不存在")
            return

        # 删除用户
        session.delete(user)
        session.commit()
        print(f"用户ID {email} 删除成功")

    def update_user(uid, uclass, email, pd, session):
        """
        修改用户信息
        """
        # 查找要修改的用户
        user = session.query(User).filter_by(uid=uid).first()

        # 如果用户不存在
        if not user:
            print(f"错误: 用户ID {uid} 不存在")
            return

        # 验证新uclass
        if uclass not in [0, 1, 2]:
            print("错误: uclass必须为0、1或2")
            return

        # 验证新邮箱格式
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            print("错误: 无效的邮箱格式")
            return

        # 验证新密码要求
        if not any(char.isdigit() for char in pd) or not any(char.isupper() for char in pd) or not any(
                char.islower() for char in pd):
            print("错误: 密码必须包含大小写和数字")
            return

        # 检查新邮箱是否已存在
        existing_user = session.query(User).filter(User.uid != uid, User.email == email).first()
        if existing_user:
            print("错误: 邮箱已存在")
            return

        # 修改用户信息
        user.uclass = uclass
        user.email = email
        user.pd = pd

        session.commit()
        print(f"用户ID {uid} 修改成功")

    def get_user(uid, session):
        """
        查询用户信息
        """
        # 查找用户
        user = session.query(User).filter_by(uid=uid).first()

        # 如果用户不存在
        if not user:
            print(f"错误: 用户ID {uid} 不存在")
            return None

        return user

    def is_password_correct(email, password, session):
        """
        检查用户密码是否正确
        """
        # 查找用户
        user = session.query(User).filter_by(email=email).first()

        # 如果用户不存在
        if not user:
            print(f"错误: 用户 {email} 不存在")
            return False

        # 检查密码是否匹配
        if user.pd == password:
            return True, user.uclass
        else:
            return False, -1

