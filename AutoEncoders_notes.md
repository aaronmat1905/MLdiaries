# Autoencoders (AE)
*Typed by AaronTM*

## Vanilla Autoencoders

**Definition**:
Autoencoders are neural networks that learn to compress data into a smaller form, and then reconstruct it, compressing essential patterns in the process.
**Goal**:
Minimize *Reconstruction Error* (Difference between original and reconstructed input).

**Architecture**
Comprises of two parts:

1.  **Encoder**
    * Compress input data ($X$) into a **Compact representation** (*Latent Space* $Z$).
    * $$Z = f(W_e X + b_e)$$
2.  **Decoder**
    * Reconstruct original space ($\hat{X}$) from the compact representation/Latent Space ($Z$).
    * $$\hat{X} = f(W_d Z + b_d)$$

**A View of Pipeline**
* Input Data ($X$) $\to$ Encoder $\to$ Latent Representation ($Z$) $\to$ Decoder $\to$ Loss

---

### Difference between PCA and Autoencoders

| Feature | PCA (Principal Component Analysis) | Autoencoders (AE) |
| :--- | :--- | :--- |
| **Technique Type** | Linear Technique; PCs are linear combinations of the Original Variable | Non-Linear Technique; Hence can Learn Non-Linear Form of data |
| **Interpretability** | Linear Combinations are interpretable | They are not-interpretable |
| **Learning Type** | Unsupervised learning technique | Self-Supervised Learning Technique |

---

**Limitations of Auto Encoders**
* **No Structure in Latent space**
    * Random Points may not decode meaningfully
* **Overfitting**
    * May Memorize data without learning generalizable features
* **No Noise Robustness**
    * Sensitive to Input perturbations
* **Limited Generative Capacity**
    * Can't easily sample new data

**Cost Function (Reconstruction Loss - e.g., MSE)**
$$
L(\theta , \phi) = \frac{1}{n} \sum_{i=1}^{n} \|X^{(i)} - \hat{X}^{(i)}\|^2
$$
*Where $\hat{X}^{(i)} = f_{\theta}(g_{\phi}(X^{(i)}))$ is the reconstructed output.*

*Advanced AE methods address these limitations*

## Sparse Autoencoders
    - These kinds of Auto Encoders learn **Sparse Representations** of the data, by only activating a _small subset_ of the neurons given time. 
    - Adds a Sparsity constraint so that most hidden neurons remain active for a given input
        - This sparisty constraint, is an **L1 Regularization to the Loss function** 
        - $ L1 = {Reconstruction_Loss} + \lambda \sum |h_i| $
            - Where $\lambda$ controls sparsity and `|h_i|` controls activations 
            - L1 acts like a soft filter encouraging activations to become exactly 0 
            - L2 shirinks Values, L1 creates true 0s 
    - **Architecture**
        - Restrict the flow of information such that network only learns the most critical features. 
        - **Implementation** 
            - Small Hidden Layer Size 
            - Sparisity constraints 
        - This forces the model to prioritize features that are essential for reconstruction. 
        - Encouraging Disentangling
**Benefits** 
    - Better Feature Learning and Interpretability 
    - Prevents Overfitting 
    - Produces More meaningful, disntangled representations 
**Tradeoff** 
    - More compression, strong feature extraction, but higher reconstruction error. 

## Denoising Autoencoders
- Denoising Autoencoders are those that add noise to the input, and train to reconstruct the clean output. 
- **Architecture**: 
    - Input Data ($X$) $\to$ Corrupted Input $\to$ Encoder $\to$ Latent Representation ($Z$) $\to$ Decoder $\to$ Loss
- This creates a more robust model. 
    - Forced meaningful representation 
    - Improved Generalization 
    - Manifold learning 
    - Feature hierarchy 
- Types of noise: 
    - Gaussian Noise  => Add random values from normal distribution 
    - Salt and Pepper  => Randomly set pixels to 0 or 1 
    - Masking => Randomly hide parts of input 
    - Dropout => Randomly set activations to 0 

## Applications of AE
- Dimensionality Reduction 
- Anomaly detection 
- Data Compression 
- Image Denoising

## Variational Autoencoders
[...working]