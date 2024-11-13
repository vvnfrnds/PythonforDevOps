s3_buckets = ["dev-bucket","stage-bucket","qa-bucket"]

print(s3_buckets)

s3_buckets.append("test-bucket")

print("new list:",s3_buckets)

a = len(s3_buckets)
print("length is:",a)

s3_buckets.sort()

print("sorted list:",s3_buckets)

s3_buckets.remove("stage-bucket")

print("List after removing:",s3_buckets)

print(s3_buckets[0] + "--" + s3_buckets[1])


