from PIL import Image
import pytesseract #gets text from image
captcha = Image.open('do.jpg') #opens the image file
breaker = pytesseract.image_to_string(captcha) #gets text from the selected jpg and stores the text
result=0
a=int(breaker[0]) #as they are in string format convert them integer by having the string inside this parathasis int()
b=breaker[-2]
c=int(breaker[-1])
if b=="+":
	result=a+c
elif b=="-":
	result=a-c
elif b=="*":
	result=a*c
elif b=="/":
	result=a/c
else:
	result="This is beyond basic mathematical operations."
print(result)  
	
