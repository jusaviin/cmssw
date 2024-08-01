### HiForest Configuration
# Input: miniAOD
# Type: mc

import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run2_2018_pp_on_AA_cff import Run2_2018_pp_on_AA
from Configuration.ProcessModifiers.run2_miniAOD_pp_on_AA_103X_cff import run2_miniAOD_pp_on_AA_103X
process = cms.Process('HiForest', Run2_2018_pp_on_AA,run2_miniAOD_pp_on_AA_103X)

###############################################################################

# HiForest info
process.load("HeavyIonsAnalysis.EventAnalysis.HiForestInfo_cfi")
process.HiForestInfo.info = cms.vstring("HiForest, miniAOD, 132X, mc")

###############################################################################

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
        '/store/himc/HINPbPbSpring21MiniAOD/DiJet_pThat-15_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8/MINIAODSIM/FixL1CaloGT_New_Release_112X_upgrade2018_realistic_HI_v9-v1/2520000/00147e49-765a-424c-a7e0-29860f11847d.root'
    ),
)

# number of events to process, set to -1 to process all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
    )

###############################################################################

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic_hi', '')
process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("BTagTrackProbability3DRcd"),
             tag = cms.string("JPcalib_MC103X_2018PbPb_v4"),
             connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
         )
])


###############################################################################

# root output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HiForestMiniAOD.root"))

# # edm output for debugging purposes
# process.output = cms.OutputModule(
#     "PoolOutputModule",
#     fileName = cms.untracked.string('HiForestEDM.root'),
#     outputCommands = cms.untracked.vstring(
#         'keep *',
#         )
#     )

# process.output_path = cms.EndPath(process.output)

###############################################################################

#############################
# Gen Analyzer
#############################
process.load('HeavyIonsAnalysis.EventAnalysis.HiGenAnalyzer_cfi')
# making cuts looser so that we can actually check dNdEta
process.HiGenParticleAna.ptMin = cms.untracked.double(0.7) # default is 5
process.HiGenParticleAna.etaMax = cms.untracked.double(2.6) # default is 2.5

# event analysis
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_mc_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.l1object_cfi')

from HeavyIonsAnalysis.EventAnalysis.hltobject_cfi import trigger_list_mc
process.hltobject.triggerNames = trigger_list_mc

# process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
################################
# electrons, photons, muons
SS2018PbPbMC = "HeavyIonsAnalysis/EGMAnalysis/data/SS2018PbPbMC.dat"
process.load('HeavyIonsAnalysis.EGMAnalysis.correctedElectronProducer_cfi')
process.correctedElectrons.correctionFile = SS2018PbPbMC

process.load('HeavyIonsAnalysis.EGMAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.doGenParticles = cms.bool(True)
process.ggHiNtuplizer.doMuons = cms.bool(False)
process.ggHiNtuplizer.electronSrc = "correctedElectrons"
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
################################
# jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.akCs4PFJetSequence_pponPbPb_mc_cff')
################################
# tracks
process.load("HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzers_cff")
#muons
#process.load("HeavyIonsAnalysis.MuonAnalysis.unpackedMuons_cfi")
#process.load("HeavyIonsAnalysis.MuonAnalysis.muonAnalyzer_cfi")
#process.muonAnalyzer.doGen = cms.bool(True)

###############################################################################



###############################################################################
# main forest sequence
process.forest = cms.Path(
    process.HiForestInfo +
    #process.hltanalysis +
    #process.hltobject +
    #process.l1object +
    #process.trackSequencePbPb +
    #process.particleFlowAnalyser +
    process.hiEvtAnalyzer +
    process.HiGenParticleAna #+
    #process.correctedElectrons +
    #process.ggHiNtuplizer #+
    #process.unpackedMuons +
    #process.muonAnalyzer
    )

#customisation

addR3Jets = False
addR3FlowJets = False
addR4Jets = True
addR4FlowJets = True
matchJets = True               # Enables q/g and heavy flavor jet identification
addCandidateTagging = False
doHIJetID = True               # Fill jet ID and composition information branches
doWTARecluster = True          # Add jet phi and eta for WTA axis

if addR3Jets or addR3FlowJets or addR4Jets or addR4FlowJets :
    process.load("HeavyIonsAnalysis.JetAnalysis.extraJets_cff")
    from HeavyIonsAnalysis.JetAnalysis.clusterJetsFromMiniAOD_cff import setupHeavyIonJets
    process.load("HeavyIonsAnalysis.JetAnalysis.candidateBtaggingMiniAOD_cff")

    if addR3Jets :
        process.jetsR3 = cms.Sequence()
        jetName = 'akCs3PF'
        setupHeavyIonJets(jetName, process.jetsR3, process, isMC = 1, radius = 0.30, JECTag = 'AK3PF', doFlow = False, matchJets = matchJets)
        process.akCs3PFpatJetCorrFactors.levels = ['L2Relative', 'L3Absolute']
        process.akCs3PFJetAnalyzer = process.akCs4PFJetAnalyzer.clone(jetTag = jetName + "patJets", jetName = jetName, genjetTag = "ak3GenJetsNoNu", matchJets = matchJets, matchTag = "ak3PFMatchingFor" + jetName + "patJets", doHiJetID = doHIJetID, doWTARecluster = doWTARecluster)      
        process.forest += process.extraJetsMC * process.jetsR3 * process.akCs3PFJetAnalyzer

    if addR3FlowJets :
        process.jetsR3flow = cms.Sequence()
        jetName = 'akCs3PFFlow'
        setupHeavyIonJets(jetName, process.jetsR3flow, process, isMC = 1, radius = 0.30, JECTag = 'AK3PF', doFlow = True, matchJets = matchJets)
        process.akCs3PFFlowpatJetCorrFactors.levels = ['L2Relative', 'L3Absolute']
        process.akFlowPuCs3PFJetAnalyzer = process.akCs4PFJetAnalyzer.clone(jetTag = jetName + "patJets", jetName = jetName, genjetTag = "ak3GenJetsNoNu", matchJets = matchJets, matchTag = "ak3PFMatchingFor" + jetName + "patJets", doHiJetID = doHIJetID, doWTARecluster = doWTARecluster)
        process.forest += process.extraFlowJetsMC * process.jetsR3flow * process.akFlowPuCs3PFJetAnalyzer

    if addR4Jets :
        # Recluster using an alias "0" in order not to get mixed up with the default AK4 collections
        process.jetsR4 = cms.Sequence()
        jetName = 'akCs0PF'
        setupHeavyIonJets(jetName, process.jetsR4, process, isMC = 1, radius = 0.40, JECTag = 'AK4PF', doFlow = False, matchJets = matchJets)
        process.akCs0PFpatJetCorrFactors.levels = ['L2Relative', 'L3Absolute']
        process.akCs4PFJetAnalyzer.jetTag = jetName + 'patJets'
        process.akCs4PFJetAnalyzer.jetName = jetName
        process.akCs4PFJetAnalyzer.matchJets = matchJets
        process.akCs4PFJetAnalyzer.matchTag = 'ak4PFMatchingFor' + jetName + 'patJets'
        process.akCs4PFJetAnalyzer.doHiJetID = doHIJetID
        process.akCs4PFJetAnalyzer.doWTARecluster = doWTARecluster
        process.forest += process.extraJetsMC * process.jetsR4 * process.akCs4PFJetAnalyzer

    if addR4FlowJets :
        process.jetsR4flow = cms.Sequence()
        jetName = 'akCs4PFFlow'
        setupHeavyIonJets(jetName, process.jetsR4flow, process, isMC = 1, radius = 0.40, JECTag = 'AK4PF', doFlow = True, matchJets = matchJets)
        process.akCs4PFFlowpatJetCorrFactors.levels = ['L2Relative', 'L3Absolute']
        process.akFlowPuCs4PFJetAnalyzer.jetTag = jetName + 'patJets'
        process.akFlowPuCs4PFJetAnalyzer.jetName = jetName
        process.akFlowPuCs4PFJetAnalyzer.matchJets = matchJets
        process.akFlowPuCs4PFJetAnalyzer.matchTag = 'ak4PFMatchingFor' + jetName + 'patJets'
        process.akFlowPuCs4PFJetAnalyzer.doHiJetID = doHIJetID
        process.akFlowPuCs4PFJetAnalyzer.doWTARecluster = doWTARecluster

        #############################################
        # Configuration for flow modulation details #
        #############################################

        # Event plane calculation for the flow fit
        process.hiFJRhoFlowModulation.doEvtPlane = False # False = Calculate event plane from PF candidates. True = Read event plane from the forest
        process.hiFJRhoFlowModulation.doFreePlaneFit = False # False = Lock the determined event plane parameters before the flow fit. True = Use the determined event plane parameters as an initial parameter value, but allow the fit to redetermine them
        process.hiFJRhoFlowModulation.evtPlaneLevel = 0 # Event plane level parameter in case the event plane is read from the forest

        # Excluding jetty regions from the flow fit
        iterativeFlowModulation = False # Iterative jetty region exclusion for flow modulation

        # If we are doing iterative jetty region exclusion, we must exclude jetty regions
        process.hiFJRhoFlowModulation.doJettyExclusion = False
        if iterativeFlowModulation:
            process.hiFJRhoFlowModulation.doJettyExclusion = True

        process.hiFJRhoFlowModulation.exclusionRadius = 0.4
        process.ak4PFJetsForFlow.jetPtMin = 15
        process.ak4PFJetsForFlow.rParam = 0.4

        # Particle flow candidates to be included in the fit
        process.hiFJRhoFlowModulation.minPfCandidatesPerEvent = 100
        process.hiFJRhoFlowModulation.pfCandidateEtaCut = 2
        process.hiFJRhoFlowModulation.pfCandidateMinPtCut = 0.3
        process.hiFJRhoFlowModulation.pfCandidateMaxPtCut = 3

        # Range of flow components extracted from the fit
        process.hiFJRhoFlowModulation.firstFittedVn = 2
        process.hiFJRhoFlowModulation.lastFittedVn = 3

        # Reliability parameters for the fit to be applied
        process.akCs4PFFlowJets.minFlowChi2Prob = 0.05;
        process.akCs4PFFlowJets.maxFlowChi2Prob = 0.95;

        if iterativeFlowModulation:

            # Flow modulation configuration for the first iteration
            process.hiFJRhoFlowModulationIteration.firstFittedVn = 2  # First flow component included in the fit
            process.hiFJRhoFlowModulationIteration.lastFittedVn = 3  # Last flow component included in the fit

            # Configure CS subtracted jets for jetty region subtraction
            process.akCs4PFJetsForFlow.src = "packedPFCandidates" # Packed candidates as a source for jets for flow subtraction in second iteration
            process.akCs4PFJetsForFlow.jetPtMin = 20 # Minimum jet pT to exclude area around it in second iteration
            process.akCs4PFJetsForFlow.rhoFlowFitParams = cms.InputTag('hiFJRhoFlowModulationIteration', 'rhoFlowFitParams') # Minimum jet pT to exclude area around it in second iteration

            # Configure the second iteration of the flow modulation to use CS subtracted jets as the jet collection
            process.hiFJRhoFlowModulation.jetTag = "akCs4PFJetsForFlow"

            # Updated process for iterative jetty region determination for flow modulation
            process.forest += process.extraIterativeFlowJetsMC * process.jetsR4flow * process.akFlowPuCs4PFJetAnalyzer 
        else:
            process.forest += process.extraFlowJetsMC * process.jetsR4flow * process.akFlowPuCs4PFJetAnalyzer


if addCandidateTagging:
    process.load("HeavyIonsAnalysis.JetAnalysis.candidateBtaggingMiniAOD_cff")

    from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
    updateJetCollection(
        process,
        jetSource = cms.InputTag('slimmedJets'),
        jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
        btagDiscriminators = ['pfCombinedSecondaryVertexV2BJetTags', 'pfDeepCSVDiscriminatorsJetTags:BvsAll', 'pfDeepCSVDiscriminatorsJetTags:CvsB', 'pfDeepCSVDiscriminatorsJetTags:CvsL'], ## to add discriminators,
        btagPrefix = 'TEST',
    )

    process.updatedPatJets.addJetCorrFactors = False
    process.updatedPatJets.discriminatorSources = cms.VInputTag(
        cms.InputTag('pfDeepCSVJetTags:probb'),
        cms.InputTag('pfDeepCSVJetTags:probc'),
        cms.InputTag('pfDeepCSVJetTags:probudsg'),
        cms.InputTag('pfDeepCSVJetTags:probbb'),
    )

    process.akCs4PFJetAnalyzer.jetTag = "updatedPatJets"

    process.forest.insert(1,process.candidateBtagging*process.updatedPatJets)


#########################
# Event Selection -> add the needed filters here
#########################

process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter)
process.load('HeavyIonsAnalysis.EventAnalysis.hffilter_cfi')
process.pphfCoincFilter2Th4 = cms.Path(process.phfCoincFilter2Th4)
process.pAna = cms.EndPath(process.skimanalysis)
