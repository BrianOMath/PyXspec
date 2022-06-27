### Makes a simultaneous fit for 6 spectra using only PSDs
import xspec
from xspec import *

## Loading Group Files
AllData("1:1 xmm0760646201_0.3_0.7kev_ps.pha 2:2 xmm0760646201_0.7_1.5kev_ps.pha 	3:3 xmm0760646301_0.3_0.7kev_ps.pha 4:4 xmm0760646301_0.7_1.5kev_ps.pha 	5:5  xmm0760646401_0.3_0.7kev_ps.pha 6:6 xmm0760646401_0.7_1.5kev_ps.pha 	7:7  xmm0760646501_0.3_0.7kev_ps.pha 8:8 xmm0760646501_0.7_1.5kev_ps.pha 9:9 xmm0760646601_0.3_0.7kev_ps.pha 10:10 xmm0760646601_0.7_1.5kev_ps.pha 11:11  xmm0760646701_0.3_0.7kev_ps.pha 12:12 xmm0760646701_0.7_1.5kev_ps.pha")

# O1
s1 = AllData(1)
s2 = AllData(2)

# O2
s3 = AllData(3)
s4 = AllData(4)

# O3
s5 = AllData(5)
s6 = AllData(6)

# O4
s7 = AllData(7)
s8 = AllData(8

# O5
s9 = AllData(9)
s10 = AllData(10)

# O6
s11 = AllData(11)
s12 = AllData(12)

## Ignoring spectrum ranges
# O1
s1.ignore("1.5-**")
s2.ignore("2.5-**")

# O2
s3.ignore("1.5-**")
s4.ignore("2.5-**")

# O3
s5.ignore("1.5-**")
s6.ignore("2.5-**")

# O4
s7.ignore("1.5-**")
s8.ignore("2.5-**")

# O5
s9.ignore("1.5-**")
s10.ignore("2.5-**")

# O6
s11.ignore("1.5-**")
s12.ignore("2.5-**")


## Model  Define
AllModels += "constant*(atable{PSDsoft.mod}) + constant*(atable{PSDhard.mod}) + constant*gaussian"
m = AllModels

# O1
m1 = AllModels(1)
m2 = AllModels(2)

# O2           
m3 = AllModels(3)
m4 = AllModels(4)

# O3             
m5 = AllModels(5)
m6 = AllModels(6)

# O4
m7 = AllModels(7)
m8 = AllModels(8)

# O5             
m9 = AllModels(9)
m10 = AllModels(10)

# O6         
m11 = AllModels(11)
m12 = AllModels(12)


# O1
# PSDsoft
x = m1
x(1).values = 1.0, 0.0 # constant PSDsoft
x(2).untie()
x(3).untie()
x(4).values = 50.0, 0.0
x(5).untie()
x(6).untie()
x(7).untie()
x(8).values = 0.0, 0.0 # constant PSDhard
x(8).frozen = True
x(9).link = x.PSDsoft.r_trc
x(10).link = x.PSDsoft.r_sh
x(11).link = x.PSDsoft.inc
x(12).link = x.PSDsoft.disc_par
x(13).link = x.PSDsoft.emiss
x(14).untie()             
x(15).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(16).values = 6.5, 0.0
x(16).frozen = True
x(17).values = 0.1, 0.0
x(17).frozen = True
x(18).values = 0.0, 0.0
x(18).frozen = True
y = m1

# PSDhard
x=m2
x(1).values = 0.0, 0.0 # constant PSDsoft
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
x(8).values = 1.0, 0.0 # constant PSDhard
x(8).frozen = True             
x(8).link = y(8)
x(9).link = y(9)
x(10).link = y(10)             
x(11).link = y(11)
x(12).link = y(12)
x(13).link = y(13)
x(14).link = y(14)
x(15).link = y(15)
x(16).link = y(16)
x(17).link = y(17)
x(18).link = y(18)
                       
# O2
## PSDsoft section
x = m3
x(1).values = 1.0, 0.0 # constant PSDsoft
x(2).untie()
x(3).untie()
x(4).values = m1.PSDsoft.inc
x(5).link = m1.PSDsoft.disc_par
x(6).link = m1.PSDsoft.emiss
x(7).untie()
x(8).values = 0.0, 0.0 # constant PSDhard
x(8).frozen = True
x(9).link = x.PSDsoft.r_trc
x(10).link = x.PSDsoft.r_sh
x(11).link = x.PSDsoft.inc
x(12).link = x.PSDsoft.disc_par
x(13).link = x.PSDsoft.emiss
x(14).untie()             
x(15).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(16).values = 6.5, 0.0
x(16).frozen = True
x(17).values = 0.1, 0.0
x(17).frozen = True
x(18).values = 0.0, 0.0
x(18).frozen = True
y = m3


## PSDhard section
x = m4
x(1).values = 0.0, 0.0 # constant PSDsoft
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
x(8).values = 1.0, 0.0 # constant PSDhard
x(8).frozen = True             
x(8).link = y(8)
x(9).link = y(9)
x(10).link = y(10)             
x(11).link = y(11)
x(12).link = y(12)
x(13).link = y(13)
x(14).link = y(14)
x(15).link = y(15)
x(16).link = y(16)
x(17).link = y(17)
x(18).link = y(18)

# O3
## PSDsoft
x = m5
x(1).values = 1.0, 0.0 # constant PSDsoft
x(2).untie()
x(3).untie()
x(4).values = m1.PSDsoft.inc
x(5).link = m1.PSDsoft.disc_par
x(6).link = m1.PSDsoft.emiss
x(7).untie()
x(8).values = 0.0, 0.0 # constant PSDhard
x(8).frozen = True
x(9).link = x.PSDsoft.r_trc
x(10).link = x.PSDsoft.r_sh
x(11).link = x.PSDsoft.inc
x(12).link = x.PSDsoft.disc_par
x(13).link = x.PSDsoft.emiss
x(14).untie()             
x(15).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(16).values = 6.5, 0.0
x(16).frozen = True
x(17).values = 0.1, 0.0
x(17).frozen = True
x(18).values = 0.0, 0.0
x(18).frozen = True
y = m5


## PSDhard section
x = m6
x(1).values = 0.0, 0.0 # constant PSDsoft
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
x(8).values = 1.0, 0.0 # constant PSDhard
x(8).frozen = True             
x(8).link = y(8)
x(9).link = y(9)
x(10).link = y(10)             
x(11).link = y(11)
x(12).link = y(12)
x(13).link = y(13)
x(14).link = y(14)
x(15).link = y(15)
x(16).link = y(16)
x(17).link = y(17)
x(18).link = y(18)

             
             
# O4
## PSDsoft
x = m7
x(1).values = 1.0, 0.0 # constant PSDsoft
x(2).untie()
x(3).untie()
x(4).values = m1.PSDsoft.inc
x(5).link = m1.PSDsoft.disc_par
x(6).link = m1.PSDsoft.emiss
x(7).untie()
x(8).values = 0.0, 0.0 # constant PSDhard
x(8).frozen = True
x(9).link = x.PSDsoft.r_trc
x(10).link = x.PSDsoft.r_sh
x(11).link = x.PSDsoft.inc
x(12).link = x.PSDsoft.disc_par
x(13).link = x.PSDsoft.emiss
x(14).untie()             
x(15).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(16).values = 6.5, 0.0
x(16).frozen = True
x(17).values = 0.1, 0.0
x(17).frozen = True
x(18).values = 0.0, 0.0
x(18).frozen = True
y = m7


## PSDhard section
x = m8
x(1).values = 0.0, 0.0 # constant PSDsoft
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
x(8).values = 1.0, 0.0 # constant PSDhard
x(8).frozen = True             
x(8).link = y(8)
x(9).link = y(9)
x(10).link = y(10)             
x(11).link = y(11)
x(12).link = y(12)
x(13).link = y(13)
x(14).link = y(14)
x(15).link = y(15)
x(16).link = y(16)
x(17).link = y(17)
x(18).link = y(18)

# O5
## PSDsoft
x = m9
x(1).values = 1.0, 0.0 # constant PSDsoft
x(2).untie()
x(3).untie()
x(4).values = m1.PSDsoft.inc
x(5).link = m1.PSDsoft.disc_par
x(6).link = m1.PSDsoft.emiss
x(7).untie()
x(8).values = 0.0, 0.0 # constant PSDhard
x(8).frozen = True
x(9).link = x.PSDsoft.r_trc
x(10).link = x.PSDsoft.r_sh
x(11).link = x.PSDsoft.inc
x(12).link = x.PSDsoft.disc_par
x(13).link = x.PSDsoft.emiss
x(14).untie()             
x(15).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(16).values = 6.5, 0.0
x(16).frozen = True
x(17).values = 0.1, 0.0
x(17).frozen = True
x(18).values = 0.0, 0.0
x(18).frozen = True
y = m9


## PSDhard section
x = m10
x(1).values = 0.0, 0.0 # constant PSDsoft
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
x(8).values = 1.0, 0.0 # constant PSDhard
x(8).frozen = True             
x(8).link = y(8)
x(9).link = y(9)
x(10).link = y(10)             
x(11).link = y(11)
x(12).link = y(12)
x(13).link = y(13)
x(14).link = y(14)
x(15).link = y(15)
x(16).link = y(16)
x(17).link = y(17)
x(18).link = y(18)


# O6
## PSDsoft
x = m11
x(1).values = 1.0, 0.0 # constant PSDsoft
x(2).untie()
x(3).untie()
x(4).values = m1.PSDsoft.inc
x(5).link = m1.PSDsoft.disc_par
x(6).link = m1.PSDsoft.emiss
x(7).untie()
x(8).values = 0.0, 0.0 # constant PSDhard
x(8).frozen = True
x(9).link = x.PSDsoft.r_trc
x(10).link = x.PSDsoft.r_sh
x(11).link = x.PSDsoft.inc
x(12).link = x.PSDsoft.disc_par
x(13).link = x.PSDsoft.emiss
x(14).untie()             
x(15).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(16).values = 6.5, 0.0
x(16).frozen = True
x(17).values = 0.1, 0.0
x(17).frozen = True
x(18).values = 0.0, 0.0
x(18).frozen = True
y = m11


## PSDhard section
x = m12
x(1).values = 0.0, 0.0 # constant PSDsoft
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
x(8).values = 1.0, 0.0 # constant PSDhard
x(8).frozen = True             
x(8).link = y(8)
x(9).link = y(9)
x(10).link = y(10)             
x(11).link = y(11)
x(12).link = y(12)
x(13).link = y(13)
x(14).link = y(14)
x(15).link = y(15)
x(16).link = y(16)
x(17).link = y(17)
x(18).link = y(18)


## Plotting...
#Plot.device = "/xw"
#Plot.xAxis = "keV"
#Plot("ldata", "del")
#Fit.renorm()


## Save file as XXX.xcm
Xset.save("pl_sim_psd_only")
