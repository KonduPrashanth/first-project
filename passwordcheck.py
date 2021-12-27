dict = {"sunny":"123456", "rajesh":"654321"}
username = input("Enter Your Username : ")
password = input("Enter Your Password : ")
dict[username]=password
print(dict)
print("check your username & password")
username = input("Enter Your Username : ")
password = input("Enter Your Password : ")
for i in dict.keys():
    if username == i:
        while password != dict.get(i):
            password =input("Enter Your Password Again : ")
        break
print("Verified")
