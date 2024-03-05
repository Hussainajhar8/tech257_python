import requests, json

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/e147jf")
#
# # print(post_codes_req)
# # print(post_codes_req.status_code)
# # print(post_codes_req.headers)
# # print(post_codes_req.content)
# # print(post_codes_req.json())
#
# # # How to access individual parts of the response
# # data_dict = post_codes_req.json()["result"]
# # print(data_dict)
# # print(f"Parish: {data_dict['parish']}")

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
print(json_body)
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())

random_postcode = requests.get("https://api.postcodes.io/random/postcodes")
print(random_postcode.json())