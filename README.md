# Exploring Multilingual Tokenization Strategies for Low-resource Languages (part of a139 tokenization initiative)

**Research Question:** How does tokenizer design impact downstream language modeling performance on low-resource target languages? Specifically, can language-specific tokenizations (shared vocabulary but language-conditional segmentation) enable better sample efficiency, thus helping to close the gap on performance between low- and high- resource languages

**Hypothesis:** Conditional tokenization (shared vocab) yields lower BPB (bits per byte. i.e., normalized perplexity) than a global tokenizer on low-resource target languages. When language-specific tokenization is unavailable for a low resource family, per-script/per-family conditioning may still outperform global tokenization due to partial structural transfer.

**Axes to vary:**
- Tokenizer variants
    - Global tokenizer (e.g., standard BPE or unigramlm)
    - Shared-vocab conditional: per-script (using global tokenizer as base tokenizer)
    - Shared-vocab conditional: per-family (using global tokenizer as base tokenizer)
    - Shared-vocab conditional: per-language (using global tokenizer as base tokenizer)
- Global/base tokenizer exposure to target (low-resource) language
    - 0%
    - Approximately proportional to presence in LM training dataset

**Hold constant for now**
- Model exposure to low resource language during pretraining, i.e., hold pretraining corpus and schedule constant

**Outcomes to measure**
    - BPB vs training step on target-language eval set
    - Final BPB + AUC + early-checkpoint BPB
