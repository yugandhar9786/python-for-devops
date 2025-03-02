import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, we will create an t2.micro instance and it is a free tier eligible instance")
elif type == "t2.medium":
    print("it will cost you upto 0.0464 USD per Hour")
elif type == "t2.large":
    print("it will cost you upto 0.0928 USD per Hour")
else:
    print("please provide a valid instance type")