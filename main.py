#...start...#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python console: https://trinket.io/embed/python3/55e4ddab4e?outputOnly=true&runOption=run&start=result


import matplotlib.pyplot as plt
import numpy as np
import time
import importlib


print('\n\n' + 60*'_' + '\nTransmissionspektra der diffraktions Bragg Spiegel\n')

#Import DBR_4L_CC_zum_Strahl
lambda_4L, intensity_4L = np.loadtxt("DBR_4L_CC_zum_Strahl.dat", unpack = True, skiprows = 2)

#Plot spectrum of DBR_4L_CC_zum_Strahl
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_4L, intensity_4L, '-', label='DBR_4L Transmissionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_4L Transmissionsspektrum")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()

# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)


#Import DBR_9L_KR_zum_Strahl
lambda_9L, intensity_9L = np.loadtxt("DBR_9L_KR_zum_Strahl.dat", unpack = True, skiprows = 2)

#Plot spectrum of DBR_9L_KR_zum_Strahl
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_9L, intensity_9L, '-', label='DBR_9L Transmissionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_9L Transmissionsspektrum")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()

# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)

#Import DBR_21L_CC13_zum_Strahl
lambda_21L, intensity_21L = np.loadtxt("DBR_21L_CC13_zum_Strahl.dat", unpack = True, skiprows = 2)

#Plot spectrum of DBR_9L_KR_zum_Strahl
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_21L, intensity_21L, '-', label='DBR_21L Transmissionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_21L Transmissionsspektrum")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()

# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)

# Alle drei Kurven in dem selben Plot
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_4L, intensity_4L, '-', label='DBR_4L Transmissionsspektrum')
plt.plot(lambda_9L, intensity_9L, '-', label='DBR_9L Transmissionsspektrum')
plt.plot(lambda_21L, intensity_21L, '-', label='DBR_21L Transmissionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"Transmissionsspektra vergleich")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()


# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)



print("\n\n" + 60*"_" + "\nReflektionsspektra der diffraktions Bragg Spiegel\n")


#Import DBR_4L_zu_Ulbricht
lambda_4L_ref, intensity_4L_ref = np.loadtxt("DBR_4L_zu_Ulbricht.dat", unpack = True, skiprows = 2)

#Plot spectrum of DBR_4L_zu_Ulbricht
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_4L_ref, intensity_4L_ref, '-', label='DBR_4L Reflektionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_4L Reflektionsspektrum")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()


# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)


#Import DBR_9L_zu_Ulbricht
lambda_9L_ref, intensity_9L_ref = np.loadtxt("DBR_9L_zu_Ulbricht.dat", unpack = True, skiprows = 2)

#Plot spectrum of DBR_9L_zu_Ulbricht
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_9L_ref, intensity_9L_ref, '-', label='DBR_9L Reflektionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_9L Reflektionsspektrum")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()


# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)


#Import DBR_21L_zu_Ulbricht
lambda_21L_ref, intensity_21L_ref = np.loadtxt("DBR_21L_zu_Ulbricht.dat", unpack = True, skiprows = 2)

#Plot spectrum of DBR_21L_zu_Ulbricht
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_21L_ref, intensity_21L_ref, '-', label='DBR_21L Reflektionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_21L Reflektionsspektrum")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()


# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)




print("\n\n" + 60*"_" + "\nReflektionsspektra und transmissionsspektra zusammen\n")

# Plot DBR_4L Trans. und Refl. Spektra
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_4L, intensity_4L, '-', label='DBR_4L Transmissionsspektrum')
plt.plot(lambda_4L_ref, intensity_4L_ref, '-', label='DBR_4L Reflektionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_4L Reflektionsspektrum und transmissionsspektrum zusammen")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()


# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)


# Plot DBR_9L Trans. und Refl. Spektra
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_9L, intensity_9L, '-', label='DBR_9L Transmissionsspektrum')
plt.plot(lambda_9L_ref, intensity_9L_ref, '-', label='DBR_9L Reflektionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_9L Reflektionsspektrum und transmissionsspektrum zusammen")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()


# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)


# Plot DBR_21L Trans. und Refl. Spektra
plt.figure(figsize=(8, 4), dpi=120)
plt.plot(lambda_21L, intensity_21L, '-', label='DBR_21L Transmissionsspektrum')
plt.plot(lambda_21L_ref, intensity_21L_ref, '-', label='DBR_21L Reflektionsspektrum')

plt.xlabel(r"Wellenlänge $\lambda$ / nm")
plt.ylabel(r"Relative intensität in %")
plt.legend()
plt.xlim(300, 800)
plt.ylim(0, 100)
plt.grid(True)
plt.title(r"DBR_21L Reflektionsspektrum und transmissionsspektrum zusammen")
#plt.savefig('plot_calibration.pdf', bbox_inches='tight')
plt.show()


# wait a second for reloading the matplotlib module due to issues
time.sleep(0.5)
importlib.reload(plt)
time.sleep(0.5)
#...end...#