# Create a Python function called reverse_string that takes a string as input and returns
# the reversed string

def reverse_string(string1):

    
    string_rev = ''
    for i in string1:
        string_rev = i + string_rev
    return string_rev

string = "reverse string for TGL"

r_string = reverse_string(string)
print (r_string)