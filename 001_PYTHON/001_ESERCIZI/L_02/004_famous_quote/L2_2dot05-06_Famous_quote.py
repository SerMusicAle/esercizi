#DESCRIPTION: function print favourites vip's quote
"""
    2-5. Famous Quote: Find a quote from a famous person you admire. 
    Print the quote and the name of its author. 
    Your output should look something like the following, including the quotation marks: 
    Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""
"""
#FUNCTION
def f_quotes (vip):

    #DECLARATION LOCAL VAR
    #list of vip's quotesjobs
    vips: dict = {
        'Einstein':'la vita è come una bicicletta', 
        'Mandela':'La istruzione è l\'arma più potente', 
        'Jobs':'Stay hungry, stay foolish'
    }

    #BODY INSTRUCTION
    #verify corrispondence
    if vips[vip]:
        quote: str = (f"{vip} una volta disse:, \"{vips[vip]}\"")
        return quote
    else: 
        return (f"inserisci il nome corretto")

#INPUT requests
print (f"chi preferisci tra Einstein, Mandela e Jobs?")
    
#ASSIGNMENTS
vip:str = input()

#CALL
res = f_quotes(vip)

print (res)

"""


