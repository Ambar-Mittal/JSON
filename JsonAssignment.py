import json

with open (r"C:\Users\ambar\Desktop\sample.json","r") as f:
    var1=json.load(f)

data=var1['RequestType']

def get_data():
    user_id=var1['usr_id']
    statement=var1['print_statement']
    print(statement.rstrip('{usr_id}'),end="")
    print(user_id)
    
def put_data():
    user_id=var1['usr_id']
    statement=var1['print_statement']
    print(statement.rstrip('{usr_id}'),end="")
    print(user_id)

def delete_data():
    user_id=var1['usr_id']
    statement=var1['print_statement']
    print(statement.rstrip('{usr_id}'),end="")
    print(user_id)

if 'HTTPGet' in data:
    get_data()

elif 'HTTPPost' in data:
    put_data()

elif ('HTTPDelete') in data:
    delete_data()

