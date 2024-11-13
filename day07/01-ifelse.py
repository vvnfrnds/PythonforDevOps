ec2 = "t2.free"

if ec2 == "t2.micro":
    print("it will charge $4")
elif ec2 == "t2.medium":
    print("It will charge $7")
else:
    print("Free EC2 Instance")