## Loading Xspec...
import xspec
from xspec import *
AllModels.lmod("relxill", dirPath="/home/brian/relxill")

### Line to load .xmc file
Xset.restore("pl_sim_psd4.xcm")

## Parallelisation 
Xset.parallel.leven = 10
Xset.parallel.steppar = 10
Xset.parallel.error = 10

## Steppar
## O1 ##
## nH
Fit.query = "no"
Fit.steppar("2 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl 
ha nH_o1/cps
qq


## Pho Index
Fit.query = "no"
Fit.steppar("3 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PhoIndex_o1/cps
qq

## powerlaw norm
Fit.query = "no"
Fit.steppar("4 0.0 1.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_po_o1/cps
qq


## Index1
Fit.query = "no"
Fit.steppar("5 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha index1/cps
qq

## gamma
Fit.query = "no"
Fit.steppar("13 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha gamma_o1/cps
qq

## logxi
Fit.query = "no"
Fit.steppar("14 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logxi_o1/cps
qq

## logN
Fit.query = "no"
Fit.steppar("16 15.0 19.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logN/cps
qq


## refl_frac
Fit.query = "no"
Fit.steppar("17 0.0 10.0 20 ")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha refl_frac_o1/cps
qq


## relxillD norm
Fit.query = "no"
Fit.steppar("18 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_relxillD_o1/cps
qq


## PSDsoft r_trc
Fit.query = "no"
Fit.steppar("20 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_trc_o1/cps
qq


## PSDsoft r_sh
Fit.query = "no"
Fit.steppar("21 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_sh_o1/cps
qq


## PSDsoft diskpar
Fit.query = "no"
Fit.steppar("23 0.001 0.1 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha disc_par_o1/cps
qq


## PSDsoft emiss
Fit.query = "no"
Fit.steppar("24 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha emiss_o1/cps
qq

## PSDsoft norm
Fit.query = "no"
Fit.steppar("25 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDsoft_norm_o1/cps
qq


## PSDhard norm
Fit.query = "no"
Fit.steppar("32 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDhard_norm_o1/cps
qq


##### O2 #####


## Pho Index
Fit.query = "no"
Fit.steppar("108 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PhoIndex_o2/cps
qq

## powerlaw norm
Fit.query = "no"
Fit.steppar("109 0.0 1.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_po_o2/cps
qq


## gamma
Fit.query = "no"
Fit.steppar("118 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha gamma_o2/cps
qq

## logxi
Fit.query = "no"
Fit.steppar("119 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logxi_o2/cps
qq


## refl_frac
Fit.query = "no"
Fit.steppar("122 0.0 10.0 20 ")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha refl_frac_o2/cps
qq


## relxillD norm
Fit.query = "no"
Fit.steppar("123 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_relxillD_o2/cps
qq


## PSDsoft r_trc
Fit.query = "no"
Fit.steppar("125 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_trc_o2/cps
qq


## PSDsoft r_sh
Fit.query = "no"
Fit.steppar("126 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_sh_o2/cps
qq


## PSDsoft emiss
Fit.query = "no"
Fit.steppar("129 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha emiss_o2/cps
qq

## PSDsoft norm
Fit.query = "no"
Fit.steppar("130 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDsoft_norm_o2/cps
qq


## PSDhard norm
Fit.query = "no"
Fit.steppar("137 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDhard_norm_o2/cps
qq
## 




##### O3 #####


## Pho Index
Fit.query = "no"
Fit.steppar("213 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PhoIndex_o3/cps
qq

## powerlaw norm
Fit.query = "no"
Fit.steppar("214 0.0 1.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_po_o3/cps
qq


## gamma
Fit.query = "no"
Fit.steppar("223 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha gamma_o3/cps
qq

## logxi
Fit.query = "no"
Fit.steppar("224 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logxi_o3/cps
qq


## refl_frac
Fit.query = "no"
Fit.steppar("227 0.0 10.0 20 ")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha refl_frac_o3/cps
qq


## relxillD norm
Fit.query = "no"
Fit.steppar("228 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_relxillD_o3/cps
qq


## PSDsoft r_trc
Fit.query = "no"
Fit.steppar("230 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_trc_o3/cps
qq


## PSDsoft r_sh
Fit.query = "no"
Fit.steppar("231 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_sh_o3/cps
qq


## PSDsoft emiss
Fit.query = "no"
Fit.steppar("234 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha emiss_o3/cps
qq

## PSDsoft norm
Fit.query = "no"
Fit.steppar("235 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDsoft_norm_o3/cps
qq


## PSDhard norm
Fit.query = "no"
Fit.steppar("242 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDhard_norm_o3/cps
qq
## 



##### O4 #####


## Pho Index
Fit.query = "no"
Fit.steppar("318 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PhoIndex_o4/cps
qq

## powerlaw norm
Fit.query = "no"
Fit.steppar("319 0.0 1.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_po_o4/cps
qq


## gamma
Fit.query = "no"
Fit.steppar("328 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha gamma_o4/cps
qq

## logxi
Fit.query = "no"
Fit.steppar("329 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logxi_o4/cps
qq


## refl_frac
Fit.query = "no"
Fit.steppar("332 0.0 10.0 20 ")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha refl_frac_o4/cps
qq


## relxillD norm
Fit.query = "no"
Fit.steppar("333 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_relxillD_o4/cps
qq


## PSDsoft r_trc
Fit.query = "no"
Fit.steppar("335 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_trc_o4/cps
qq


## PSDsoft r_sh
Fit.query = "no"
Fit.steppar("336 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_sh_o4/cps
qq


## PSDsoft emiss
Fit.query = "no"
Fit.steppar("339 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha emiss_o4/cps
qq

## PSDsoft norm
Fit.query = "no"
Fit.steppar("340 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDsoft_norm_o4/cps
qq


## PSDhard norm
Fit.query = "no"
Fit.steppar("347 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDhard_norm_o4/cps
qq
## 




##### O5 #####


## Pho Index
Fit.query = "no"
Fit.steppar("423 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PhoIndex_o5/cps
qq

## powerlaw norm
Fit.query = "no"
Fit.steppar("424 0.0 1.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_po_o5/cps
qq


## gamma
Fit.query = "no"
Fit.steppar("433 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha gamma_o5/cps
qq

## logxi
Fit.query = "no"
Fit.steppar("434 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logxi_o5/cps
qq


## refl_frac
Fit.query = "no"
Fit.steppar("437 0.0 10.0 20 ")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha refl_frac_o5/cps
qq


## relxillD norm
Fit.query = "no"
Fit.steppar("438 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_relxillD_o5/cps
qq


## PSDsoft r_trc
Fit.query = "no"
Fit.steppar("440 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_trc_o5/cps
qq


## PSDsoft r_sh
Fit.query = "no"
Fit.steppar("441 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_sh_o5/cps
qq


## PSDsoft emiss
Fit.query = "no"
Fit.steppar("444 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha emiss_o5/cps
qq

## PSDsoft norm
Fit.query = "no"
Fit.steppar("445 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDsoft_norm_o5/cps
qq


## PSDhard norm
Fit.query = "no"
Fit.steppar("452 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDhard_norm_o5/cps
qq
## 





##### O6 #####


## Pho Index
Fit.query = "no"
Fit.steppar("528 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PhoIndex_o6/cps
qq

## powerlaw norm
Fit.query = "no"
Fit.steppar("529 0.0 1.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_po_o6/cps
qq


## gamma
Fit.query = "no"
Fit.steppar("538 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha gamma_o6/cps
qq

## logxi
Fit.query = "no"
Fit.steppar("539 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logxi_o6/cps
qq


## refl_frac
Fit.query = "no"
Fit.steppar("542 0.0 10.0 20 ")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha refl_frac_o6/cps
qq


## relxillD norm
Fit.query = "no"
Fit.steppar("543 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_relxillD_o6/cps
qq


## PSDsoft r_trc
Fit.query = "no"
Fit.steppar("545 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_trc_o6/cps
qq


## PSDsoft r_sh
Fit.query = "no"
Fit.steppar("546 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_sh_o6/cps
qq


## PSDsoft emiss
Fit.query = "no"
Fit.steppar("549 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha emiss_o6/cps
qq

## PSDsoft norm
Fit.query = "no"
Fit.steppar("550 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDsoft_norm_o6/cps
qq


## PSDhard norm
Fit.query = "no"
Fit.steppar("557 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot("cont")
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDhard_norm_o6/cps
qq
## 

Xset.save("pl_sim_psd4_1")
