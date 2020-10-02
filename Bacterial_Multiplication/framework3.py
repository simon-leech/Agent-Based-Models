import random

#Schoolchildren class
class Schoolchildren():
    def __init__(self, schoolchildren, schoolrooms, schooloutside, staff, bacteria, children_ill, visitors):
        #Setting up the schoolchildrens x values, with a randomvalue of any of the numbers in the schoolrooms list.
        self._x=random.choice(schoolrooms)
        #Setting up the schoolchildrens y values, with a randomvalue of any of the numbers in the schoolrooms list.
        self._y=random.choice(schoolrooms)
        #Setting up the lists that the schoolchildren require.
        self.schoolchildren=schoolchildren
        self.schoolrooms=schoolrooms
        self.staff=staff
        self.schooloutside=schooloutside
        self.bacteria=bacteria
        self.children_ill=children_ill
        self.visitors=visitors
        #Setting infect variable to 0 as no child is infected before the program runs.
        self.infect=0
        #Setting time infected variable to 0 as no child is infected before the program runs, so cannot have a time infected value.
        self.time_infected=0        

    #Move function for the schoolchildren
    def move(self):     
       if random.random()<0.5:
           self._x=(self._x+1)
       else:
           self._x=(self._x-1)
       if random.random()<0.5:
           self._y=(self._y+1)
       else:
           self._y=(self._y-1) 
           
     #Calculating distance between the schoolchild and the bacteria.
    def bact_dist(self, bacteria):
       return (self._x - bacteria._x) + (self._y - bacteria._y)
       pass    

    #Calculating distance between the schoolchild and another schoolchild. The is good as children can infect other child, so makes the model more realistic.
    def child_dist(self, child):
       return (self._x - child._x) + (self._y - child._y)
       pass 

   #Calculating distance between the schoolchild and staff members. The is good as staff can infect children, so makes the model more realistic.
    def staff_dist(self, staff):
       return (self._x - staff._x) + (self._y - staff._y)
       pass

   #Calculating distance between the schoolchild and visitors. The is good as visitors can infect children, so makes the model more realistic.
    def visitor_dist(self, visitor):
       return (self._x - visitor._x) + (self._y - visitor._y)
       pass

   #Infection function for the schoolchildren.
    def infection (self):
        #Create index_list as a new list to store into.
        index_list=[]
        #For every child in the schoolchildren list.
        for child in self.schoolchildren:
            #Calculate the childs position in the schoolchildren and store it to the index_pos variable.
            index_pos= self.schoolchildren.index(child)
            #Append the index_pos variable to the index_list list. 
            index_list.append(index_pos)
            #Calculate the distance between each child and every other child.
            child_dist=self.child_dist(child)
            #For every staff member, calculate the distance between the child and the staff members.
            for staff in self.staff:
                staff_dist=self.staff_dist(staff)
            #For every visitor, calculate the distance between the child and the visitors.
            for visitor in self.visitors:
                visitor_dist=self.visitor_dist(visitor)
            #For every bacteria, calculate the distance between the child and every bacteria.
            for bacteria in self.bacteria:
                bact_dist_child=self.bact_dist(bacteria)
            #If the distance is 1 from the distance and less than 2% chance, then the child becomes ill. This is to simulate real life, whereby you must be in close contact with a bacteria, with a low likelihood of becoming infected.
            if bact_dist_child==1 and random.random()<0.02:
                #Set the childs infect variable to 1, as they have been infected.
                self.infect=1
                #If that child is not already in the children_ill, ie they are not already ill.
                if child not in self.children_ill:
                         #Print function for testing and debugging.
                         #print("Child is infected")
                        #If the child is not yet in the children_ill list, the child is added to the children_ill list. This is good as it creates a separate list of the children_ill, in which x and y values of the children_ill remain the same, so they can be plotted visually.
                        self.children_ill.append(child)
                        #20% chance of this function happening.
                        if random.random()<0.2:
                            #Print that the child was taken home to inform the user. This is to model real life whereby some children are ill and taken home during the day.
                            print("Child is very unwell, so was taken home from school.")
                            #Set x and y values of the children to 1000, this is used as a proxy value for the home of the children.
                            self._x=1000
                            self._y=1000
            #If the child is not yet infected, but the nearby child is infected, and a 1% chance is met. Then the child becomes ill. This is used to model real life as children can infect other children.
            if self.infect==0 and child.infect==1 and random.random()<0.01 and child_dist==1:
                #Set infect variable to 1, as the child is now infected.
                self.infect=1
                #Print function to tell the user that a child has infected another child directly.
                print ("child has been infected by another child")
            #If the child is not yet infected, but the nearby staff member is infected, and a 1% chance is met. Then the child becomes ill. This is used to model real life as staff can infect children.
            if self.infect==0 and staff.infect==1 and random.random()<0.01 and staff_dist==1:
                #Set infect variable to 1, as the child is now infected.
                self.infect=1
                #Print function to tell the user that a child has been infected by staff directly.
                print ("child has been infected by Staff")
            #For every visitor in the vistors list. This is required as the visitor.infect variable will create an error, referenced before assignment without including this, as there may be no visitors or visitors are removed often. So this allows it to run well.
            for visitors in self.visitors:
            #If the child is not yet infected, but the nearby visitor is, and a 1% chance is met then the child becomes infected. This is used to model real life as visitors can infect children.    
                if self.infect==0 and visitor.infect==1 and random.random()<0.01 and visitor_dist==1:
                    #Set infect variable to 1, as the child is now infected.
                    self.infect=1
                    #Print function to tell the user that the child has been infected by visitor.
                    print ("Child has been infected by Visitor")
                    #Print function to check that the children_ill list was functioning correctly during testing.
                    #print (self.children_ill) 

#Breaktime function for the schoolchildren, which sets the schoolchildrens x and y values into the playground.
    def breaktime (self):
            #Print function to tell the user the children move outside.
            print("Breaktime, children move outside")
            #Creation of two lists to store all the x and y values of the children from inside for when they return from outside. Supposed to simulate the child remembering where their seat is in the classroom.
            self.child_roomloc_x=[]
            self.child_roomloc_y=[]
            #for all children in the schoolchildren list.
            for children in self.schoolchildren:
                #Print function to check that the self._x value was the same as the values in the child_roomloc_x list during testing.
                #print(self._x)
                #Print function to check that the self._y value was the same as the values in the child_roomloc_y list during testing.
                #print(self._y)
                #Looked into using a dictionary to store the x and y values as a tuple of keys, of the children before they go to breaktime, but dictionaries are unordered. As such, this is not possible as i need the coordinates to stay in the same order to retrieve them after breaktime.
                #Storing the childs self._x value into the childroomloc_x list to ensure it is remembered when they return from break.
                self.child_roomloc_x.append(self._x)
                #Storing the childs self._y value into the childroomloc_y list to ensure it is remembered when they return from break.
                self.child_roomloc_y.append(self._y)
                #Giving the child a random self._x coordinate of the playground. To simulate the child moving into the playground and running around.
                self._x=random.randint(70,100)
                #Giving the child a random self._x coordinate of the playground. To simulate the child moving into the playground and running around.
                self._y=random.randint(70,100)
            #Used these print functions to check that the lists were functioning correctly. initially i had made an error where the lists were created inside the loop, so were re-created each loop through and only ended up with the last coordinates. These print functions helped me to notice and rectify that.
            #print(self.child_roomloc_x)
            #print(self.child_roomloc_y)
                
    def end_breaktime (self):
            #Print function to tell the user that breaktime is now over and children are returning to class.
            print("Back to class")
            #for all children in the schoolchildren list.
            for children in self.schoolchildren:
                #Find the index_position, the numeric position of that child in the schoolchildren list and store it.
                index_pos=self.schoolchildren.index(children)
                #Used this print function to check that teh index_pos variable increments up by 1 each iteration. This checks to ensure that every schoolchild is included and their x and y values stored.
                #print(index_pos)
                #Use the index_pos variable to find that particular childs self._x value and set their self._x value back to that. This simulates the child returning to class and going to their assigned seat.
                self._x=self.child_roomloc_x[index_pos]
                #Use the index_pos variable to find that particular childs self._x value and set their self._x value back to that. This simulates the child returning to class and going to their assigned seat.
                self._y=self.child_roomloc_y[index_pos]
            #Used these print functions to check that the lists were functioning correctly. Helped me to see the error in list creation, as a traceback 'list index out of range' occurred here, warning me that the index_pos value was higher than the length of list, not what should be occurring.
            #print(self.child_roomloc_x)
            #print(self.child_roomloc_y)
            #Used these print functions to check that the self._x and y values were the same before the change of them in the breaktime function, as they are at the end of this end_breaktime function.
            #print(self._x)
            #print(self._y)

    #Weekend function
    def weekend (self):
        #Create lists
        grouplists=[]
        grouppositions=[]
        #set sum to 0 as this variable has not yet been used.
        sum=0
        #While loop for sum being less than length of the schoolchildren list. This is to ensure the number of schoolchildren are broken into randomly sized groups each time the code runs, to mimic children meeting up outside of school.
        while sum<len(self.schoolchildren):
            #Calculate a random number ranging from 0 to the maximum (length of schoolchildren list) minus the sum. This is used to ensure that the random number is generated from the values left over, so that the total at the end always adds up to the length of the schoolchildren.
            n=random.randint(0,80-sum)
            #Calculate sum as the previous sum value added to the random number generated of n.
            sum= sum+n
            #Append the sum value to the grouplists list so it is stored for use later on.
            grouplists.append(sum)
            #Print function to print grouplists to check that this functions correctly during testing.
            #print (grouplists)
        #for loop for the length of the grouplists list.
        for i in range (len(grouplists)):  
            #If loop for checking if the grouplists value is the first value in the list. 
            if grouplists[i]==grouplists[0]:
                #If the grouplists value is the first vlaue in the list then append this directly to the grouppositions list. DUring testing i noticed that when running the code below for all list positions, when the first list position was reached it would calculate the first list position minus the last, so always minus 80 which would create a negative number. 
                grouppositions.append(grouplists[i])
            #Else clause to run if the grouplists position is not the first.
            else:
                #Take away the grouplists value from the grouplists value of the position before, and then append this to the grouppositions list.
                grouppositions.append(grouplists[i] - grouplists[i-1])
                #Print function to tell the user the size of the groups that are being created.
        print("Children are meeting in groups of: ", grouppositions)
        #Set group variable to 0 to allow for testing and debugging as this can be used to assess what children end up in which groups.
        group=0
        #Created a list to store the children in once they had been put into a group. This is good as it allows for the groups to be created only once, as a loop can be used to ensure that only those children not in this list are considered, so is memory-efficient.
        stored_weekend_child=[]
        #for loop to run through the length of grouplists. This is good as it builds a group for each of the numbers, or group sizes, in the list.
        for i in range(len(grouplists)):
            #Add one to the group variable to allow for testing and debugging as this can be used to asees which children end up in which groups.
            group=group+1
            #Print grouplists, this was for testing to check that the children were placed into the correct groups.
            #print(grouplists)
            #For loop for every child in the schoolchildren list.
            for child in self.schoolchildren:
                #Calculate the indexpos, the position of that child in the schoolchildren list.
                indexpos=self.schoolchildren.index(child)
                #If this child is not already in the stored_weekend_child list, ie it has not yet got a group, then run this code. This is memory efficient as it only runs once for each child, and does not continue to reappend them.
                if child not in stored_weekend_child:
                    #If the grouplists value is more than the indexpos of that child, ie if that child should be within that group.
                    if grouplists[i]>indexpos:
                        #Append that child to the stored_weekend_child list.
                        stored_weekend_child.append(child)
                        #Print function for testing and debugging to ensure that the children are put into the right groups.
                        #print("I'm involved in group", group, "Child", indexpos)

    #Off ill function                                
    def off_ill (self):
        #For every child in the schoolchildren list
        for child in self.schoolchildren:
            #If they are infected and 80% chance is met then set their x and y to 1000. This is used as a proxy for home, so they are at home for the day. 80% chance is used to model real life whereby children may be sent into school when ill.
            if self.infect==1 and random.random()<0.8:
                #Print function used during testing to see which children were off ill.
                #index_pos=self.schoolchildren.index(child)
                #print ("Child", index_pos," is off ill")
                self._x=1000
                self._y=1000
        #For every child who is ill, in the children_ill list.
        for child in self.children_ill:
            #If they are infected then increase their time_infected variable by 1 each time.
            if self.infect==1:
                self.time_infected=self.time_infected+1
            #If the child is infected, and has been for 2 iterations and a 50% chance is met. This is used to model real life, where you are ill for a small amount of time and then can get better.
            if self.infect==1 and self.time_infected>2 and random.random()<0.5:
                #Print function to tell the user which children have recovered and are back in school, used during testing and then was removed to reduce print clutter.
#                print("Child: ", index_pos, "recovered from illness")
                #Set infect variable to 0 as the child is no longer infected.
                self.infect==0
                #Remove that child from the children_ill list.
                self.children_ill.remove(child)
                #Print functions used during testing of this function.
                #print("ATTEND", 80-len(self.children_ill))
                #print("Child removed")
                #print(len(self.children_ill))
                #print("ATTENDANCE: ", 80-len(self.children_ill))

#Staff class    
class Staff():
    def __init__ (self, schoolchildren, schoolrooms, schooloutside, staff, bacteria, killed_bact, staff_ill, visitors):
        #Setting the x coordinate of the staff member to one of the numbers in the schoolrooms list.
        self._x=random.choice(schoolrooms)
        #Setting the y coordinate of the staff member to one of the numbers in the schoolrooms list.
        self._y=random.choice(schoolrooms)
        #Setting the lists up.
        self.schoolchildren=schoolchildren
        self.schoolrooms=schoolrooms
        self.schooloutside=schooloutside
        self.bacteria=bacteria
        self.killed_bact=killed_bact
        self.staff_ill=staff_ill
        self.staff=staff
        self.visitors=visitors
        #Setting infect variable to 0, as no staff are infected prior to the model being run.
        self.infect=0
        #Set time infected variable to 0, as no staff is yet infected prior to the model being run.
        self.time_infected=0     

    #Move function for the schoolchildren
    def move(self):    
           if random.random()<0.5:
               self._x=(self._x+1)
           else:
               self._x=(self._x-1)
           if random.random()<0.5:
               self._y=(self._y+1)
           else:
               self._y=(self._y-1)         

    #Calculating distance between the staff member and the bacteria. 
    def bact_dist_staff(self, bacteria):
       return (self._x - bacteria._x) + (self._y - bacteria._y)
       pass 

    #Calculating distance between the staff member and the schoolchildren. This is as schoolchildren can infect the staff members.
    def child_dist(self, child):
       return (self._x - child._x) + (self._y - child._y)
       pass 

    #Calculating distance between the staff member and the other staff members. This is as staff can infect the staff members.
    def staff_dist(self, staff):
       return (self._x - staff._x) + (self._y - staff._y)
       pass

   #Calculating distance between the staff member and the visitors. This is as visitors can infect the staff members.
    def visitor_dist(self, visitor):
       return (self._x - visitor._x) + (self._y - visitor._y)
       pass

   #Infection function
    def infection (self):
        #Create the index_list to store index positions into.
        index_list=[]
        #For staff in the staff list
        for staff in self.staff:
            #Find out the index position of the staff in the staff list, and store to the index_pos variable.
            index_pos= self.staff.index(staff)
            #Append this variable to the index_list list for later use.
            index_list.append(index_pos)
            #Calculate the distance between the staff and the other staff members.
            staff_dist=self.staff_dist(staff)
            #For every child in the schoolchildren list.
            for child in self.schoolchildren:
                #Calculate the distance between the staff member and every child.
                child_dist=self.child_dist(child)
            #For every visitor in the visitor list
            for visitor in self.visitors:
                #Calculate the distance between the staff member and every visitor.
                visitor_dist=self.visitor_dist(visitor)
            #For every bacteria in the bacteria list
            for bacteria in self.bacteria:
                #Calculate the distance between the staff member and every bacteria.
                bact_dist_staff=self.bact_dist_staff(bacteria)
            #If the distance to the staff member from the bacteria is 1, and 2% chance is met, then the staff member becomes infected.
            if bact_dist_staff==1 and random.random()<0.02:
                self.infect=1
                #if staff member is not yet ill, not in staff_ill list.
                if staff not in self.staff_ill:
                    #Print function to check this worked.
                    #print("Staff member is infected"
                    #append the staff member to the staff_ill list.
                    self.staff_ill.append(staff)
                    #If random.random<0.2, ie 20% chance of this occurring.
                    if random.random()<0.2:
                        #Print function to tell the user a staff member went home. This is realistic as sometimes people are required to leave when they are too ill.
                        print("Staff is very unwell, so went home from school.")
                        #Set x and y values to 1000, this is the proxy value for the homes of the staff.
                        self._x=1000
                        self._y=1000
            #If the staff member is not infected, and the nearby child is and a 10% chance is met.
            if self.infect==0 and child.infect==1 and random.random()<0.1 and child_dist==1:
                #The staff member becomes ill.
                self.infected=1
                #Print function to tell the user the staff member has been infected by a child.
                print ("Staff has been infected by Child")
            #If the staff member is not infected, and the nearby staff member is infected and a 10% chance is met.
            if self.infect==0 and staff.infect==1 and random.random()<0.1 and staff_dist==1:
                #The staff member becomes ill.
                self.infect=1
                #Print function to tell the user the staff member has been infected by staff.
                print ("Staff has been infected by Staff")
            #For visitors in visitors list is used as the visitors list is often empty, so this function would run an error without this line of code.
            for visitor in self.visitors:
                #If the staff member is not infected, and the nearby visitor is infected, and a 10% chance is met.
                if self.infect==0 and visitor.infect==1 and random.random()<0.1 and visitor_dist==1:
                    #Staff member becomes ill
                    self.infect=1
                    #Print function for the user to know that the staff member has been infected by visitor.
                    print ("Staff has been infected by Visitor")

    #Weekend function
    def weekend(self):
        #If 5% chance is met
        if random.random()<0.05:
            #Print function to tell the user that a staff member has come into work.
            print("Staff member has come into work at the weekend")
            #For i in range 0,10. This is used to model the amount of the time the staff member intends to stay at work during this day.
            for i in range (random.randint(0,10)):
                #Run the staff move function, to model the staff member moving around the buildling while working.
                Staff.move(self)
            #Once this for loop is over,then tell the user via print function that the staff member has gone home.
            print("Staff member has gone home")
            #Set the x and y values to 1000, as a proxy value for their home.
            self._x=1000
            self._y=1000
         #This else function was used for testing and debugging. This is good as it ensured that the function was running correctly.
         #else:
           #print("Staff member is not at work currently")    

    #Off_ill function           
    def off_ill (self):
        #For every staff member in the staff list
        for staff in self.staff:
            #If they are infected and a 80% chance is met. This is to model the chance that the staff member may be ill but come into work anyway.
            if self.infect==1 and random.random()<0.8:
                #Find the index position of the staff member in the staff list.
                index_pos=self.schoolchildren.index(staff)
                #Print function to tell the user that a staff member is off ill this day.
                print ("staff", index_pos," is off ill")
                #Set x and y value to 1000, as a proxy for their home.
                self._x=1000
                self._y=1000

        #For every staff member in the staff_ill list.
        for staff in self.staff_ill:
            #If they are infected.
            if self.infect==1:
                #Add one to the time_infected variable, to model the time they have been ill.
                self.time_infected=self.time_infected+1
            #Find out the index_pos of that staff member in the staff_ill list.
            index_pos=self.staff_ill.index(staff)
            #If the staff member is ill and they have been ill for >2 iterations and a 50% chance is met. This is used to model the variation in the illness and how it affects people.
            if self.infect==1 and self.time_infected>2 and random.random()<0.5:
                #Print function to tell the user that the staff member has recovered, used during testing but removed to reduce clutter.
                #print("Staff: ", index_pos, "recovered from illness")
                #Set the infect variable to 0.
                self.infect==0
                #Remove this staff member from the staff_ill list.
                self.staff_ill.remove(staff)
                #Print functions used during testing and debugging.
                #print("ATTEND", 6-len(self.staff_ill))
                #print("Staff removed")
                #print(len(self.staff_ill))
                #print("ATTENDANCE: ", 80-len(self.staff_ill))
        
#Bacteria class.  
class Bacteria_class():
    def __init__ (self, schoolrooms, schooloutside,bacteria, killed_bact):
        #Setting up the lists.
        self.schoolrooms=schoolrooms
        self.schooloutside=schooloutside
        self.killed_bact=killed_bact
        self.bacteria=bacteria
        #Setting self.clean to 0 as the bacteria is not yet connected to any surface so cannot be cleaned yet.
        self.clean=0
        #Setting self._x and self._y to 1000, the home of the humans who have brought the bacteria onto site.
        self._x=1000
        self._y=1000

    #Initiate bacteria function.
    def initiate_bacteria (self, schoolrooms):
        #If loop for 50% chance of it occurring. Simulating random variation in nature.
        if random.random()<0.5:
            #Set the self._x to a random value within the schoolrooms. This is to simulate the bacteria has been brought into the school and settled on a surface in the schoolroom.
            self._x=random.choice(schoolrooms)
            #Set the self._x to a random value within the schoolrooms. This is to simulate the bacteria has been brought into the school and settled on a surface in the schoolroom.
            self._y=random.choice(schoolrooms)
            #Print function to show where the bacteria is located, used during testing to check functionality.
            #print ("Bacteria found at : ", self._x, self._y)
        else:
            #Self._x is 1000 and self._y is 1000. This is to simulate the bacteria was brought into the school but did not come into contact and settle on a surface, so remained at the humans home.
            self._x=1000
            self._y=1000
            #Print function used during testing to tell the user the bacteria did not settle in the school.
            #print("Bacteria not found on school premises")
      
    #Multiply bacteria function.
    def multiply (self):
        #If loop for less than 1% chance of reproduction, and self.clean must be 1. This is to simulate clean at 1 meaning the bacteria was not cleaned away, so can reproduce as it is still alive. 
        if random.random()<0.01 and self.clean==1:
            #Multiplier variable created from 1 to 10 to simulate random reproduction level of the bacteria.
            multiplier=random.randint(1,10)
            #For loop for the range of the multiplier variable to check iterating through.
            for i in range (multiplier):
                #Print function to tell user that bacteria multiplied, used during testing.
                #print("Bacteria multiplied")
                #Appending a new bacteria onto the bacteria list as they have multiplied.
                self.bacteria.append(Bacteria_class(self.schoolrooms,self.schooloutside,self.bacteria,self.killed_bact))
            #Print bacteria list to check that this function was working correctly during testing.
            #print(self.bacteria)

#Cleaner class  
class Cleaners ():
    def __init__ (self, schoolrooms, bacteria, killed_bact, cleaners,cleaners_ill):
        #Setting up lists needed for the cleaners.
        self.schoolrooms= schoolrooms
        self.bacteria=bacteria
        self.killed_bact= killed_bact
        self.cleaners=cleaners
        self.cleaners_ill=cleaners_ill
        #Set x and y values to a random value within the schoolrooms.
        self._x= random.choice(schoolrooms)
        self._y=random.choice(schoolrooms)
        #Set infect variable to 0 as cannot be ill before the model runs.
        self.infect=0
        
     #Move function for the cleaners. Cleaners move twice as fast as children and staff as they have a large area to clean before they leave the school.
    def move(self):     
       if random.random()<0.5:
           self._x=(self._x+2)
       else:
           self._x=(self._x-2)
       if random.random()<0.5:
           self._y=(self._y+2)
       else:
           self._y=(self._y-2) 

    #Calculating distance between the cleaner and the bacteria.
    def bact_dist_cleaners(self, bacteria):
       return (self._x - bacteria._x) + (self._y - bacteria._y)
       pass 

    #Cleaning function to prevent bacteria multiplying     
    def cleaning (self):
        #For every cleaner in the cleaners list.
        #for cleaner in self.cleaners:
            #For every bacteria in the bacteria list.
            for bacteria in self.bacteria:
                #Calculate the distance between the cleaner and the bacteria
                distancewithinspray=self.bact_dist_cleaners(bacteria)
                #Calculate the index position variable for the bacteria in the bacteria list.
                index_pos=self.bacteria.index(bacteria)
                #Print function to check the function works correctly during testing.
                #print(bact_dist_child, index_list)
                #print("Distance: ", distancewithinspray, "Bacteria:", index_pos)
                #If the distance is less than 5 but more than -5, then the bacteria is cleaned and removed. This value is used as a proxy for the bacteria spray with a distance across the surface of 5. -5 is required as the calculation can create negative values depending on cleaner or bacteria having the higher value.
                if distancewithinspray<5 and distancewithinspray>-5:
                #Set bacteria clean value to 0.
                    bacteria.clean=0
                #If the bacteria is not in killed_bact list
                    if bacteria not in self.killed_bact:
                            #Append the bacteria to the killed_bact list.
                            self.killed_bact.append(bacteria)
                            #Print function to tell the user that a bacteria has been removed and the distance from the spray, used during testing.
                            #print("Bacteria removed via cleaning as distance to cleaning spray: ", distancewithinspray)
                            #Delete this bacteria from the bacteria list using the index_pos variable to do so.
                            del self.bacteria[index_pos]  
                else:
                    bacteria.clean=1

    #Infection function
    def infection (self):   
        #For every cleaner in the cleaners list.
        for cleaner in self.cleaners:
            #For every bacteria in the bacteria list.
            for bacteria in self.bacteria:
                #Calculate the distance between the bacteria and cleaner.
                bact_dist_cleaner=self.bact_dist_cleaners(bacteria)
                #Print function during testing to check this.
                #print(bact_dist_child, index_list)
            #If the value is less than 3 and a 50% chance is met, and the value is more than 0. During testing it was noted that the distance can be negative, so 0 was needed to stop this.
            if bact_dist_cleaner<3 and bact_dist_cleaner>=0 and random.random()<0.5:
                #Infect variable set to 1.
                self.infect=1
                #If the cleaner is not in the cleaner_ill list.
                if cleaner not in self.cleaner_ill:
                        #Print that the cleaner is infected.
                        print("Cleaner is infected")
                        #Append the cleaner to the cleaner_ill list.
                        self.cleaner_ill.append(cleaner)
                        #If the random value is less than 0.2
                        if random.random()<0.2:
                            #Print function to tell the user the cleaner is unwell.
                            print("Cleaner is unwell, so was taken home from school.")
                            #Set the x and y values to 1000, the proxy for their home.
                            self._x=1000
                            self._y=1000

    #Weekend function                        
    def weekend(self):
        #If random value less than 0.05, or 5% chance.
        if random.random()<0.05:
            #Print function to tell the user that a cleaner has come into work at the weekend.
            print("Cleaner has come into work at the weekend")
            #For i in range 0,10. Used as a proxy to simulate how long the cleaner is coming into work during the day.
            for i in range (random.randint(0,10)):
                #Run the cleaning function.
                Cleaners.cleaning(self)
            #Once this for loop is done, print the cleaner has gone home.
            print("Cleaner has gone home")
            #Set x and y values to 1000, the proxy for their home.
            self._x=1000
            self._y=1000
        #This else function was used for testing and debugging. This is good as it ensured that the function was running correctly.
        #else:
            #print("Cleaner is not at work currently")    

    #Off_ill function         
    def off_ill (self):
        #For every cleaner in the cleaners list.
        for cleaner in self.cleaners:
            #If the cleaner is infected and 80% chance is met.
            if self.infect==1 and random.random()<0.8:
                #Set x and y value to 1000, the proxy for their home. Used to model that the cleaner could come to work while being ill.
                self._x=1000
                self._y=1000
        #For every cleaner in the cleaners_ill list.
        for cleaners in self.cleaners_ill:
            #If the infect variable is 1.
            if self.infect==1:
                #Add one to the time_infected variable.
                self.time_infected=self.time_infected+1
            #Calculate the index_pos for the cleaner in the cleaners_ill list. To use for print testing.
            #index_pos=self.cleaners_ill.index(cleaner)
            #If the cleaner is ill and the time_infected is more than 2 and 50% chance is met.
            if self.infect==1 and self.time_infected>2 and random.random()<0.5:
                #Print cleaner, number, recovered from illness.
                #print("Cleaner: ", index_pos, "recovered from illness")
                #Set infect to 0, as no longer ill.
                self.infect==0
                #Remove the cleaner from the cleaners_ill variable.
                self.cleaners_ill.remove(cleaner)

#Visitors class             
class Visitors():
    def __init__ (self, schoolchildren, schoolrooms, schooloutside, staff, bacteria, visitors, visitors_ill):
        #Setting the x coordinate of the staff member to one of the numbers in the schoolrooms list.
        self._x=random.choice(schoolrooms)
        #Setting the y coordinate of the staff member to one of the numbers in the schoolrooms list.
        self._y=random.choice(schoolrooms)
        #Setting the lists up that the visitors need.
        self.schoolchildren=schoolchildren
        self.schoolrooms=schoolrooms
        self.schooloutside=schooloutside
        self.bacteria=bacteria
        self.visitors=visitors
        self.visitors_ill=visitors_ill
        self.staff=staff
        #Setting infect variable to 0, as no visitors are infected prior to the model being run.
        self.infect=0
        #Setting the time_infected variable to 0, as no visitors can be infected prior to the model being run.
        self.time_infected=0
           
    #Move function for the visitors
    def move(self):    
           if random.random()<0.5:
               self._x=(self._x+1)%100
           else:
               self._x=(self._x-1)%100
           if random.random()<0.5:
               self._y=(self._y+1)%100
           else:
               self._y=(self._y-1)%100
           
    #Calculating distance between the visitor and the bacteria. 
    def bact_dist(self, bacteria):
       return (self._x - bacteria._x) + (self._y - bacteria._y)
       pass 
    
    #Calculating distance between the visitor and the schoolchild. This is done as the schoolchildren can infect the visitor.
    def child_dist(self, child):
       return (self._x - child._x) + (self._y - child._y)
       pass 

    #Calculating distance between the visitor and the staff. This is done as the staff can infect the visitor.
    def staff_dist(self, staff):
       return (self._x - staff._x) + (self._y - staff._y)
       pass

   #Calculating distance between the visitor and the other visitors. This is done as the visitors can infect each other.
    def visitor_dist(self, visitor):
       return (self._x - visitor._x) + (self._y - visitor._y)
       pass

    #Infection function
    def infection (self):
        #Creating a list for the index positions to be stored in for later use.
        index_list=[]
        #For every visitor in the visitors list.
        for visitor in self.visitors:
            #Calculate the position of that visitor within the visitors list.
            index_pos= self.visitors.index(visitor)
            #Append that index position to the index_list list.
            index_list.append(index_pos)
            #Calculate the distance between the visitor and the visitors.
            visitor_dist=self.visitor_dist(visitor)
            #For every child in schoolchildren list.
            for child in self.schoolchildren:
                #Calculate the distance between the visitor and the children.
                child_dist=self.child_dist(child)
            #For every staff member in the staff list.
            for staff in self.staff:
                #Calculate the distance between the visitor and the staff members.
                staff_dist=self.staff_dist(staff)
            #For every bacteria in the bacteria list.
            for bacteria in self.bacteria:
                #Calculate the distance between the visitor and the bacteria.
                bact_dist=self.bact_dist(bacteria)
                #Print function to check the function was working correctly during testing. 
                #print(bact_dist_child, index_list)
            #If the bacteria distance is 1, and the 2% chance is met. This is done to simulate the probability of becoming infected.
            if bact_dist==1 and random.random()<0.02:
                #Set the visitor infect value to 1.
                self.infect=1
                #If the visitor is not in visitors_ill list.
                if visitor not in self.visitor_ill:
                    #Print function for testing.
                    #print("Visitor is infected")
                    #Append that visitor to the visitor_ill list
                    self.visitor_ill.append(visitor)
                    #If 20% chance is met.This is used to model the chance of a visitor going home early because of illness.
                    if random.random()<0.2:
                        #Print function to tell the user that the visitor went home.
                        print("Visitor is very unwell, so went home from school.")
                        #Set the x and y values to 1000, the proxy for their home.
                        self._x=1000
                        self._y=1000
            #If the visitor is not infected, but the nearby child is, and a 10% chance is met.
            if self.infect==0 and child.infect==1 and random.random()<0.1 and child_dist==1:
                #The visitor is now ill.
                self.infect=1
                #Print function is used to tell the user that the visitor has been infected by child.
                print ("Visitor has been infected by Child")
            #If the visitor is not infected, but the nearby staff member is, and a 10% chance is met.
            if self.infect==0 and staff.infect==1 and random.random()<0.1 and staff_dist==1:
                #the visitor is now ill.
                self.infect=1
                #Print function to tell the user that visitor has been infected by staff.
                print ("Visitor has been infected by Staff")
            #For every visitor in the visitors list. This is used to ensure errors do not occur with reference before assignment, as visitors are added and removed often.
            for visitor in self.visitors:
                #If visitor is not ill, and nearby visitor is ill and 10% chance is met.
                if self.infect==0 and visitor.infect==1 and random.random()<0.1 and visitor_dist==1:
                    #Print function to tell the user that the visitor has been infected by another visitor.
                    print ("Visitor has been infected by Visitor")
            #If self.infect is 1, then add one to the time infected variable. This is to model the real life time a person would be infected.
            if self.infect==1:
                self.time_infected=+1
                #Print function used during testing.
                #print(self.time_infected)
            #If the visitor is ill and the time_infected is more than 2.
            if self.infect==1 and self.time_infected>=2:
                #If the 70% chance is met.
                if random.random()<0.7:
                    #Print function to tell the user that the visitor has recovered from illness, used during testing and removed as print statements added clutter.
                    #print("Visitor has recovered from illness")
                    #Set the infect variable to 0.
                    self.infect==0

    #Leave function
    def leave (self):
        #Set up visitors store list
        visitors_store=[]
        #For every visitor in the visitors list
        for visitor in self.visitors:
            #Calculate the position of that visitor in the visitors list.
            index_pos_vis=self.visitors.index(visitor)
            #If 50% chance is met, or the visitor is infected.
            if random.random()<0.5 or self.infect==1:
                #If the visitor is not currently in the visitors_store, used as a proxy for a real life register of those who have visited a school.
                if visitor not in visitors_store:
                    #Print function to tell the user the vistor has left.
                    print("Visitor has left the school")
                    #Append the visitors_store list with the visitor, to keep a record of this on the register for visitors.
                    visitors_store.append(visitor)
                    #Delete the visitor from the visitors list using their index position.
                    del self.visitors[index_pos_vis]