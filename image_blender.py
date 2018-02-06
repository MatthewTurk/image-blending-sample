import astropy.io.fits as fits
nmos502 = fits.open("502nmos.fits")
nmos656 = fits.open("656nmos.fits")
nmos673 = fits.open("673nmos.fits")
v1 = nmos502[0].data
v2 = nmos656[0].data
v3 = nmos673[0].data

print("This is a mistake!")
