from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Home Page", content="DSA - GROUP LABORATORY")


@app.route('/about')
def about():
    return render_template('about.html', title="About Page", content="This page contains information about our site.")


@app.route('/profile')
def profile():
    return render_template('profile.html', title="Profile Page", content="Welcome to your profile!")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Page", content="Get in touch with us via the contact form.")


@app.route('/link list')
def link_list():
    return render_template('link list.html', title="Link List Page", content="link list ito")


if __name__ == '__main__':
    app.run(debug=True)
