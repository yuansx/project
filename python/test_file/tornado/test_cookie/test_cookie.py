import os
import re
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line


define('port', default=8000, type=int)
users = dict()


class User(object):
    def __init__(self, nickname, gender, birthday):
        self.nickname = nickname
        self.gender = gender
        self.birthday = birthday


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        nickname = self.get_cookie('nicname')
        if nickname in users:
            self.render('userinfo.html', user=user[nickname])
        else:
            self.render('userform.html', hint='请填写个人信息')


class UserHandler(tornado.web.RequestHandler):
    """自定义请求处理器"""

    def post(self):
        # 从表单参数中读取用户昵称、性别和生日信息
        nickname = self.get_body_argument('nickname').strip()
        gender = self.get_body_argument('gender')
        birthday = self.get_body_argument('birthday')
        # 检查用户昵称是否有效
        if not re.fullmatch(r'\w{6,20}', nickname):
            self.render('userform.html', hint='请输入有效的昵称')
        elif nickname in users:
            self.render('userform.html', hint='昵称已经被使用过')
        else:
            users[nickname] = User(nickname, gender, birthday)
            # 将用户昵称写入Cookie并设置有效期为7天
            self.set_cookie('nickname', nickname, expires_days=7)
            self.render('userinfo.html', user=users[nickname])


if __name__ == '__main__':
    parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', MainHandler), (r'/register', UserHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


