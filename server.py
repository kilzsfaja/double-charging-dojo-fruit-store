from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

list_of_students = []

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    student = {
        "id": request.form["student_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"]
    }
    list_of_students.append(student)
    print(f"Charging {student['first_name']} for some fruits")
    return render_template("checkout.html", list_of_students = list_of_students, student = student)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
