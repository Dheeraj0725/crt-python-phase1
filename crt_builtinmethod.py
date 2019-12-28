s1 = "abc"
s2 = "abc123"
s3 = "123"
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
s4 = '''abc123 abc123'''
print(s4)
print(s1.upper())
s1=s1.upper()
print(s1)
s5 = "abc def ghi"
s5 = s5.replace("def","xyz")
print(s5)