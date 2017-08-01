import hashlib


# 可以加入自己的Key，增强安全性。
def encrypt_text(text, encrypt_func, key=''):
    hash = encrypt_func(key.encode('utf-8'))
    hash.update(text.encode('utf-8'))
    return hash.hexdigest()


text = 'hello world'

# md5 5eb63bbbe01eeed093cb22bb8f5acdc3
print('md5', encrypt_text(text, hashlib.md5))

# sha1 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed
print('sha1', encrypt_text(text, hashlib.sha1))

# sha256 b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
print('sha256', encrypt_text(text, hashlib.sha256))

# sha384 fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd
print('sha384', encrypt_text(text, hashlib.sha384))

# sha512 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f
print('sha512', encrypt_text(text, hashlib.sha512))
