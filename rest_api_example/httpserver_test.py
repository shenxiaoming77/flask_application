import requests
import  json

s = requests


def post_test():

    data={"username":"zhangsan","password":"123",}
    r = s.post('http://127.0.0.1:5000/register', data)

    print (r.status_code)
    print (r.headers['content-type'])
    print (r.encoding)
    print (r.text)

def get_test():
    res = requests.get("http://10.8.26.25:5000/api/tasks", timeout = 3)
    res_json = res.json()
    print(res_json)

def predict():
    data={"username":"zhangsan","password":"123"}
    param = {'param' : data}
    r = s.post('http://10.8.26.25:5000/api/predict', data = param)
    result = json.loads(r.text)
    print(result['data'])

if __name__ == '__main__':
    predict()