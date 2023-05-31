class Test:
    global_var = 0
    
    def __init__(self):
        print('object created')
        print('global_var',self.global_var)
    
    def increase(self):
        self.global_var += 1
        print("current global_var value:",self.global_var)
        
obj = Test()
obj.increase()
obj.increase()
print(obj.global_var)