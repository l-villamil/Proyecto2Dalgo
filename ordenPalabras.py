# def ordenPalabra(palabra1,palabra2,i):
#     centinela=-1
#     extencion=0
#     if len(palabra1)>len(palabra2):
#         extencion=len(palabra1)-len(palabra2)+1
#     else:
#         extencion=len(palabra1)
#     print(extencion)
#     while i<extencion and centinela==-1:
#         if palabra1[i]!=palabra2[i]:
#             centinela=i
#         else:
#             i+=1
#             centinela=ordenPalabra(palabra1,palabra2,i)
#     return centinela



def ordenPalabra(palabra1,palabra2):
    centinela=-1
    extencion=0
    if len(palabra1)>len(palabra2):
         extencion=len(palabra1)-len(palabra2)+1
    else:
         extencion=len(palabra1)
    # print(extencion)
    i=0
    while i< extencion and centinela==-1:
        if palabra1[i]!=palabra2[i]:
            centinela=i
        else:
            i+=1
    return centinela 

print(ordenPalabra("alla","casa"))

