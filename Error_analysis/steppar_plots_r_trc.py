## Loading Xspec...
import xspec
from xspec import *
AllModels.lmod("relxill", dirPath="/home/brian/relxill")

### Line to load .xmc file
Xset.restore("pl_sim_psd_final.xcm")

## Parallelisation 
Xset.parallel.leven = 28
Xset.parallel.steppar = 28
Xset.parallel.error = 28
Fit.nIterations = 20
Fit.query = "no"

## Steppar
# O1 ##


## PSDsoft r_trc
Fit.steppar("20 15.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o1/cps")
xspec.Plot("cont")



##### O2 #####



## PSDsoft r_trc
Fit.steppar("116 15.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o2/cps")
xspec.Plot("cont")



##### O3 #####



## PSDsoft r_trc
Fit.steppar("212 15.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o3/cps")
xspec.Plot("cont")


##### O4 #####


## PSDsoft r_trc
Fit.steppar("308 15.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o4/cps")
xspec.Plot("cont")

##### O5 #####




## PSDsoft r_trc
Fit.steppar("404 15.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o5/cps")
xspec.Plot("cont")



##### O6 #####



## PSDsoft r_trc
Fit.steppar("500 15.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o6/cps")
xspec.Plot("cont")

