#!/usr/bin/env python
# coding: utf-8

import GEOparse
import pandas as pd

# returns a GEO object
try:
    gse = GEOparse.get_GEO(filepath="./data/GSE11501_family.soft")
except:
    gse = GEOparse.get_GEO("GSE11501")

# subset descriptions: top of GDS file
healthy_controls = ['GSM289580','GSM289581','GSM289582','GSM289583','GSM289584','GSM289585',
                    'GSM289586','GSM289587','GSM289588','GSM289589','GSM289590','GSM289591',
                    'GSM289592','GSM289593','GSM289594','GSM289595','GSM289596','GSM289597',
                    'GSM289598','GSM289599','GSM289600','GSM289601']

gene_lookup_table = gse.gpls['GPL6104'].table[['ID', 'RefSeq_ID', 'Symbol', 'Definition']]
gene_lookup_table.to_csv('gene_lookup.csv')

# Make dataframe of expression values for each sample
df = gse.pivot_samples('VALUE')
df = df.transpose()
df.reset_index(inplace=True) # numeric index

# Append disease status to each sample
# 1 = celiac, 0 = control
def subset(row):
    sample = row['name']
    if sample in healthy_controls:
        return 0
    return 1

df['CELIAC'] = df.apply(subset, axis=1)

# remove rows with null values
df.dropna(inplace=True)

# Convert sample ID and disease status to categorical
df['name'] = pd.Categorical(df['name'])
df['name'] = df.name.cat.codes
df['CELIAC'] = pd.Categorical(df['CELIAC'])
df['CELIAC'] = df.CELIAC.cat.codes

df.to_csv('all_samples.csv')
