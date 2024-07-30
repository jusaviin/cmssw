# How to use this code

## Setting up the CMSSW anf HiForest areas

Start by getting the relevant CMSSW version:

```
cmsrel CMSSW_13_2_4
cd CMSSW_13_2_4/src
cmsenv
```

Load the HiForest version compatible with this CMSSW version

```
git cms-merge-topic CmsHI:forest_CMSSW_13_2_X
scram build -j8
```

## Getting my code on top of the HiForest code

When you are in the branch, checkout my code

```
git remote add flowPatch git@github.com:jusaviin/cmssw.git
git fetch flowPatch flowSubtractionUpdate --no-tags
git checkout -b flowSubtractionUpdate remotes/flowPatch/flowSubtractionUpdate
```

Recompile to make sure everything is ok

```
scram build -j8
```

## Running the code

You can run the code from the following directory:

```
cd HeavyIonsAnalysis/Configuration/test
```

More instructions on what can be configured can be found from this directory
