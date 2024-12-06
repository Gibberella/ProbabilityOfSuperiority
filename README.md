# ProbabilityOfSuperiority
---
Code snippet for probability of superiority calculation from Monte Carlo samples of a Metabolic Flux Analysis model. 
## Instructions
---
1. Unzip contents of the two compressed files to separate folders on a remote cluster. These are the flux estimates in .csv format for each Monte Carlo sample for two different model setups.
2. Change the path variables in *systematic.py* to point at these two folders.
3. Run the .slurm file to distribute jobs to the cluster.
4. Each output file will contain the probability of superiority of a random value taken from the 21% O2 flux distribution to a random value taken from the 2% O2 flux distribution for a single flux.
