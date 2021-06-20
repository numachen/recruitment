#功能：
1、权限管理、日志记录、LDAP域集成、钉钉群消息通知集成；<br>
#2021年6月19日
**实现功能**：后台管理系统实现多语言切换；<br>
第一步：本地安装gettext；<br>
第二步：生成文本格式的多语言资源文件 .po 文件<br>
  翻译 .po 文件中的内容到不同语言<br>
  django-admin makemessages -l zh_HANS -l en<br>
第三步：编译生成可以高效使用的二进制文件 (.mo) 文件<br>
django-admin compilemessages<br>
第四步：配置URL路由，前端添加切换语言的功能按钮；

#2021年6月20日<br>

