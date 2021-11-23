from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/') # the @ decorator associates this route w/ the function that follows
def formTest():
   return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
   print("Got Post Info")
   print(request.form)
   # never render a template on a POST request
   # instead, redirect
   return redirect('/')

if __name__=="__main__":
   app.run(debug=True)

