This small project show a basic template to drive an RGB LED lightstrip from a raspberry pico-w using microphyton
Also incéuded are the schemas to test the programm, as well as to drive the lightstrip with the required MOSFET transistors.
The lightstrip uses a certain amount of power, which the pico GPIO pins are not able to provide.
We use a MOSFET transsistor, acting as a switch to switch on and off the external power.
In order to define the color, a combination of values for the R, G and B led's is provided. 
In our case, we create a random value every second for the different colors.
The transistor acting only as a switch, we therefor use PWM to change the values of the different colors.
The PWM is used to switch the transistor on and off for different portions of a cyvle. Thus the LED's are receiving a different mean value for every cycle

