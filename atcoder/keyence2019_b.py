import re

s = input().strip()

def check(s):
    p = [
            '\A.*keyence\Z'
            , '\Ak.*eyence\Z'
            , '\Ake.*yence\Z'
            , '\Akey.*ence\Z'
            , '\Akeye.*nce\Z'
            , '\Akeyen.*ce\Z'
            , '\Akeyenc.*e\Z'
            , '\Akeyence.*\Z'
        ]
    for _p in p:
        if re.match(_p, s):
            return True
        # print(s, _p)
    return False

print('YES' if check(s) else 'NO')
