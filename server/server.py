from bottle import static_file, Bottle, run

app = Bottle()

@app.route('/<filename>')
def serve_static(filename):
    return static_file(filename, root='./public')

def start():
    run(app, host='localhost', port=8080)