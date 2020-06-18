import random
def bubble_sort(raw):
    for i in range(len(raw)-1):
        for j in range(len(raw)-i-1):
            if raw[j]>raw[j+1]:
                raw[j],raw[j+1]=raw[j+1],raw[j]

def select_sort(raw):
    for i in range(len(raw)-1):
        pos=i
        for j in range(i+1,len(raw)):
            if raw[pos]>raw[j]:
                pos=j
        raw[pos],raw[i]=raw[i],raw[pos]

def insert_sort(raw):
    for i in range(1,len(raw)):
        pos=i
        cur = raw[i]
        for j in range(i):
            if raw[j]>cur:
                pos=j
                break
        for k in range(i-1,pos-1,-1):
            raw[k+1]=raw[k]
        raw[pos]=cur



l=[random.randint(1,100) for i in range(10)]
print(l)
#bubble_sort(l)
#insert_sort(l)
select_sort(l)
print(l)