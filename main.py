from flask import Flask
import utils


app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.get_all()

    result = ""
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += "<br>"
    result += ""

    return f"<pre>{result}</pre"


@app.route('/candidate/<int:pk>')
def get_candidate(pk):
    candidate = utils.get_by_pk(pk)

    result = "<br>"
    result += candidate['name'] + "<br>"
    result += candidate['position'] + "<br>"
    result += candidate['skills'] + "<br>"
    result += "<br>"

    return f"""
        <img src="{candidate['picture']}">
        <pre>{result}</pre>
    """


@app.route('/skills/<skill>')
def get_candidates_by_skill(skill):
    candidates = utils.get_by_skill(skill)

    result = ""

    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += "<br>"

    return result


app.run(host='0.0.0.0', port=8000)
