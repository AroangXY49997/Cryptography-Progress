import numpy as np

# 参数设置
n = 256
q = 4096

# 生成密钥
def lwe_keygen(n=256, q=4096):
    A = np.random.randint(0, q, (n, n))
    s = np.random.randint(0, q, (n, 1))
    e = np.random.randint(-1, 2, (n, 1))  # 误差范围缩小到[-1,1]
    b = (A @ s + e) % q
    return A, b, s

# 加密
def lwe_encrypt(A, b, q, m):
    r = np.random.randint(0, 2, (A.shape[0], 1))  # 改为二进制随机向量
    u = (A.T @ r) % q
    v = (b.T @ r + m) % q
    return u, v

# 解密
def lwe_decrypt(u, v, s, q):
    m_ = (v - (u.T @ s)) % q
    # 正确处理标量提取
    m_scalar = m_.item() if m_.size == 1 else m_[0,0]
    # 四舍五入处理误差
    return int(round(m_scalar))

A, b, s = lwe_keygen(n, q)
m = np.random.randint(0, q//2)  
u, v = lwe_encrypt(A, b, q, m)
m_decrypt = lwe_decrypt(u, v, s, q)

# 输出实验结果
print("明文：", m)
print("加密密文：u.shape =", u.shape, "v =", v.item())
print("解密结果：", m_decrypt)
print("解密是否正确：", "正确" if m == m_decrypt else "错误")