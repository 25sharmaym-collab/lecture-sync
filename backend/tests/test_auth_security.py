from app.core.security import hash_password,verify_password
def test_password_hash_roundtrip():
    h=hash_password('correct horse battery staple'); assert h!='correct horse battery staple'; assert verify_password('correct horse battery staple',h); assert not verify_password('wrong-password',h)
