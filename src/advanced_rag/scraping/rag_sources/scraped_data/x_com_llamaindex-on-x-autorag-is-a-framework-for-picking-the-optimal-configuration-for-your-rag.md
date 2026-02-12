# Source: https://x.com/llama_index/status/1878881368186454161
Number of words: 106

# LlamaIndex 🦙 on X: "AutoRAG is a framework for picking the optimal configuration for your RAG pipelines, introduced in this paper. For LlamaIndex users, this is particularly interesting because it systematically evaluates different RAG techniques and components that you might be using or https://t.co/LTnuAoLK8E" / X

AutoRAG is a framework for picking the optimal configuration for your RAG pipelines, introduced in this paper.

For LlamaIndex users, this is particularly interesting because it systematically evaluates different RAG techniques and components that you might be using or considering in your applications.

Some interesting findings:
➡️ Hybrid retrieval methods (combining BM25 and vector search) often outperformed pure vector or BM25 approaches
➡️ Query expansion wasn't always beneficial - it depends on your use case
➡️ Some rerankers actually performed worse than no reranking - suggesting you should test before implementing
➡️ Simple approaches sometimes outperform more complex ones

The paper covers evaluation techniques and includes the data sets they used.

