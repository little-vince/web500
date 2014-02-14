#!/usr/bin/python

import os.path
import tornado.ioloop
import tornado.web
import tornado.websocket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def main():
    application = tornado.web.Application(
        [(r"/", MainHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
