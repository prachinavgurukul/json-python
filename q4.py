import json
a={
'4': 5, 
'6': 7, 
'1': 3, 
'2': True}
key={k:v for k,v in sorted(a.items())}
j=json.dumps(key)
print(j)
    