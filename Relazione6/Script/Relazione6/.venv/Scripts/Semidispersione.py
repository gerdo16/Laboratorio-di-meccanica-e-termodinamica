import numpy as np

data = np.loadtxt('diametropalline.txt')

x = data
x_error = 0.005

min = min(x)
max = max(x)

x_fin = (min+max)/2
delta_x_fin = (max-min)/2

print(x_fin, " +/- ", delta_x_fin, " mm")

r = x_fin/2
delta_r = delta_x_fin/2

r=r/1000
delta_r=delta_r/1000

print("raggio sfera: ", r, "+/-", delta_r, " m")

v = (4/3)*3.14*(r**3)
delta_v = 3*(delta_r/r)*v

m_pallina = 0.0692/1000
delta_m_pallina = 0.0004/1000

p_pallina = m_pallina/v
delta_p_pallina = ((delta_m_pallina/m_pallina)+(delta_v/v))*p_pallina

print("Volume sfera = ", v, "+/-", delta_v, " m^3")
print("Densità pallina = ", p_pallina, "+/-", delta_p_pallina)

m = 129.30-79.27
delta_m = 0.01

print("massa l=", m)
print("delta_m=", delta_m)

m=m/1000
delta_m=delta_m/1000

v_liquido = 0.00005
delta_v_liquido = 1*10**(-6)

p = m/v_liquido
delta_p = ((delta_m/m)+(delta_v_liquido/v_liquido))*p

print("Densità liquido = ", p, "+/-", delta_p, " kg/m^3")


