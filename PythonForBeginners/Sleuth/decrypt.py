print("Hello, Contosoville!")
# This is a comment that won't be interpreted as a command. 
# Associate variable town with the value "Contosoville"
town = "Contosoville"
# Print a message about the secret location
print("The town I am looking for is " + town)

# Define a power (function) to chant a phrase
def chant( phrase ):
    # Glue three copies together and print it as a message
    print( phrase + phrase + phrase )
    
chant( "Contosoville! " )
 
# old examples    
# def lasso_letter( letter, shit_amount ):
#    letter_code = ord(letter.lower())
    
#letter = 'N'
#shift_amount = 13
#letter_code = ord('n') = 110
# ord converts char/num to ASCII character code    
#ord('N')

def lasso_letter( letter, shift_amount ):
    letter_code = ord(letter.lower())
    decoded_letter_code = letter_code + shift_amount
    decoded_letter = chr(decoded_letter_code)
    return decoded_letter

print(lasso_letter('a', 2))
print(lasso_letter('N', 13))
