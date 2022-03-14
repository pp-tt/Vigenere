import math

charset = "abcdefghijklmnopqrstuvwxyz"

# 加密
def encryption(in_path, out_path, key):
    with open(in_path, "r") as f:  # 打开文件
        text = f.read()  # 读取文件
    text = is_alpha(text)
    t_len = len(text)
    k_len = len(key)
    i = 0
    res = ''
    while i < t_len:
        j = i % k_len
        k = charset.index(key[j])
        m = charset.index(text[i])
        res += charset[(m+k)%26]
        i += 1
    with open(out_path,"w") as f:
        f.write(res)
    return res
    
def is_alpha(text):
    res = ''
    for i in range(len(text)):
        res += text[i] if text[i].isalpha() else ''
    return res.lower()

def cal_CI(text):
    L = len(text)
    x = []
    CI = 0
    for e in charset:
        x.append(text.count(e))
    for i in range(26):
        CI += ((x[i]*(x[i]-1)) / (L*(L-1)))
    return CI

def cal_d(text, k_len):
    d_str = ['' for i in range(k_len)]
    for i, c in enumerate(text):
        d_str[i % k_len] += c
    return d_str

def cal_CIave(text, k_len): 
    d_str = cal_d(text, k_len)
    CI_average = 0
    for i in range(k_len):
        d_str[i] = cal_CI(d_str[i])
        CI_average += d_str[i]
    CI_average = CI_average / len(d_str)
    return CI_average

def get_k_len(text):
    M = [(1,cal_CI(text))]+[(0,0.0) for i in range(49)]
    for i in range(2,50):
        M[i] = (i,abs(0.065 - cal_CIave(text,i)))
    M = sorted(M,key = lambda x:x[1])

    n = [0 for i in range(10)]
    for i in range(2, 10):
        for e in M[1:10]:
            if e[0] % i == 0:
                n[i-1] += 1
    return n.index(max(n)) + 1  
        
F = [
0.0651738, 0.0124248, 0.0217339,
0.0349835, 0.1041442, 0.0197881,
0.0158610, 0.0492888, 0.0558094,
0.0009033, 0.0050529, 0.0331490,
0.0202124, 0.0564513, 0.0596302,
0.0137645, 0.0008606, 0.0497563,
0.0515760, 0.0729357, 0.0225134,
0.0082903, 0.0171272, 0.0013692,
0.0145984, 0.0007836
]       # 英文字符频率.



# 猜测单个秘钥得到的重合指数
def count_CI2(cipher,n):     # n 代表我们猜测的秘钥，也即偏移量
    N = [0.0 for i in range(26)]
    cipher = is_alpha(cipher)
    L = len(cipher)
    for i in range(L):     #计算所有字母的频数，存在数组N当中
        if (cipher[i].islower()):
            N[(ord(cipher[i]) - ord('a') - n)%26] += 1
        else:
            N[(ord(cipher[i]) - ord('A') - n)%26] += 1  
    CI_2 = 0
    for i in range(26):
        CI_2 += ((N[i] / L) * F[i])
    return CI_2

def get_key(in_path, out_path):
    with open(in_path, "r") as f:  # 打开文件
        cipher = f.read()  # 读取文件
    key_len = get_k_len(cipher)
    un_cip = ['' for i in range(key_len)]   
    cipher_alpha = is_alpha(cipher)
    for i in range(len(cipher_alpha)):     # 完成分组工作
        z = i % key_len
        un_cip[z] += cipher_alpha[i]
    s = ''
    for i in range(key_len):
        s += pre_5_key(un_cip[i])     ####这里应该将5个分组的秘钥猜测全部打印出来
    
    with open(out_path,"w") as f:
        f.write(s)
    return s


## 找出前5个最可能的单个秘钥
def pre_5_key(cipher):
    M = [(0,0.0) for i in range(26)]
    for i in range(26):
        M[i] = (chr(ord('a')+i),abs(0.065 - count_CI2(cipher,i)))
    M = sorted(M,key = lambda x:x[1])   #按照数组第二个元素排序
    return M[0][0]

# 根据密钥解密
def decrypt(in_path, out_path, key):
    with open(in_path, "r") as f:  # 打开文件
        text = f.read()  # 读取文件
    text = is_alpha(text)
    t_len = len(text)
    k_len = len(key)
    i = 0
    res = ''
    while i < t_len:
        j = i % k_len
        k = charset.index(key[j])
        m = charset.index(text[i])
        m += 26 if m < k else 0
        res += charset[m-k]
        i += 1
    with open(out_path,"w") as f:
        f.write(res)
    return res

if __name__ == "__main__":
    cipher = encryption('./原始文件.txt', './加密文件.txt', 'hello')
    key = get_key('./加密文件.txt', 'KEY.txt')
    decrypt('./加密文件.txt', './解密结果.txt', key)