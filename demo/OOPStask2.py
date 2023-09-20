

class obj:
    

    def __init__(self,Office,Python,PHP,Java):
        self.Office=Office
        self.Python=Python
        self.PHP=PHP
        self.Java=Java


store=obj('Webilok',['Vikash','Sumit','Atul','Rahul','Mitesh','Ravi'],['Rajesh','Vivek','Nikhil','Rana'],['Nilesh','Hitesh','Sunil','Dhaval'])        

print(store.__dict__)
python=0
php=0
Java=0
for i in store.Python:
    python+=1

for i in store.PHP:
    php+=1

for i in store.Java:
    Java+=1

print(f'Python : {python}\nPHP : {php}\nJava : {Java}')            
