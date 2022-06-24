from capitu import Capitu

app = Capitu()


@app.route("^/$")
def hello_world():
    return "<strong>Hello</strong>"

app.run()
