import base64 as bs



def encode(original):
    original=str(original)
    reversed=[]

    count=-1
    for x in original:
        reversed.append(original[count])
        count=count-1
    count=0
    set1=[]
    set2=[]
    set3=[]
    
    for x in reversed:
        if count%3==0:
            set1.append(x)
        if count%3==1:
            set2.append(x)
        if count%3==2:
            set3.append(x)
        count=count+1

    final=set1+set2+set3
    final = ''.join([str(elem) for elem in final])

    encoded=bs.b64encode(bytes(final,"ascii"))

    print(encoded)
    return(encoded)
    

def decode(encodedx):
    encodedx = bytes(encodedx, 'utf-8') 
    
    decoded=str(bs.b64decode(encodedx))[2:][:-1]
    

    value1=len(decoded)//3
    value2=len(decoded)//3
    value3=len(decoded)//3
    if len(decoded)%3==1:
        value1=value1+1
    
    if len(decoded)%3==2:
        value1=value1+1
        value2=value2+1
        value3=value3+1
    value2=value1+value2
    value3=value2+value3
    

    list1=decoded[0:value1]
    list2=decoded[value1:value2]
    list3=decoded[value2:value3]

   
    ori=""
    co=0
    for x in list1:
        ori=ori+list1[co]
        try:
            ori=ori+list2[co]
            ori=ori+list3[co]
        except:
            print (ori)
        co=co+1
    
    count=-1
    f=""
    for x in ori:
        f=f+ori[count]
        count=count-1
    print(f)
    return(f)

encode("hello bro")





decode('byBscm9lYmxo')