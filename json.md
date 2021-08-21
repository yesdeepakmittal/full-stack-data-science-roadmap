import json
f = open('abc.json','r')
g = open('xyz.json','r')
a_json = json.loads(f.read())
x_json = json.loads(g.read())

