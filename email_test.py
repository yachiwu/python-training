#寄送email的程式
#準備訊息物件的設定
import email.message
msg = email.message.EmailMessage()
msg["From"] = "n0975116268@gmail.com"
msg["To"] = "chi86829@g.ncu.edu.tw"
msg["Subject"] = "測試"
#純文字內容
# msg.set_content("測試看看")
#寄送多樣化內容
msg.add_alternative("<div style='font-family:微軟正黑體;font-size: 40px;'>測試一下</div>",subtype="html")
#連線到SMTP server 驗證寄件人身分並發送郵件
import smtplib
#到網路上搜尋 gmail smtp server
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("gmail信箱","密碼")
server.send_message(msg)
server.close()
