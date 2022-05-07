import json
dic={
    "shopping_list":
        { 
            "choco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
a=input("enter the item:")
b=int(input("enter the value:"))
for i in dic:
    for j in dic[i]:
        if a in dic[i]:
            if j==a and int(dic[i][j])>=b:
                c=int(dic[i][j])-b
                dic[i][j]=str(c)
                break
        elif j!=a:
            print("none")
            break
w=json.dumps(dic,indent=4)
with open("z.json","w") as t:
    t.write(w)