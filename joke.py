import random
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from json import dumps
from sqlalchemy import create_engine
e = create_engine('sqlite:///jokes.db')
app = Flask(__name__)
api = Api(app)
# i used the jokes.txt file that contained Yo' mama jokes to insert
# them to db using this funciton
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
    return {'message': "This a FREE Yo' mama jokes api that gives random jokes. Created by Himanshu Gautam (http://www.github.com/himanshu81494)", "paths": ["/joke"]}

api.add_resource(getRandomJoke, '/joke')
api.add_resource(Home, '/')

if __name__ == '__main__':
  app.run(host="0.0.0.0")

# insert()

# to search for process id , as we know port is 5000
# netstat -anp tcp | grep 5000
# kill -9 <PID>
