# login.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import socket
import ipaddress
from send_email import send_email


def login(username, password, email_account, email_password):
    # username = None
    # password = None
    hostname = socket.gethostname()
    # ipaddr = socket.gethostbyname(hostname)
    # print("IP: ", IPAddr)
    network = ipaddress.ip_network("10.100.0.0/18")
    current_ip = ipaddress.ip_address(socket.gethostbyname(hostname))

    if current_ip in network:
        print("校园网有线连接中")

        driver = webdriver.Chrome()
        driver.get("http://10.1.1.131/")
        print("打开登录界面")

        time.sleep(2)
        try:
            driver.find_element(By.CLASS_NAME, "btn-logout")
            # 读取账户信息
            used_flow = (driver.find_element(By.ID, "used-flow")).text
            print("读取流量完成")
            rest_pocket = (driver.find_element(By.ID, "balance")).text
            print("读取余额完成")
            print("校园网已登录")
            driver.quit()

            send_email(email_account, email_password, title="校园网已登录",
                       content="校园网余额：{}\n已使用流量：{}\n当前IP：{}".format(rest_pocket, used_flow, str(current_ip)))
            return str(current_ip), str(used_flow), str(rest_pocket)
        except:
            # 查找账号输入框元素
            username_input = driver.find_element(By.ID, "username")
            username_input.send_keys(username)
            # 查找密码输入框元素
            password_input = driver.find_element(By.ID, "password")
            password_input.send_keys(password)
            print("账号密码填充完成")
            # 点击登录按键
            login_key = driver.find_element(By.CLASS_NAME, "btn-login")
            login_key.click()
            print("登录完成")

            time.sleep(2)
            # 读取账户信息
            used_flow = (driver.find_element(By.ID, "used-flow")).text
            print("读取流量完成")
            rest_pocket = (driver.find_element(By.ID, "balance")).text
            print("读取余额完成")
            # 发送邮件
            # title = "校园网自动登录成功"
            # content = "校园网余额：{}\n已使用流量：{}\n当前IP：{}".format(rest_pocket, used_flow, str(current_ip))
            send_email(email_account, email_password, title="校园网自动登录成功",
                       content="校园网余额：{}\n已使用流量：{}\n当前IP：{}".format(rest_pocket, used_flow, str(current_ip)))
            return (str(current_ip),
                    str(used_flow),
                    float(rest_pocket))
    else:
        print("不在校园网中")
        return str(current_ip)
