import itchat
import os
import shutil
import subprocess

subprocess.call("ansible-playbook "/Users/houzhimeng/Desktop/deploy/push_apph5.yml", shell=True)

def weixin_mes():
    itchat.auto_login()
    name = itchat.search_friends(name=u'Jason.Wan')
    JW = name[0]["UserName"]
    message_concent = '1'
    itchat.send(message_concent, JW)
    itchat.run()

weixin_mes()