from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'pp2017_HIZeroBias1_Run2017G-09Aug2019_UL2017_LUM-v2_2025-06-16'
config.General.workArea = config.General.requestName

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'forest_miniAOD_run3_ppref_DATA.py'
config.JobType.maxMemoryMB = 2000
config.JobType.maxJobRuntimeMin = 800
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
#config.Data.userInputFiles = open("sixLowEGFiles.txt").readlines()
#config.Data.totalUnits = len(config.Data.userInputFiles)
config.Data.inputDataset = '/LowEGJet/Run2017G-UL2017_MiniAODv2-v2/MINIAOD'
config.Data.lumiMask = "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt"
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False

config.Data.outLFNDirBase = '/store/user/jviinika/'+config.General.requestName

config.section_("Site")
#config.Site.whitelist = ['T2_US_*']
config.Site.storageSite = 'T2_US_Vanderbilt'
