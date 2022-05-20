## Load up Xspec and Relxill
import xspec
from xspec import *
AllModels.lmod("relxill", dirPath="/home/brian/relxill")



### Line to load xmc file
Xset.restore("pl_o1_relxillD.xcm")

## Defining Model
m1 = AllModels(1)
#m2 = AllModels(2)
#m3 = AllModels(3)
#m4 = AllModels(4)
#m5 = AllModels(5)
#m6 = AllModels(6)
m = AllModels

s1 = AllData(1)
s1.ignore("0.0-3.0,10.0-**")

## Need this fit method to avoid error
Fit.statMethod = "cstat"

## Using BXA....
import bxa.xspec as bxa
import ultranest.stepsampler

#frac_remain = 0.5
#sampler.stepsampler = ultranest.stepsampler.RegionSliceSampler(nsteps=100, adaptive_nsteps='move-distance')

# define prior
transformations = [
	#bxa.create_uniform_prior_for(m1, m1.relxillD.Index1),
	bxa.create_uniform_prior_for(m1, m1.relxillD.Incl),
  	bxa.create_uniform_prior_for(m1, m1.relxillD.Rin),
  	bxa.create_uniform_prior_for(m1, m1.relxillD.gamma),
  	bxa.create_uniform_prior_for(m1, m1.relxillD.logxi),
  	#bxa.create_uniform_prior_for(m1, m1.relxillD.Afe),
  	#bxa.create_uniform_prior_for(m1, m1.relxillD.logN),
  	bxa.create_uniform_prior_for(m1, m1.relxillD.refl_frac),
  	#bxa.create_uniform_prior_for(m1, m1.relxillD.norm),
]

## Generate nested sampling
# Set output file name...
print(" Running BXA...")
outputfiles_basename = 'bxa_o1_relxillD_test6/'
solver = bxa.BXASolver(transformations=transformations, outputfiles_basename=outputfiles_basename) #, n_live_points= 100)
#solver.ultranest.ReactiveNestedSampler(num_live_points=100)
#solver.stepsampler = ultranest.stepsampler.RegionSliceSampler(nsteps=100, adaptive_nsteps='move-distance')
results = solver.run(resume=True, frac_remain=0.5) #, n_live_points= 100)
print(" BXA Finished!")


### Plotting

import matplotlib.pyplot as plt

plt.figure()
data = solver.posterior_predictions_convolved(nsamples=100)
# plot data
#plt.errorbar(x=data['bins'], xerr=data['width'], y=data['data'], yerr=data['error'],
#	label='data', marker='o', color='green')
# bin data for plotting

binned = bxa.binning(outputfiles_basename=outputfiles_basename,
  bins = data['bins'], widths = data['width'],
  data = data['data'], models = data['models'])
for point in binned['marked_binned']:
  plt.errorbar(marker='o',zorder=-1, **point)
plt.xlim(binned['xlim'])
plt.ylim(binned['ylim'][0], binned['ylim'][1]*2)
plt.gca().set_yscale('log')
if Plot.xAxis == 'keV':
	plt.xlabel('Energy [keV]')
elif Plot.xAxis == 'channel':
	plt.xlabel('Channel')
plt.ylabel('Counts/s/cm$^2$')
print('saving plot...')
plt.savefig(outputfiles_basename + 'convolved_posterior.pdf', bbox_inches='tight')
plt.close()



print('creating plot of posterior predictions ...')
plt.figure()
solver.posterior_predictions_unconvolved(nsamples=100)
ylim = plt.ylim()
# 3 orders of magnitude at most
plt.ylim(max(ylim[0], ylim[1] / 1000), ylim[1])
plt.gca().set_yscale('log')
if Plot.xAxis == 'keV':
	plt.xlabel('Energy [keV]')
elif Plot.xAxis == 'channel':
	plt.xlabel('Channel')
plt.ylabel('Energy flux density [erg/s/cm$^2$/keV]')
print('saving plot...')
plt.savefig(outputfiles_basename + 'unconvolved_posterior.pdf', bbox_inches='tight')
plt.close()



print('creating quantile-quantile plot ...')
plt.figure(figsize=(7,7))
with bxa.XSilence():
	solver.set_best_fit()
	bxa.qq.qq(prefix=outputfiles_basename, markers=5, annotate=True)
print('saving plot...')
plt.savefig(outputfiles_basename + 'qq_model_deviations.pdf', bbox_inches='tight')
plt.close()
