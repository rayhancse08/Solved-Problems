
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        item=int(item)
        
        self.items.append(item)
        print(item)
    def pop(self):
        return self.items.pop()


    def is_empty(self):
        if self.items ==[]:
            print("none")
            return True
        return False
    def increment(self,element,increment_value):
               self.element=int(element)
               self.increment_value=int(increment_value)
               
               for i in range(self.element):
                   #print(self.items[i])
                   self.items[i]+=self.increment_value
               print(self.items[-1])
               


s=Stack()
operation_no=int(input("Operation No: "))
operation_list=[]
for i in range(operation_no):
    operation_name=input()
    operation_list.insert(i,operation_name)


for item in operation_list:
    if "push" in item:
        eliminate=item.strip('push ')
        
        s.push(eliminate)
    if "pop" in item:
        while not s.is_empty():
                  pop_item=s.pop()
                  
    if "inc" in item:
        eliminate=item.strip('inc ')
        element=eliminate[0]
        increment_value=eliminate[2]
        s.increment(element,increment_value)
        
