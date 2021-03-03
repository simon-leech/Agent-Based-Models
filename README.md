# PythonFiles
Files used in Python Courseworks for GEOG_5990M at University of Leeds. 

## Agent-Based Model- Coursework 1: Built a model of Sheep and Predators.

This is an Agent-Based Model that includes agents (sheep) and Predators (wolves) that will eat the sheep. The sheep can also be killed by an infection in the model. <br>
The model will run until the user-specified number of iterations has been completed, or all the agents have been killed.<br>
The model allows for user input to set parameters, but if the user input is not an integer default values will be used instead.<br>
When the model runs, it is expected that you will see filled circles of white and grey (agents) move around the area, and red triangles (predators) also moving. <br>
Once an agent has been killed, a print statement will occur notifying you how they died, and a grey cross will appear in the location they died.<br>
Model should be run through Spyder, using the GUI to enhance the model and its animation. <br>

The Model code: <br>
This ABM uses agents to move around a 100x100 grid environment and eat the environment. <br>
The agents will move randomly, and move more quickly if they have less food stored, as they are hungry! <br>
The agents will share food with other sheep nearby, but if they have less food stored will be more greedy.<br>
The agents will throw up if their food store exceeds 100. <br>
The agents have a 5% chance of becoming ill and then subsequently a 10% chance of dying from this illness. <br>
The agents have a 10% chance of passing on the infection to other agents if they are nearby. <br> 
The predators will move around the 100x100 grid twice as fast as the agents and move even faster if they have already eaten one agent.<br>
The predators will throw up if their food store exceeds 300, if they have eaten 3 agents.<br>
The predators have a 30% chance of killing the agents for food if they are within a certain distance of them. <br>

## Bacterial Multiplication- Coursework 2: Model of Bacterial Multiplication within a school .

Software Outline:
The software will model the bacterial multiplication within a school setting over time. The number of weeks is a user input and allows the user to set the number of weeks ran.
The model will create schoolchildren, staff and cleaners at the beginning of the code. 
For the number of weeks the user has specified, the model will run functions within another loop for the number of days in a week.
If the model is running for Saturday or Sunday, a reduced number of functions are ran as schoolchildren are not at school, but do meet up outside of school.
The staff and cleaners may come into school during the weekend, and bacteria will always multiply. 
At the end of the day, a scattergraph of the bacteria and killed bacteria is produced and saved to the working directory.
For weekdays, a time counter is added to simulate the 8-hour schoolday. At a time of 0, the humans are able to bring bacteria onto the schoolgrounds as they move to school.
During the schoolday schoolchildren and staff move about, can become infected and bacteria multiply. 
At time of 4 and 5, breaktime functions are ran for the schoolchildren in which they leave the schoolrooms and go outside, to mingle and play. 
When the time is 8, cleaners will come into the school and clean the surfaces, if the bacteria are not removed they will be able to continue multiplying.
There is a small chance that visitors can come into school during the school day.
At the end of the day, a scattergraph of the bacteria and killed bacteria is produced and saved to the working directory.
At the end of the model, the graphs are read back into the model to put them all together for easy comparison of change over time.

How the model can be run:
The model has been tested within Spyder, using the dedicated console of an iPython Console to do so, MUST use dark mode of Spyder to run as some print statements are in white (Tools->Preferences->Syntax Colouring->Solarised Dark)
Currently, a bug is seen whereby a smaller graph of the final day in the model is created right at the bottom underneath all other graphs of an identical size (ignore the final smaller graph).

What is expected when the model runs:
When the model runs, the user will first be asked for the number of weeks they wish to run the code for.
After this, the model will loop through the number of weeks, and subsequent days in these weeks.
Within the iPython Console, during the week, the user will see print statements outlining the current day, total staff and student attendance, hour of school, any unwell children or staff that are taken home.
Within the iPython Console, during the weekend, the user will see print statements outlining the current day, the size of groups that children are meeting in, and if any cleaners or staff come into work.
WIthin the iPython Console, at the end of the model, print statements in white will appear for emphasis, and a graph for every day in the model will be produced. 

