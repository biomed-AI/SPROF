# SPROF: To Improve Protein Sequence Profile Prediction through Image Captioning on Pairwise Residue Distance Map

## Getting Start
These instructions will get you a copy of the project up and running on your local machine.

### Environment

SPROF has been implemented in `Python3`.

### Requirements
Installing requirements:  
```
pip3 install -r requirements.txt
```

or avoiding problems in multiple Python environments:  

```
python3 -m pip install -r requirements.txt
```
if you want to generate features by 'raw_feature_generate.py', install dssp by 
```
apt-get install dssp
```

## Data Preprocess

This repository has include the CASP13 test set data on 'input/casp_test/', 'target/casp_test/' and raw features on 'raw_features/', raw pdbs on 'raw_pdbs/'.

if you want to generate other data for training/test:

Firstly, install dssp by 'apt-get install dssp' and deposite your pdbs(the examples of pdb in correct format are on 'raw_pdbs/') on 'raw_pdbs/'. 

Secondly you should make a list file namd 'xxx.txt' (for example) which contains all your training/test pdbs' name.

Thirdly use the 'raw_feature_generate.py' to generate raw features:
```
usage: raw_feature_generate.py [-h] [--preprocess_list PREPROCESS_LIST]
--preprocess_list PREPROCESS_LIST
                        The path of your preprocess list.
```
The generated raw-features will be deposit on 'raw_features', use 'preprocess.py' to generate features for model training/test:
```
usage: preprocess.py [-h] [--preprocess_list  PREPROCESS_LIST] 
                [--pdb_path PDB_PATH] [--features_path FEATURES_PATH]
                [--input_path INPUT_PATH] [--target_path TARGET_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --preprocess_list PREPROCESS_LIST
                        he path of a preprocess pdb list.
  --pdb_path PDB_PATH
                        the path of pdb
  --features_path FEATURES_PATH
                        the path of features
  --input_path INPUT_PATH
                        the path of input to save
  --target_path TARGET_PATH
                        the path of target to save
```
The generated input&target data for training/test will be deposit on the input_path and target_path.
## Training

### Command line:  
```
usage: train.py [-h] [--batch_size BATCH_SIZE] [--learning_rate LEARNING_RATE]
                [--maximum_epoch MAXIMUM_EPOCH]
                [--sequential_features SEQUENTIAL_FEATURES]
                [--pairwise_features PAIRWISE_FEATURES]
                [--target_output TARGET_OUTPUT] 
                [--train_list TRAIN_LIST] [--models_name MODELS_NAME]

optional arguments:
  -h, --help            show this help message and exit
  --learning_rate LEARNING_RATE
                        The learning rate of ADAM optimization.
  --maximum_epoch MAXIMUM_EPOCH
                        The maximum epoch of training
  --sequential_features SEQUENTIAL_FEATURES
                        The full path of sequential features of training data.
  --pairwise_features PAIRWISE_FEATURES
                        The full path of pairwise features of training data.
  --target_output TARGET_OUTPUT
                        The full path of the target outputs.
  --train_list TRAIN_LIST
                        The full path of the train list.
  --models_name MODELS_NAME
                        The name of models.
```

### Start Training: 
The input data of training is too large to upload. To get these data, please refer to 'Data Preprocess' and use the 'train_list' as preprocess_list, if any problem, contact chensh88@mail2.sysu.edu.cn.

Example of training:  
* Using default paramters to train:
```
    python3 train.py 
```  

* Using different paramters to train:
```
    python3 train.py --learning_rate=0.0005 --maximum_epoch=40 --sequential_features='input/casp_test/sequential_features' --pairwise_features='input/casp_test/pairwise_features' --target_output='target/casp_test' --train_list='train_list' --models_name='models'
```
Then you can obtain several models and save them in the your models_name directory.

## Testing

### Command line:  
```
usage: test.py [-h] [--sequential_features SEQUENTIAL_FEATURES]
               [--pairwise_features PAIRWISE_FEATURES]
               [--target_output TARGET_OUTPUT] [--feature_list FEATURE_LIST]
               [--models_path MODELS_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --sequential_features SEQUENTIAL_FEATURES
                        The full path of sequential features of test data.
  --pairwise_features PAIRWISE_FEATURES
                        The full path of pairwise features of test data.
  --target_output TARGET_OUTPUT
                        The full path of the target outputs.
  --feature_list FEATURE_LIST
                        The full path of the test list.
  --models_path MODELS_path
                        parent path of your models.
```

### Usage:
The CASP13 test set has been included in the repository, so you can test our model's perpormance easily.
* Using default paramters to test:
``` 
    python3 test.py
```

* Using different paramters test
```
    python3 test.py --sequential_features='input/casp_test/sequential_features' --pairwise_features='input/casp_test/pairwise_features' --target_output='target/casp_test' --train_list='train_list' --models_path='models'
```

## Cite
If you find this work useful in your research, please consider citing the paper:  
**"To Improve Protein Sequence Profile Prediction through Image Captioning on Pairwise Residue Distance Map"**
https://pubs.acs.org/doi/10.1021/acs.jcim.9b00438

## Contact
`yuedong.yang@gmail.com`or `chensh88@mail2.sysu.edu.cn`
