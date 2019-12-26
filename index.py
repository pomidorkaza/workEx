import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        data =["Karl","Sam","Bob"];
        self.render('index.html',title="Main page",data=data)


if __name__ == "__main__":
    app = tornado.web.Application([
        ("/", basicRequestHandler)
    ])

    app.listen(8881)
    print("I'm listening")
    tornado.ioloop.IOLoop.current().start()