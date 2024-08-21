import requests

# from stage dev
url = "url/content-summary"
file_path = "test.vtt"

with open(file_path, 'rb') as file:
    file_content = file.read()

headers = {
    'Content-Type': 'application/octet-stream'
}

try:
    response = requests.post(url, data=file_content, headers=headers)

    if response.status_code == 200:
        print("POST successful")
        print("Response:", response.text.encode(
            'utf-8').decode('unicode_escape'))
    else:
        print(f"Failed with status code: {response.status_code}")
        print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", str(e))
