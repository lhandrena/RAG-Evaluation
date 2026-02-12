# Source: https://x.com/_avichawla/status/1977260787027919209
Number of words: 421

# Avi Chawla on X: "Researchers from Meta built a new RAG approach that: - outperforms LLaMA on 16 RAG benchmarks. - has 30.85x faster time-to-first-token. - handles 16x larger context windows. - and it utilizes 2-4x fewer tokens. Here's the core problem with a typical RAG setup that Meta solves: https://t.co/lAdpiFlgJo" / X

Researchers from Meta built a new RAG approach that:

- outperforms LLaMA on 16 RAG benchmarks.
- has 30.85x faster time-to-first-token.
- handles 16x larger context windows.
- and it utilizes 2-4x fewer tokens.

Here's the core problem with a typical RAG setup that Meta solves:

Most of what we retrieve in RAG setups never actually helps the LLM.

In classic RAG, when a query arrives:

- You encode it into a vector.
- Fetch similar chunks from vector DB.
- Dump the retrieved context into the LLM.

It typically works, but at a huge cost:

- Most chunks contain irrelevant text.
- The LLM has to process far more tokens.
- You pay for compute, latency, and context.

That’s the exact problem Meta AI’s new method REFRAG solves.

It fundamentally rethinks retrieval and the diagram below explains how it works.

Essentially, instead of feeding the LLM every chunk and every token, REFRAG compresses and filters context at a vector level:

- Chunk compression: Each chunk is encoded into a single compressed embedding, rather than hundreds of token embeddings.
- Relevance policy: A lightweight RL-trained policy evaluates the compressed embeddings and keeps only the most relevant chunks.
- Selective expansion: Only the chunks chosen by the RL policy are expanded back into their full embeddings and passed to the LLM.

This way, the model processes just what matters and ignores the rest.

Here's the step-by-step walkthrough:

- Step 1-2) Encode the docs and store them in a vector database.
- Step 3-5) Encode the full user query and find relevant chunks. Also, compute the token-level embeddings for both the query (step 7) and matching chunks.
- Step 6) Use a relevance policy (trained via RL) to select chunks to keep.
- Step 8) Concatenate the token-level representations of the input query with the token-level embedding of selected chunks and a compressed single-vector representation of the rejected chunks.
- Step 9-10) Send all that to the LLM.

The RL step makes REFRAG a more relevance-aware RAG pipeline.

Based on the research paper, this approach:

- has 30.85x faster time-to-first-token (3.75x better than previous SOTA)
- provides 16x larger context windows
- outperforms LLaMA on 16 RAG benchmarks while using 2–4x fewer decoder tokens.
- leads to no accuracy loss across RAG, summarization, and multi-turn conversation tasks

That means you can process 16x more context at 30x the speed, with the same accuracy.

The code has not been released yet by Meta. They intend to do that soon.

