from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'PythiaHydjet2018_Dijet_Spring21MiniAOD_FixL1CaloGT_112X_2023-01-30'
config.General.workArea = config.General.requestName

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'forest_miniAOD_run2_MC.py'
config.JobType.maxMemoryMB = 3500
config.JobType.maxJobRuntimeMin = 1000
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.userInputFiles = open("allPbPbMCFiles.txt").readlines()
config.Data.totalUnits = len(config.Data.userInputFiles)
#config.Data.inputDataset = '/DiJet_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/HINPbPbSpring21MiniAOD-FixL1CaloGT_112X_upgrade2018_realistic_HI_v9-v1/MINIAODSIM'
#config.Data.partialDataset = True
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False

config.Data.outLFNDirBase = '/store/user/jviinika/'+config.General.requestName

config.section_("Site")
config.Site.whitelist = ['T2_US_*']
config.Site.storageSite = 'T2_US_Vanderbilt'
