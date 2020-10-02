Files:
Model.py (Model file used to run the program)
Framework.py (Containing the classes of schoolchildren, staff, visitors, bacteria and cleaners)
Datastore.txt (Stores the student and staff attendance into the working directory, at the end of each day within the model- the file may or may not be created before running the code, but will be created if not)
Day{0}.jpg (The model will create a jpg file of the bacteria plotted in the schoolrooms for every day within the model. N.B. computers begin counting at 0, so Day0 is the first day of bacteria plotted and so on)

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
