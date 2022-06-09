# Project Title:
Virtual Car Controller For Racing Games

#### Video Demo link:
< https://drive.google.com/file/d/1jZJ2z8lBtmnkbCMCIdjZ7SVomrefSvOk/view?usp=drivesdk >

#### Description:
This is an OpenCV project that uses computer vision to detect contours and filters out the blue color on the steering wheel,The center blue area is used as the origin, and the top blue area is used for calculating the angle around the cente.
It then calculates the slope of the line formed using the center of the wheel and the top of the wheel and uses that to determine the steering input,The position of the center of the wheel is responsible for braking and accelerating.
The area between the two white lines is a neutral region. If the red region goes above the top line, the “up” key is pressed. If the red region goes below the bottom line, the “down” key is pressed.

Technologies I used:
NumPy
Python
imutils
OpenCV-Python
pynput

Use OpenCV to detect contours and filters out the blue color on the steering wheel (See Sample steering wheel)
It then gets the slope of the line formed using the center of the wheel and the top of the wheel and uses that to determine the steering inputAlso, the position center of the wheel is responsible for braking and accelerating
instead of playing with boring joystick and touch screen games.Lets try this new Virtual Gaming . In this project i developed only using hand steering to play. Same time i have developed one more project where we dont need hand steering our hands are enough to drive based on your hand gesture you can drive the car. And if you show only one hand in front of webcam then the car will move in backward direction. This project is an amazing one.Every students impressed and addicted playing my project. Soon i will plan to execute it to next level.

With the help of this project  you can drive Car you can take turn Right Left, Press Break Like other gaming Cars. you can Drive game with super stunning graphics, challenging multi-stage levels and real-time Single Player.
Use the Python openCV and Numpy libraries to monitor a steering wheel racing game. It offers you the feeling of futuristic driving.The panel is split in 4 sections, logically. When a certain color (in my case Blue) is observed in certain pieces it is considered a main click. Suppose Blue color has been identified at the top left of the panel, so a “A” key press is begun and the car turns left. The color boundaries were established using color.py, in which we defined Blue color range of HSV values.I gave up and forgot about it for a while, but the idea still seemed exciting. Finally, I decided to put some more mental energy into it, and questioned whether or not I even needed Open AI at all for a task like this. Sure, it's nice for simpler games that can be run en masse, so you can train thousands of iterations in moments,so here I used Asphalt 9 Gaming for the interaction. Because you may have to translate some things and tweak to get things working on your end, this is probably not going to be a beginner-friendly series.

My initial goal is to just create a sort of self-driving car. Any game with lanes and cars should be just fine for you to follow along. The method I will use to access the game should be do-able on almost any game. A simpler game will likely be much more simple of a task tooI may also try other games with this method, since I also think we can teach an AI to play games by simply showing it how to play for a bit, using a Convolutional Neural Network on that information, and then letting the AI poke around.In the contemporary world, new interaction forms for digital games have been developing increasingly. In this work, we present an Car controller for games using OpenCV.
