# Algorithmic Immunity: Technical Design Document
**System:** Thermodynamically Constrained Generative Adversarial Network (TC-GAN)
**Role:** Predictive modeling of viral escape within physical capability.

## 1. Architectural Philosophy
Standard viral prediction models (EVE, MutaGAN) operate on **Probabilistic Evolution** ("What is likely?").
Our system operates on **First Principles Constraint** ("What is physically allowed?").
We inject the "Entropic Vise" (thermodynamic immutability) as a non-negotiable axiom in the neural network's loss landscape.

## 2. System Architecture

### A. The Generator ($G$)
*   **Architecture:** Transformer-based Decoder (e.g., GPT-2 variant adapted for Protein sequences).
*   **Input:** 
    *   Latent Noise ($z \sim \mathcal{N}(0,1)$)
    *   Conditioning Vector ($c$): Represents the immune pressure (e.g., "Anti-V3-Loop Antibody").
*   **Output:** $S_{gen}$ (A generated amino acid sequence of the HIV-1 Env spike).

### B. The Dual-Discriminator System
Instead of a single critic, we employ two distinct feedback loops:

#### 1. The Semantic Discriminator ($D_{bio}$)
*   **Role:** The "Virologist."
*   **Mechanism:** A standard Deep CNN or Transformer Classifier.
*   **Training:** Trained on real Los Alamos sequences vs. Generated sequences.
*   **Output:** `Realness_Score` (Probability that the sequence is a valid, functional virus).
*   **Goal:** Ensures the output looks like HIV.

#### 2. The Thermodynamic Discriminator ($D_{phys}$)
*   **Role:** The "Physicist" (The Entropic Vise).
*   **Mechanism:** A deterministic, non-learnable filter function.
*   **Logic:**
    1.  Extract residues corresponding to **HR1 (568-576)** and **MPER (678-682)** from $S_{gen}$.
    2.  Calculate **Hamming Distance** ($H$) between $S_{gen}[region]$ and the Immutable Reference (`LTVWGIKQL`).
    3.  If $H > 0$: Return **Heavy Penalty**.
*   **Goal:** Strictly strictly forbids "cheating" (mutating the un-mutable to escape).

## 3. Loss Function ($L$)
The total loss function guides the Generator's learning process:

$$L_{total} = L_{WGAN} + \lambda_{vise} \cdot L_{vise}$$

*   **$L_{WGAN}$:** Wasserstein Loss (Standard GAN loss for stability and sequence quality).
*   **$L_{vise}$:** The Entropic Penalty.
    *   Defined as: $\sum_{region} || S_{gen}^{region} - S_{ref}^{region} ||^2$
    *   **$\lambda_{vise}$:** A hyperparameter set to a massive value (e.g., $10^5$). This acts as an "Infinite Wall," forcing the gradient descent to steer away from mutating these regions instantly.

## 4. Execution Workflow
1.  **Training:** Train TC-GAN on the 8,735 sequences from Phase 1.
2.  **Inference (The Attack Simulation):**
    *   Simulate "high antibody pressure" (via Conditioning Vector).
    *   Generate 1,000,000 potential escape variants.
3.  **Filtering:** Keep only unique, bio-plausible variants.
4.  **Result:** A library of "Future Viruses" that have escaped the antibody *but* still have the "Vise" (HR1) intact.
5.  **Therapeutic Validation:** Verify that our "Proteolytic Nanobomb" (which targets HR1) would still kill 100% of these future predicted strains.

## 5. Summary
We are not just predicting evolution; we are **channeling** it. By blocking the "easy" escape routes (thermodynamically impossible ones), we force the AI to reveal the *actual* dangerous mutations that could emerge in the real world.
