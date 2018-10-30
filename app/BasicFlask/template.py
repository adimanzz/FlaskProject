from flask import Flask,  render_template
app= Flask(__name__)

@app.route('/')
def index():
          name1="Jackson"
          dict={'Brad':"Beautiful day in SriLanka",'Amar':'Irrepaceable you'}
          
          return render_template('tmp.html',name=name1,name2=dict)

if __name__ == '__main__':
          app.run(debug=True)
