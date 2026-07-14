import numpy as np

def recover_reflectance(log_image, illumination):

    reflectance_log = log_image - illumination

    reflectance = np.exp(reflectance_log)

    # Stretch contrast
    reflectance = np.power(reflectance, 0.6)

    return reflectance