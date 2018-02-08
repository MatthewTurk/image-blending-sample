import matplotlib
matplotlib.rcParams["backend"] = "agg"
import numpy as np
import astropy.io.fits as fits
import h5py
import matplotlib.pyplot as plt

nmos502 = fits.open("502nmos.fits")
nmos656 = fits.open("656nmos.fits")
nmos673 = fits.open("673nmos.fits")
v1 = nmos502[0].data
v2 = nmos656[0].data
v3 = nmos673[0].data

image_array = np.array([v1,v2,v3]).transpose()

red_blend = np.array(   [1.0, 0.0, 0.0] )
green_blend = np.array( [0.0, 1.0, 0.0] )
blue_blend = np.array(  [0.0, 0.0, 1.0] )

red_channel = (red_blend * image_array).sum(axis=2)
green_channel = (green_blend * image_array).sum(axis=2)
blue_channel = (blue_blend * image_array).sum(axis=2)

image_array[:,:,0] = red_channel
image_array[:,:,1] = green_channel
image_array[:,:,2] = blue_channel

image_array = (image_array - image_array.min())/(image_array.max() -
        image_array.min())

f = h5py.File("blended.h5")
f.create_dataset("/blended", data=image_array)
f.close()
