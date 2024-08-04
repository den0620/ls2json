import json

# First dict entry eg `"plan9": {...}` is needed and at the end of the file will be removed
json_fs = {"plan9": {}}

# Replace `9front-ls.txt` with your `ls -Rl` output file
with open("9front-ls.txt", "r") as IF:
    paths = IF.readlines()

index = 0
while index < len(paths):
    path = paths[index]
    print(path)
    # I dont rember why I did this probably because ALL files in my result were 2019 so good luck fixing it 
    if not "2019" in path and not "total" in path and path != "\n":  # then actual path
        rootpath = [f"\"{point}\"" for point in list(map(str,path[2:len(path)-2].split("/")))]
        appendroot = "[" + "][".join(rootpath) + "]"
        index += 2
        path = paths[index].rstrip()
        while path != "":
            _,_,_,_,_,_,_,_,obj = map(str,path.split())
            clearrootpath = [point.replace("\"", "") for point in rootpath]
            if "./"+"/".join(clearrootpath)+f"/{obj}"+":"+"\n" in paths:
                exec(f"json_fs{appendroot}[\"{obj}\"] = dict()")
            else:
                # Replace `nothing here` with desired file contents
                exec(f"json_fs{appendroot}[\"{obj}\"] = \"nothing here\"")
            index += 1
            path = paths[index].rstrip()
    index += 1

# You can manually set contents of a file as such:
json_fs["plan9"]["sys"]["src"]["games"]["mix"]["examples"]["newfilename"] = "whatever"

# Output file name
with open("9front-ls.json", "w") as OF:
    # Removed here by calling it
    json.dump(json_fs["plan9"], OF)

