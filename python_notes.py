# Northspyre backend challenge

# import boto3
# from botocore import UNSIGNED
# from botocore.client import Config

# BUCKET_NAME = 'coderbytechallengesandbox'
# s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
# resource = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
# bucket = s3.list_objects_v2(BUCKET_NAME)
# for file in bucket['Contents']:
#   if file['Key'].startswith('__cb__'):
#     target_file = resource.Object(BUCKET_NAME, file['Key']).get()['Body'].read()
#     print(target_file)

# [[[[[[[[[[[[[[[[[[[[[[[[[ Differences with JavaScript ]]]]]]]]]]]]]]]]]]]]]]]]]

# ========================= Whitespace-aware =========================

# Python uses a colon and whitespace to indicate a code block

if (False):
  print('Hello world')

# ========================= Declaring Functions =========================

def sayHello():
  print('Hello')

# ========================= Semicolons =========================

# Python does not need semicolons
# Putting more than 1 statement on a line is bad form
  # print('first'); print('second');

# ========================= Logical Operators =========================

# Python was designed to be readable, hence the operators are `and`, `or`, and `not`

if ((False and False) or not True):
  print('Hello world')

# ========================= Math Operators =========================

# // is used for integer division
  # 10 // 3 ==> 3

# The rest is the same
  # Addition with +
  # Subtraction with -
  # Multiplication with *
  # Division with /
  # Mod (remainder) with %