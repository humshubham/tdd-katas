class RecentlyUsedList:

    def __init__(self, size_limit=5):
        self.item_list=[]
        self.size_limit=size_limit

    def add_item(self, item):
        if type(item)!=str:
            raise TypeError("Only Strings Allowed")
        if item=="":
            raise ValueError("Empty String Not Allowed")
        if self.size_limit!=None and (len(self.item_list)==self.size_limit):
            self.item_list.pop()
        if item in self.item_list:
            self.item_list.remove(item)
        
        self.item_list.insert(0, item)
        
    
    def lookup_item(self, index):
        if index < 0:
            raise IndexError("Negative Lookup Not Allowed")
        if index >= len(self.item_list):
            raise IndexError("Lookup Index Out Of Range")
        return self.item_list[index]
    
    def get_length(self):
        return len(self.item_list)
    