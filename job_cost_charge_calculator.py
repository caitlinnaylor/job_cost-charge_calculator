from tkinter import *
import math
from tkinter.scrolledtext import *
#15/05/21
#Caitlin Naylor 
#Job Cost/Charge Calulator

class Job:
    def __init__(self, job_num, name, distance, minutes, wof_and_tune, charge):
        self.job_num = job_num
        self.name = name
        self.distance = distance
        self.minutes = minutes
        self.wof_and_tune = wof_and_tune
        self.charge = charge

class JobCostGUI:
    def __init__(self, parent):
        self.jobs = []
        #Add Jobs Frame
        self.add_job_frame = Frame(parent)
        self.add_job_frame.configure(pady = 10, padx = 10, bg = "#cceeff")
        self.add_job_frame.grid(row = 0, column = 0)

        #Company Logo
        #Suzy has supplied and given permission for this logo to be used in this programme

        self.logo = PhotoImage(file = "logo.gif")
        self.logo_label = Label(self.add_job_frame, image = self.logo, bg = "#cceeff")
        self.logo_label.grid(row = 0, column = 0, columnspan = 4)
            
        #Add a Job Label
        self.add_job_label = Label(self.add_job_frame, text = "Add a Job",
                                   font = ("Sans Serif", 17), bg = "#cceeff")
        self.add_job_label.grid(row = 1, column = 0, sticky = NW, pady = 5)

        #Job Number Label
        self.job_num_label = Label(self.add_job_frame, text = "Job Number",
                                   font = ("Sans Serif", 11), bg = "#cceeff")
        self.job_num_label.grid(row = 2, column = 0, sticky = NW)

        #Job Number Input
        self.job_num_var = StringVar() #StringVar so that the text box is blank upon opening
        self.job_num_var.set("")
        self.job_num_box = Entry(self.add_job_frame, font = ("Sans Serif", 10),
                                 textvariable = self.job_num_var, width = 30)
        self.job_num_box.grid(row = 2, column = 1, columnspan = 3, sticky = NW)

        #Name Label
        self.name_label = Label(self.add_job_frame, text = "Customer Name",
                                font = ("Sans Serif", 11), bg = "#cceeff")
        self.name_label.grid(row = 3, column = 0, sticky = NW)

        #First Name Input
        self.first_name_var = StringVar()
        self.first_name_var.set("")
        self.first_name_box = Entry(self.add_job_frame, font = ("Sans Serif", 10),
                                    width = 30, textvariable = self.first_name_var)
        self.first_name_box.grid(row = 4, column = 0, sticky = NW)

        #Last Name Input
        self.last_name_var = StringVar()
        self.last_name_var.set("")
        self.last_name_box = Entry(self.add_job_frame, font = ("Sans Serif", 10),
                                   width = 30, textvariable = self.last_name_var)
        self.last_name_box.grid(row = 4, column = 1, columnspan = 3, sticky = NW)

        #First Name Label
        self.first_name_label = Label(self.add_job_frame, text = "First Name",
                                      font = ("Sans Serif", 8), bg = "#cceeff")
        self.first_name_label.grid(row = 5, column = 0, sticky = NW)

        #Last Name Label
        self.last_name_label = Label(self.add_job_frame, text = "Last Name",
                                     font = ("Sans Serif", 8), bg = "#cceeff")
        self.last_name_label.grid(row = 5, column = 1, sticky = NW)

        #Distance Travelled Label
        self.distance_label = Label(self.add_job_frame,
                                    text = "Distance Travelled to Client (km)",
                                    font = ("Sans Serif", 11), bg = "#cceeff")
        self.distance_label.grid(row = 6, column = 0, sticky = NW)

        #Distance Input
        self.distance_var = StringVar() #String not Int as IntVar automatically rounds down
        self.distance_var.set("")
        self.distance_box = Entry(self.add_job_frame, font = ("Sans Serif", 10),
                                  width = 30, textvariable = self.distance_var)
        self.distance_box.grid(row = 6, column = 1, columnspan = 3, sticky = NW)

        #Minutes Spent on Virus Protection Label
        self.minutes_label = Label(self.add_job_frame,
                                   text = "Minutes Spent on Virus Protection",
                                   font = ("Sans Serif", 11), bg = "#cceeff")
        self.minutes_label.grid(row = 7, column = 0, sticky = NW)

        #Minutes Input
        self.minutes_var = StringVar() #StringVar so that the text box is blank upon opening
        self.minutes_var.set("") 
        self.minutes_box = Entry(self.add_job_frame, font = ("Sans Serif", 10),
                                 width = 30, textvariable = self.minutes_var)
        self.minutes_box.grid(row = 7, column = 1, columnspan = 3, sticky = NW)

        #Wof and tune Label
        wof_and_tune_label = Label(self.add_job_frame, text = "Was a WOF and Tune Required?",
                                   font = ("Sans Serif", 11), bg = "#cceeff")
        wof_and_tune_label.grid(row = 8, column = 0, sticky = NW)

        #Wof and tune radiobuttons
        self.wof_tune_var = StringVar()
        self.wof_tune_var.set(0)
        self.wof_tune_rbs_names = ["Yes", "No"]
        self.wof_tune_rbs = []
        
        for i in range(len(self.wof_tune_rbs_names)):
            self.wof_tune_rbs.append(Radiobutton(self.add_job_frame,
                                                 text = self.wof_tune_rbs_names[i],
                                                 value = self.wof_tune_rbs_names[i],
                                                  variable = self.wof_tune_var,
                                                 font = ("Sans Serif", 11), bg = "#cceeff"))
            self.wof_tune_rbs[i].grid(row = 8, column = i +1, sticky = NW)

        #Enter Button to add a job
        #lambda code from
        #https://www.reddit.com/r/learnpython/comments/cdfmn5/tkinter_help_command_running_before_clicked/
        self.enter_job_btn = Button(self.add_job_frame, text = "Enter",
                                    font = ("Sans Serif", 11),width = 8, bg = "white", 
                                    command = lambda:self.store_input(Job)) 
        self.enter_job_btn.grid(row = 9, column = 2, pady = 5, sticky = NE)

        #Reminder jobs a final label
        self.reminder_label = Label(self.add_job_frame,
                                    text = """Note: All job entries are final so please
double check before pressing enter""", 
                                    font = ("Sans Serif", 7), bg = "#cceeff")
        self.reminder_label.grid(row = 10, column = 2, columnspan = 2)
                                    

        #Show Jobs Buttons
        self.show_jobs_btn = Button(self.add_job_frame, text = "Show Jobs",
                                    font = ("Sans Serif", 11), width = 8, bg = "white", 
                                    command = lambda:self.get_to_job_cards())
        self.show_jobs_btn.grid(row = 9, column = 3, padx = 5, pady = 5, sticky = NE)

        #Creation of other frames
        self.job_cards_frame = Frame(parent)

        self.error_message_frame = Frame(parent)

        self.summary_frame = Frame(parent)

        #Error message label creation
        self.error_label = Label(self.error_message_frame, font = ("Sans Serif", 9))

    def store_input(self, Job):
        self.error_label.configure(text = "") #Removing any previous error messages
        self.error_message_frame.grid_remove()

        #All input places need to be filled in 
        if self.minutes_var.get() == "" or self.wof_tune_var.get() == "0" or \
           self.first_name_var.get() == "" or self.last_name_var.get() == "" or \
           self.job_num_var.get() == "" or self.distance_var.get() == "":
            self.add_job_frame.update_idletasks()
            self.error_label.configure(text = "Please fill in all the entry areas before pressing enter.")
            self.error_label.grid(row = 0, column = 1 )
            self.error_message_frame.grid(row = 0, column = 0, sticky = N)
        else:
            #If letters or decimals are entered in a field that does not take that type 
            while True:
                try:
                    self.error_label.configure(text = "") #Removing any previous error messages
                    self.error_message_frame.grid_remove()
                    self.add_job_frame.update_idletasks() 
                    self.minutes = float(self.minutes_var.get())
                    self.wof_and_tune = self.wof_tune_var.get()
                    #WOF and tune cannot be No if minutes is zero as then no task has been done 
                    if  self.minutes == 0 and self.wof_and_tune == "No":
                        self.add_job_frame.update_idletasks()
                        self.error_label.configure(text = """There is no task chosen.
Please increase minutes spent on virus protection or change WOF and Tune to 'Yes'""")
                        self.error_label.grid(row = 0, column = 1 )
                        self.error_message_frame.grid(row = 0, column = 0, sticky = N)
                        break

                    else:
                        self.distance = float(self. distance_var.get())
                        self.job_num = int(self.job_num_var.get())
                            
                        #If numbers below boundary are entered
                        #Placed after storage as for calculation variables must be int/float
                        if self.minutes < 0 or self.distance < 0 or self.job_num < 1:
                            self.add_job_frame.update_idletasks()
                            self.error_label.configure(text = """That is not a valid entry. Please note that
job number cannot be below 1, and minutes and distance cannot be below 0.""")
                            self.error_label.grid(row = 0, column = 1 )
                            self.error_message_frame.grid(row = 0, column = 0, sticky = N)
                            break
                        else:
                            self.name = self.first_name_var.get().strip().capitalize() + " " + \
                                        self.last_name_var.get().strip().capitalize()


                            #job number must be unique
                            if len(self.jobs)>0:
                                self.add_job_frame.update_idletasks()
                                for i in range(len(self.jobs)):
                                    if self.job_num == self.jobs[i].job_num: #comparing with other job numbers
                                        self.add_job_frame.update_idletasks() 
                                        self.error_label.configure(text = """Please change the job number.
The entered job number belongs to another job.""")
                                        self.error_label.grid(row = 0, column = 1 )
                                        self.error_message_frame.grid(row = 0, column = 0, sticky = N)
                                        self.job_num = 0 #this allows this entry to be easily identified as a repeat

                            #Round Distance
                            if self.distance % 1 >=0.5:
                                self.distance = math.ceil(self.distance)
                            else:
                                self.distance = math.floor(self.distance)
                                

                            self.calc_charge()

                            #Indivual Job Objects
                            self.job = Job(self.job_num, self.name, self.distance, self.minutes,
                                           self.wof_and_tune, self.charge)
                            
                            #Collection of the Objects  
                            self.jobs.append(self.job)
                            
                            #If job number has been repeated, remove the entry that was saved
                            if self.jobs[-1].job_num == 0:
                                self.jobs.pop(-1)
                                        

                            #Reset Input Areas
                            if self.job_num !=0:
                                self.job_num_var.set("")
                                self.first_name_var.set("")
                                self.last_name_var.set("")
                                self.distance_var.set("")
                                self.minutes_var.set("")
                                self.wof_tune_var.set(0)

                            break
                       
                            
                except:
                    self.add_job_frame.update_idletasks() 
                    self.error_label.configure(text = """That is not a valid entry. Please note that job number, minutes,
and distance must be numbers and that job number must be a whole number.""")
                    self.error_label.grid(row = 0, column = 1 )
                    self.error_message_frame.grid(row = 0, column = 0, sticky = N)
                    break
                

    def calc_charge(self):
        self.charge = 0
        FLAT_RATE = 10
        if self.distance <= 5:
            self.charge += FLAT_RATE
        else:
            self.charge += FLAT_RATE + ((self.distance - 5)*0.5)

        if self.wof_and_tune == self.wof_tune_rbs_names[0]: #yes
            self.charge += 100

        if self.minutes >0:
            self.charge += 0.80 *self.minutes

        #making charge 2dp as common for money
        #code inspired by:
        #https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:
            #text=Use%20str.,number%20with%20two%20decimal%20places.
        self.charge = "{:.2f}".format(self.charge) 


    def get_to_job_cards(self):
         self.error_label.configure(text = "")
         self.error_message_frame.grid_remove() #removing any previous error messages
         if len(self.jobs)>0:
             self.add_job_frame.grid_remove()
             self.summary_frame.grid_remove()
             self.job_cards_frame.grid(row = 0, column = 0)
             self.job_cards_frame.configure(pady = 10, padx = 13, bg = "#cceeff")
             self.index = 0 #which job the cards are on
             self.job_cards_frame.update_idletasks()
             #Company Logo
             #Suzy has supplied and given permission for this logo to be used in this programme

             self.logo_label = Label(self.job_cards_frame, image = self.logo, bg = "#cceeff")
             self.logo_label.grid(row = 0, column = 0, columnspan = 4)

             #Jobs Heading Label
             self.jobs_label = Label(self.job_cards_frame, text = "Jobs",
                                     font = ("Sans Serif", 17), pady = 5, bg = "#cceeff")
             self.jobs_label.grid(row = 1, column = 0, sticky = NW, pady = 5)

             #Text Box of Job Info
             self.job_info = Text(self.job_cards_frame, width = 48, height = 3,
                                     font = ("Sans Serif", 13), pady = 8, padx = 8)
             self.job_info.grid(row = 2, column = 0, columnspan = 4)


             self.job_info.insert(END,"Job Number: "+ str(self.jobs[self.index].job_num) + "\n" +
                                  "Customer Name: " + self.jobs[self.index].name + "\n" +
                                  "Total Charge: $" + str(self.jobs[self.index].charge))

             self.job_info.configure(state = 'disabled') #Disabling so the box is not typable in

             #Next and Prev Buttons
             self.nextbtn = Button(self.job_cards_frame, text = "Next Job",
                                  font = ("Sans Serif", 11), width = 8, bg = "white",
                                   command = self.nextjob)
             self.nextbtn.grid(row = 3, column = 2, sticky = NW, pady = 5)

             self.prevbtn = Button(self.job_cards_frame, text = "Prev Job",
                                  font = ("Sans Serif", 11), width = 8, bg = "white",
                                   command = self.prevjob)
             self.prevbtn.grid(row = 3, column = 1, sticky = NE, pady = 5, padx = 5)

             #Getting to Add a Job Frame Button
             self.add_job_btn = Button(self.job_cards_frame, text = "Add a Job",
                                  font = ("Sans Serif", 11), width = 8, bg = "white", 
                                       command = self.get_to_add_jobs)
             self.add_job_btn.grid(row = 4, column = 3, sticky = NE, pady = 5)

             #Getting to Summary Frame Button
             #Icon from flaticon, free licensed for use,
             self.icon = PhotoImage(file = "info-button.png")
             self.summary_btn = Button(self.job_cards_frame, image = self.icon,
                                       font = ("Sans Serif", 11), width = 30, height = 30,
                                       bg = "white", command = self.get_to_summary)
             self.summary_btn.grid(row = 1, column = 3, sticky = NE, pady = 5)
             
         else:
             self.add_job_frame.update_idletasks()
             self.error_label.configure(text = "There are no jobs stored")
             self.error_label.grid(row = 0, column = 1 )
             self.error_message_frame.grid(row = 0, column = 0, sticky = N)

            
    def nextjob(self):
        if len(self.jobs) > 1:
            if self.index != (len(self.jobs)-1): #if at end of list, go back to start
                self.index+=1
            else:
                self.index = 0

            self.job_info.configure(state = "normal") #undisabling box so content can change
            #updating text box to info for next job
            self.job_info.delete(1.0, END)
            self.job_info.insert(END,"Job Number: "+ str(self.jobs[self.index].job_num) + "\n" +
                                  "Customer Name: " + self.jobs[self.index].name + "\n" +
                                  "Total Charge: $" + str(self.jobs[self.index].charge))
            self.job_info.configure(state = "disabled")
        else:
            self.error_label.configure(text = "There is only one job stored")
            self.error_label.grid(row = 0, column = 1 )
            self.error_message_frame.grid(row = 0, column = 0, sticky = N)                                     

    def prevjob(self):
        if len(self.jobs) > 0:
            if self.index !=0:
                self.index-=1
            else:
                self.index = (len(self.jobs)-1)

            self.job_info.configure(state = "normal")
            self.job_info.delete(1.0, END)
            self.job_info.insert(END,"Job Number: "+ str(self.jobs[self.index].job_num) + "\n" +
                                  "Customer Name: " + self.jobs[self.index].name + "\n" +
                                  "Total Charge: $" + str(self.jobs[self.index].charge))
            self.job_info.configure(state = "disabled")
        else:
            self.error_label.configure(text = "There is only one job stored")
            self.error_label.grid(row = 0, column = 1 )
            self.error_message_frame.grid(row = 0, column = 0, sticky = N)

    def get_to_add_jobs(self):
        self.error_label.configure(text = "")
        self.error_message_frame.grid_remove() #removing any previous error messages
        self.job_cards_frame.grid_remove()
        self.summary_frame.grid_remove()
        self.add_job_frame.grid(row = 0, column = 0)
        self.add_job_frame.update_idletasks()

    def get_to_summary(self):
        self.job_cards_frame.grid_remove()
        self.summary_frame.grid(row = 0, column = 0)
        self.summary_frame.update_idletasks()
        self.summary_frame.configure(pady = 10, padx = 13, bg = "#cceeff")

        #Company Logo
        #Suzy has supplied and given permission for this logo to be used in this programme

        self.logo_label = Label(self.summary_frame, image = self.logo, bg = "#cceeff")
        self.logo_label.grid(row = 0, column = 0, columnspan = 2)

        #Summary Heading Label
        self.summary_label = Label(self.summary_frame, text = "Summary of Jobs",
                                 font = ("Sans Serif", 17), pady = 5, bg = "#cceeff")
        self.summary_label.grid(row = 1, column = 0, sticky = NW, pady = 5)

        #Scrolled Text box of Job Information
        self.job_summary_box = ScrolledText(self.summary_frame, font = ("Sans Serif", 13),
                                            pady = 8, padx = 8, height = 8, width = 46,
                                            wrap = 'word')
        self.job_summary_box.grid(row = 2, column = 0, columnspan = 2)

        for i in range(len(self.jobs)):
            self.job_summary_box.insert(END,"Job Number: "+ str(self.jobs[i].job_num) + "\n" +
                                      "Customer Name: " + self.jobs[i].name + "\n" +
                                        "Distance Travelled to Client (km): "
                                        + str(self.jobs[i].distance) +
                                        "\n" + "Minutes spent on Virus Protection: "
                                        + str(self.jobs[i].minutes) +
                                        "\n" + "Was WOF and Tune Required? "
                                        + self.jobs[i].wof_and_tune + "\n"
                                        + "Total Charge: $" + str(self.jobs[i].charge)
                                        + "\n" + "_____________________________" + "\n")

        self.job_summary_box.configure(state = 'disabled') #Disabling so the box is not typable in

        #Getting to Add job frame button
        self.add_a_job_btn = Button(self.summary_frame, text = "Add a Job",
                                  font = ("Sans Serif", 11), width = 8, bg = "white", 
                                       command = self.get_to_add_jobs)
        self.add_a_job_btn.grid(row = 3, column = 1, sticky = NE, pady = 10)

        #Back to Job Cards frame button
        self.back_to_job_cards_btn = Button(self.summary_frame, text = "Back",
                                            font = ("Sans Serif", 11), width = 8, bg = "white", 
                                               command = self.get_to_job_cards)
        self.back_to_job_cards_btn.grid(row = 1, column = 1, pady = 5, sticky = NE)
                                            
        

#Main Routine
if __name__=="__main__":
    root= Tk()
    ratings = JobCostGUI(root)
    root.title("Job Cost/Charge Calculator")
    root.mainloop()

