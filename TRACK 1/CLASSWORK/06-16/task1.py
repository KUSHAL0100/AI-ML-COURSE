import requests

#1 send get request to public api url

response=requests.get("https://jsonplaceholder.typicode.com/comments")

#2 check if the connection was successfull(status code 200)
if response.status_code==200:
    #3 parse the structured data into a native Python dictionary
    data=response.json()
    print(data)
    print("Success! Data Retrived")
else:
    print(f"Error: {response.status_code }")