from vpython import *
#GlowScript 2.7 VPython
m1=vec(56,0,0)
m2=vec(90.7,0,0)
t = 0
g=9.81
scene=display(title="Physics Final Project - Motion of a Belayer", center=vec(0,20,0), width = 400, height = 300)
print_options(pos='right', width = 300, height = 500)
floor=box(pos=vec(0,-3,0), size=vec(100, 0.1,5))
onebox=box(pos=vec(-5,0,0), size=vec(3,3,3))
twobox=box(pos=vec(5,40,0),size=vec(5,5,5))
pulley=cylinder(pos=vec(0,50,0), axis=vec(0,0,1), radius = 5)
stringa=cylinder(pos=vec(-5, 50, 0), axis=vec(0,-1,0), length=50 ,height=0.1, width=0.1)
stringb=cylinder(pos=vec(5, 50, 0), axis=vec(0,-1,0), length=10 ,height=0.1, width=0.1)
gd3=gdisplay(width = 400, height=200, title="Acceleration vs. Time")
DE = series(graph=gd3)
f3=gcurve(color=color.green)
gd=gdisplay(width = 400, height=200, title="Velocity vs. Time")
E = series(graph=gd)
f1=gcurve(color=color.red)
gd2=gdisplay(width = 400, height=200, title="Position vs. Time")
Ed = series(graph=gd2)
f2=gcurve(color=color.cyan)
jerk = vec(-0.04312,0,0)
    
def S(s):
    print(f"Belayer's mass = {str(s.value)}kg")
    m1.x= s.value
slider(bind=S, min = 10, max=100)

def T(t):
    print(f"Climber's mass = {str(t.value)}kg")
    m2.x = t.value
slider(bind=T, min = 10, max=100)

scene2=display(width = 1, height = 1)

def V(v):
    print("Jerk = " + str(v.value) + "m/s/s/s")
    jerk.x = v.value
slider(bind=V, min = -0.1, max=-0.01, pos = scene2.caption_anchor)

print(f"Adjust the belayer's mass with the first slider, the climber's mass with the second slider, and the jerk with the third slider.\nBelayer's mass = {m1.x}kg\nClimber's mass = {m2.x}kg\nJerk = {jerk.x}m/s/s/s")

scene.waitfor('click')

while m1.x >= m2.x:
    print('There will be no movement with the given masses. Please adjust the sliders and try again.\n')
    scene.waitfor('click')
    
mass_total=m1.x+m2.x
w1=m1.x*g
w2=m2.x*g
acceleration=(w2-w1)/mass_total
accelini=acceleration
vm1 = 0
vm2 = 0

ini_h_c = twobox.pos.y

print("Scroll down to view the acceleration, velocity and position graphs!\n")

while vm1 > -0.01:
    rate(60)
    t+=.01
    acceleration += jerk.x*t
    onebox.pos.y+= 1/2*acceleration*t*t
    twobox.pos.y+= 1/2*-acceleration*t*t
    stringa.length=50-onebox.pos.y
    stringb.length=50-twobox.pos.y
    vm1 = acceleration*t
    vm2 = acceleration*t
    f3.plot(t, acceleration)
    f1.plot(t, vm1)
    f2.plot(t, onebox.pos.y)
    if twobox.pos.y <0:
        print("Ouch! Your climber fell, probably to his death. Try making the belayer a bit heavier, or the climber a bit lighter.\n")
        break
    
f_h_c = twobox.pos.y
f_h_b = onebox.pos.y

Eth = m2.x*g*ini_h_c - (f_h_c*g*m2.x + f_h_b*g*m1.x)

print(f'''The climber is {m2.x/m1.x} times heavier than the belayer

The initial acceleration of the system is {accelini}m/s/s

The final acceleration of the system is about {round(acceleration)}m/s/s

The final velocity of the belayer is about {round(vm1)}m/s

The final height of the belayer is {onebox.pos.y}m.

The final height of the climber is {twobox.pos.y}m

The vertical distance between the two climbers is {abs(twobox.pos.y-onebox.pos.y)}m

The thermal energy lost is {Eth}J''')