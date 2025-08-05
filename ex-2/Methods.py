from Grid import Grid
import pyconrad as pyc
import math
import numpy as np
import pyopencl as cl
import matplotlib.pyplot as plt


def create_sinogram(phantom, number_of_projections, detector_spacing, detector_size, scan_range):

    angular_increment = #calculate angular_increment
    sinogram =  #define sinogram as a Grid 
            #set sinogram origin

    #for loop over angular range 

        ...

        #for loop over detector size

            ...

            # Point on the line parallel to the detector through the origin of the phantom
            ...

            ray_sum = 0.0
            # for loop to sample along the X ray with a sampling distance delta_t
                ...
            # integral is a sum over samples, afterwards the sum need to be multiplied by delta_t

            # set the value to the sinogram

    return sinogram


def backproject(sinogram, size_x, size_y, grid_spacing):
    # reco = define reco as a Grid
    #   set reco as a
    #
    # ...
    #
    # for loop over x index
    #     for loop over y index
    #         calculate world coordinate (x,y)
    #
    #         for loop over angular index
    #             calculate rotation angle
    #             calculate physical detector position s
    #             read the corresponding sinogram value and add the value to the reconstruction pixel value at x_i, y_j
    #
    # return reco


def ramp_filter(sinogram, detector_spacing):
    filter_array = np.zeros(sinogram.width)
    ...
    return result


def ramlak_filter(sinogram, detector_spacing):
    #next_power_of_2 = next_power_of_two(sinogram.width)
    #filter_array = np.zeros(2 * next_power_of_2)

    filter_array = np.zeros(sinogram.width)



    return result


def next_power_of_two(value):
    if is_power_of_two(value):
        return value * 2
    else:
        i = 2
        while i <= value:
            i *= 2
        return i * 2


def is_power_of_two(k):
    return k and not k & (k - 1)


