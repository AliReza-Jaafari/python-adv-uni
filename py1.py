import requests as r

class Fetcher:
    __studensts = []
    
    def  __init__(self):
       self.__studensts = r.get("https://cdn.ituring.ir/ex/users.json").json()
        
       
    def nerds(self):
        list1 = set()
        for i in self.__studensts:
            if i["score"]>18.5:
                list1.add(i["name"] + "_"  + i["last_name"])
        return list1
    def sultans(self):
        lis1 = []
        max = 0
        for i in self.__studensts:
            if i["score"] > max:
                max = i["score"]
        
        for i in self.__studensts:
            if i["score"] == max:
                lis1.append(i["name"]+ "_" + i["last_name"])
        return tuple(lis1)
    def mean(self):
        min = 0
        for i in self.__studensts:
            min += i["score"]
        min /= len(self.__studensts)
        return min
    def get_students(self):
        list1 = []
        for i in self.__studensts:
            list1.append(i["name"] + "_" + i["last_name"])
        return list1
            
         
                
    
     
        
               
                
        



        
            
            
        
       
     






