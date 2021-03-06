#ifndef FWCore_Framework_one_EDFilter_h
#define FWCore_Framework_one_EDFilter_h
// -*- C++ -*-
//
// Package:     FWCore/Framework
// Class  :     edm::one::EDFilter
// 
/**\class edm::one::EDFilter EDFilter.h "FWCore/Framework/interface/one/EDFilter.h"

 Description: [one line class summary]

 Usage:
    <usage>

*/
//
// Original Author:  Chris Jones
//         Created:  Thu, 09 May 2013 19:53:55 GMT
//

// system include files

// user include files
#include "FWCore/Framework/interface/one/filterAbilityToImplementor.h"

// forward declarations
namespace edm {
  namespace one {
    template< typename... T>
    class EDFilter : public filter::AbilityToImplementor<T>::Type...,
                       public virtual EDFilterBase {
      
    public:
      EDFilter() = default;
      //virtual ~EDFilter();
      
      // ---------- const member functions ---------------------
      bool wantsGlobalRuns() const final {
        return WantsGlobalRunTransitions<T...>::value;
      }
      bool wantsGlobalLuminosityBlocks() const final {
        return WantsGlobalLuminosityBlockTransitions<T...>::value;
      }

      bool hasAbilityToProduceInRuns() const final {
        return HasAbilityToProduceInRuns<T...>::value;
      }

      bool hasAbilityToProduceInLumis() const final {
        return HasAbilityToProduceInLumis<T...>::value;
      }

      // ---------- static member functions --------------------
      
      // ---------- member functions ---------------------------
      SerialTaskQueue* globalRunsQueue() final { return globalRunsQueue_.queue();}
      SerialTaskQueue* globalLuminosityBlocksQueue() final { return globalLuminosityBlocksQueue_.queue();}

    private:
      EDFilter(const EDFilter&) = delete;
      const EDFilter& operator=(const EDFilter&) = delete;
      
      // ---------- member data --------------------------------
      impl::OptionalSerialTaskQueueHolder<WantsGlobalRunTransitions<T...>::value> globalRunsQueue_;
      impl::OptionalSerialTaskQueueHolder<WantsGlobalLuminosityBlockTransitions<T...>::value> globalLuminosityBlocksQueue_;

    };
    
  }
}


#endif
