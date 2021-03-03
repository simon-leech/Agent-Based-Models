import matplotlib.pyplot, matplotlib.animation, agentframework, sys, matplotlib, tkinter, requests, bs4
#Read in the environment data as f
f= open("in.txt")
#Read in the x and y data as r from the geog.leeds.ac.uk website
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
#Create variable called content from the read in data of variable r
content = r.text
#Parse the content variable using html parser
soup = bs4.BeautifulSoup(content, 'html.parser')
#Create a new variable holding all the attributes from the class y on the website from html. This holds all the y coordinates that can be used for agents.
td_ys = soup.find_all(attrs={"class" : "y"})
#Create a new variable holding all the attributes from the class x on the website from html. This holds all the x coordinates that can be used for agents.
td_xs = soup.find_all(attrs={"class" : "x"})
            
matplotlib.use('Tkagg')

#Accepting user input for the agent variable creation.
inpnum_of_agents=input ("How many agents would you like? (Default is 10):")
# try except loop where if the input from the user is not an integer, the value for num_of_agents is automatically set to a default of 10. This is good as it ensures any user input error does not crash the model running.
try:
    num_of_agents=int(inpnum_of_agents) 
except ValueError: 
    print ("Input was not an integer, so agents has been set to default of 10")
    num_of_agents=10
    
#Accepting user input for the predator variable creation.  
inpnum_of_predators=input ("How many predators would you like? (Default is 2):")
# try except loop where if the input from the user is not an integer, the value for num_of_preds is automatically set to a default of 3. This is good as it ensures any user input error does not crash the model running.
try:
    num_of_preds=int(inpnum_of_predators) 
except ValueError: 
    print ("Input was not an integer, so predators has been set to default of 3")
    num_of_preds=3
    
#Accepting user input for the iteration variable creation.
inpnum_of_iterations=input ("How many iterations would you like? (Default is 1000, as likely model runs to completion at this value):")
# try except loop where if the input from the user is not an integer, the value for num_of_iterations is automatically set to a default of 100. This is good as it ensures any user input error does not crash the model running.
try:
    num_of_iterations=int(inpnum_of_iterations) 
except ValueError: 
    print ("Input was not an integer, so iterations has been set to default of 100")
    num_of_iterations=1000
    
#Accepting user input for the neighbourhood variable creation.   
inpneighbourhood=input ("From how close would you like agents to share food?(Default is 20):")
# try except loop where if the input from the user is not an integer, the value for neighbourhood is automatically set to a default of 20. This is good as it ensures any user input error does not crash the model running.
try:
    neighbourhood=int(inpneighbourhood)
except ValueError: 
    print ("Input was not an integer, so neighbourhood has been set to default of 20")
    neighbourhood=20
    
#Accepting user input for the infect variable creation. 
inpinfect=input ("How infectious would you like the infection to be? (Default is 3):")
# try except loop where if the input from the user is not an integer, the value for infect is automatically set to a default of 3. This is good as it ensures any user input error does not crash the model running.
try:
    infect=int(inpinfect)
except ValueError: 
    print ("Input was not an integer, so infect has been set to default of 3")
    infect=3
    
#Accepting user input for the predator_distance variable creation. 
inppred_dist=input ("From how close would you like the predators to be able to kill agents from? (Default is 10):")
# try except loop where if the input from the user is not an integer, the value for predator_distance is automatically set to a default of 10. This is good as it ensures any user input error does not crash the model running.
try:
    pred_dist=int(inppred_dist)
except ValueError: 
    print ("Input was not an integer, so predator distance has been set to default of 10")
    pred_dist=10

#Creation of lists for use in the model.
environment=[]
agents = []
predators=[]
agentnum=[]
killed=[]
dead=[]
#Creation of num variable to allow each agent to be differentiated when the data is written out to a file (see line 84).
num=1
#Carry_on set as True to ensure the model runs to at least 10 iterations. 
carry_on=True

#Reading in the data in the variable f, and parsing this based upon the commas in the data, then creating a new list titled rowlist.
for line in f: 
    parsed_line= str.split(line, ",")
    rowlist=[]
#For every value in each parsed_line append every value into the rowlist as a float. This means each value in each row is converted to a float and appended into rowlist.
    for coord in parsed_line:
        rowlist.append(float(coord))
    #Append the whole rowlist to the environment list once each and every value from every row has been appended to it. This is good as this finalises the creation of the environment from the data read in as f, converted into individual float values and appended to the environment list.
    environment.append(rowlist)
                    
#For loop that up to the maximum of num_of_agents, so by default this loop runs 10 times.
for i in range(num_of_agents):
    #For every agent they are the corresponding y and x value from the list of coordinates for their position [i] in the loop. Coordinates are from the geog.leeds.ac.uk website. This is good as every agent begins at a different starting coordinate.
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    #Every agent is given the environment as a list, the rest of the agents as a list, the killed agents as a list and their own y and x values. This ensures that the every agent in the agents list has all the data required within the agentframework Agent class, so functions can be run with them.
    agents.append(agentframework.Agent(environment, agents, killed, y, x))
    #Every agent is given a number associated to them, to enable each agent to be differentiated from another when the data is written out to a file.
    agentnum.append("Agent " + str(num)+ " Stored : ")
    #Number counter to ensure that each agent is given a different number to enable them to be differentiated from another when the data is written out to a file.
    num=num+1

#For loop that up to the maximum of num_of_preds, so by default this loop runs 3 times.
for i in range(num_of_preds):
    #Every predator is given the environment as a list and the killed agents as a list. This ensures that the every predator in the predators list has all the data required within the agentframework Predator class, so functions can be run with them.
    predators.append(agentframework.Predator(agents, killed))


#Make the graph axes, create a variable called fig that holds the figure, and create its axes.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)

#Define function update that holds the main section of code. 
def update(frame_number):
    fig.clear()
    global carry_on

#All the code is written inside a loop that will end the program if there are no agents still alive. This is useful as it ensures the program does not run to an index out of range error, as it is prevented from running when all agents are dead.
    if (len(agents))==0:
        print("All agents have been killed, program will now end via System Exit.")
        sys.exit()
    else:
        #For loop that will complete functions based upon the number of agents still alive. Using len(agents) is good as it prevents any errors when the agent list is shortened by agents dying and being removed.
        for i in range(len(agents)):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        #Create a new list to store all the dead agents. This is good as it removes the errors that occur when you are looping through a list while also removing from it.
        alldead = []
        # loop through for all agents and set dead as infection_func, this means that dead= dead agents from infection.
        for i in range(len(agents)):
            dead = agents[i].infection_func(infect)
            # append all the dead agents from the infection function to the alldead list. This again removes the errors that occur when you are looping through a list while also removing from it.
            alldead.append(dead)
            # loop through all the dead agents in the alldead list
        for dead in alldead:
            # for all index_pos, so for all positions in the agents list that are dead, delete these agents from the agent list. This is an improved method than removing when they initially die, as it prevents errors when looping through a list that is being altered.
            for index_pos in dead:
                del agents[index_pos]
            
         #For loop that will complete functions based upon the number of predators still alive. Using len(predators) is good as it prevents any errors when the predator list is shortened by predators dying and being removed.
        for i in range(len(predators)):
            predators[i].move()
            predators[i].eat(pred_dist)

        #For loop that will plot the graph based upon the number of agents still alive. Using len(agents) is good as it prevents any errors when the agent list is shortened by agents dying and being removed.
        for i in range(len(agents)):    
            #Plot any agents on a graph that have an infection value of 0. A value of 0 means that the agent is not infected by the infection. This is good as it gives a visual representation of the way infection passes through the agents in the model.
            if agents[i].infection ==0: 
                matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, color="white")
            #Plot any agents on a graph that have an infection value of 1. A value of 1 means that the agent is infected by the infection. This is good as it gives a visual representation of the way infection passes through the agents in the model.
            if agents[i].infection==1: 
                matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, color="grey") 
    #Plot all killed agents contained within the killed list using black marker as a visual representation. This is good as it allows for all agents still alive to continue moving, but killed will always remain in the same spot as it plots their x and y which remains constant.
        for i in range (len(killed)):
                matplotlib.pyplot.scatter(killed[i]._x,killed[i]._y, color="black", marker="x")     
    #Plot all the predators onto the graph in red to show their locations visually.
        for i in range (len(predators)):
           matplotlib.pyplot.scatter(predators[i]._x,predators[i]._y, color="red", marker="^")
            
              
    #Plot the graph with the environment as the background portion of this.
    matplotlib.pyplot.imshow(environment)   
    #Set the y axis limit to 100, which is the maximum of the environment data values.
    matplotlib.pyplot.ylim(0, 100)
    #Set the x axis limit to 100, which is the maximum of the environment data values.
    matplotlib.pyplot.xlim(0, 100)

#Function call loop, ensuring a runs to the number of iterations the user specified. This is good as it allows the user to specify the number of iterations they would like the model to run for, and can just be set as very high if the user wants to run the model until all agents die.
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
    else:
        print("Stopping condition was reached, as the model ran for the number of iterations you specified")

#Plotting the GUI animation to allow the agents to be seen moving over time. This is good as it visually represents the model and it changing.
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    pass
# Allows model to be stopped when running. This is good for developer as you can stop whenever is needed.
def stop():
    root.destroy()
    pass

#Plotting GUI interface. Stop button was added for ease of use to allow the user to stop the program running at any point.
root = tkinter.Tk()
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
menu_bar.add_cascade(label="Stop", command=stop)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop() # Wait for interactions.
        
#Writing out environment data to a file.        
f2=open ('dataout.txt', 'w')
#For loop ensuring that for each line in the environment, each line is wrote out as a string into the text file. 'W' means create this file.
for line in environment: 
    f2.write(str(line))  
f2.close()

#Writing out to agentstore file
f3=open ('agentstore.txt', 'a+')
#For loop through the length of agents and writing the agents number defined earlier and the amount of food that agent has stored within it. This is useful as it allows the amount each agent has eaten to be seen after the program has ended. 'a+' means create this file if it is not already a file, and if it is then append that file with the data.
for i in range(len(agents)):
    f3.write(str(agentnum[i]))
    f3.write(str(agents[i].store))
    f3. write ("\n")
f3.close()
