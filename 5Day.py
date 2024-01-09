#                                                           ℂ𝕠𝕞𝕞𝕒𝕟𝕕 𝕃𝕚𝕟𝕖 𝔸𝕣𝕘𝕤🙌🙌 
# Alow us to execute function / operation through command line interface eg-: aws ec2 ls 
#  "sys" -> module used.

import sys

def add (a,b): 
    return (a+b)
def sub(a,b) :
    return (a-b)
def mul(a,b):
    return (a*b)
def div(x,z):
    return (x/z)

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if (operation =='add'):
    output = add(num1,num2)
    print(output)
if (operation =='sub'):
    output = sub(num1,num2)
    print(output)
if (operation =='mul'):
    output = mul(num1,num2)
    print(output)
if (operation =='div'):
    output = div(num1,num2)
    print(output)            

# HOW TO USE-> python FILE_NAME num1 operation num2
# eg. :-python 5Day.py 2 add 3, python 5Day.py 2 sub 3, python 5Day.py 2 mul 3, python 5Day.py 2 div 3

#                                                               𝔼𝕟𝕧 𝕍𝕒𝕣𝕤🙌🙌
# When we have to deal with sensitive information in command line interface we use Environment Variables(Env Vars).
#  We will create seperate .env file which will be secure and hidden
#  1st -> pip install python-dotenv
# The load_dotenv function from the python-dotenv library is used to load variables from a file named .env into the environment.
#  When you have sensitive information such as API keys, passwords, or other configuration details in your project, it's a good practice to store them in a separate file (usually named .env) rather than hardcoding them directly into your code.
#  2nd -> store your secret credential in .env file
from dotenv import load_dotenv
import os
# Load environment variables from .env
load_dotenv()
# Access the environment variable
print(os.getenv("PASSWORD"))
print(os.getenv("Secret_key"))






