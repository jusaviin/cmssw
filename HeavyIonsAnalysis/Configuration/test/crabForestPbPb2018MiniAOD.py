from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'PbPb2018_HardProbes-HIRun2018_MiniAODv1-v1_jet80or100Trigger_2023-01-28'
config.General.workArea = config.General.requestName

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'forest_miniAOD_run2_DATA.py'
config.JobType.maxMemoryMB = 3200
config.JobType.maxJobRuntimeMin = 900
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
#config.Data.userInputFiles = open("sixTestFilesPbPb.txt").readlines()
#config.Data.totalUnits = len(config.Data.userInputFiles)
config.Data.inputDataset = '/HIHardProbes/HIRun2018A-PbPb18_MiniAODv1-v1/MINIAOD'
config.Data.lumiMask = "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt"
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.publication = False

config.Data.outLFNDirBase = '/store/user/jviinika/'+config.General.requestName

config.section_("Site")
config.Site.whitelist = ['T2_US_Vanderbilt']
config.Site.storageSite = 'T2_US_Vanderbilt'
