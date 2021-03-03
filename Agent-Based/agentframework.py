#agentframework.py
import random

#Initialising the agent class
class Agent():
    #Each agent is given the environment as a list, agents as a list, killed as a list, and y and x coordinates.       
    def __init__ (self, environment, agents, killed, y=None, x=None):
            self.environment=environment
            self.agents=agents
            self.killed=killed
            self.store=0
            self.time_infected=0
            self.infection=0
            self.dead=0
            #If x is none from the website html data, then a random number between 0-100 is given to it. This is a good as it prevents errors when plotting data and moving agents as a value of None cannot be plotted or moved from.
            if (x == None):
               self._x = random.randint(0,100)
            else:
               self._x = x
            #If y is none from the website html data, then a random number between 0-100 is given to it. This is a good as it prevents errors when plotting data and moving agents as a value of None cannot be plotted or moved from.
            if (y == None):
                 self._y = random.randint(0,100)
            else:
                 self._y = y
    
    def getx(self): 
        return self._x
    def gety(self):
        return self._y
    def setx (self, value):
        self._x=value
    def sety (self, value):
        self._y=value
    def delx (self):
        del self._x
    def dely (self):
        del self._y
    x= property (getx, setx, delx, "I'm the 'x' property.")
    y= property (gety, sety, dely, "I'm the 'y' property.")

#Agents moving 
    def move(self): 
        #50% chance that the agents will move 1 step forwards or 1 step backwards on the x coordinate, this ensures random movement.
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        #50% chance that the agents will move 1 step forwards or 1 step backwards on the y coordinate, this ensures random movement.
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

    #Agents eating the environment around them
    def eat(self): 
        #If the environment contains more than 10 than the agent will remove 10 from the environment and store this into its own internal store.
        if self.environment[self._y][self._x]>10:
           self.environment[self._y][self._x]-=10
           self.store +=10
        #If the environment contains less than 10, the value of the environment is removed and stored into the agents own internal store. This is good as otherwise when the value falls below 10, 10 would still be removed and so the environment would contain negative values which is not realistic.
        if self.environment[self._y][self._x] < 10:
           self.store += self.environment[self._y][self._x]
           self.environment[self._y][self._x] = 0
        #If the agent has a store of more than 100, then they will throw up the contents of this store into the environment as they have eaten too much. 
        if self.store >=100:
            self.store=0
            self.environment[self._y][self._x]=+100
            
    #Calculating distance between agents
    def distance_between(self, agent):
       return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
       pass
   
    #Sharing food between agents              
    def share_with_neighbours(self, neighbourhood):
       #For loop that will loop through all the agents in the agents list. 
       for agent in self.agents:
           #Distance between each agent is calculated using the function distance_between.
           distance= self.distance_between(agent)
           #If distance less than the neighbourhood value, the max distance agents can share food between themselves then changes are made to the agents and nearby agents food stores.
           if distance <= neighbourhood:
               #Both the agents and nearby agents stores are added together.
               sum= self.store + agent.store
               #The sum of both agents food stores is divided by two, and both agents are given this value. They have shared their food stores equally.
               average= sum/2
               self.store=average
               agent.store=average
               
           #If distance less than the neighbourhood value, the max distance agents can share food between themselves, and the agent has very little food stored, then changes are made to the agents and nearby agents food stores.
           if distance <= neighbourhood and self.store<10:
                #Both the agents and nearby agents stores are added together.
                sum=self.store+ agent.store
                #The sum of both agents food stores is multiplied by 0.25, so a quarter of the food is given to the nearby agent.
                exploited=sum*0.25
                #The sum of both agents food stores is multiplied by 0.75, so three quarters of the food is given to the hungry agent.
                greedy=sum*0.75
                #The hungry agent is given three quarters of the total food.
                self.store=greedy
                #The other nearby agent is given just one quarter of the total food.
                agent.store=exploited

    #Infection of the agents function      
    def infection_func(self, infect):
        #Set up new list for the dead agents that are created by infection.
        dead=[]
        #For loop that runs through all the agents within the agents list.
        for agent in self.agents:
            #Calculate distance between each agent, using the distance_between function.
            distance= self.distance_between(agent)
            #Sheep chance of getting infected <5%, as random.random must be less than 5%. This makes the model more realistic, as their is only a  small chance that infection occurs.
            if random.random()<0.05:
                #All sheep are ill permanently when they contract this infection. This was chosen to model infections that can be dormant in the animal for long periods of time.
                self.infection=1
                
                #10% chance of the sheep dying from infection. This makes the model more realistic, as their is only a  small chance that infection occurs, as they have to both have been infected prior to this, and then still only have 10% chance of death.
                if random.random()<0.1:
                    #This causes the agent to throw up their food store into the environment, as they are now infected.
                    self.environment[self._y][self._x]=+self.store
                    #The agents food store is then empty, so is set back to 0.
                    self.store=0
                    #This if loop checks to see if that agent has already been appended to the killed list, ie if that agent is already killed. 
                    if agent not in self.killed:
                      #If the agent is not yet in the killed list, the agent is added to the killed list. This is good as it creates a separate list of the dead agents, in which x and y values of the dead agents remain the same, so they can be plotted visually.
                      self.killed.append(agent)
                      print("Agent lost to infection")
                    #Checking for the position in the agent list of that particular agent and storing this to the index_pos variable. This is good as it finds that agent in the list, but does not remove it yet as this would causes errors through iterating through a loop while removing from it. 
                    index_pos=self.agents.index(agent)
                    #Append this index position into the dead list. This will then be used in the Model python file to remove all agents from the agents list that are within the dead list. This is good at it stores the dead agents in a separate list using their position in the agent list, and removes any errors causes by iterating through a loop while removing from it.
                    dead.append(index_pos)
            #Agents have a <10% chance of getting ill if they are within a distance of another sheep who is infected, are not yet infected themselves. This is good at it models real-life, where nearby contact with others can have a low chance of passing on infection.
            if distance <= infect and random.random()<0.1 and agent.infection==0:
                    #This gives the nearby agent the infection, as their infection value changes from 0 to 1.
                    agent.infection=1
                    #This causes the nearby agent to throw up their food store into the environment, as they are now infected.
                    agent.environment[agent._y][agent._x]=+agent.store
                    #The nearby agents food store is then empty, so is set back to 0.
                    agent.store=0
                    #Print statement to tell the user that an infection has been passed on to another agent.
                    print ("An infected sheep has passed on the infection")
        #At the end of the infection function, the dead list is returned. This means that no errors occur due to altering a list while iterating through it, and it is completed at the end to avoid confusion and ensure that the list has been appended to if needed.
        return dead
    
    #Redifining the __str__ function to alter what is returned when agents list is printed. This is good as it allows for much easier debugging and testing, as you can see any errors for an agent. It also provides much clearer information to the user.    
    def __str__ (self):
        return "I am an Agent, located at: " '{} {}' "\nI am storing: " '{}'.format(self._x,self._y, self.store)
 
            
#Initialising Predator Class
class Predator():
    #Each predator is given the agents as a list and killed as a list.        
    def __init__ (self, agents, killed):
            self.store=0
            self.agents=agents
            self.killed=killed
            #The predators x and y values are provided via random numbers initially. This is good as it is realistic in that they may attack the area from different positions and the randomness simulates the real-world.
            self._x = random.randint(0,100)
            self._y = random.randint(0,100)
    def getx(self): 
        return self._x
    def gety(self):
        return self._y
    def setx (self, value):
        self._x=value
    def sety (self, value):
        self._y=value
    def delx (self):
        del self._x
    def dely (self):
        del self._y
    x= property (getx, setx, delx, "I'm the 'x' property.")
    y= property (gety, sety, dely, "I'm the 'y' property.")
    
    #Moving the Predators, speed based on amount already stored.
    def move(self):
        #Predators move twice as fast as agents normally. This was to simulate a real-world predation attempt, where the predator will attack at speed.
            if random.random() < 0.5:
                self._x = (self._x + 2) % 100
            else:
                self._x = (self._x - 2) % 100
            if random.random() < 0.5:
                self._y = (self._y + 2) % 100
            else:
                self._y = (self._y - 2) % 100
            #Predators will move faster still if they have already eaten one agent. This was to simulate that once the predators have a taste for blood and the agents, they may increase their speed to aid the capture of food.
            if self.store>=100:
                if random.random() < 0.5:
                    self._x = (self._x + 3) % 100
                else:
                    self._x = (self._x - 3) % 100
                if random.random() < 0.5:
                    self._y = (self._y + 3) % 100
                else:
                    self._y = (self._y - 3) % 100

    #Calculating distance between the predators and the agents
    def distance_between_pred(self, agent):
       return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
       pass
   
    #Finding and eating the agents, filling the food store.
    def eat(self, pred_dist): 
        #Looping through all the agents in the agents list.
        for agent in self.agents:
           #Calculating the distance between each predator and each agent, using the distance_between_pred function.
           dist_pred= self.distance_between_pred(agent)
           #Predator has to be within range of agent, and only 30% chance of kill when within range. This is to simulate the real-world likelihood of a predator securing the kill.
           if dist_pred <= pred_dist and random.random()<0.9:
               #100 is added to the predators food store once an agent has been killed, as they are eating the agents.
               self.store=+100
               #Runs a loop that checks if the agent is already in the killed list, which would mean it was already dead. 
               if agent not in self.killed:
                  #If agent not already in the killed list, then it adds the agent to the killed list.
                  self.killed.append(agent)
                  #Print statement to tell the user that an agent has been lost to predation.
                  print("Agent lost to predation")
                #Finding out the index position of the agent within the agent list, and appending the index position to the dead list. This is good as it allows a store of the dead agents in a separate list to avoid error when deleting agents from the list at the same time as looping through the agent list.
               index_pos=self.agents.index(agent)
               #The agent has now been added to the killed list, so is now removed from the agents using the index position to do so. This is good as it has been stored to a separate killed list and is now removed as an active agent.
               del self.agents[index_pos]
        #If statement that checks if the predators store is more than 300, ie if the predator has eaten more than three agents. 
        if self.store >=300:
            #The store of the predator is thrown up onto the environment. This is realistic as it is added to the environment, rather than just removed from the model.
            self.environment[self._y][self._x]=+self.store
            #Print statement to tell the user how much the predator threw up, and at what location they threw up.
            print("Predator threw up: '{}' at: " '{} {}'.format(self.store, self._x,self._y))
            #Predators store of food is set back to 0 as they have thrown up.
            self.store=0
    #Redifining the __str__ function to alter what is returned when predators list is printed. This is good as it allows for much easier debugging and testing, as you can see any errors for a predator. It also provides much clearer information to the user.            
    def __str__ (self):
        return "I am a Predator, located at: " '{} {}' "\nI am storing: " '{}'.format(self._x,self._y, self.store)
 