from WMCore.Configuration import Configuration

day = "20042019"
version = "v1"

config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'Step2Sexaq_'+day+'_'+version 

config.section_('JobType') 
config.JobType.pluginName = 'Analysis' 
config.JobType.psetName = 'SUS-RunIISummer16DR80Premix-00068_IIDD_cfg.py' 

config.section_('Data') 
config.Data.unitsPerJob = 1 
config.Data.totalUnits = 6997 
config.Data.publication = False 
config.Data.splitting = 'FileBased' 
config.Data.outLFNDirBase = '/store/user/jdeclerc/crmc_Sexaq/Step2' 
config.Data.userInputFiles = open('/user/jdeclerc/CMSSW_8_0_30/src/STEP2_Sexaq/crab/inputFiles.txt').readlines() 
config.Data.outputPrimaryDataset = "CRAB_SimSexaq_7000Step2InputFiles"

config.section_('User') 
config.User.voGroup = 'becms'

config.section_('Site') 
config.Site.whitelist = ['T2_BE_IIHE'] 
config.Site.storageSite = 'T2_BE_IIHE'
