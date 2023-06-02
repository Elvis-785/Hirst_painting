# Hirst_painting
Using the turtle graphics, the Hirst dotted paint is reconstructed.

This is a reconstruction of Hirst's dotted Painting using Python with the help of the Turtle graphics.
Using the Installed Colorgram Package I extract the colors from the Hirst's painting to be able to use in the project.

The process of extraction of the Colors is;
- We start by downloading a spot painting image, which we use to extract the colors using the colorgram package.
- We run a for loop that taps into each of the colors, and extracts the red(r), green(g) and blue(b) colors.
- Further we initiate a tuple that holds (r, g, b) and append the tuples into an empty list.
- Lastly, we copy & paste the entire output list into our main.py and comment out the prior code 

Then we frame the dotted spaces and sizes to assmble the dots to look the Hirst's.

- Inorder to prevent the turtle to start from the center and move out of the frame, we play around with setheading() & forward() to move the turtle to the intended position.

- We then add more codes to the for loop to make the turtle move to the next row and start from the front & keep moving further drawing dots.


- Lastly, we can increase the speed of our turtle by using speed(), make the forward lines vanish by using penup() and make the turtle invisible by using hideturtle().
