# -*- coding: utf8 -*-

from tornado.web import RequestHandler, StaticFileHandler, Application
from tornado.websocket import WebSocketHandler
from tornado.gen import coroutine
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

# index_app
class index_handler(RequestHandler):
    def get(self):
        self.render("index.html")

# websocket handler
class infoHandler(WebSocketHandler):
    def open(self):
        pass
    
    def on_message(self, message):
        pass
    
    def on_close(self):
        pass
    
# 主函数
def main():
    application = Application([
        (r"/", index_handler),
        (r"/ws", infoHandler),
        (r"/static/(.*)", StaticFileHandler, {"path": "./static"})
    ])
    server = HTTPServer(application)
    server.listen(9108)

    try:
        # 开启事件循环
        IOLoop.current().start()
    except:
        # 关闭事件循环
        IOLoop.current().stop()

if __name__ == "__main__":
    main()