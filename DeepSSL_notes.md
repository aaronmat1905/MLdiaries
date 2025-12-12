# **Deep Semi Supervised Learning**
## 1. Restricted Boltzmann Machines
Motivation: Before DL took koff, we needed models that could extract features automatically from raw data without labels.
An RBM is a two-layer neural model that learns to represent the *probability distribution* of the input data. 
It has: 
  - Visible Layer: Takes the Input
  - Hidden Layer: Learns the features
  - No connections within a layer (only between layers)
This restriction makes learning easier
**What RBMs Do**
An RBM learns what combinations are the Inputs are likely.
Because it models probability, it can
  - Learn features without labels
  - Reconstruct inputs
  - Generate new samples similar to data
**Data Flow**
1. Input activates hidden units (pattern detectors)
2. Hidden units try to reconstruct input
3. If reconstruction accurate, RBM has learned useful features. 
**Summary**: _An RBM learns hidden patterns in the data by modeling which input configurations are likely_


## 2. Deep Boltzmann Machines 
Motivation: If one RBM learns simple patterns, then stacking many RBMs should learn increasingly abstact patterns. 
This gives rise to hierarchy. 

**DBMs** perform deep reasoning -- layers talk back and forth (iterative inference until they agree on the xplaination of data) 

## **3. Ladder Networks [focus]**
Dataflow Intuition

There are three paths:

Clean encoder: produces ideal activations

Noisy encoder: produces corrupted activations

Decoder: tries to denoise each layer

Learning happens from both:

supervised classification loss,

unsupervised layer-wise denoising loss.

