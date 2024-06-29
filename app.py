from pymongo import MongoClient
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
# Connect to MongoDB
client = MongoClient("mongodb://admin:secret@172.18.0.2:27017/")
# Access the test_py database
db = client['db_test']
# Access the test_collection collection
collection = db['notes']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert_document():
    collection.insert_one({"date": datetime.now()})
    return "Document inserted successfully!"

@app.route('/print')
def print_documents():
    documents = []
    for x in collection.find():
        documents.append(x)
    return render_template('print.html', documents=documents)


#insert_document()
#print_documents(collection)

# Close the connection
#client.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8006)