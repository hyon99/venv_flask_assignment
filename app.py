from flask import *
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('assignment.html')

def validator(age):
    if(age)>=18:
        return 'ELIGIBLE FOR VOTE'
    else:
        return 'NOT ELIGIBLE FOR VOTE'

@app.route('/valid',methods=['POST'])
def validate():
    user=request.form['name']
    age=int(request.form['age'])
    return validator(age=age)

if __name__=='__main__':
    app.run()