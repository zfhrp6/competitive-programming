v1,v2,v3,v4=int(input()),int(input()),int(input()),int(input())
print( ( (v1|v2)&(v3^v4) )|( (v2&v3)^(v1|v4) ) )
