import json

with open('C:/Users/kheledorogh/PycharmProjects/gitproject/inventory/user/fixture/categories.json', 'rb') as f:
    a = json.load(f)

with open('C:/Users/kheledorogh/PycharmProjects/gitproject/inventory/user/fixture/categories.json', 'w',
          encoding='utf8') as f1:
    json.dump(a, f1, indent=5)
