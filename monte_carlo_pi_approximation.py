import tkinter as tk
from tkinter import ttk
import math
import random
import time

class MonteSim: 
    def __init__(self, root_frame):
        self.x1 = self.y1 = None
        self.window = root_frame
        self.window.wm_title('Monte Carlo Simulation')
        self.window.resizable(False, False)
        
        # Default values for the variables
        self.Animate_Sim = tk.BooleanVar(value=True)
        self.Hit_Col = tk.StringVar(value='dodgerblue2')
        self.Miss_Col = tk.StringVar(value='firebrick1')
        self.Dart_Cnt = tk.IntVar(value=10)
        self.Answer = tk.StringVar(value='')

        # Initialize the Label texts
        self.Hit_Color_Label = tk.Label(self.window, text='Hit Color:')
        self.Miss_Color_Label = tk.Label(self.window, text='Miss Color:')
        self.Dart_Count_Label = tk.Label(self.window, text='Dart Count:')
        self.Result_Label = tk.Label(self.window, text='Calculated:')
        
        # Initialize the canvas and its components
        self.MC_Canvas = tk.Canvas(window, width=300, height=300, highlightthickness=1, highlightbackground='steelblue', bg='white')
        self.Animate_Simulation = ttk.Checkbutton(window, text='Animate Simulation', variable= self.Animate_Sim, onvalue=True, offvalue=False)
        self.Hit_Color = ttk.Combobox(window, textvariable=self.Hit_Col, state=['readonly'], values=['dodgerblue2', 'steelblue3', 'lightskyblue1'])
        self.Miss_Color = ttk.Combobox(window, textvariable=self.Miss_Col, state=['readonly'], values=['firebrick1', 'coral2', 'firebrick4'])
        self.Dart_Count = tk.Scale(window, variable=self.Dart_Cnt, from_=10, to=100000, orient=tk.HORIZONTAL)
        self.Clear_Sim = tk.Button(window, text='Clear Simulation', command=self.Clear_MC_Canvas)
        self.Run_Sim = tk.Button(window, text='Run Simulation', command=self.Run_Simulation)
        self.MC_Result = tk.Entry(window, textvariable=self.Answer, state=['readonly'])
        
        # Layout of canvas components
        self.Animate_Simulation.place(x=390,y=10)#revert back to place() instead of grid()
        self.MC_Canvas.grid(row=3, column=1, rowspan=4, padx=10, pady=10)
        self.Dart_Count.grid(row=3, column=3, pady=10, padx=40)
        self.Hit_Color.place(x=419, y=125)
        self.Miss_Color.place(x=419, y=180)
        self.Clear_Sim.place(x=460, y=230)
        self.Run_Sim.place(x=325, y=230)
        
        # Layout of labels
        self.Hit_Color_Label.place(x=330, y=125)
        self.Miss_Color_Label.place(x=330, y=180)
        self.Dart_Count_Label.grid(row=3, column=2, pady=10, padx=10)
        self.MC_Result.place(x=435, y=280)
        self.Result_Label.place(x=330, y=280)

        # Draw axis lines and circle outline on canvas
        self.MC_Canvas.create_line(150, 0, 150, 300, width=0.001)
        self.MC_Canvas.create_line(0, 150, 300, 150, width=0.001)
        self.MC_Canvas.create_oval(0, 0, 300, 300, outline='black')

        """This function monteCarloPi uses parameter dartCount determined by the Scale to place dots
            on the canvas and perform the calculations"""
    def monteCarloPi(self, dartCount):
        dartsWithinCircle = 0       
        HitColor = self.Hit_Col.get()
        MissColor = self.Miss_Col.get()
        Animate_Bool = self.Animate_Sim.get()

        for i in range(dartCount):
            x = random.random()
            y = random.random()
            self.x1 = x * 300
            self.y1 = y * 300
            distance = math.sqrt((self.x1-150)**2 + (self.y1-150)**2)
            if Animate_Bool == False:
                if distance <= 150:  # assumes that the radius is 1
                    self.MC_Canvas.create_oval(self.x1, self.y1, self.x1+5, self.y1+5, fill=f'{HitColor}')
                    dartsWithinCircle = dartsWithinCircle + 1
                else:
                    self.MC_Canvas.create_oval(self.x1, self.y1, self.x1+5, self.y1+5, fill=f'{MissColor}')
                    
            elif Animate_Bool == True:
                if distance <= 150:
                    self.MC_Canvas.create_oval(self.x1, self.y1, self.x1+5, self.y1+5, fill=f'{HitColor}')
                    dartsWithinCircle = dartsWithinCircle + 1
                    self.window.update()
                    time.sleep(0.1)
                else:
                    self.MC_Canvas.create_oval(self.x1, self.y1, self.x1+5, self.y1+5, fill=f'{MissColor}')
                    self.window.update()
                    time.sleep(0.1)

        pi = 4 * dartsWithinCircle / dartCount
        self.Answer.set(f'{pi}')
        return

    """This function runs the simulation if the button is pressed"""
    def Run_Simulation(self):
        dart_count = self.Dart_Cnt.get()
        pi_estimate = self.monteCarloPi(dart_count)
    
    """This function clears the dots off the canvas, and resets the value of the Result Entrybox"""
    def Clear_MC_Canvas(self):
        ''' Clears the dots when active '''
        self.MC_Canvas.delete('all')
        self.Answer.set('')
        print(f"CLEARED")
    
window = tk.Tk()
app = MonteSim(window)
window.mainloop()