from ast import literal_eval
import control as ct
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
class PID:
    def __init__ (self,pol_num,pol_den,kp,input,amp,sys_gain):
        self.pol = [pol_num,pol_den]
        self.gain = sys_gain
        self.input_amplitude = amp
        self.kp = kp    
        self.input = input
        self.pol_sys = ct.tf(pol_num,pol_den)
    
    def test_paremeters(self):
        try:
            self.kp = literal_eval(self.kp)
        except:
            raise SystemError("O valor de kp")
        if input != "degrau" or input != "impulso":
            raise SystemError("Tipo de entrada não suportado")
    
    def get_pid(self):
        pass
    
    def get_step_response(self):
        x = ct.tf([1],[1],1)
        y = self.pol_sys
        Y_response,X = ct.step_response(y)
        X_response,X_2 = ct.step_response(x)
        plt.plot(X,Y_response,label = "output")
        plt.plot(X_2,X_response, label = "input")
        plt.xlabel("Amplitude")
        plt.ylabel("Tempo")
        plt.legend()
        plt.grid()
        plt.show()

    def get_impulse_response(self,**kwargs):
        x = kwargs["entrada"]
        y =  kwargs["ft"]
        X_response,Y_response = ct.impulse_response(x,y)
        plt.plot(X_response,Y_response,label = "output")
        plt.plot(X_response,x, label = "input")
        plt.xlabel("Amplitude")
        plt.ylabel("Tempo")
        plt.legend()
        plt.grid()
    
    def close_system(self):
        self.pol_sys = ct.feedback(self.pol_sys)
    
    def open_system(self):
        self.pol_sys = ct.tf(self.pol[0],self.pol[1])
    
    def pz_map_plot(self):
        x,y = ct.pzmap(self.pol_sys)
        print(x,y)
        plt.plot(x,label = "pzmap")
        plt.xlabel("Eixo Real")
        plt.ylabel("Eixo imaginário")
        plt.legend()
        plt.grid()
        plt.show()
    
    def lgr_plot(self):
        y,x = ct.root_locus(self.pol_sys)
        print(y)
        print(x == y)
        plt.xlabel("Eixo Real")
        plt.ylabel("Eixo imaginário")
        plt.legend()
        plt.grid()
        plt.show()
    
    def pid_support(self):
        pass
