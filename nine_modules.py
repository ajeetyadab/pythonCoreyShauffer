print("module imported")

test = "this is test variable"

def search_index(sources,target):
    for i,item in enumerate(sources):
        if item == target:
            return i
    return -1
    
        
# subjects = ["history", "math","arts"]

# print(search_index(subjects,"arts"))