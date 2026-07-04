# lst=[[1,2],[3,4],[5,6]]
# result=list(map(lambda x:list(map(lambda y:y+5,x)),lst))
#
# print(result)
# d={"apple":100, "banana":40, "cherry":150}
# result=dict(filter(lambda items:items[1]>50,d.items()))
# # print(result)
# from functools import reduce
# lst=[12,45,78,23,99,34]
# largest=reduce(lambda a,b:a if a>b else b,lst)
#
# from functools import reduce
# nums=[5,10,15,20,25,30]
# result=reduce(lambda x,y:x+y,filter(lambda x:x%5==0,map(lambda x:x**2,nums)))
# def area_of_rectangle(x,y):
#     return x*y
# # print(area_of_rectangle(6,4))
# def subtract(a,b):
#     return a-b
#
# # print(subtract(3,10))
# nums=[4,8,12,16,20.24]
# from functools import reduce
# result=reduce(lambda x,y:x+y,filter(lambda x:x%4==0,map(lambda x:x**2,nums)))
# print(result)
l=["hello","hii","who","sandeep"]
def fun(x):
    if x is not in "AEIOU aeiou":
        return x
    k=[]
    for i in l:
        s=list(map(fun,i))
        s="".join(s)
        k.append(s)
    print(k)


