

class CentralTendency:
    def __init__ (self):
        self.elements = []
        
    def addValue(self,value):
        self.elements.append(value)
        
    def removeValue(self,value):
        self.elements.remove(value)
        
    def mean(self):
        return sum(self.elements)/len(self.elements)
    
    def median(self):
        self.elements.sort()
        mid = len(self.elements)//2
        
        if len(self.elements) % 2 != 0:
            return self.elements[mid]
        else:
            return(self.elements[mid] + self.elements[mid-1])/2
        
    def mode(self):
        uniqueList = []
        for i in self.elements:
            if i not in uniqueList:
                uniqueList.append(i)
        
        max_count = 0
        mode = self.elements[0]
        
        for i in uniqueList:
            count = self.elements.count(i)
            if count > max_count:
                max_count = count
                mode = i
                
        return mode
    
ct = CentralTendency()
ct.addValue(5)
ct.addValue(8)
ct.addValue(2) 
ct.addValue(3) 
ct.addValue(1) 
ct.addValue(1) 
ct.removeValue(1)
        
print("Average : {} ".format(ct.mean()))
print("Mode : {} ".format(ct.mode()))
print("Median : {} ".format(ct.median()))