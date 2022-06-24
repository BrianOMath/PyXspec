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
# nH
#Fit.query = "yes"
#Fit.steppar("2 0.0 10.0 20")

## Saving Plotsf
#Plot.device = "/xw"
#Plot("cont")
#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("ha nH_o1/cps")


## Pho Index
#Fit.query = "yes"
#Fit.steppar("3 0.0 10.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")
#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("PhoIndex_o1/cps")


## powerlaw norm
#Fit.query = "yes"
#Fit.steppar("4 0.0 1.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")
#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("norm_po_o1/cps")



## Index1
Fit.query = "yes"
Fit.steppar("5 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("index1/cps")


## gamma
Fit.query = "yes"
Fit.steppar("13 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("gamma_o1/cps")


## logxi
Fit.query = "yes"
Fit.steppar("14 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("logxi_o1/cps")


## logN
Fit.query = "yes"
Fit.steppar("16 15.0 19.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("logN/cps")



## refl_frac
#Fit.query = "yes"
#Fit.steppar("17 0.0 10.0 20 ")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("refl_frac_o1/cps")



## relxillD norm
Fit.query = "yes"
Fit.steppar("18 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("norm_relxillD_o1/cps")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("20 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_trc_o1/cps")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("21 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_sh_o1/cps")



## PSDsoft diskpar
Fit.query = "yes"
Fit.steppar("23 0.001 0.1 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("disc_par_o1/cps")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("24 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("emiss_o1/cps")


## PSDsoft norm
Fit.query = "yes"
Fit.steppar("25 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDsoft_norm_o1/cps")



## PSDhard norm
Fit.query = "yes"
Fit.steppar("32 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDhard_norm_o1/cps")



##### O2 #####


## Pho Index
#Fit.query = "yes"
#Fit.steppar("108 0.0 10.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("PhoIndex_o2/cps")


## powerlaw norm
#Fit.query = "yes"
#Fit.steppar("109 0.0 1.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("norm_po_o2/cps")



## gamma
Fit.query = "yes"
Fit.steppar("118 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("gamma_o2/cps")


## logxi
Fit.query = "yes"
Fit.steppar("119 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("logxi_o2/cps")



## refl_frac
#Fit.query = "yes"
#Fit.steppar("122 0.0 10.0 20 ")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("refl_frac_o2/cps")



## relxillD norm
Fit.query = "yes"
Fit.steppar("123 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("norm_relxillD_o2/cps")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("125 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_trc_o2/cps")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("126 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_sh_o2/cps")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("129 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("emiss_o2/cps")


## PSDsoft norm
Fit.query = "yes"
Fit.steppar("130 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDsoft_norm_o2/cps")



## PSDhard norm
Fit.query = "yes"
Fit.steppar("137 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDhard_norm_o2/cps")

## 




##### O3 #####


## Pho Index
#Fit.query = "yes"
#Fit.steppar("213 0.0 10.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("PhoIndex_o3/cps")


## powerlaw norm
#Fit.query = "yes"
#Fit.steppar("214 0.0 1.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("norm_po_o3/cps")



## gamma
Fit.query = "yes"
Fit.steppar("223 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("gamma_o3/cps")


## logxi
Fit.query = "yes"
Fit.steppar("224 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("logxi_o3/cps")



## refl_frac
#Fit.query = "yes"
#Fit.steppar("227 0.0 10.0 20 ")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("refl_frac_o3/cps")



## relxillD norm
Fit.query = "yes"
Fit.steppar("228 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("norm_relxillD_o3/cps")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("230 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_trc_o3/cps")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("231 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_sh_o3/cps")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("234 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("emiss_o3/cps")


## PSDsoft norm
Fit.query = "yes"
Fit.steppar("235 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDsoft_norm_o3/cps")



## PSDhard norm
Fit.query = "yes"
Fit.steppar("242 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDhard_norm_o3/cps")

## 



##### O4 #####


## Pho Index
#Fit.query = "yes"
#it.steppar("318 0.0 10.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("PhoIndex_o4/cps")


## powerlaw norm
#Fit.query = "yes"
#Fit.steppar("319 0.0 1.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("norm_po_o4/cps")



## gamma
Fit.query = "yes"
Fit.steppar("328 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("gamma_o4/cps")


## logxi
Fit.query = "yes"
Fit.steppar("329 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("logxi_o4/cps")



## refl_frac
#Fit.query = "yes"
#Fit.steppar("332 0.0 10.0 20 ")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("refl_frac_o4/cps")



## relxillD norm
Fit.query = "yes"
Fit.steppar("333 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("norm_relxillD_o4/cps")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("335 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_trc_o4/cps")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("336 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_sh_o4/cps")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("339 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("emiss_o4/cps")


## PSDsoft norm
Fit.query = "yes"
Fit.steppar("340 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDsoft_norm_o4/cps")



## PSDhard norm
Fit.query = "yes"
Fit.steppar("347 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDhard_norm_o4/cps")

## 




##### O5 #####


## Pho Index
#Fit.query = "yes"
#Fit.steppar("423 0.0 10.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("PhoIndex_o5/cps")


## powerlaw norm
#Fit.query = "yes"
#Fit.steppar("424 0.0 1.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("orm_po_o5/cps")



## gamma
Fit.query = "yes"
Fit.steppar("433 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("gamma_o5/cps")


## logxi
Fit.query = "yes"
Fit.steppar("434 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("logxi_o5/cps")



## refl_frac
#Fit.query = "yes"
#Fit.steppar("437 0.0 10.0 20 ")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("refl_frac_o5/cps")



## relxillD norm
Fit.query = "yes"
Fit.steppar("438 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("norm_relxillD_o5/cps")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("440 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_trc_o5/cps")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("441 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_sh_o5/cps")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("444 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("emiss_o5/cps")


## PSDsoft norm
Fit.query = "yes"
Fit.steppar("445 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDsoft_norm_o5/cps")



## PSDhard norm
Fit.query = "yes"
Fit.steppar("452 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDhard_norm_o5/cps")

## 





##### O6 #####


## Pho Index
#Fit.query = "yes"
#Fit.steppar("528 0.0 10.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("PhoIndex_o6/cps")


## powerlaw norm
#Fit.query = "yes"
#Fit.steppar("529 0.0 1.0 20")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("norm_po_o6/cps")



## gamma
Fit.query = "yes"
Fit.steppar("538 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("gamma_o6/cps")


## logxi
Fit.query = "yes"
Fit.steppar("539 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("logxi_o6/cps")



## refl_frac
#Fit.query = "yes"
#Fit.steppar("542 0.0 10.0 20 ")

## Saving Plots
#Plot.device = "/xw"
#Plot("cont")

#xspec.Plot.addCommand("la t")
#xspec.Plot.addCommand("tim off")
#xspec.Plot.addCommand("fo ro")
#xspec.Plot.addCommand("lw 3")
#Plot()
#xspec.Plot.addCommand("refl_frac_o6/cps")



## relxillD norm
Fit.query = "yes"
Fit.steppar("543 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("norm_relxillD_o6/cps")



## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("545 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_trc_o6/cps")



## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("546 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("r_sh_o6/cps")



## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("549 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("emiss_o6/cps")


## PSDsoft norm
Fit.query = "yes"
Fit.steppar("550 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDsoft_norm_o6/cps")



## PSDhard norm
Fit.query = "yes"
Fit.steppar("557 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")

xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
Plot()
xspec.Plot.addCommand("PSDhard_norm_o6/cps")

## 

Xset.save("pl_sim_psd4_1")
