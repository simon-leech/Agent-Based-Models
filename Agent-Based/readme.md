# simonl11.github.io

Contents of Files: <br>
/agentframework.py - containing all the code for the Agent and Predator classes used in the model.<br>
/MODELWEBSITE.py - containing the code for the Model to run.<br>

Running the model:<br>
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



