import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line


# --port=8888, options.port取命令行参数
define('port', default=8000, type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1>Hello, tornado!</h1>')


if __name__ == '__main__':
    parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', MainHandler), ])
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

