import json
dict1={"Name":"Abhishek",
"Designation":"CEOofnavgurukul",
"Gender":"male",
"Age":29}
with open ("Json_file.json","w") as f:
    json.dump(dict1,f,indent=4)