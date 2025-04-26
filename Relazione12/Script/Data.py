import math
import numpy as np

# DEGREES

theta_i_degrees = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0,
                   15.0, 16.0, 17.0, 18.0, 19.0, 20.0,
                   21.0, 22.0, 23.0, 24.0, 25.0, 28.0]
dtheta_i_degrees = 0.5

theta_ip_degrees = [69.0, 66.5, 64.5, 62.5, 61.0, 59.5,
                    58.0, 56.5, 55.0, 53.5, 52.5, 50.5,
                    49.5, 48.5, 47.5, 45.5, 45.0, 41.5]
dtheta_ip_degrees = 0.5

theta_min_degrees = 36.0
dtheta_min_degrees = 1.0

alpha_degrees = 45

# RADIANS

theta_i_radians = np.radians(theta_i_degrees)
dtheta_i_radians = np.radians(dtheta_i_degrees)

theta_ip_radians = np.radians(theta_ip_degrees)
dtheta_ip_radians = np.radians(dtheta_ip_degrees)

theta_min_radians = np.radians(theta_min_degrees)
dtheta_min_radians = np.radians(dtheta_min_degrees)

alpha_radians = np.radians(alpha_degrees)