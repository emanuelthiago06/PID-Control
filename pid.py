from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import time
import sys

class PID:
    def __init__ (self,**kwargs):
        self.set_point = kwargs["set_point"]
        self.kp = kwargs["kp"]
        self.ki = kwargs["ki"]
        self.kd = kwargs["kd"]
        self.windup_value = 25
        self.dt = 0 ## tempo inicial
        self.sample_time = 10**-2 if "sample_time" not in kwargs else kwargs["sample_time"]
        self.I = 0
        self.P = 0
        self.D = 0
        self.x_axis = [0]
        ## Variables to use on the feedback system
        self.old_err = 0
        self.initial_time = time.time()
        self.old_time = self.initial_time
        self.old_output = 0
        self.system_counts = 0
        self.control_list = []
## Conta paralelo : u(t) = Kp*e(t)+Ki*integral(e(t)*dt)+kd*de/dt


    def update_pid(self,fd = 0):
        time_t = time.time()
        delta_t = time_t - self.old_time if time_t-self.old_time else 10**-8
        if self.sample_time <= delta_t:  ## Dont take a sample if the delta_t is lower than sample time, otherwise this can cause problems on the sampling and also on the convergence time
            err = self.set_point - fd
            delta_err = err - self.old_err
            self.P = self.kp * err
            self.I += self.ki*err * delta_t
            self.I = self.check_windup(self.I)
            self.D = delta_err/delta_t
            output = self.P + (self.I) + (self.kd*self.D)
            self.old_time = time_t
            self.old_err = err
            self.old_output = output
            return output
        else:
            return self.old_output ## Return the old output if delta_t is lower (experimental phase)

    def check_windup(self,value):
        if abs(value) > self.windup_value:
            value = abs(value)/value*self.windup_value
        return value
## IGNORE THIS FUNCTION, IT WILL BE IMPLEMENTED ON THE MAIN FILE FOR NOW


    def calcule_pid(self,max_range):
        control = 0
        self.control_list.append(control)
        for i in range(1,max_range):
            control += self.update_pid(control) + 1/i
            print(control)
            time.sleep(0.03)
            self.control_list.append(control)
            self.x_axis.append(i)
    def plot_graph(self):
        plt.plot(self.x_axis,self.control_list,color = 'r',label = 'simulado')
        set_point_list = []
        for _ in self.control_list:
            if len(set_point_list) == 0:
                set_point_list.append(0)
            else:    
                set_point_list.append(self.set_point)
        plt.plot(self.x_axis,set_point_list,color = 'b',label = 'ideal')
        plt.show()
    def run(self,max_range):
        self.calcule_pid(max_range)
        self.plot_graph()


def test_pid():
    pid = PID(kp = 1.2,kd = 0.01,ki =1,set_point = 2)
    pid.run(100)

if __name__ == "__main__":
    test_pid()
