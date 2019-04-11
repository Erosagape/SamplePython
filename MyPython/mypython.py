from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/post',methods=['POST','GET'])
def greeting():
    if request.method=='POST':
        user=request.form['myname']
        return render_template('greeting.html',name=user)
    else:
        return 'No data posted'

if __name__=='__main__':
    app.run()

