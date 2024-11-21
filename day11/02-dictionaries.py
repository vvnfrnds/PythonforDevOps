ec2_instances = [
    {
        "ec2_name" : "production-server",
        "ec2_type" : "t2.micro"
    },

    {
        "ec2_name" : "test-server",
        "ec2_type" : "t2.mini"
    },

    {
        "ec2_name" : "qa-server",
        "ec2_type" : "t3.xlarge"      
    }
]

print(ec2_instances[0]["ec2_type"]) 