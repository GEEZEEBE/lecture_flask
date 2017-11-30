class DobDict(dict):
    def __init__(self, name):
        dict.__init__({})
        self.dob = name
instance = DobDict({'composer':'2017.10.10','Arranger':'2018.10.10','Musician':'2019.10.10'})

for key,value in instance.dob.items():
    print(key,':',value)

instance.dob.pop('Musician')

instance.dob.update({'earth':'2019.10.10'})

print()

for key,value in instance.dob.items():
    print(key,':',value)