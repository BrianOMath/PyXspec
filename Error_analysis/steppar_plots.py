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
Fit.query = "yes"
Fit.steppar("2 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl 
ha nH_o1/cps
qq


## Pho Index
Fit.query = "yes"
Fit.steppar("3 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PhoIndex_o1/cps
qq

## powerlaw norm
Fit.query = "yes"
Fit.steppar("4 0.0 1.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_po_o1/cps
qq


## Index1
Fit.query = "yes"
Fit.steppar("5 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha index1/cps
qq

## gamma
Fit.query = "yes"
Fit.steppar("13 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha gamma_o1/cps
qq

## logxi
Fit.query = "yes"
Fit.steppar("14 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logxi_o1/cps
qq

## logN
Fit.query = "yes"
Fit.steppar("16 15.0 19.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logN/cps
qq


## refl_frac
Fit.query = "yes"
Fit.steppar("17 0.0 10.0 20 ")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha refl_frac_o1/cps
qq


## relxillD norm
Fit.query = "yes"
Fit.steppar("18 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_relxillD_o1/cps
qq


## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("20 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_trc_o1/cps
qq


## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("21 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_sh_o1/cps
qq


## PSDsoft diskpar
Fit.query = "yes"
Fit.steppar("23 0.001 0.1 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha disc_par_o1/cps
qq


## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("24 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha emiss_o1/cps
qq

## PSDsoft norm
Fit.query = "yes"
Fit.steppar("25 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDsoft_norm_o1/cps
qq


## PSDhard norm
Fit.query = "yes"
Fit.steppar("32 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
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
Fit.query = "yes"
Fit.steppar("108 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PhoIndex_o2/cps
qq

## powerlaw norm
Fit.query = "yes"
Fit.steppar("109 0.0 1.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_po_o2/cps
qq


## gamma
Fit.query = "yes"
Fit.steppar("118 0.0 10.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha gamma_o2/cps
qq

## logxi
Fit.query = "yes"
Fit.steppar("119 0.0 4.7 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha logxi_o2/cps
qq


## refl_frac
Fit.query = "yes"
Fit.steppar("122 0.0 10.0 20 ")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha refl_frac_o2/cps
qq


## relxillD norm
Fit.query = "yes"
Fit.steppar("123 0.0 1000.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha norm_relxillD_o2/cps
qq


## PSDsoft r_trc
Fit.query = "yes"
Fit.steppar("125 4.0 15.0 40")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_trc_o2/cps
qq


## PSDsoft r_sh
Fit.query = "yes"
Fit.steppar("126 3.0 100.0 40")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha r_sh_o2/cps
qq


## PSDsoft diskpar
Fit.query = "yes"
Fit.steppar("129 0.001 0.1 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha disc_par_o2/cps
qq


## PSDsoft emiss
Fit.query = "yes"
Fit.steppar("129 0.0 2.0 20")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha emiss_o2/cps
qq

## PSDsoft norm
Fit.query = "yes"
Fit.steppar("130 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDsoft_norm_o2/cps
qq


## PSDhard norm
Fit.query = "yes"
Fit.steppar("137 0.0 1000 40")

## Saving Plots
Plot.device = "/xw"
Plot.iplot()
la t
tim off
fo ro
lw 3
pl
ha PSDhard_norm_o2/cps
qq
## 



Xset.save("pl_sim_psd4_1")
