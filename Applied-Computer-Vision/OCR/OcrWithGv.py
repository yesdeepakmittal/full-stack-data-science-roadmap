import requests
import json

gv_key = '------Google API Key-----------'
gv_client_id = '---------client id from Service Account KEY JSON file----------'
gv_client_secret = '--------------Private key from Service Account KEY JSON file------'

url = "https://vision.googleapis.com/v1/images:annotate?key=" + gv_key

payload = json.dumps({
  "requests": [
    {
      "image": {
        "content": "------Base64 String of image---------"
      },
      "features": [
        {
          "type": "TEXT_DETECTION"
        }
      ]
    }
  ]
})
headers = {
  'Authorization': 'Basic ' + gv_client_id + ':' + gv_client_secret,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

import json

ocr = json.loads(response.text)
arr = ocr.get('responses')[0].get('textAnnotations')

for i in range(1,2):
    word = arr[i].get('description')
    vertices_arr = arr[i].get("boundingPoly").get("vertices")
    
    left = vertices_arr[0].get('x')
    top = vertices_arr[0].get('y')
    width = vertices_arr[2].get('x')
    height = vertices_arr[2].get('x')

print(word,left,top,width,height)