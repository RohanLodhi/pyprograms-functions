#default Argument
def demo(name,msg='H'):
	'''Demo of Keyword Argument'''
	print(name , " : ", msg)
	
	
#demo("Ram","Hello")
#demo(msg="Hello",name="Ram")
#demo(msg="Hello",name) Error

demo("Hello",msg="Ram")

	

