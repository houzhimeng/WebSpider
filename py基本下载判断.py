#coding = utf-8
import os

if os. getuido ==0:
    pass
eLse:
    print'当期用户不是root用户,请以root用户执行脚本
    syS. exit(1

versLon=raw_ input("请输入你想安装的 python版本(2.7/3.5))
if version == 2.7
    url = https://www.python.orgftp/python/2.7.12/Python-2.7.12.tgz  
elif versLon == 3.5
    urL = https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz 
else:
    print("输入版本号有误")    
    sys.exit(1)


cmd = 'wget'+urL
res=os.system(cmd)

if version ==2.7
    package_name = "Python-27.12"
else:
    package_name = "Python-3.5.2"
cmd = 'tar xf ' +package_name+'.tgz'
res =o. system(cmd)
if res !=0:
    os system('rm '+ package_name+'.tgz')
    print("解压源码包失败,请重新运行这个脚本下载源码包")
    sys. exit(1

cmd = 'cd '+ packagename+' && ./configure --prefix=/usr/LocaL/python && make && make install
res = os.system(cmd)
if res !=0
    print("编译 python源码失败,请检查是否缺少依赖库")
    SyS. exit(1)

