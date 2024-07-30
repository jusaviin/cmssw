import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.producersHeavyIons.heavyIonJets_cff import PackedPFTowers, hiPuRho, hiSignalGenParticles, allPartons, hiFJRhoFlowModulation, ak4PFJetsForFlow
from RecoHI.HiJetAlgos.HiRecoPFJets_cff import hiFJRhoFlowModulationIteration, akCs4PFJetsForFlow
hiSignalGenParticles.src = "prunedGenParticles"
hiPuRho.src = 'PackedPFTowers'

# Configuration for flow subtracted jets
ak4PFJetsForFlow.src = "PackedPFTowers" # Use packed towers as a source if jetty areas are excluded in flow estimate
hiFJRhoFlowModulation.jetTag = "ak4PFJetsForFlow"  # Jet collection used for jetty region exclusion
akCs4PFJetsForFlow.src = "packedPFCandidates"
hiFJRhoFlowModulationIteration.jetTag = "ak4PFJetsForFlow"


# Create extra jet sequences
extraJetsData = cms.Sequence(PackedPFTowers + hiPuRho)
extraFlowJetsData = cms.Sequence(PackedPFTowers + hiPuRho + ak4PFJetsForFlow + hiFJRhoFlowModulation)
extraPpJetsMC = cms.Sequence(hiSignalGenParticles + allPartons)
extraJetsMC = cms.Sequence(PackedPFTowers + hiPuRho + hiSignalGenParticles + allPartons)
extraFlowJetsMC = cms.Sequence(PackedPFTowers + hiPuRho + hiSignalGenParticles + allPartons + ak4PFJetsForFlow + hiFJRhoFlowModulation)
extraIterativeFlowJetsMC = cms.Sequence(PackedPFTowers + hiPuRho + hiSignalGenParticles + allPartons + ak4PFJetsForFlow + hiFJRhoFlowModulationIteration + akCs4PFJetsForFlow + hiFJRhoFlowModulation)
