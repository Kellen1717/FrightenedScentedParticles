



class ariplane:



  speed=0
  speedLimit=600
  fueltakeSize=1000
  curentfule=800
  mph=300




  def __init__(self,colorInput,wingspanInput,modleInput,engineszieInput):
   self.color=colorInput 
   self.wingspan=wingspanInput
   self.modle=modleInput
   self.engineszie=engineszieInput

  def increasespeed(self,speedChange):
    self.speed += speedChange  
   
    self.curentfule -= 50
    if self.curentfule <= 0
      return -1
    
    if self.speed >= self.speedLimit
      return -2

    return self.speed

  def Fly(self):
    print("we are flying high")

  def changespeed(self,speedChange):
    print ("we've changed speed by "+str(speedChange))

  def winglights(self):
    print ("the wing lights are on")

print ("welcome to the airplane factory ")
Planemodle=input ("what type of plane do you want ")
Planewingspan=input ("what would you like you wingspan to be ")
seats=input ("how many seats so do you want ")
enginsize=input ("how big do you want your engine to be")
newPlane=airplane(Planemodle,Planewingspan,seats,enginsize)


#return new speed if successful 
#return -1 if not enough fuel 
#Increase Speed By inpuT  
#If too fast oR nOt enough fuel
#Decrease currentFuel By 10