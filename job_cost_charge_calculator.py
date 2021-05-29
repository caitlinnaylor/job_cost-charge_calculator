from tkinter import *
import math
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
        self.add_job_frame.configure(pady = 10, padx = 10)
        self.add_job_frame.grid(row = 0, column = 0)

        #Company Logo
        #Suzy has supplied and given permission for this logo to be used in this programme

        self.logo = PhotoImage(file = "logo.gif")
        self.logo_label = Label(self.add_job_frame, image = self.logo)
        self.logo_label.grid(row = 0, column = 0, columnspan = 4)
            
        #Add a Job Label
        self.add_job_label = Label(self.add_job_frame, text = "Add a Job",
                                   font = ("Sans Serif", 17))
        self.add_job_label.grid(row = 1, column = 0, sticky = NW)

        #Job Number Label
        self.job_num_label = Label(self.add_job_frame, text = "Job Number",
                                   font = ("Sans Serif", 11))
        self.job_num_label.grid(row = 2, column = 0, sticky = NW)

        #Job Number Input
        self.job_num_var = IntVar()
        self.job_num_var.set("")
        self.job_num_box = Entry(self.add_job_frame, font = ("Sans Serif", 10),
                                 textvariable = self.job_num_var, width = 30)
        self.job_num_box.grid(row = 2, column = 1, columnspan = 3, sticky = NW)

        #Name Label
        self.name_label = Label(self.add_job_frame, text = "Name",
                                font = ("Sans Serif", 11))
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
                                      font = ("Sans Serif", 8))
        self.first_name_label.grid(row = 5, column = 0, sticky = NW)

        #Last Name Label
        self.last_name_label = Label(self.add_job_frame, text = "Last Name",
                                     font = ("Sans Serif", 8))
        self.last_name_label.grid(row = 5, column = 1, sticky = NW)

        #Distance Travelled Label
        self.distance_label = Label(self.add_job_frame,
                                    text = "Distance Travelled to Client (km)",
                                    font = ("Sans Serif", 11))
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
                                   font = ("Sans Serif", 11))
        self.minutes_label.grid(row = 7, column = 0, sticky = NW)

        #Minutes Input
        self.minutes_var = IntVar()
        self.minutes_var.set("")
        self.minutes_box = Entry(self.add_job_frame, font = ("Sans Serif", 10),
                                 width = 30, textvariable = self.minutes_var)
        self.minutes_box.grid(row = 7, column = 1, columnspan = 3, sticky = NW)

        #Wof and tune Label
        wof_and_tune_label = Label(self.add_job_frame, text = "Was a WOF and Tune Required?",
                                   font = ("Sans Serif", 11))
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
                                                 font = ("Sans Serif", 11)))
            self.wof_tune_rbs[i].grid(row = 8, column = i +1, sticky = NW)

        #Enter Button to add a job
        #lambda code from
        #https://www.reddit.com/r/learnpython/comments/cdfmn5/tkinter_help_command_running_before_clicked/
        self.enter_job_btn = Button(self.add_job_frame, text = "Enter",
                                    font = ("Sans Serif", 11),width = 10,
                                    command = lambda:self.store_input(Job)) 
        self.enter_job_btn.grid(row = 9, column = 3, sticky = NE)

        #Show Jobs Buttons
        self.show_jobs_btn = Button(self.add_job_frame, text = "Show Jobs",
                                    font = ("Sans Serif", 11), width = 10,
                                    command = lambda:self.get_to_job_cards())
        self.show_jobs_btn.grid(row = 10, column = 3, pady = 5, sticky = NE)

        #Creation of other frames
        self.job_cards_frame = Frame(parent)

        self.error_message_frame = Frame(parent)

        #Error message creation
        self.error_label = Label(self.error_message_frame, font = ("Sans Serif", 9))

    def store_input(self, Job):
        self.minutes = self.minutes_var.get()
        self.wof_and_tune = self.wof_tune_var.get()
        self.error_label.configure(text = "")
        self.error_message_frame.grid_remove()
        if self.minutes == 0 and self.wof_and_tune == "No":
            self.minutes_var.set("")
            self.wof_tune_var.set(0)
            self.error_label.configure(text = """There is no task chosen.
Please increase minutes spent on virus protection or change WOF and Tune to 'Yes'""")
            self.error_label.grid(row = 0, column = 1 )
            self.error_message_frame.grid(row = 0, column = 0, sticky = N)

        else:
            self.job_num = self.job_num_var.get()
            self.name = self.first_name_var.get().strip().capitalize() + " " + self.last_name_var.get().strip().capitalize()
            self.distance = float(self. distance_var.get())

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

            #Reset Input Areas
            self.job_num_var.set("")
            self.first_name_var.set("")
            self.last_name_var.set("")
            self.distance_var.set("")
            self.minutes_var.set("")
            self.wof_tune_var.set(0)

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
         self.error_message_frame.grid_remove()
         if len(self.jobs)>0:
             self.add_job_frame.grid_remove()
             self.job_cards_frame.grid(row = 0, column = 0)
             self.job_cards_frame.configure(pady = 10, padx = 10)
             self.index = 0 #which job the cards are on

             #Company Logo
             #Suzy has supplied and given permission for this logo to be used in this programme

             self.logo_label = Label(self.job_cards_frame, image = self.logo)
             self.logo_label.grid(row = 0, column = 0, columnspan = 2)

             #Jobs Heading Label
             self.jobs_label = Label(self.job_cards_frame, text = "Jobs",
                                     font = ("Sans Serif", 17), pady = 5)
             self.jobs_label.grid(row = 1, column = 0, sticky = NW, pady = 5)

             #Text Box of Job Info
             self.job_info = Text(self.job_cards_frame, width = 47, height = 3,
                                     font = ("Sans Serif", 13), pady = 8, padx = 8)
             self.job_info.grid(row = 2, column = 0, columnspan = 2)


             self.job_info.insert(END,"Job Number: "+ str(self.jobs[self.index].job_num) + "\n" +
                                  "Customer Name: " + self.jobs[self.index].name + "\n" +
                                  "Total Charge: $" + str(self.jobs[self.index].charge))

             self.job_info.configure(state = 'disabled') #Disabling so the box is not typable in

             #Next and Prev Buttons
             self.nextbtn = Button(self.job_cards_frame, text = "Next Job",
                                  font = ("Sans Serif", 11), width = 8, command = self.nextjob)
             self.nextbtn.grid(row = 3, column = 1, sticky = NE, pady = 5)

             self.prevbtn = Button(self.job_cards_frame, text = "Prev Job",
                                  font = ("Sans Serif", 11), width = 8, command = self.prevjob)
             self.prevbtn.grid(row = 3, column = 0, sticky = NW, pady = 5)

             #Getting to Add a Job Frame Button
             self.add_job_btn = Button(self.job_cards_frame, text = "Add a Job",
                                  font = ("Sans Serif", 11), width = 8,
                                       command = self.get_to_add_jobs)
             self.add_job_btn.grid(row = 4, column = 1, sticky = NE)
         else:
             self.error_label.configure(text = "There are no jobs stored")
             self.error_label.grid(row = 0, column = 1 )
             self.error_message_frame.grid(row = 0, column = 0, sticky = N) 
            
    def nextjob(self):
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


    def prevjob(self):
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

    def get_to_add_jobs(self):
        self.job_cards_frame.grid_remove()
        self.add_job_frame.grid(row = 0, column = 0)

#Main Routine
if __name__=="__main__":
    root= Tk()
    ratings = JobCostGUI(root)
    root.title("Job Cost/Charge Calculator")
    root.mainloop()

