# README
# Unveiling Crucial Connectomes in Autism through Heterogeneous Graph Networks and Federated Learning #


 **Get.py**

(1) inputs:

"/aal.nii.gz": AAL template file

"/bm20.nii.gz":20-dimensional ICA file,BrainMap components,see [Correspondence between BrainMap and Resting-FMRI ICA components](https://www.fmrib.ox.ac.uk/datasets/brainmap+rsns/)

(2) outputs:

"/BM20_%s.npy": node connections  for different thresholds

---

 **ModelsForGraph.py**

SEHGT model and other baseline graph models(HGT,HAN)

---

**graphclassification.ipynb**

(1) inputs:

"/DataInfo.csv": information file of subjects, inluding <u>SubID,SITE,LABEL,AGE,SEX</u>

"/data/RawFunc": functional connection matrixes for diffrent subjects.

(2) outputs:

"result.json": train parameters, model parameters and classification results.

---

**FedAvg.ipynb**

federated learning trained

(1)inputs:

see inputs of **graphclassification.ipynb**

(2)outputs:

"fedavg.txt":

including  train parameters, model parameters and classification results in each site for different communication rounds.
