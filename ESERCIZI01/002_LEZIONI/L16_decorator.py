def decorator (func):
	def wrapper ():
		print (frase)
		func ()
		print (frase)
	return wrapper
def func2 ():
	print (testo2)

variabile = decorator(func2)
func2()
