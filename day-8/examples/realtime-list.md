# What is a list in Python, and how is it used in DevOps?

basically the list is used to lists the S3 buckets for example
'''python
list= ["yugandhar_bucket",demo_bucket",bucket_123"]
print(list)
'''
 similarly for EC2 instances also and the admins..

 in the lists we can add or remove the elements from the lists by using the key words called "append", "remove"
# example for adding elements from the lists
'''python
list=["ramu-bucket","demo-bucket,yugandhar_bucket]
list.append("bob-bucket")
print(list)
'''

# example for removing elements from the lists
'''python
list=["ramu-bucket","demo-bucket","yugandhar_bucket"]
list.remove("demo-bucket)
'''
# What is the difference between a list and a tuple in Python, and when would you choose one over the other in a DevOps context?

list is collection of hetrogenous elements where tuple is also a hetragenous elements

here the list is mutuable like we can maniplucate the data inside the lists by using some specific key words

where in the tuple is immutable we can't maniplucate the data inside the tuple but we can access the elements by using indexing concepts.

'''python
tup1=("yugandhar_bucket","demo-bucket")
print(tup1)
print(len(tup1))
'''

