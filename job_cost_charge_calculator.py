from tkinter import * 
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
        self.jobs = [self.job_num, self.name, self.distance, self.minutes, self.wof_and_tune, self.charge]

class JobCost:
    def __init__(self, parent):
        #Add Jobs Frame
        self.add_job_frame = Frame(parent)

        #Add a Job Label
        self.add_job_label = Label(text = "Add a Job", anchor = NW, font = ("Sans Serif", 16))
        self.add_job_label.grid(row = 1, column = 0)

        #Job Number Label
        self.job_num_label = Label(text = "Job Number", anchor = NW, font = ("Sans Serif", 12))
        self.job_num_label.grid(row = 2, column = 0)

        #Name Label
        self.name_label = Label(text = "Name", anchor = NW, font = ("Sans Serif", 14))
        self.name_label.grid(row = 3, column = 0)


        
        self.add_job_frame.grid(row = 0, column = 0)

#Main Routine
if __name__=="__main__":
    root= Tk()
    ratings = JobCost(root)
    root.title("Job Cost/Charge Calculator")
    root.mainloop()
