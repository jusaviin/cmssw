from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import getUsername

config = Configuration()

inputList = 'fileListHIPhysicsRawPrimePromptReco_run374322.txt'
#jobTag = "PbPb2023_run374354_HIExpressRawPrime_noEmap_2023-09-28"
jobTag = "HIPhysicsRawPrime0_HIRun2023A-PromptReco-v1_run374322_2023-09-29"
username = getUsername()

config.section_("General")
config.General.requestName = jobTag
config.General.workArea = config.General.requestName
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'forest_miniAOD_run3_DATA.py'
config.JobType.maxMemoryMB = 2500
config.JobType.maxJobRuntimeMin = 120
config.JobType.scriptExe = 'submitScript.sh'
config.JobType.inputFiles = ['emap_2023_newZDC_v3.txt']
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.userInputFiles = open(inputList).readlines()
config.Data.totalUnits = len(config.Data.userInputFiles)
#config.Data.inputDataset = '/Alternatively/DefineDataset/InsteadOf/InputFileList'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/phys_heavyions/' + username + '/run3RapidValidation/' + config.General.requestName
config.Data.publication = False

config.section_("Site")
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'
