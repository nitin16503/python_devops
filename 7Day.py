#                                                           🙌🙌 ℂ𝕠𝕟𝕕𝕚𝕥𝕚𝕠𝕟𝕒𝕝 ℍ𝕒𝕟𝕕𝕝𝕚𝕟𝕘
import sys
 
type = sys.argv[1]

if type == "t1.micro":
    print("it is free") 
elif  type == "t2.micro":
    print ( "👉it will charge you 2 dollar per hour")
elif type =="t2.medium":
    print("👉it will charge you 4 dollar  per hour")
else:
    print("👉As a beginner, I recommend not to use this service.")
