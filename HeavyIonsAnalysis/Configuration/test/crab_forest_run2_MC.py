from WMCore.Configuration import Configuration
config = Configuration()

from datetime import date
today = date.today().strftime('%Y-%m-%d')

config.section_("General")
config.General.requestName = 'Run2MC_Dijet_CP5_HydjetDrumMB_MiniAOD_NewRelease_iterativeFlow_minJetPt60_' + today
config.General.workArea = config.General.requestName

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'forest_miniAOD_run2_MC_iterativeFlow_minJetPt60.py'
config.JobType.maxMemoryMB = 2800
config.JobType.maxJobRuntimeMin = 800
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.userInputFiles = open("vandyFilesForFlowStudy.txt").readlines()
#config.Data.userInputFiles = open("twoTestFiles.txt").readlines()
config.Data.totalUnits = len(config.Data.userInputFiles)
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False

config.Data.outLFNDirBase = '/store/user/jviinika/'+config.General.requestName

config.section_("Site")
config.Site.whitelist = ['T2_US_Vanderbilt']
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T2_US_Vanderbilt'
