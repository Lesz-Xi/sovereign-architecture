# HIV Entropic Vise

**A Physics-Based Framework for HIV-1 Eradication**

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LaTeX](https://img.shields.io/badge/Preprint-Zenodo-blue.svg)](proposals/arxiv_preprint.tex)

---

## Overview

This repository contains the source code, computational analysis, and research preprint for a physics-based approach to HIV-1 eradication. Unlike traditional biological targeting that fails due to viral mutation, this framework exploits **high-barrier thermodynamic constraints**—regions where mutations impose severe fitness costs on the virus.

### The Core Discovery: The Entropic Vise

**Shannon entropy analysis of 3,552+ HIV-1 envelope sequences reveals a high-barrier region in the gp41 HR1 domain (HXB2 residues 546-556, sequence SGIVQQQNNLL) with near-zero entropy**—indicating strong purifying selection across 40 years of global evolution. While resistance mutations (e.g., V38A, N43D) can emerge under selective pressure (as seen with Enfuvirtide), these mutants exhibit significant fitness costs.

---

## Repository Structure

### 1. The Trap (`/1_the_trap`)
**Objective:** Identify and validate high-barrier thermodynamically constrained regions.
- `core_algorithms/` — Python scripts for Shannon Entropy analysis and Gap Filtering
- `visualization/` — PyMOL scripts for mapping "Dead Zones" to PDB:5FUU
- `Entropic_Vise_Summary.md` — Discovery report on the HR1 "Vise"

### 2. The Oracle (`/2_the_oracle`)
**Objective:** Predict future viral variants before they emerge.
- `models/` — Prototypes for thermodynamically constrained generative models (transitioning to diffusion-based architectures like RFdiffusion)
- `Algorithmic_Immunity_Design.md` — Technical specification for the constrained architecture

### 3. The Watchman (`/3_the_watchman_designs`)
**Objective:** Real-time detection of viral reactivation (Zero-Trust Bio-Forensics).
- `designs/` — Conceptual frameworks for "Sentinel Cells" with humanized reporters (ΔNGFR, Truncated CD19)
- `Zero_Trust_Feasibility.md` — Literature validation of biosensor implants

### 4. Proposals (`/proposals`)
**Objective:** Research Preprint and Theoretical Framework.
- `arxiv_preprint.tex` — Final Preprint (Submitted to Zenodo)
- `main.tex` — Original NIH-style draft (reference only)
- `references.bib` — BibTeX bibliography (17 citations)
- `image.png` — Entropy analysis figure

---

## Quick Start

### Run the TC-GAN Prototype
```bash
python3 2_the_oracle/models/TC_GAN_Prototype.py
```

### Compile the Preprint
Upload `proposals/arxiv_preprint.tex` and `proposals/references.bib` to [Overleaf](https://overleaf.com) and compile with **pdfLaTeX**.

---

## Key Publications & References

The framework builds on foundational work in:
- **Entropy-based targeting:** Wylie & Shakhnovich (2011), Gong et al. (2013)
- **Latent reservoir quantification:** Ho et al. (2013), Siliciano & Siliciano (2022)
- **Aptamer therapeutics:** Shum et al. (2013), Chakraborty et al. (2022)

See [`proposals/references.bib`](proposals/references.bib) for the complete citation list.

---

## Project Status

| Component | Status |
|-----------|--------|
| Entropy Analysis | ✅ Complete |
| Generative Models | 🔄 Transitioning to Diffusion |
| Sentinel Cell Design | 📋 Conceptual (ΔNGFR reporters) |
| Research Preprint v2 | 🚀 Published (Zenodo) |
| External Validation | ✅ Confirmed (Consensus.app + Gemini) |

---

## Author

**Lesz Xi**  
*Physics-Based Targeting • Adversarial Prediction • Zero-Trust Detection*

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
