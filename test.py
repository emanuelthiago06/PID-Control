import control as ct
import matplotlib.pyplot as plt
from pid import PID
import sys

def test_sim():
    x = [1,[1,1]]
    num_y = 1
    den_y = [2,1,1]
    pid = PID(num_y,den_y,1,"degrau",1,1)
   # pid.get_step_response()
    #pid.close_system()
    #pid.pz_map_plot()
    pid.lgr_plot()

if __name__ == "__main__":
    test_sim()