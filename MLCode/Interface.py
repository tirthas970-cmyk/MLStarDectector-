import sys
from MLModel import MLStarDectector

class Interface:

    def __init__(self):
        self.mldectector = MLStarDectector()
    
    def interfaceAskData(self):
        while True:
            try:
                distance = float(input("What is the distance of this star from the earth? "))
                luminosity = float(input("What is the luminosity of this star? "))
                radius = float(input("What is the radius of this star? "))
                temperature = float(input("What is the temperature of this star? "))

                stars = []

                stars.append(distance)
                stars.append(luminosity)
                stars.append(radius)
                stars.append(temperature)
                    
            except ValueError:
                # Catches non-numeric input similar to Java's InputMismatchException
                print("Please try again", file=sys.stderr)
                continue
            except Exception as e:
                # Catches other potential errors
                print(f"An unexpected error occurred: {e}", file=sys.stderr)
                continue

            print(self.mldectector.TrainModel_Test(stars))

model = Interface()

print(model.interfaceAskData())


            


                

