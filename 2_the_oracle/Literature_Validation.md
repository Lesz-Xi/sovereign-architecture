# Algorithmic Immunity: Literature Review & Gap Analysis
**Date:** January 2, 2026
**Topic:** Adversarial AI for Viral Mutation Prediction

## 1. State of the Art (SOTA)
Current approaches to predicting viral evolution fall into three categories:

### A. Evolutionary Probability (EVE / EVEscape)
*   **Mechanism:** Deep Variational Autoencoders (VAEs) train on historical sequences to learn the distinct "distribution" of functional proteins.
*   **Logic:** "If a mutation has never been seen in 10,000 sequences, it's likely deleterious."
*   **Limitation:** It relies on *past* data. It cannot easily distinguish between "rare but possible" and "physically impossible."

### B. Sequence GANs (MutaGAN, ProteinGAN)
*   **Mechanism:** GANs learn the syntax of amino acid sequences.
*   **Application:** Generating synthetic HIV data to augment small clinical datasets.
*   **Limitation:** These models optimize for "believability" (looking like HIV), not necessarily "viability" (folding correctly). They often generate "hallucinations" that are biologically dead.

## 2. The "Thermodynamic Gap"
While "Physics-Informed Neural Networks" (PINNs) exist for protein folding (AlphaFold), **no current evolutionary model explicitly integrates local thermodynamic constraints as a hard discriminator.**

Existing models treat the "Entropic Vise" (HR1, MPER) essentially as just "highly conserved regions." They do not mechanistically understand *why* they are conserved. Consequently, they may "drift" into allowing mutations there during long-horizon predictions.

## 3. The "Algorithmic Immunity" Proposal
We propose a **Thermodynamically Constrained GAN (TC-GAN)**.

### Architecture
1.  **Generator ($G$):** A Transformer-based model (e.g., GPT-2 architecture) trained on the Los Alamos HIV dataset. It proposes mutation trajectories to escape antibodies.
2.  **Dual Discriminator System:**
    *   **$D_{seq}$ (The Critic):** "Does this sequence look like valid HIV Env?" (Standard/SOTA).
    *   **$D_{vise}$ (The Physicist):** A non-learnable, rule-based filter.
        *   **Input:** Generated Sequence.
        *   **Logic:** Check coordinates 568-576 (HR1) and 678-682 (MPER).
        *   **Constraint:** ANY mutation in these "Dead Zones" results in an immediate **Loss Penalty of $\infty$**.
    
### Value Proposition
By mathematically forbidding the AI from "cheating" (mutating the un-mutable), we force the Generator to discover **High-Risk/High-Reward escape paths** in the variable loops (V1-V5) that standard models might miss.
We essentially "stress test" the virus in silico by locking its ankles (the Vise) and seeing if it can still run.
