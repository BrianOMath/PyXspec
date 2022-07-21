
## Loading Xspec...
import xspec
from xspec import *
AllModels.lmod("relxill", dirPath="/home/brian/relxill")

### Line to load .xmc file
Xset.restore("pl_sim_psd_only.xcm")

## Parallelisation 
Xset.parallel.leven = 8
Xset.parallel.steppar = 8
Xset.parallel.error = 8
Fit.nIterations = 50


## Steppar
### O1 ###

## r_trc
Fit.query = "yes"
Fit.steppar("2 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o1/cps")
xspec.Plot("cont")


## inclination
Fit.query = "yes"
Fit.steppar("4 15.0 60.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha inclination/cps")
xspec.Plot("cont")

## emiss
Fit.query = "yes"
Fit.steppar("6 0.0 2.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha emiss_o1/cps")
xspec.Plot("cont")

### O2 ###

## r_trc
Fit.query = "yes"
Fit.steppar("38 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o2/cps")
xspec.Plot("cont")

### O3 ###

## r_trc
Fit.query = "yes"
Fit.steppar("74 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o3/cps")
xspec.Plot("cont")

### O4 ###

## r_trc
Fit.query = "yes"
Fit.steppar("110 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o4/cps")
xspec.Plot("cont")

### O5 ###

## r_trc
Fit.query = "yes"
Fit.steppar("146 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o5/cps")
xspec.Plot("cont")

### O6 ###

## r_trc
Fit.query = "yes"
Fit.steppar("182 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o6/cps")
xspec.Plot("cont")

### End ### 
Xset.save("pl_sim_psd4_only_1")
