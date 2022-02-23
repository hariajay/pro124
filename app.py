from flask import Flask,jsonify,request
app = Flask(__name__)
tasks=[
    {'contact':'9987644456',
     'name':'raju',
     'done':False,
     'id':1
    },
    {'contact':'998764456',
     'name':'rahul',
     'done':False,
     'id':1
    }
]

@app.route("/")
def hello_world():
    return("hellow world")

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

    task = {
        'id':tasks[-1] ['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "meassage":"added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if (__name__ == "__main__"):
    app.run(debug = True)