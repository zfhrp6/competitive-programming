w=lambda x:((10*x/60)//1 + ((100*x/60)%10>=5))/10
dr=lambda x:x/112.5
def dr(x):
    d=lambda a,x:a<x<a+2
    x=x/112.5
    for i in range(1,30,2):
        if d(i,x): return (i+1)//2
    return 0
dc=['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW','N']
def wp(x):
    if 0.0<=x<=0.2: return 0
    if 0.3<=x<=1.5: return 1
    if 1.6<=x<=3.3: return 2
    if 3.4<=x<=5.4: return 3
    if 5.5<=x<=7.9: return 4
    if 8.0<=x<=10.7: return 5
    if 10.8<=x<=13.8: return 6
    if 13.9<=x<=17.1: return 7
    if 17.2<=x<=20.7: return 8
    if 20.8<=x<=24.4: return 9
    if 24.5<=x<=28.4: return 10
    if 28.5<=x<=32.6: return 11
    if 32.7<=x: return 12
# 風力0   0.0m⁄s 以上 0.2m⁄s 以下    
# 風力5   8.0m⁄s 以上 10.7m⁄s 以下　　   
# 風力10　　  24.5m⁄s 以上 28.4m⁄s 以下　　
# 風力1　　   0.3m⁄s 以上 1.5m⁄s 以下　　     
# 風力6　　   10.8m⁄s 以上 13.8m⁄s 以下　　   
# 風力11　　  28.5m⁄s 以上 32.6m⁄s 以下　　
# 風力2　　   1.6m⁄s 以上 3.3m⁄s 以下　　     
# 風力7　　   13.9m⁄s 以上 17.1m⁄s 以下　　   
# 風力12　　  32.7m⁄s 以上　　
# 風力3　　   3.4m⁄s 以上 5.4m⁄s 以下　　     
# 風力8　　   17.2m⁄s 以上 20.7m⁄s 以下　　   　
# 風力4　　   5.5m⁄s 以上 7.9m⁄s 以下　　     
# 風力9　　   20.8m⁄s 以上 24.4m⁄s 以下　
#

deg,dis=map(int,input().split())
# print(dr(deg))
# print(w(dis))
print(('C' if w(dis)<=0.2 else dc[dr(deg)]) + ' {}'.format(int(wp(w(dis)))))
