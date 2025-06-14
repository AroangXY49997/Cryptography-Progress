import hashlib
import time

# 哈希函数
def H(data):
    return hashlib.sha256(data).digest()

# 生成密钥
def gen_keypair(tree_height=10):
    sk = [H(i.to_bytes(4, 'big')) for i in range(2**tree_height)]
    return sk

# 签名
def xmss_sign(sk, message, index):
    sig = H(sk[index] + message.encode())
    return sig, index

# 验证
def xmss_verify(pk, sig, message, index):
    expected = H(pk[index] + message.encode())
    return sig == expected

# 实验
tree_height = 10
message = "Post Quantum Signature Test"
sk = gen_keypair(tree_height)

index = 1023
start_sign = time.time()
sig, idx = xmss_sign(sk, message, index)
sign_time = time.time() - start_sign

start_verify = time.time()
result = xmss_verify(sk, sig, message, idx)
verify_time = time.time() - start_verify

# 输出结果
print("签名索引：", idx)
print("签名时间：{:.5f}秒".format(sign_time))
print("验证时间：{:.5f}秒".format(verify_time))
print("验证结果：", result)
