from flask import Flask, render_template
app = Flask(__name__)
color = "#9fc5f8"
@app.route('/')
def welcome():
    return "Welcome to Playground!!!"
@app.route('/play')
def three_box():
    return render_template('index.html', times = 3, color = color)
@app.route('/play/<int:post_id>')
def postId(post_id):
    return render_template('index.html', times = post_id, color = color)
@app.route('/play/<int:num>/<color>')
def subPath(num, color):
    return render_template('index.html', times = num, color = color)














if __name__ == "__main__":
    app.run(debug=True)
