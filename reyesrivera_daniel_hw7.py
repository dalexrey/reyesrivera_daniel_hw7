# Import modules
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.table import Table, Column


# 1. Read the datafile sed.txt and save to table
  # columns are wavelength (micron) and 
  # specific luminosity (Lsun/micron)
data = Table.read('sed.txt', format='ascii')
data.rename_column('col1', 'Wavelength')
data.rename_column('col2', 'Luminosity')
data['Wavelength'].unit = u.micron
data['Luminosity'].unit = u.Lsun / u.micron


# 2. Integrate from 10 - 1000 microns
IR_data = data[(data['Wavelength'] > 10) & (data['Wavelength'] < 1000)]
IR_ergs = (np.trapz(IR_data['Luminosity'], -IR_data['Wavelength']) << u.Lsun ).to(u.erg/u.s)
print('Specific Luminosity in the IR: ', IR_ergs)


# 3. Plot spectral energy distribution
plt.rcParams["figure.figsize"] = [16, 9]
plt.style.use('dark_background')
plt.rc('axes', labelsize=16, titlesize=20)

xs = data['Wavelength']
ys = data['Luminosity']

plt.plot(xs, ys, c='c')
plt.xscale('log')
plt.yscale('log')

plt.title('Spectral Energy Distribution')
plt.xlabel(r'Wavelength  $\mu m$')
plt.ylabel(r'Specific Luminosity  $\frac{L_{\odot}}{\mu m}$')
_=plt.xlim(0.09)

plt.savefig('reyesrivera_daniel_hw7.png')