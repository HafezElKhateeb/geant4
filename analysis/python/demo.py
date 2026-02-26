#!/usr/bin/env python

# %% get path to the script relative to the workdir of the kernel
import os
workdir = os.getcwd()
print(f"workdir in the container: {workdir}")
scriptdir = os.path.dirname(__file__)
print(f"script path in the host: {scriptdir}")
subdir = scriptdir.rpartition("geant4/")[-1]
print(f"path relative to the workdir: {subdir}")

# %% generate random numbers based on a gaussian distribution
import numpy as np
data = np.random.normal(loc=100.0, scale=2.0, size=100000)
print(f"random numbers: {data}")

# %% save data to a root file
import uproot
filename = subdir + "/spectrum.root"
with uproot.recreate(filename) as f:
    f["t"] = {"e": data}
print(f"data saved to {filename} (tree: t, branch: e)")

# %% read data from the root file
with uproot.open(filename) as f:
    e = f["t"]["e"].array()
print(f"read branch e from {filename}")

# %% plot data
import matplotlib.pyplot as plt
plt.hist(e, bins=100)
plt.title("Spectrum generated from a ROOT TTree")
plt.xlabel("Energy [MeV]")
plt.ylabel("Events")
plt.grid(axis='both', alpha=0.3)
plt.show()

# %%
