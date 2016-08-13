import random
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from sqlalchemy import create_engine
e = create_engine('sqlite:///jokes.db')
app = Flask(__name__)
api = Api(app)

def insert():
  fname = 'jokes.txt'
  with open(fname) as f:
    content = f.readlines()
  # print random.choice(content)[:-1]
  conn = e.connect()
  for item in content:
    data = "insert into jokes(joke) values(" + (dumps(item[:-1])) + ")"
    query = conn.execute(data)
    # print data
  print query

class getRandomJoke(Resource):
  def get(self):
    conn = e.connect()
    query = conn.execute("select joke from jokes order by RANDOM() LIMIT 1;")
    return {'joke': [i[0] for i in query.cursor.fetchall()]}
class Home(Resource):
  def get(self):
    return "Welcome \n This is a FREE Yo' mama jokes api. \n Made with love in India by Himanshu Gautam (github.com/himanshu81494)."

api.add_resource(getRandomJoke, '/joke')
api.add_resource(Home, '/')

if __name__ == '__main__':
  app.run(host="0.0.0.0")

# insert()