# TO_DO list
# hidden the redirect to /upload folder


import tornado.web
import tornado.ioloop


class uploadImgHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["files"]
        for f in files:
            fh = open(f"upload/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8080/upload/{f.filename}")

    def get(self):
        self.render("index.html")


if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadImgHandler),
        ("/upload/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])

    app.listen(8080)
    print("Listening on port 8080")
    tornado.ioloop.IOLoop.instance().start()
