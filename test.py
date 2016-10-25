import urllib
import httplib

def post2():
    params = urllib.urlencode({'user_id':"1234"})

    headers = {"Content-type":"application/x-www-form-urlencoded"}
    conn=httplib.HTTPConnection("52.78.88.51:8080")
    conn.request("POST","/BadgeMaServer/declaration.do", params, headers)
    response = conn.getresponse()
    data = response.read()
    print data
    conn.close()

post2()
