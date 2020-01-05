import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
if __name__=="__main__":
    email = input("Please enter your email address: ")
    if(re.search(regex,email)):
        print("valid Email")
    else:
        print("Invalid Email")