import yagmail


def send_email(email_account, email_password, title, content):

    yag_server = yagmail.SMTP(user=email_account, password=email_password, host='smtp.qq.com')

    # 发送对象列表
    email_to = [email_account]
    email_title = title
    email_content = content

    # 发送邮件
    yag_server.send(email_to, email_title, email_content)

    print("邮件发送完成")
    print("执行完成")
