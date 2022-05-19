### Makes a simultaneous fit for 6 spectra using Relxill and PSDs
### Insert Relxill Directory Here ###
relxill_path = "/home/brian/relxill"

import xspec
from xspec import *


## Loading Group Files
AllData("o1_grp.fits 2:2 xmm0760646201_0.3_0.7kev_ps.pha 3:3 xmm0760646201_0.7_1.5kev_ps.pha 	4:4 o2_grp.fits 5:5 xmm0760646301_0.3_0.7kev_ps.pha 6:6 xmm0760646301_0.7_1.5kev_ps.pha 	7:7 o3_grp.fits 8:8 xmm0760646401_0.3_0.7kev_ps.pha 9:9 xmm0760646401_0.7_1.5kev_ps.pha 	10:10 o4_grp.fits 11:11 xmm0760646501_0.3_0.7kev_ps.pha 12:12 xmm0760646501_0.7_1.5kev_ps.pha 	13:13 o5_grp.fits 14:14 xmm0760646601_0.3_0.7kev_ps.pha 15:15 xmm0760646601_0.7_1.5kev_ps.pha 	16:16 o6_grp.fits 17:17 xmm0760646701_0.3_0.7kev_ps.pha 18:18 xmm0760646701_0.7_1.5kev_ps.pha")

# O1
s1 = AllData(1)
s2 = AllData(2)
s3 = AllData(3)

# O2
s4 = AllData(4)
s5 = AllData(5)
s6 = AllData(6)

# O3
s7 = AllData(7)
s8 = AllData(8)
s9 = AllData(9)

# O4
s10 = AllData(10)
s11 = AllData(11)
s12 = AllData(12)

# O5
s13 = AllData(13)
s14 = AllData(14)
s15 = AllData(15)

# O6
s16 = AllData(16)
s17 = AllData(17)
s18 = AllData(18)



## Ignoring spectrum ranges
# O1
s1.ignore("0.0-0.7,2.0-2.3,10.0-**")
s2.ignore("1.5-**")
s3.ignore("2.5-**")

# O2
s4.ignore("0.0-0.7,2.0-2.3,10.0-**")
s5.ignore("1.5-**")
s6.ignore("2.5-**")

# O3
s7.ignore("0.0-0.7,2.0-2.3,10.0-**")
s8.ignore("1.5-**")
s9.ignore("2.5-**")

# O4
s10.ignore("0.0-0.7,2.0-2.3,10.0-**")
s11.ignore("1.5-**")
s12.ignore("2.5-**")

# O5
s13.ignore("0.0-0.7,2.0-2.3,10.0-**")
s14.ignore("1.5-**")
s15.ignore("2.5-**")

# O6
s16.ignore("0.0-0.7,2.0-2.3,10.0-**")
s17.ignore("1.5-**")
s18.ignore("2.5-**")



## Loading Relxill
AllModels.lmod("relxill", dirPath=relxill_path)	## Define Relxill file loactiona here

## Model  Define
AllModels += "constant*(Tbabs*(powerlaw + relxillD)) + constant*(atable{PSDsoft.mod}) + constant*(atable{PSDhard.mod}) + constant*gaussian"
m = AllModels

# O1
m1 = AllModels(1)
m2 = AllModels(2)
m3 = AllModels(3)

# O2
m4 = AllModels(4)
m5 = AllModels(5)
m6 = AllModels(6)

# O3
m7 = AllModels(7)
m8 = AllModels(8)
m9 = AllModels(9)

# O4
m10 = AllModels(10)
m11 = AllModels(11)
m12 = AllModels(12)

# O5
m13 = AllModels(13)
m14 = AllModels(14)
m15 = AllModels(15)

# O6
m16 = AllModels(16)
m17 = AllModels(17)
m18 = AllModels(18)


# O1
## RelxillD section
x = m1
x(1).values = 1.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).untie()
x(3).untie()
x(4).untie()
x(5).values = 2.0, 0.1 
x(6).link = x.relxillD.Index1
x(7).values = 100.0
x(7).frozen = True
x(8).values = 0.998, 0.0
x(8).frozen = True
x(9).link = x.PSDsoft.inc
x(10).link = x.PSDsoft.r_trc
x(11).values = 400.0, 0.0
x(11).frozen = True
x(12).values = 0.0, 0.0
x(12).frozen = True
x(13).untie()
x(14).untie()
x(15).values = 10.0, 0.0
x(15).frozen = True
x(16).untie()
x(17).untie()
x(18).untie()
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).values = 20.0, 0.1, 5.0, 5.0, 100.0, 100.0 
x(21).untie()
x(22).values = 50.0, 0.0
x(22).frozen = True
x(23).untie()
x(24).untie()
x(25).untie()
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = x.PSDsoft.r_trc
x(28).link = x.PSDsoft.r_sh
x(29).link = x.PSDsoft.inc
x(30).link = x.PSDsoft.disc_par
x(31).link = x.PSDsoft.emiss
x(32).untie()
x(33).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(34).values = 6.5, 0.0
x(34).frozen = True
x(35).values = 0.1, 0.0
x(35).frozen = True
x(36).values = 0.0, 0.0
x(36).frozen = True
y = m1


## PSDsoft section
x = m2
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 1.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)


## PSDhard section
x = m3
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 1.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)



# O2
## RelxillD section
x = m4
x(1).values = 1.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).untie()
x(3).untie()
x(4).untie()
x(5).values = 2.0, 0.1 
x(6).link = x.relxillD.Index1
x(7).values = 100.0, 0.0
x(7).frozen = True
x(8).values = 0.998, 0.0
x(8).frozen = True
x(9).link = x.PSDsoft.inc
x(10).link = x.PSDsoft.r_trc
x(11).values = 400.0, 0.0
x(11).frozen = True
x(12).values = 0.0, 0.0
x(12).frozen = True
x(13).untie()
x(14).untie()
x(15).link = m1.relxillD.Afe
x(16).link = m1.relxillD.logN
x(17).untie()
x(18).untie()
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).values = 20.0, 0.1, 1.0, 1.0, 100.0, 100.0 
x(21).untie()
x(22).link = m1.PSDsoft.inc
x(23).link = m1.PSDsoft.disc_par
x(24).untie()
x(25).untie()
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = x.PSDsoft.r_trc
x(28).link = x.PSDsoft.r_sh
x(29).link = x.PSDsoft.inc
x(30).link = m1.PSDhard.disc_par
x(31).link = x.PSDsoft.emiss
x(32).untie()
x(33).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(34).values = 6.5, 0.0
x(34).frozen = True
x(35).values = 0.1, 0.0
x(35).frozen = True
x(36).values = 0.0, 0.0
x(36).frozen = True
y = m4


## PSDsoft section
x = m5
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 1.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)


## PSDhard section
x = m6
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 1.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)


# O3
## RelxillD section
x = m7
x(1).values = 1.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).untie()
x(3).untie()
x(4).untie()
x(5).values = 2.0, 0.1 
x(6).link = x.relxillD.Index1
x(7).values = 100.0, 0.0
x(7).frozen = True
x(8).values = 0.998, 0.0
x(8).frozen = True
x(9).link = x.PSDsoft.inc
x(10).link = x.PSDsoft.r_trc
x(11).values = 400.0, 0.0
x(11).frozen = True
x(12).values = 0.0, 0.0
x(12).frozen = True
x(13).untie()
x(14).untie()
x(15).link = m1.relxillD.Afe
x(16).link = m1.relxillD.logN
x(17).untie()
x(18).untie()
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).values = 20.0, 0.1, 1.0, 1.0, 100.0, 100.0 
x(21).untie()
x(22).link = m1.PSDsoft.inc
x(23).link = m1.PSDsoft.disc_par
x(24).untie()
x(25).untie()
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = x.PSDsoft.r_trc
x(28).link = x.PSDsoft.r_sh
x(29).link = x.PSDsoft.inc
x(30).link = m1.PSDhard.disc_par
x(31).link = x.PSDsoft.emiss
x(32).untie()
x(33).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(34).values = 6.5, 0.0
x(34).frozen = True
x(35).values = 0.1, 0.0
x(35).frozen = True
x(36).values = 0.0, 0.0
x(36).frozen = True
y = m7


## PSDsoft section
x = m8
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 1.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)


## PSDhard section
x = m9
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 1.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)


# O4
## RelxillD section
x = m10
x(1).values = 1.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).untie()
x(3).untie()
x(4).untie()
x(5).values = 2.0, 0.1 
x(6).link = x.relxillD.Index1
x(7).values = 100.0, 0.0
x(7).frozen = True
x(8).values = 0.998, 0.0
x(8).frozen = True
x(9).link = x.PSDsoft.inc
x(10).link = x.PSDsoft.r_trc
x(11).values = 400.0, 0.0
x(11).frozen = True
x(12).values = 0.0, 0.0
x(12).frozen = True
x(13).untie()
x(14).untie()
x(15).link = m1.relxillD.Afe
x(16).link = m1.relxillD.logN
x(17).untie()
x(18).untie()
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).values = 20.0, 0.1, 1.0, 1.0, 100.0, 100.0 
x(21).untie()
x(22).link = m1.PSDsoft.inc
x(23).link = m1.PSDsoft.disc_par
x(24).untie()
x(25).untie()
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = x.PSDsoft.r_trc
x(28).link = x.PSDsoft.r_sh
x(29).link = x.PSDsoft.inc
x(30).link = m1.PSDhard.disc_par
x(31).link = x.PSDsoft.emiss
x(32).untie()
x(33).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(34).values = 6.5, 0.0
x(34).frozen = True
x(35).values = 0.1, 0.0
x(35).frozen = True
x(36).values = 0.0, 0.0
x(36).frozen = True
y = m10


## PSDsoft section
x = m11
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 1.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)


## PSDhard section
x = m12
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 1.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)




# O5
## RelxillD section
x = m13
x(1).values = 1.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).untie()
x(3).untie()
x(4).untie()
x(5).values = 2.0, 0.1 
x(6).link = x.relxillD.Index1
x(7).values = 100.0, 0.0
x(7).frozen = True
x(8).values = 0.998, 0.0
x(8).frozen = True
x(9).link = x.PSDsoft.inc
x(10).link = x.PSDsoft.r_trc
x(11).values = 400.0, 0.0
x(11).frozen = True
x(12).values = 0.0, 0.0
x(12).frozen = True
x(13).untie()
x(14).untie()
x(15).link = m1.relxillD.Afe
x(16).link = m1.relxillD.logN
x(17).untie()
x(18).untie()
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).values = 20.0, 0.1, 1.0, 1.0, 100.0, 100.0 
x(21).untie()
x(22).link = m1.PSDsoft.inc
x(23).link = m1.PSDsoft.disc_par
x(24).untie()
x(25).untie()
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = x.PSDsoft.r_trc
x(28).link = x.PSDsoft.r_sh
x(29).link = x.PSDsoft.inc
x(30).link = m1.PSDhard.disc_par
x(31).link = x.PSDsoft.emiss
x(32).untie()
x(33).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(34).values = 6.5, 0.0
x(34).frozen = True
x(35).values = 0.1, 0.0
x(35).frozen = True
x(36).values = 0.0, 0.0
x(36).frozen = True
y = m13


## PSDsoft section
x = m14
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 1.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)

## PSDhard section
x = m15
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 1.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)




# O6
## RelxillD section
x = m16
x(1).values = 1.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).untie()
x(3).untie()
x(4).untie()
x(5).values = 2.0, 0.1 
x(6).link = x.relxillD.Index1
x(7).values = 100.0, 0.0
x(7).frozen = True
x(8).values = 0.998, 0.0
x(8).frozen = True
x(9).link = x.PSDsoft.inc
x(10).link = x.PSDsoft.r_trc
x(11).values = 400.0, 0.0
x(11).frozen = True
x(12).values = 0.0, 0.0
x(12).frozen = True
x(13).untie()
x(14).untie()
x(15).link = m1.relxillD.Afe
x(16).link = m1.relxillD.logN
x(17).untie()
x(18).untie()
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).values = 20.0, 0.1, 1.0, 1.0, 100.0, 100.0 
x(21).untie()
x(22).link = m1.PSDsoft.inc
x(23).link = m1.PSDsoft.disc_par
x(24).untie()
x(25).untie()
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = x.PSDsoft.r_trc
x(28).link = x.PSDsoft.r_sh
x(29).link = x.PSDsoft.inc
x(30).link = m1.PSDhard.disc_par
x(31).link = x.PSDsoft.emiss
x(32).untie()
x(33).values = 1.0, 0.1, 0.0, 0.0, 50.0 , 50.0 # constant gaussian
x(34).values = 6.5, 0.0
x(34).frozen = True
x(35).values = 0.1, 0.0
x(35).frozen = True
x(36).values = 0.0, 0.0
x(36).frozen = True
y = m16


## PSDsoft section
x = m17
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 1.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 0.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)

## PSDhard section
x = m18
x(1).values = 0.0, 0.0 # constant relxillD
x(1).frozen = True
x(2).link = y(2)
x(3).link = y(3)
x(4).link = y(4)
x(5).link = y(5)
x(6).link = y(6)
x(7).link = y(7)
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
x(19).values = 0.0, 0.0 # constant PSDsoft
x(19).frozen = True
x(20).link = y(20)
x(21).link = y(21)
x(22).link = y(22)
x(23).link = y(23)
x(24).link = y(24)
x(25).link = y(25)
x(26).values = 1.0, 0.0 # constant PSDhard
x(26).frozen = True
x(27).link = y(27)
x(28).link = y(28)
x(29).link = y(29)
x(30).link = y(30)
x(31).link = y(31)
x(32).link = y(32)
x(33).link = y(33)
x(34).link = y(34)
x(35).link = y(35)
x(36).link = y(36)




## Plotting...
#Plot.device = "/xw"
#Plot.xAxis = "keV"
#Plot("ldata", "del")
#Fit.renorm()


## Save file as XXX.xcm
Xset.save("pl_sim_psd")
