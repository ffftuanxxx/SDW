import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
def sendemail(receivers,content):
    send_email([str(receivers)],"verify code",str(content),None)
def send_email(receivers, subject, content, image_path):
    # 读取环境变量中的敏感信息 发送邮箱账户和对应授权码
    sender = '2879907402@qq.com'
    password = 'wyectrxugvevdeca'

    try:
        # 构造邮件对象
        msg = MIMEMultipart()
        msg['From'] = formataddr(['From goliathli@uic.edu.cn', sender])
        msg['Subject'] = subject

        # 添加正文
        text = MIMEText(content, 'plain', 'utf-8')
        msg.attach(text)
        if(image_path!=None):
            # 添加图片附件
            with open(image_path, 'rb') as f:
                mime = mimetypes.guess_type(image_path)[0]
                image = MIMEImage(f.read(), _subtype=mime)
                image.add_header('Content-ID', '<image>')
                image.add_header('Content-Disposition', 'attachment', filename=image_path)
                msg.attach(image)

        # 连接邮箱服务器并登录
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, password)

        # 发送邮件
        for receiver in receivers:
            msg['To'] = formataddr(['FK', receiver])
            server.sendmail(sender, [receiver], msg.as_string())

        server.quit()

        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    # 设置收件人列表、邮件内容和图片路径
    receivers = ['r130026037@mail.uic.edu.cn']
    subject = 'Congraluation!'
    content = 'You just recieve the offer from The University of Hong Kong (HKU), please check more detail information in attachment.'
    image_path = '允许涩涩.jpg'  # 替换为你的图片路径

    # 发送邮件
    if send_email(receivers, subject, content, image_path):
        print('邮件发送成功')
    else:
        print('邮件发送失败')