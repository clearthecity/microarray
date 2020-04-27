# microarray

COMP 4980, Winter 2020

These notebooks document a series of experiments in applying machine learning models to microarray data. Specifically, I attempted to predict disease state based on the expression levels of 18,981 genes from 132 human subjects (110 with celiac disease and 22 healthy controls). The gene expression series can be found at https://www.ncbi.nlm.nih.gov/sites/GDSbrowser?acc=GDS3646. I summarize the results in **GeneExpressionReport.pdf**.


## Utilities

  + **GSE_Parser**: Reads a SOFT file and extracts useful information (expression levels, the gene that corresponds to each microarray probe) to CSV files for later use. Uses [GeoParse](https://github.com/guma44/geoparse).

## Trained models

  + **GeneExpression**: Compares the performance of various SciKit Learn models and parameters
  + **GeneExpression_Trees**: Compares the performance of two decision tree algorithms and visualizes the best-performing tree, correlating probes with genes
  + **SVC-RecursiveFeatureElimination**: Comparing the efficacy of SelectPercentile and RFECV for dimensionality reduction

## Unsuccessful

  + *KerasClassifier*: Did not perform (curse of dimensionality: CPU timeout)
  + *KerasClassifer-DimRed* Keras classifier with dimensionality reduction: Uses top 10% of features. Unable to train beyond AUC 0.5 (i.e., random guessing).
