

#Start Program

#MainFunction
import math   
    #Indroductory Message
print("Big Blue WindChill")
print('    ')
    #Get users input's (Temp and MPH)
TempF= float(input(" What is your staring air temperature (F) ?: "))
Velocity=int(input(" What is your starting wind speed (MPH)? : "))
print('    ')
print("Temperature=", TempF, "Degrees F")
print('    ')
print('Wind Speed', '\t', 'Old Formula', '\t','New Formula', '\t','Difference')

OldStyleWC = 0.081*(3.71*math.sqrt(Velocity) + 5.81 - (0.25* Velocity))*(TempF - 91.4) + 91.4
NewStyleWC = 35.74 + 0.6215*TempF - 35.75*math.pow(Velocity, 0.16) + 0.4275*TempF*math.pow(Velocity, 0.16)
difference = OldStyleWC - NewStyleWC

#Calculate input's from User & round the function if necessary. Formulas (Old & New) are rounded off to zero places. Numbers from difference is rounded off to 1 place

    #Set range to STOP at 90
for windspeed in range(Velocity, 90, 5):
    print (windspeed , '\t', '\t',round(OldStyleWC), '\t', '\t', round(NewStyleWC), '\t', '\t',round(difference, 1))
    Velocity= Velocity + 5
    
    #Calculate the windchill with Old Formula
    OldStyleWC = 0.081*(3.71*math.sqrt(Velocity) + 5.81 - (0.25 * Velocity))*(TempF - 91.4) + 91.4
    
    #Calculate the windchill with NewFormula
    NewStyleWC = 35.74 + 0.6215*TempF - 35.75*math.pow(Velocity, 0.16) + 0.4275*TempF*math.pow(Velocity, 0.16)
    
    #Difference betwen Old vs New
    difference = (OldStyleWC - NewStyleWC)


#End of Program
