def shift(s,n=1):
    ret = ''
    ret += '>' * (s-1)
    for i in range(10):
        ret += '{}[-]{}[<+>-]'.format('<'*n, '>'*n)
        ret += '>'
    ret += '<'*10
    ret += '<' * (s-1)
    return ret

exp = input()
nums = []
ops = []
for c in exp:
    if c in '0123456789':
        nums.append(int(c))
    else:
        ops.append(c)
lg = len(nums)

ret = ''
for n in nums:
    ret += '+' * n
    ret += '>'
    ret += '\n'
ret += '<'*lg
ret += '\n'

pos = 1
for op in ops:
    if op == '-':
        ret += '>[-<->]'
    elif op == '+':
        ret += '>[-<+>]'
    pos += 1
    ret += '<'*(pos-1)
    ret += shift(pos+1)
    ret += '>'*(pos-1)
    ret += '\n'
ret += '.'
print(ret)




def ope(op, idx1, val1, idx2, val2, ridx):
    ret = ''
    if op == '+':
        ret += '>' * ridx
        ret += '+' * (val1+val2)
        ret += '<' * ridx
    elif op == '-':
        ret += '>' * ridx
        ret += '-' 


def move(sidx, eidx):
    if sidx <= eidx:
        raise Exception
    ret = ''
    ret += '>' * (eidx - 1)
    ret += '[-]'
    ret += '>' * (sidx - eidx)
    ret += '[-{}+{}]'.format('<'*(sidx-eidx),'>'*(sidx-eidx))
    ret += '<' * (sidx-1)
    return ret
