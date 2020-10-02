import framework3, matplotlib.pyplot as plt, random
from IPython.display import Image, display
from matplotlib.patches import Rectangle
#Reset the parameter of facecolor of the axis, so the axis background to grey, so that the bacteria colors will stand out much more using this.
plt.rcParams['axes.facecolor'] = 'grey'
#Creating the classrooms on the graphs for later use. Each rectangle represents a classrooms of equal size, and they are all outlined in black to represent the walls of the classrooms.
rectangle0=Rectangle((0,0),20,20,fc='none',edgecolor="black")
rectangle1=Rectangle((40,0),20,20,fc='none',edgecolor='black')
rectangle2=Rectangle((0,40),20,20,fc='none',edgecolor='black')
rectangle3=Rectangle((40,40),20,20,fc='none',edgecolor='black')
#Add the patches of rectangles to the graphs for later use, so they are displayed on every graph created each time, rather than reapplying them to every graph which would add additional code and be less efficient.
plt.gca().add_patch(rectangle0)
plt.gca().add_patch(rectangle1)
plt.gca().add_patch(rectangle2)
plt.gca().add_patch(rectangle3)

#Set number of children to 80
num_of_children=80
#Set number of staff to 6
num_of_staff= 6
#Set number of cleaners to 2
num_of_cleaners=2
#Create variable to count for the colors used to display the bacteria each day.
colornum=0
#Create list of the colours for the bacteria used to display each day.
color=["Orange","Green","Blue","Pink","Red","Black","Yellow"]
#Setting up list for the number of schoolchildren
schoolchildren=[]
#Setting up list for the coordinates of the schoolrooms
schoolroomslist=[]
#Setting up list for the coordinates of the locations of the school outside
schooloutside=[]
#Setting up list for the bacteria
bacteria=[]
#Setting up list for the number of staff
staff=[]
#Setting up list for killed bacteria.
killed_bact=[]
#Setting up list for staff illness.
staff_ill=[]
#Setting up list for children illness.
children_ill=[]
#Setting up list for cleaners.
cleaners=[]
#Setting up list for visitors.
visitors=[]
#Setting up list for visitor illness.
visitors_ill=[]
#Setting up list for cleaner illness.
cleaners_ill=[]
#Setting up the schoolroom list.
schoolrooms=[]
#Setting time to 0 as the day has not yet started
time=0

#Open the schoolrooms text file.
f=open("schoolrooms.txt")
#For every line in the file.
for line in f:
    #Split the line at each comma in the data. This is good as it allows for all the values of the schoolrooms coordinates to be separated.
    parsedline=str.split(line,",")
    #Print function to check the line was parsed correctly, used during testing and debugging.
    #print(parsedline)
    #For every value in the parsedline variable
    for value in parsedline:
        #Append the schoolrooms list with the float value of all the values in the parsedline. This means that every value for the schoolrooms coordinate is appended to the schoolrooms list.
        schoolrooms.append(float(value))
#Close the file as this is better for memory usage and in case any other program is using it.
f.close()
#Print function for the schoolrooms list to check that this was functioning correctly.
#print(schoolrooms)
#Open the datastore file, and if it is not yet created then create it, and allow it to be appended if it is already a file.
f2=open ('datastore.txt', 'a+')

#For loop for every child in the school
for i in range (num_of_children):
    #For every child, append the schoolchildren list with that child, the location of the rooms and outside spaces at the school, the staff list and the bacteria list.
    schoolchildren.append(framework3.Schoolchildren(schoolchildren, schoolrooms, schooloutside, staff, bacteria,children_ill,visitors))
#For loop for every staff member in the school
for i in range (num_of_staff):
    #For every staff member, append the staff list with that staff member, the schoolchildren, location of the rooms and outside spaces at the school, the staff list and the bacteria list.
    staff.append(framework3.Staff(schoolchildren, schoolrooms, schooloutside, staff, bacteria, killed_bact, staff_ill,visitors))
#For loop that runs the length of the bacteria list, this is good as it prevents errors when the length of the bacteria list is 0, and allows bacteria to multiply and die over time.    
for i in range (len(bacteria)):
    #For every bacteria, append the bacteria list with the schoolrooms list, the location of the outside spaces and the bacteria list.
    bacteria.append(framework3.Bacteria_class(schoolrooms,schooloutside,bacteria,killed_bact)) 
#For loop that runs for number of cleaners
for i in range(num_of_cleaners):
    #Append the cleaners list with the schoolrooms, bacteria, killed_bact, cleaners and cleaners ill list.
    cleaners.append(framework3.Cleaners(schoolrooms, bacteria, killed_bact, cleaners,cleaners_ill))

#Accepting user input for the number of weeks.
inpnum_of_weeks=input ("How many Weeks would you like the model to run for? (Default is 1):")
# try except loop where if the input from the user is not an integer, the value for num_of_weeks is automatically set to a default of 1. This is good as it ensures any user input error does not crash the model running.
try:
    num_of_weeks=int(inpnum_of_weeks) 
except ValueError: 
    print ("Input was not an integer, so number of weeks has been set to default of 1")
    num_of_weeks=1
    
#Set number of days to 7 (length of a week) multiplied by the number of weeks
num_of_days= 7*num_of_weeks
#Set daynum to 0.
daynum=0
#Set week to 1.
Week= 1
#Set day variable to 1, first day of the schoolweek.
day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#For loop for the number of days in the week.
for i in range (num_of_weeks):
    #Print the week that is currently being simulated. This is good for user experience as they can see where the model is currently at.
    print("\nWeek",Week)
    #Write out to the datastore file the week and its value to ensure the user can understand the output.
    f2.write("\nWeek %d\n" % Week)
    #Add one to the week counter. This is done to ensure that the value given to the user of weeks is accurate.
    Week=Week+1
    #Reset the colornum variable to 0 at the start of the week. This is so the 7 colours are always used for the same day of the week, no matter how many weeks the model is ran for and the list index is never out of range. This error was found during testing.
    colornum=0
    #For loop in range 7, so for everyday in a week, complete these functions.
    for i in range(7):
        #Set time to 0 at the start of each day, in this model the day starts with 0 being at school, it is not run the same as a 24 hour clock. 
        time=0
        #Print function to create space in the visualisation so it is not too cramped.
        print(" ")
        #Print function for the day list to tell the user what day it is.
        print(day[i])
        #Add the day to the datastore text file to write out, this is to ensure the user can understand the output.
        f2.write("\n" + day[i])
        #If the day is Saturday or Sunday, ie if the model is currently at the weekend then run a reduced number of functions.This is good as it ensures model realism as the students are not at school at the weekend.
        if day[i]=="Saturday" or day[i]=="Sunday":
            #Print function to tell the user that it is the weekend.
            print("It's the weekend")
            #For every staff member, run the weekend function. This is done to simulate realism and the length of staff is used incase staff are added or removed.
            for i in range (len(staff)):
                staff[i].weekend()
            #Run the schoolchildren weekend function. This is ran only once for all the children as the function puts all the children into separate groups and gets them to interact, modelling meeting up outside of school.
            schoolchildren[i].weekend()
            #For every bacteria in the bacteria list. Run the multiply function. This is ran even at the weekend to simulate model realism and ensure the bacteria continue to multiply every day.
            for i in range (len(bacteria)):
                bacteria[i].multiply()
            #For every cleaner in the cleaner list, run the weekend function. This is ran at the weekend as the cleaners wouldn't necessarily be expected to work, so the function simulates this using random numbers for their work at the weekend.
            for i in range(len(cleaners)):
                cleaners[i].weekend()
            #Run the off ill function for the schoolchildren. This is ran at the weekend to ensure that the schoolchildren can recover at the weekend without school. This is good as it simulates real life.
            schoolchildren[i].off_ill()
            #Run the off ill function for the staff. This is ran at the weekend to ensure that the staff can recover at the weekend without school. This is good as it simulates real life.
            staff[i].off_ill()
            #Run the off ill function for the cleaners. This is ran at the weekend to ensure that the cleaners can recover at the weekend without school. This is good as it simulates real life.
            cleaners[i].off_ill()            
            #For every bacteria in the bacteria list.
            for i in range (len(bacteria)):
#               #Plot on the scattergraph, the location of the bacteria coordinates and a smaller size than normal as bacteria are small in nature.
                plt.scatter(bacteria[i]._x, bacteria[i]._y, color=color[colornum], s=10)
            #For every bacteria in the killed_bact list    
            for i in range(len(killed_bact)):
                 #Plot on the scattergraph, the location of the killed bacteria coordinates in the colour white and a smaller size than normal as bacteria are small in nature. Plotted as x to provide differentation.
                plt.scatter(killed_bact[i]._x, killed_bact[i]._y, s=10, color="white", marker="x")
            #After the bacteria have all been plotted, use this print function during testing to check that the weekend plots were being plotted as i was having errors with this.
            #print("Saving figure at weekend")  
            #Save the figure to file, with the name Day{0} meaning Day, then the number 0 would be altered to the daynum value for that day. So these weekend days would have values 5 and 6, as the counter begins at 0 to satisfy the for i in range 7 variable that reprints the figures at the end of the model.
            plt.savefig("Day{0}.jpg".format(daynum))
            #Add one to the daynum variable, used for saving the bacteria outputs to file. 
            daynum=daynum+1
        else:
            #Run schoolchildren off ill function at the beginning of each day, to simulate the attendance register being taken. 
            schoolchildren[i].off_ill()
            #Run staff off ill function at the beginning of each day, to simulate the attendance register being taken for staff.
            staff[i].off_ill()
            #Run the cleaners off ill function at the beginning of each day, to simulate the cleaners coming into work or not.
            for i in range(len(cleaners)):
                cleaners[i].off_ill()
            #Print function to show how many students are in that day and the total number of children.
            print("Total student attendance:" , len(schoolchildren)-len(children_ill), "out of", len(schoolchildren))
            #Print function to show how many staff are in that day and the total number of staff.
            print("Total staff attendance:" , len(staff)-len(staff_ill), "out of", num_of_staff)
            f2.write("\nTotal Student Attendance: %d" % (len(schoolchildren)-len(children_ill)))
            f2.write("\nTotal Staff Attendance: %d" % (len(staff)-len(staff_ill)))            
            #For loop that runs for 24, ie the length of a day. This is good as it allows the 7 hours you will be school to run different functions to the rest of the day when children and staff are elsewhere.
            for i in range (24):
                #If loop for time less than or equal to 8. This mimics the 8-hour school day where children are in school.
                    if time<=8:
                        #Print function to show the user what hour of school it is.
                        print ("Hour of school is: ", time)
                        #If loop for time is 0. This is used as hour 0 is the hour in which the children travel to, and arrive at school.
                        if time==0:
                            #For loop for the number of children present in the school.
                            for i in range (num_of_children):
                                #If random function less than 0.1. This represents the chance of a schoolchild being a carrier of the bacteria.
                                if random.random()<0.1:
                                    #The bacteria is created, and appended to the bacteria list, with the schoolrooms and schooloutside spaces also added.
                                    bacteria.append(framework3.Bacteria_class(schoolrooms,schooloutside,bacteria, killed_bact))
                                    #Print function to show the user that the bacteria was carried into school by the child.
                                    #print("Bacteria has been carried into the school by Schoolchild")
                                #After the random function, the schoolchildren will move around the classrooms during hours to represent normal movement during lessons.
                                schoolchildren[i].move()
                            #For loop for the number of staff present in the school.
                            for i in range (num_of_staff):
                                 #If random function less than 0.1. This represents the chance of a staff member being a carrier of the bacteria.
                                if random.random()<0.1:
                                    #The bacteria is created, and appended to the bacteria list, with the schoolrooms and schooloutside spaces also added.
                                    bacteria.append(framework3.Bacteria_class(schoolrooms,schooloutside,bacteria, killed_bact))
                                    #Print function to show the user that the bacteria was carried into school by staff member.
                                    #print("Bacteria has been carried into the school by Staff member")
                                #After the random function, the staff will move around the classrooms during hours to represent normal movement during lessons.
                                staff[i].move()
                            #for loop for the length of the bacteria list. This is good as it prevents errors when the bactteria list is empty or bacteria are killed or added.
                            for i in range(len(bacteria)):
                                #Once the loops for bacterial creation have completed, then the bacteria are all initiated in the schoolrooms. They initially only have coordinates within the schoolrooms as it is assumed that the staff and children will go to the classrooms on arrival at school.
                                bacteria[i].initiate_bacteria(schoolrooms)
                        #Else keyword refers to if time more than 8, and is not 0 then complete this section. Bacteria are only initially brought into school by the staff and children on arrival at the start of the day.
                        else:
                            #For loop for the number of children in the school.
                            for i in range(num_of_children):
                                #Move the schoolchildren around the classrooms randomly to simulate lessons and getting up in the classroom to fetch things.
                                schoolchildren[i].move()
                            #For loop for the number of staff in the school.
                            for i in range (len(staff)):
                                #Move the schoolchildren around the classrooms randomly to simulate lessons and getting up in the classroom to fetch things.
                                staff[i].move()
                            #For loop for the length of the bacteria list. This is good as it allows for bacteria to be added and killed without traceback errors.
                            for i in range (len(bacteria)):
                                #Allow each bacteria to multiply. This is to simulate the natural reproduction of bacteria on surfaces that have not been cleaned.
                                bacteria[i].multiply()
                            #For loop for the length of the staff list. This is good as it allows for staff to be added and removed when ill without errors regarding the length of the list.
                            for i in range (len(staff)):
                                #Run the infection function for each staff member. This simulates the chance of the staff member becoming ill through contact with the bacteria.
                                staff[i].infection()
                            #For loop for the length of the schoolchildren list. This is good as it allows for children to be added and removed when ill without errors regarding the length of the list.
                            for i in range (len(schoolchildren)):
                                #Run the infection function for each staff member. This simulates the chance of the child becoming ill through contact with the bacteria.
                                schoolchildren[i].infection()
                     #if loop for time is 4. This is used as the midday lunch-hour break, and simulates the children going onto the playground and running around. 
                    if time==4:
                                #Run the breaktime function for every schoolchild. So that every schoolchild has a break at lunch.
                                schoolchildren[i].breaktime()
                    #if loop for time is 5. This is used as the end of the midday lunch-hour break.
                    if time==5:
                                #Run the end_breaktime function for every child that returns the children back into the class for afternoon classes.
                                schoolchildren[i].end_breaktime()
                    #if loop for time is 8. This signals the end of the schoolday when children go home.
                    if time==8:
                        #Print function for showing that the school is now being cleaned.
                        print("Time for school cleaning")
                        #This for loop is used to simulate the amount of movement a cleaner makes, so helps simulate cleaning whereby they may spend more time in certain locations so get less areas done in a day.
                        for i in range(0,10):
                            #for loop at range of length of the staff.
                            for i in range(len(cleaners)):
                                #Cleaners move around within the schoolrooms.
                                cleaners[i].move()
                        #Run the cleaning function once, so [0] is used to run the function just once. This is ran only once as the cleaning function uses both cleaners within it, so don't want it to repeat unneccessarily.
                        cleaners[0].cleaning()
                        #If random number less than 0.05, less than 5% chance of this.
                        if random.random()<0.05:
                                #Print function to tell the user that a visitor has come to school.
                                print("A visitor has arrived at school")
                                #Append the visitors list, so create a new visitors and give that visitors, the schoolchildren list, schoolrooms, staff, bacteria, visitors and visitors_ill lists.
                                visitors.append(framework3.Visitors(schoolchildren,schoolrooms,schooloutside,staff,bacteria,visitors,visitors_ill))
                        #For the length of the visitors list. This is good as the visitors only have a 5% chance of being created, so this list is constantly being added to and removed, and using len of the list stops errors from this.
                        for i in range (len(visitors)):
                                #Run the visitors leave function.
                                visitors[i].leave()
                        #For all bacteria in the bacteria list. Length is used to ensure that no errors occur when the code is ran after bacteria are added and removed.
                        for i in range (len(bacteria)):
                            #Set the ylimit and xlimit of the graph to 60, the locations of the schoolrooms at school. This is done as x,y of 1000 are used in the model to simulate the homes of all humans, so otherwise they would be plotted too.
                            plt.ylim(0,60)
                            plt.xlim(0,60)
                            #Plot on the scattergraph, the location of the bacteria coordinates in the colour for that day from the colornum list and a smaller size than normal.
                            plt.scatter(bacteria[i]._x, bacteria[i]._y, color=color[colornum],s=10)
                        #For every bacteria in the killed_bact list    
                        for i in range(len(killed_bact)):
                             #Plot on the scattergraph, the location of the killed bacteria coordinates in the colour white and a smaller size than normal as bacteria are small in nature.
                            plt.scatter(killed_bact[i]._x, killed_bact[i]._y, color="white", s=10, marker="x")
                        #Add one to the colornum variable, which means that the color of each day of bacteria is different, so that change over each day can be seen.
                        colornum=colornum+1
                        #Save the figure to the working directory, with the filename Day{0}, {0} is a tuple variable that adds the daynum number to the end of the filename, so that each day the file is saved with a different name to avoid overwriting each other.
                        plt.savefig("Day{0}.jpg".format(daynum))
                        #Print function used during testing and debugging to ensure that the file is successfully saved to the file.
                        #print("Saving figure during week")
                        #Used during testing and debugging to ensure that the plots were plotting differently for each day, at the end of the day. 
                        #plt.show()
                    #Once functions for that hour have been completed, then add one to the time variable.
                    time=time+1
            #Add one to the daynum variable, used for saving the bacteria outputs to file. 
            daynum=daynum+1
            
            
#At the end of the program running, this print function is used to tell the user that they can now see how the bacteria has changed over time.
print("\n\nSee how the bacteria has grown over time")
#Reset colornum to 0 for the showing of the graphs, found during testing as this value was not at 0 so each day had a different colour to the one specified in the text output.
colornum=0
#for loop for i in range num_of_days which is the 7 multipled by the number of weeks, to allow every day's bacteria to be plotted. This was added during testing as it was noted that using 7 here would mean the files for each day of the week would be overwritten when the second week began, so changes over longer periods could not be seen.
for i in range(num_of_days):
    #print function to tell the user which day the bacteria are being shown for. I+1 is used as python begins counting from 0 but day0 is not user friendly as this does not make sense. Plotted in bright white to alter the user to this text as it is important for seeing change over time.
    print("\033[1;37mAdditional bacteria for Day", i+1, "are shown in", color[colornum])
    #print function to tell the user that the cleaner removed bacteria is shown in white. Plotted in bright white to alter the user to this text as it is important for seeing change over time.
    print("\033[1;37mAny bacteria removed by cleaners are shown in White Crosses")
    #Display the image of the bacteria files into the iPython console directly.
    display(Image(filename="Day{0}.jpg".format(i)))
    #Add one to the colornum counter
    colornum=colornum+1
    #If colornum is equal to 7, set it back to 0. This is as when the model runs for over one week, without this function the model would crash with an index out of range error, so is reset to 0 to colour each day the same, for each week in the model.
    if colornum==7:
        colornum=0
        
#Close the datastore file, as everything needed has been written to it now.
f2.close()