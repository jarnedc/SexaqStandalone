from WMCore.Configuration import Configuration

day = "25052019"
version = "v2"

config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'SkimmingSexaq_'+day+'_'+version 

config.section_('JobType') 
config.JobType.pluginName = 'Analysis' 
config.JobType.psetName = 'treeproducer_data_cfg.py' 

config.section_('Data') 
config.Data.unitsPerJob = 35
config.Data.totalUnits = 7000
config.Data.publication = False 
config.Data.splitting = 'FileBased' 
config.Data.outLFNDirBase = '/store/user/jdeclerc/crmc_Sexaq/Skimmed' 
config.Data.userInputFiles = open('/user/jdeclerc/CMSSW_8_0_30/src/SexaQAnalysis/RunManySkimming/crab/inputFiles.txt').readlines() 
config.Data.outputPrimaryDataset = "CRAB_SimSexaq_Skimmed_completely_disabled_cosThetaXYCut_innerHitPosCut_"+day+"_"+version

config.section_('User') 
config.User.voGroup = 'becms'

config.section_('Site') 
config.Site.whitelist = ['T2_BE_IIHE'] 
config.Site.storageSite = 'T2_BE_IIHE'
