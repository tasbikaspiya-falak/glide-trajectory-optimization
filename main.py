import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize,NonlinearConstraint


rho= 1.225
g=9.81

m=5.0
s=0.6

cl_alpha=4.0
cd0=0.04

k=0.06

#Time

t=20.0
n=100
dt=t/n

def simulate(alpha_array):
    x=0.0
    h=1000.0

    vx=25.0
    vh=0.0

    x_hist=[x]
    h_hist=[h]
    v_hist=[np.sqrt(vx**2+vh**2)]

    for alpha_deg in alpha_array:
        alpha = np.radians(alpha_deg)

        v=np.sqrt(vx**2+vh**2)
        v=max(v,0.1)

        cl=cl_alpha * alpha
        cd=cd0+k*cl**2

        lift=0.5 * rho * v**2 * s * cl
        drag=0.5 * rho * v**2 * s * cd

        gamma = np.arctan2(vh,vx)

        ux=np.cos(gamma)
        uy=np.sin(gamma)

        drag_x = -drag * ux
        drag_y=-drag * uy

        lift_x = -lift * ux
        lift_y = -lift * uy

        fx = drag_x + lift_x
        fy = drag_y + lift_y-m*g


        ax = fx/m
        ay=fy/m

        vx += ax * dt
        vh += ay * dt

        x += vx * dt
        h += vh * dt


        if h<=0:
            h=0



        
        x_hist.append(x)
        h_hist.append(h)
        
        v_hist.append(np.sqrt(vx**2+vh**2))


    return np.array(x_hist) , np.array(h_hist) ,np.array(v_hist) , h   



def obj(alpha_array):
    x_hist,h_hist,v_hist,final_h=simulate(alpha_array)

    return -x_hist[-1]


def final_altitude(alpha_array):
    x_hist,h_hist,v_hist,final_h=simulate(alpha_array)

    return final_h

constraint = NonlinearConstraint(
    final_altitude,
    -5.0,
    5.0
)

#initial guess

i_g=np.ones(n)*2.0

bounds=[(-5,10)]*n


result=minimize(
    obj,
    i_g,
    method='SLSQP',
    bounds=bounds,
    constraints=[constraint],
    options={
        'maxiter':200,
        'disp':True
    }
)

optical_alpha=result.x

print("\nOpmization success:")
print(result.success)

print("\nOptical alpha")
print(optical_alpha)

#final simulation


x_hist,h_hist,v_hist,final_h=simulate(optical_alpha)

time=np.linspace(0,t,len(x_hist))


print("\nfinal range = ",x_hist[-1])
print("final altitude = ",final_h)


plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(np.linspace(0,t,n),optical_alpha)
plt.ylabel("Alpha")
plt.grid(True)



plt.subplot(3,1,2)
plt.plot(time,h_hist)
plt.ylabel("Altitude")
plt.grid(True)



plt.subplot(3,1,3)
plt.plot(time,v_hist)
plt.xlabel("time")
plt.ylabel("speed")
plt.grid(True)


plt.tight_layout()
plt.savefig("results.png", dpi=300)
plt.show()


