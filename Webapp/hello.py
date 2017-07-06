from flask import Flask,render_template,request,send_from_directory
import ics_file
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def cal():
    if request.method == 'GET':
        # show html form
        return render_template('forms.html')
    elif request.method == 'POST':
        # calculate result
        courses=[]
        for i in range(75):
            if request.form.get('course'+str(i)) != None:
                courses.append(request.form.get('course'+str(i)).encode('utf8'))
        print courses
        ics_file.run(courses)
        return "Done"


@app.route('/view')
def view_timetable():
    return 'Hello, World!'


app.run() #Debug mode 
#app.run(host= '0.0.0.0') #External server
