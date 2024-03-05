import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/e147jf")

print(post_codes_req)
print(post_codes_req.status_code)
print(post_codes_req.headers)
print(post_codes_req.content)
print(post_codes_req.json())

# How to access individual parts of the response
data_dict = post_codes_req.json()["result"]
print(data_dict)
print(f"Parish: {data_dict['parish']}")