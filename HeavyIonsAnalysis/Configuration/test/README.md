# Jet background subtraction study

## Customization in this repository

On top of the options that are in regular HiForest, this repository adds option to do jetty region exclusion from determining the event-by-event flow background iteratively. In this method, the flow background is first determined using the default parameters in the forest. Then constituent subtracted jets including this flow modulatind are recontructed. This collection is then used to locate jets in the events. Anything within R=0.4 within the jet axis is exluded from the underlying event flow determination in the second iteration. Flow fits are repeated with the jetty regions removed, and this new flow estimate is used to create the final constituent subtracted jet collection with flow modulation.

## Configuration available for determining event-by-event flow

If there is only one iteration, hiFJRhoFlowModulation produces the event-by-event flow modulation. In case there is two iterations, hiFJRhoFlowModulationIteration produces the flow for the first iteration, and hiFJRhoFlowModulation for the second iteration. The available parameters to tune the configuration and performance of these producers are explained below.

Variable | Default value | Explanation
-------- | ------------- | -----------
EvtPlane | "hiEvtPlane" | If event plane angles are read from the forest, this gives a name for the event plane collection
doEvtPlane | false | true = Read event plane angles from the forest. false = Calculate event plane angles from particle flow candidates
doFreePlaneFit | false | true = Treat event plane angle as free parameter in flow fit. false = Fix event plane angle to determined value before flow fit
doJettyExclusion | false | true = Exclude region close to jets from determining event flow. false = Do not exclude any regions from flow fit
evtPlaneLevel | 0 | Event plane level parameter in case reading the event planes from the forest
exclusionRadius | 0.4 | DeltaR region around the jet axes that is excluded from the flow fit, if jetty regions are excluded
firstFittedVn | 2 | First vn component that is included in the flow fit
jetTag | "ak4PFJetsForFlow" | Name of the jet collection that gives the jets used to determine jetty regions
lastFittedVn | 3 | Last vn component that is included in the flow fit
minPfCandidatesPerEvent | 100 | Minimum number of particle flow candidates in the event such that flow fit is attempted. If there are less particle flow candidates than this number, no flow modulation is done
pfCandSource | "packedPFCandidates" | Name of the collection from which particle flow candiadtes are obtained.
pfCandidateEtaCut | 1.0 | Maximum eta value for particle flow candidates which are indluded in the flow fit
pfCandidateMaxPtCut | 3.0 | Maximum pT value for particle flow candidates which are included in the flow fit
pfCandidateMinPtCut | 0.3 | Minimum pT value for particle flow candidates which are included in the flow fit

## Running the code

There are several python configurations in this folder that contain premade configurations for different parameter sets. You can simply modify them according to your needs. When you are ready to test if they work, first ensure you have a grid proxy:

```
voms-proxy-init --voms cms
```

After you have created a proxy, you can test the code with

```
cmsRun forest_miniAOD_run2_MC.py
```

The CRAB configuration is provided in `crab_forest_run2_MC.py` file. You will need to make the necessary configuration changes there, for example setting `config.JobType.psetName` to be the configuration you want to run, and changing `config.Data.outLFNDirBase` to a folder where you can actually write. Once you are done with these, you can send the jobs to CRAB using

```
crab submit -c crab_forest_run2_MC.py
```

For analyzing the created forests, there is a separate code available in https://github.com/jusaviin/jetBackgroundSubtraction
