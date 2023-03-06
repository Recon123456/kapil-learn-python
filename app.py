from flask import Flask, render_template, jsonify

app = Flask(__name__)

Courses = [
  {
    'id': 1,
    'title': 'Angular',
    'location': 'Online',
    'country': 'India',
    'Cost': 320
  }, 
  {
    'id': 2,
    'title': 'SQL',
    'location': 'Online',
    'country': 'India',
    'Cost': 220
  }, 
  {
    'id': 3,
    'title': 'JAVA',
    'location': 'Offline',
    'country': 'India',
    'Cost': 250
  }
]


@app.route("/")
def hello():
  return render_template('home.html',jobs=Courses,Compnay="Kapil's")

@app.route("/api/course")
def list_course():
  return jsonify(Courses)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
