# Autoencoders (AE)
_Typed by AaronTM_
## Vanila Autoencoders 

**Definition**: 
    Autoencoders are neural networks that learn to compress data into a smaller form, and then reconstruct it, compressing essential patterns in the process. 
**Goal**:
    Minimize _Reconstruction Error_ (Difference between original and reconstructed input)

**Architecture** 
    Comprises of two parts:
        1. **Encoder**
            Compress input data into a **Compact representation** (_Latent Space_).
            $Z = f(w_e \cdot X + b_e)$
        2. **Decoder**
            Reconstruct original space from the compact representation/Latent Space
            $X' = f(w_d \cdot Z + b_d)$ 
        


## Sparse Autoencoders 
## Denoising Autoencoders 
## Variational Autoencoders 