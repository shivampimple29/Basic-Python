#Q7:Write a Python program that executes a list operation and handles an
#AttributeError exception if the attribute does not exist.
def stimulate_attribute_error():
    my_string="Hello World!"
    try:
        my_string.append("Welcome!")
    except AttributeError:
        print("Observed function belongs to different datatype!")
stimulate_attribute_error()