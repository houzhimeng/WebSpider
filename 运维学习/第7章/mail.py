import yagmail

yag = yagmail.SMTP('652783902@qq.com', host='smtp.qq.com', port='25')

yag.send(to = '601416320@qq.com',subject ='test',contents = 'This is a test e-mail from Windows CMD tools with the yagmai')
