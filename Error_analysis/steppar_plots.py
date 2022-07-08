## Loading Xspec...
import xspec
from xspec import *
AllModels.lmod("relxill", dirPath="/home/brian/relxill")

### Line to load .xmc file
Xset.restore("pl_sim_psd4.xcm")

## Parallelisation 
Xset.parallel.leven = 28
Xset.parallel.steppar = 28
Xset.parallel.error = 28
Fit.nIterations = 50

## Steppar
# O1 ##

## Index1
Fit.query = "yes"
Fit.steppar("5 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha index1/cps")
xspec.Plot("cont")


## gamma
Fit.query = "yes"
Fit.steppar("13 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha gamma_o1/cps")
xspec.Plot("cont")

## logxi
Fit.query = "yes"
Fit.steppar("14 0.0 4.7 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha logxi_o1/cps")
xspec.Plot("cont")


## logN
Fit.query = "yes"
Fit.steppar("16 15.0 19.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha logN/cps")
xspec.Plot("cont")


## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("20 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o1/cps")
xspec.Plot("cont")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("21 10.0 100.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_sh_o1/cps")
xspec.Plot("cont")



## PSDsoft diskpar
Fit.query = "yes"
Fit.steppar("23 0.001 0.1 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha disc_par_o1/cps")
xspec.Plot("cont")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("24 0.0 2.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha emiss_o1/cps")
xspec.Plot("cont")


##### O2 #####


## gamma
Fit.query = "yes"
Fit.steppar("118 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha gamma_o2/cps")
xspec.Plot("cont")


## logxi
Fit.query = "yes"
Fit.steppar("119 0.0 4.7 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha logxi_o2/cps")
xspec.Plot("cont")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("125 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o2/cps")
xspec.Plot("cont")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("126 10.0 100.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_sh_o2/cps")
xspec.Plot("cont")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("129 0.0 2.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha emiss_o2/cps")
xspec.Plot("cont")


##### O3 #####


## gamma
Fit.query = "yes"
Fit.steppar("223 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha gamma_o3/cps")
xspec.Plot("cont")


## logxi
Fit.query = "yes"
Fit.steppar("224 0.0 4.7 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha logxi_o3/cps")
xspec.Plot("cont")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("230 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o3/cps")
xspec.Plot("cont")


## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("231 10.0 100.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_sh_o3/cps")
xspec.Plot("cont")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("234 0.0 2.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha emiss_o3/cps")
xspec.Plot("cont")


##### O4 #####


## gamma
Fit.query = "yes"
Fit.steppar("328 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha gamma_o4/cps")
xspec.Plot("cont")


## logxi
Fit.query = "yes"
Fit.steppar("329 0.0 4.7 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha logxi_o4/cps")
xspec.Plot("cont")


## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("335 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o4/cps")
xspec.Plot("cont")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("336 10.0 100.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_sh_o4/cps")
xspec.Plot("cont")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("339 0.0 2.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha emiss_o4/cps")
xspec.Plot("cont")

##### O5 #####


## gamma
Fit.query = "yes"
Fit.steppar("433 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha gamma_o5/cps")
xspec.Plot("cont")


## logxi
Fit.query = "yes"
Fit.steppar("434 0.0 4.7 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha logxi_o5/cps")
xspec.Plot("cont")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("440 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o5/cps")
xspec.Plot("cont")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("441 10.0 100.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_sh_o5/cps")
xspec.Plot("cont")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("444 0.0 2.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha emiss_o5/cps")
xspec.Plot("cont")



##### O6 #####



## gamma
Fit.query = "yes"
Fit.steppar("538 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha gamma_o6/cps")
xspec.Plot("cont")


## logxi
Fit.query = "yes"
Fit.steppar("539 0.0 4.7 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha logxi_o6/cps")
xspec.Plot("cont")




## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("545 4.0 150.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_trc_o6/cps")
xspec.Plot("cont")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("546 10.0 100.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha r_sh_o6/cps")
xspec.Plot("cont")


## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("549 0.0 2.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha emiss_o6/cps")
xspec.Plot("cont")


Xset.save("pl_sim_psd4_1")
