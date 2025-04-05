import flask
from exam import Exam
import threading

app = flask.Flask(__name__,
                  static_url_path="",
                  static_folder="public")

serial_lock = threading.Lock()

@app.get("/")
def naked_domain_redirect():
    return flask.redirect("index.html")


@app.route("/api/<command>/<command2>")
def api_command(command,command2):
    with serial_lock:
        exam = Exam()
        exam.connect("/dev/ttyACM0")
        finalCommand = str(command) + " " + str(command2)
        resp = exam.send_command(finalCommand)
        exam.disconnect()
        return resp


app.run(host="0.0.0.0", port=5000, debug=True)
