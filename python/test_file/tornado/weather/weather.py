import os
import random

import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line


define('port', default=8000, type=int)


class SayingHandler(tornado.web.RequestHandler):
    def get(self):
        words = [
            'good good study, day day up',
            'never give up',
            'oh, my god',
        ]
        self.render('index.html', message=random.choice(words))


class WeatherHandler(tornado.web.RequestHandler):
    def get(self, city):
        weathers = {
            u'北京': {'temperature': '-4~4', 'pollution': '195 中度污染'},
            u'成都': {'temperature': '3~9', 'pollution': '53 良'},
            u'深圳': {'temperature': '20~25', 'pollution': '25 优'},
            u'广州': {'temperature': '18~23', 'pollution': '56 良'},
            u'上海': {'temperature': '6~8', 'pollution': '65 良'}
        }
        raise '{0} -- {1}'.format(city, city in weathers)
        if city in weathers:
            self.render('weather.html', city=city, weather=weathers[city])
        else:
            self.render('index.html', message=u'没有{0}的天气信息'.format(city))


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/saying')


if __name__ == '__main__':
    parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/saying/?', SayingHandler),
            (r'weather/', WeatherHandler),
            #(r'weather/([^/]{2,})/?', WeatherHandler),
            (r'/.+', ErrorHandler),
            ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates')
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

