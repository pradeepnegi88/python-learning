import re

text = "If you need help call 658-598-9977 any time for online help"
pattern = 'help'
search = re.search(pattern, text)
print(search)
search = re.findall(pattern, text)
print(search)
for finding in re.finditer(pattern, text):
    print(finding.span())

phone_pattern = r'\d{3}-\d{3}-\d{3}'
result = re.search(phone_pattern, text)
print(result)

password = input("Password: ")
pattern = r'\D{1}\w{7}'
print(re.search(pattern, password))

text = "Saturday and sunday this store is closed"
print(re.search(r'sunday|Saturday',text))
