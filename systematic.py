# This scripts compiles the confidence intervals from the output csv files 
# obtained from newmontecarlo.m, the output is saved in a csv file.
import sys
import glob
import pandas as pd
import os

index = int(sys.argv[-1]) - 1

# Path of folder with your csv files obtained from newmontecarlo.m 
path = r"/mnt/gs21/scratch/kastejos/systematic_test/21%"
path2 = r"/mnt/gs21/scratch/kastejos/systematic_test/2%"

files = glob.glob(os.path.join(path, "*.csv"))
files_2 = glob.glob(os.path.join(path2, "*.csv"))

all_df = []
all_df2 = []
for f in files:
    df = pd.read_csv(f, sep=',')
    df['file_name'] = f.split('/')[-1]
    all_df.append(df)
    
for f in files_2:
    df = pd.read_csv(f, sep=',')
    df['file_name'] = f.split('/')[-1]
    all_df2.append(df)
    
merged_df = pd.concat(all_df, ignore_index=True)
merged_df2 = pd.concat(all_df2, ignore_index=True)

merged_df = pd.concat(all_df, ignore_index=True)
merged_df = merged_df[merged_df['type'] == 'Net flux']
merged_df2 = pd.concat(all_df2, ignore_index=True)
merged_df2 = merged_df2[merged_df2['type'] == 'Net flux']

# find unique ids 

parameters = merged_df['id'].unique()

parameters_values_21 = []
parameters_values_2 = []

for i in range(len(parameters)):
    temp_21 = []
    temp_2 = []
    temp_21 = merged_df[merged_df['id'] == parameters[i]]
    temp_2 = merged_df2[merged_df2['id'] == parameters[i]]
    parameters_values_21.append(temp_21)
    parameters_values_2.append(temp_2)

boolean_list = []

temp_list = []
for i in range(len(parameters_values_21[index])):
    for p in range(len(parameters_values_2[index])):
        sample = parameters_values_21[index].iloc[i]['val']
        sample2 = parameters_values_2[index].iloc[p]['val']
        temp_list.append(sample > sample2)
boolean_list.append(temp_list)

probabilities = []

for n in range(len(boolean_list)):

    probability = sum(boolean_list[n])/(len(parameters_values_21[index])*(len(parameters_values_2[index])))
    probabilities.append(probability)

print(probability)