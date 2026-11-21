# Removing the duplicate elements
def remove(duplicate):
    final_list=[]
    for n in duplicate:
        if n not in final_list:final_list.append(n)
    return final_list

duplicate=[2,2,15,14,15,1,6,8,5,147,1,47]
print(remove(duplicate))
    
