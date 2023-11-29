from flask import Flask 
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
import csv

app = Flask(__name__)
# print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

#Dynamic mode
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

#txt file
# def write_to_file(data):
#     with open('database.txt', mode = 'a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email}, {subject}, {message}')


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         # data = request.form[email]
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'Somthing went wrong. Try again!'
    


#csv      #######################
def write_to_csv(data):
    with open('database.csv', 'a' , newline='',) as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # data = request.form[email]
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Somthing went wrong. Try again!'














#static mode
# @app.route("/works.html")
# def my_works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


#learning 

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

# @app.route("/")
# def hello_world():
#     return render_template('index.html')

# @app.route("/<username>/<int:post_id>")
# def hello_world(username = None, post_id=None):
#     return render_template('index.html', name = username, id=post_id)

# #url_for()
# @app.route("/")
# def hello_world():
#     print(url_for('static', filename='favicon.png'))
#     return render_template('index.html')


# @app.route("/about")
# def about():
#     return render_template('about.html')

# @app.route("/blog")
# def blog():
#     return "These are my thoughts on blogs"

# @app.route("/blog/2023/dogs")
# def blog2():
#     return "This is my dog!"