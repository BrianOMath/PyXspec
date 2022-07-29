## Loading Xspec...
import xspec
from xspec import *

### Line to load .xmc file
Xset.restore("pl_po_laor_inde.xcm")

## Parallelisation 
Xset.parallel.leven = 8
Xset.parallel.steppar = 8
Xset.parallel.error = 8
Fit.nIterations = 50

## Steppar
### O1 ###

## PhoIndex
Fit.query = "yes"
Fit.steppar("1 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha phoindex_o1_po_laor/cps")
xspec.Plot("cont")

## LineE
Fit.query = "yes"
Fit.steppar("3 6.4 6.9 24")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha lineE_o1_po_laor/cps")
xspec.Plot("cont")

## Index
Fit.query = "yes"
Fit.steppar("4 -10.0 10.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha index_o1_po_laor/cps")
xspec.Plot("cont")

## Rin_G
Fit.query = "yes"
Fit.steppar("5 1.235 400.0 50.0")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha rin_o1_po_laor/cps")
xspec.Plot("cont")

## Incl
Fit.query = "yes"
Fit.steppar("7 0.0 90.0 36")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha incl_o1_po_laor_po_laor/cps")
xspec.Plot("cont")



### O2 ###

## PhoIndex
Fit.query = "yes"
Fit.steppar("9 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha phoindex_o2_po_laor/cps")
xspec.Plot("cont")

## LineE
Fit.query = "yes"
Fit.steppar("11 6.4 6.9 24")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha lineE_o2_po_laor/cps")
xspec.Plot("cont")

## Index
Fit.query = "yes"
Fit.steppar("12 -10.0 10.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha index_o2_po_laor/cps")
xspec.Plot("cont")

## Rin_G
Fit.query = "yes"
Fit.steppar("13 1.235 400.0 50.0")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha rin_o2_po_laor/cps")
xspec.Plot("cont")

## Incl
Fit.query = "yes"
Fit.steppar("15 0.0 90.0 36")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha incl_o2_po_laor_po_laor/cps")
xspec.Plot("cont")



### O3 ###

## PhoIndex
Fit.query = "yes"
Fit.steppar("17 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha phoindex_o3_po_laor/cps")
xspec.Plot("cont")

## LineE
Fit.query = "yes"
Fit.steppar("19 6.4 6.9 24")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha lineE_o3_po_laor/cps")
xspec.Plot("cont")

## Index
Fit.query = "yes"
Fit.steppar("20 -10.0 10.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha index_o3_po_laor/cps")
xspec.Plot("cont")

## Rin_G
Fit.query = "yes"
Fit.steppar("21 1.235 400.0 50.0")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha rin_o3_po_laor/cps")
xspec.Plot("cont")

## Incl
Fit.query = "yes"
Fit.steppar("23 0.0 90.0 36")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha incl_o3_po_laor_po_laor/cps")
xspec.Plot("cont")



### O4 ###

## PhoIndex
Fit.query = "yes"
Fit.steppar("25 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha phoindex_o4_po_laor/cps")
xspec.Plot("cont")

## LineE
Fit.query = "yes"
Fit.steppar("27 6.4 6.9 24")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha lineE_o4_po_laor/cps")
xspec.Plot("cont")

## Index
Fit.query = "yes"
Fit.steppar("28 -10.0 10.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha index_o1_po_laor/cps")
xspec.Plot("cont")

## Rin_G
Fit.query = "yes"
Fit.steppar("29 1.235 400.0 50.0")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha rin_o4_po_laor/cps")
xspec.Plot("cont")

## Incl
Fit.query = "yes"
Fit.steppar("31 0.0 90.0 36")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha incl_o4_po_laor_po_laor/cps")
xspec.Plot("cont")



### O5 ###

## PhoIndex
Fit.query = "yes"
Fit.steppar("33 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha phoindex_o5_po_laor/cps")
xspec.Plot("cont")

## LineE
Fit.query = "yes"
Fit.steppar("35 6.4 6.9 24")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha lineE_o5_po_laor/cps")
xspec.Plot("cont")

## Index
Fit.query = "yes"
Fit.steppar("36 -10.0 10.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha index_o5_po_laor/cps")
xspec.Plot("cont")

## Rin_G
Fit.query = "yes"
Fit.steppar("37 1.235 400.0 50.0")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha rin_o5_po_laor/cps")
xspec.Plot("cont")

## Incl
Fit.query = "yes"
Fit.steppar("39 0.0 90.0 36")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha incl_o5_po_laor_po_laor/cps")
xspec.Plot("cont")



### O6 ###

## PhoIndex
Fit.query = "yes"
Fit.steppar("41 0.0 10.0 20")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha phoindex_o6_po_laor/cps")
xspec.Plot("cont")

## LineE
Fit.query = "yes"
Fit.steppar("43 6.4 6.9 24")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha lineE_o6_po_laor/cps")
xspec.Plot("cont")

## Index
Fit.query = "yes"
Fit.steppar("44 -10.0 10.0 40")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha index_o6_po_laor/cps")
xspec.Plot("cont")

## Rin_G
Fit.query = "yes"
Fit.steppar("45 1.235 400.0 50.0")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha rin_o6_po_laor/cps")
xspec.Plot("cont")

## Incl
Fit.query = "yes"
Fit.steppar("47 0.0 90.0 36")

## Saving Plots
xspec.Plot.device = "/xs"
xspec.Plot.commands = ()
xspec.Plot.addCommand("la t")
xspec.Plot.addCommand("tim off")
xspec.Plot.addCommand("fo ro")
xspec.Plot.addCommand("lw 3")
xspec.Plot.addCommand("ha incl_o6_po_laor_po_laor/cps")
xspec.Plot("cont")



### End ### 
Xset.save("pl_po_laor_inde1.xcm")
