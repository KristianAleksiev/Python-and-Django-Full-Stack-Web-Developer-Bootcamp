# try:
#     pass
#     #Attempt to do it
# except #KindOfError:
#     #If KindOfError, execute this
#     pass
# else:
#     #If no Exception, execute this
#     pass


# try:
#     file = open("simple.txt", "w")
#     file.write("Test write to simple txt document")
# except IOError:
#     print("ERROR: COULD NOT FIND FILE OR READ DATA")
# else:
#     print("SUCCESS")
#     file.close()
#finally:
#    print("always executes")

try:
    file = open("simple.txt", "r")
    file.write("Test write to simple txt document")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
else:
    print("SUCCESS")
    file.close()
finally:
    print("I always work")
