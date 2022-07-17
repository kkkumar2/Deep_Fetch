import json

def flask_call(path):
    url = "http://localhost:8080/detect"
    import requests

    files = {'image': open(path, 'rb')}
    out = requests.post(url, files=files)
    print(out.content)
    print(json.loads(out.content))
    # return json.loads(out.content)

flask_call(r"D:\Data science\Github\Deep_Fetch\uploads\mohan.jpg")