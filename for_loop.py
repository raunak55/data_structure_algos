import datetime,time

files= ['affinity.zip','affinity_copy.zip']

def printed():
    return "Hello"

for zip_file in files:
    print(zip_file)
    ct = datetime.datetime.now()
    print("current time:-", ct)
    #printed()
    time.sleep(2)
    data = printed()
    print(data)



