import requests

def app_version(host, port):
    try:
        url = f"http://{host}:{port}/"
        response = requests.get(url)
        header = response.headers.get('Server')
        
        if header:
            return header, header.split('/')[1]
        else:
            return None
        
    except Exception as e:
        print(f"Error retrieving application version: {e}")
        return None



host = input ("Enter host to check: ")
port = input ("Enter port to check: ")
app = app_version(host, port)
print(f"{app} running on port: {port} \n \n")
