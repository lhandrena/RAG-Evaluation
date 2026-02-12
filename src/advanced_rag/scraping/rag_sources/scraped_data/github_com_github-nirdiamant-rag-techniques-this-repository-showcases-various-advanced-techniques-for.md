# Source: https://github.com/NirDiamant/RAG_Techniques
Number of words: 2793

# GitHub - NirDiamant/RAG_Techniques: This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. RAG systems combine information retrieval with generative models to provide accurate and contextually rich responses.

This repository showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems. RAG systems combine information retrieval with generative models to provide accurate and contextually rich responses. 


Advanced RAG Techniques: Elevating Your Retrieval-Augmented Generation Systems 🚀

Welcome to one of the most comprehensive and dynamic collections of Retrieval-Augmented Generation (RAG) tutorials available today. This repository serves as a hub for cutting-edge techniques aimed at enhancing the accuracy, efficiency, and contextual richness of RAG systems.
📫 Stay Updated!
🚀
Cutting-edge
Updates 	💡
Expert
Insights 	🎯
Top 0.1%
Content

Subscribe to DiamantAI Newsletter

Join over 50,000 AI enthusiasts getting unique cutting-edge insights and free tutorials! Plus, subscribers get exclusive early access and special 33% discounts to my book and the upcoming RAG Techniques course!

DiamantAI's newsletter
Introduction

Retrieval-Augmented Generation (RAG) is revolutionizing the way we combine information retrieval with generative AI. This repository showcases a curated collection of advanced techniques designed to supercharge your RAG systems, enabling them to deliver more accurate, contextually relevant, and comprehensive responses.

Our goal is to provide a valuable resource for researchers and practitioners looking to push the boundaries of what's possible with RAG. By fostering a collaborative environment, we aim to accelerate innovation in this exciting field.
Related Projects

🚀 Level up with my Agents Towards Production repository. It delivers horizontal, code-first tutorials that cover every tool and step in the lifecycle of building production-grade GenAI agents, guiding you from spark to scale with proven patterns and reusable blueprints for real-world launches, making it the smartest place to start if you're serious about shipping agents to production.

🤖 Explore my GenAI Agents Repository to discover a variety of AI agent implementations and tutorials, showcasing how different AI technologies can be combined to create powerful, interactive systems.

🖋️ Check out my Prompt Engineering Techniques guide for a comprehensive collection of prompting strategies, from basic concepts to advanced techniques, enhancing your ability to interact effectively with AI language models.
A Community-Driven Knowledge Hub

This repository grows stronger with your contributions! Join our vibrant communities - the central hubs for shaping and advancing this project together 🤝

Educational AI Subreddit

RAG Techniques Discord Community

Whether you're an expert or just starting out, your insights can shape the future of RAG. Join us to propose ideas, get feedback, and collaborate on innovative techniques. For contribution guidelines, please refer to our CONTRIBUTING.md file. Let's advance RAG technology together!

🔗 For discussions on GenAI, RAG, or custom agents, or to explore knowledge-sharing opportunities, feel free to connect on LinkedIn.
Key Features

    🧠 State-of-the-art RAG enhancements
    📚 Comprehensive documentation for each technique
    🛠️ Practical implementation guidelines
    🌟 Regular updates with the latest advancements

Advanced Techniques

Explore our extensive list of cutting-edge RAG techniques:
# 	Category 	Technique 	View
1 	⭐ Key Collaboration 	Agentic RAG with Contextual AI 	
2 	Foundational 🌱 	Basic RAG 	
3 	Foundational 🌱 	RAG with CSV Files 	
4 	Foundational 🌱 	Reliable RAG 	
5 	Foundational 🌱 	Optimizing Chunk Sizes 	
6 	Foundational 🌱 	Proposition Chunking 	
7 	Query Enhancement 🔍 	Query Transformations 	
8 	Query Enhancement 🔍 	HyDE (Hypothetical Document Embedding) 	
9 	Query Enhancement 🔍 	HyPE (Hypothetical Prompt Embedding) 	
10 	Context Enrichment 📚 	Contextual Chunk Headers 	
11 	Context Enrichment 📚 	Relevant Segment Extraction 	
12 	Context Enrichment 📚 	Context Window Enhancement 	
13 	Context Enrichment 📚 	Semantic Chunking 	
14 	Context Enrichment 📚 	Contextual Compression 	
15 	Context Enrichment 📚 	Document Augmentation 	
16 	Advanced Retrieval 🚀 	Fusion Retrieval 	
17 	Advanced Retrieval 🚀 	Reranking 	
18 	Advanced Retrieval 🚀 	Multi-faceted Filtering 	
19 	Advanced Retrieval 🚀 	Hierarchical Indices 	
20 	Advanced Retrieval 🚀 	Ensemble Retrieval 	
21 	Advanced Retrieval 🚀 	Dartboard Retrieval 	
22 	Advanced Retrieval 🚀 	Multi-modal RAG with Captioning 	
23 	Iterative Techniques 🔁 	Retrieval with Feedback Loop 	
24 	Iterative Techniques 🔁 	Adaptive Retrieval 	
25 	Iterative Retrieval 🔄 	Iterative Retrieval 	
26 	Evaluation 📊 	DeepEval 	
27 	Evaluation 📊 	GroUSE 	
28 	Explainability 🔬 	Explainable Retrieval 	
29 	Advanced Architecture 🏗️ 	Graph RAG with LangChain 	
30 	Advanced Architecture 🏗️ 	Microsoft GraphRAG 	
31 	Advanced Architecture 🏗️ 	RAPTOR 	
32 	Advanced Architecture 🏗️ 	Self-RAG 	
33 	Advanced Architecture 🏗️ 	Corrective RAG (CRAG) 	
34 	Special Technique 🌟 	Sophisticated Controllable Agent 	
🌱 Foundational RAG Techniques

    Simple RAG 🌱
        LangChain:
        LlamaIndex:
        Runnable Script
    Overview 🔎

    Introducing basic RAG techniques ideal for newcomers.
    Implementation 🛠️

    Start with basic retrieval queries and integrate incremental learning mechanisms.

    Simple RAG using a CSV file 🧩
        LangChain:
        LlamaIndex:
    Overview 🔎

    Introducing basic RAG using CSV files.
    Implementation 🛠️

    This uses CSV files to create basic retrieval and integrates with openai to create question and answering system.

    Reliable RAG 🏷️:
    Overview 🔎

    Enhances the Simple RAG by adding validation and refinement to ensure the accuracy and relevance of retrieved information.
    Implementation 🛠️

    Check for retrieved document relevancy and highlight the segment of docs used for answering.

    Choose Chunk Size 📏
        LangChain:
        Runnable Script
    Overview 🔎

    Selecting an appropriate fixed size for text chunks to balance context preservation and retrieval efficiency.
    Implementation 🛠️

    Experiment with different chunk sizes to find the optimal balance between preserving context and maintaining retrieval speed for your specific use case.

    Proposition Chunking ⛓️‍💥:
    Overview 🔎

    Breaking down the text into concise, complete, meaningful sentences allowing for better control and handling of specific queries (especially extracting knowledge).
    Implementation 🛠️
        💪 Proposition Generation: The LLM is used in conjunction with a custom prompt to generate factual statements from the document chunks.
        ✅ Quality Checking: The generated propositions are passed through a grading system that evaluates accuracy, clarity, completeness, and conciseness.

Additional Resources 📚

    The Propositions Method: Enhancing Information Retrieval for AI Systems - A comprehensive blog post exploring the benefits and implementation of proposition chunking in RAG systems.

🔍 Query Enhancement

    Query Transformations 🔄
        LangChain:
        Runnable Script
    Overview 🔎

    Modifying and expanding queries to improve retrieval effectiveness.
    Implementation 🛠️
        ✍️ Query Rewriting: Reformulate queries to improve retrieval.
        🔙 Step-back Prompting: Generate broader queries for better context retrieval.
        🧩 Sub-query Decomposition: Break complex queries into simpler sub-queries.

    Hypothetical Questions (HyDE Approach) ❓
        LangChain:
        Runnable Script
    Overview 🔎

    Generating hypothetical questions to improve alignment between queries and data.
    Implementation 🛠️

    Create hypothetical questions that point to relevant locations in the data, enhancing query-data matching.
    Additional Resources 📚
        HyDE: Exploring Hypothetical Document Embeddings for AI Retrieval - A short blog post explaining this method clearly.

📚 Context and Content Enrichment

    Hypothetical Prompt Embeddings (HyPE) ❓🚀
        LangChain:
        Runnable Script
    Overview 🔎

    HyPE (Hypothetical Prompt Embeddings) is an enhancement to traditional RAG retrieval that precomputes hypothetical prompts at the indexing stage, but inseting the chunk in their place. This transforms retrieval into a question-question matching task. This avoids the need for runtime synthetic answer generation, reducing inference-time computational overhead while improving retrieval alignment.
    Implementation 🛠️
        📖 Precomputed Questions: Instead of embedding document chunks, HyPE generates multiple hypothetical queries per chunk at indexing time.
        🔍 Question-Question Matching: User queries are matched against stored hypothetical questions, leading to better retrieval alignment.
        ⚡ No Runtime Overhead: Unlike HyDE, HyPE does not require LLM calls at query time, making retrieval faster and cheaper.
        📈 Higher Precision & Recall: Improves retrieval context precision by up to 42 percentage points and claim recall by up to 45 percentage points.
    Additional Resources 📚
        Preprint: Hypothetical Prompt Embeddings (HyPE) - Research paper detailing the method, evaluation, and benchmarks.

    Contextual Chunk Headers 🏷️:
    Overview 🔎

    Contextual chunk headers (CCH) is a method of creating document-level and section-level context, and prepending those chunk headers to the chunks prior to embedding them.
    Implementation 🛠️

    Create a chunk header that includes context about the document and/or section of the document, and prepend that to each chunk in order to improve the retrieval accuracy.
    Additional Resources 📚

    dsRAG: open-source retrieval engine that implements this technique (and a few other advanced RAG techniques)

    Relevant Segment Extraction 🧩:
    Overview 🔎

    Relevant segment extraction (RSE) is a method of dynamically constructing multi-chunk segments of text that are relevant to a given query.
    Implementation 🛠️

    Perform a retrieval post-processing step that analyzes the most relevant chunks and identifies longer multi-chunk segments to provide more complete context to the LLM.

    Context Enrichment Techniques 📝

    LangChain:
    LlamaIndex:
    Runnable Script

Overview 🔎

Enhancing retrieval accuracy by embedding individual sentences and extending context to neighboring sentences.
Implementation 🛠️

Retrieve the most relevant sentence while also accessing the sentences before and after it in the original text.

    Semantic Chunking 🧠

    LangChain:
    Runnable Script

Overview 🔎

Dividing documents based on semantic coherence rather than fixed sizes.
Implementation 🛠️

Use NLP techniques to identify topic boundaries or coherent sections within documents for more meaningful retrieval units.
Additional Resources 📚

    Semantic Chunking: Improving AI Information Retrieval - A comprehensive blog post exploring the benefits and implementation of semantic chunking in RAG systems.

    Contextual Compression 🗜️

    LangChain:
    Runnable Script

Overview 🔎

Compressing retrieved information while preserving query-relevant content.
Implementation 🛠️

Use an LLM to compress or summarize retrieved chunks, preserving key information relevant to the query.

    Document Augmentation through Question Generation for Enhanced Retrieval

    LangChain:
    Runnable Script

Overview 🔎

This implementation demonstrates a text augmentation technique that leverages additional question generation to improve document retrieval within a vector database. By generating and incorporating various questions related to each text fragment, the system enhances the standard retrieval process, thus increasing the likelihood of finding relevant documents that can be utilized as context for generative question answering.
Implementation 🛠️

Use an LLM to augment text dataset with all possible questions that can be asked to each document.
🚀 Advanced Retrieval Methods

    Fusion Retrieval 🔗
        LangChain:
        LlamaIndex:
        Runnable Script
    Overview 🔎

    Optimizing search results by combining different retrieval methods.
    Implementation 🛠️

    Combine keyword-based search with vector-based search for more comprehensive and accurate retrieval.

    Intelligent Reranking 📈
        LangChain:
        LlamaIndex:
        Runnable Script
    Overview 🔎

    Applying advanced scoring mechanisms to improve the relevance ranking of retrieved results.
    Implementation 🛠️
        🧠 LLM-based Scoring: Use a language model to score the relevance of each retrieved chunk.
        🔀 Cross-Encoder Models: Re-encode both the query and retrieved documents jointly for similarity scoring.
        🏆 Metadata-enhanced Ranking: Incorporate metadata into the scoring process for more nuanced ranking.
    Additional Resources 📚
        Relevance Revolution: How Re-ranking Transforms RAG Systems - A comprehensive blog post exploring the power of re-ranking in enhancing RAG system performance.

    Multi-faceted Filtering 🔍
    Overview 🔎

    Applying various filtering techniques to refine and improve the quality of retrieved results.
    Implementation 🛠️
        🏷️ Metadata Filtering: Apply filters based on attributes like date, source, author, or document type.
        📊 Similarity Thresholds: Set thresholds for relevance scores to keep only the most pertinent results.
        📄 Content Filtering: Remove results that don't match specific content criteria or essential keywords.
        🌈 Diversity Filtering: Ensure result diversity by filtering out near-duplicate entries.

    Hierarchical Indices 🗂️
        LangChain:
        Runnable Script
    Overview 🔎

    Creating a multi-tiered system for efficient information navigation and retrieval.
    Implementation 🛠️

    Implement a two-tiered system for document summaries and detailed chunks, both containing metadata pointing to the same location in the data.
    Additional Resources 📚
        Hierarchical Indices: Enhancing RAG Systems - A comprehensive blog post exploring the power of hierarchical indices in enhancing RAG system performance.

    Ensemble Retrieval 🎭
    Overview 🔎

    Combining multiple retrieval models or techniques for more robust and accurate results.
    Implementation 🛠️

    Apply different embedding models or retrieval algorithms and use voting or weighting mechanisms to determine the final set of retrieved documents.

    Dartboard Retrieval 🎯
        LangChain:
    Overview 🔎

    Optimizing over Relevant Information Gain in Retrieval
    Implementation 🛠️
        Combine both relevance and diversity into a single scoring function and directly optimize for it.
        POC showing plain simple RAG underperforming when the database is dense, and the dartboard retrieval outperforming it.

    Multi-modal Retrieval 📽️
    Overview 🔎

    Extending RAG capabilities to handle diverse data types for richer responses.
    Implementation 🛠️
        Multi-model RAG with Multimedia Captioning: - Caption and store all the other multimedia data like pdfs, ppts, etc., with text data in vector store and retrieve them together.
        Multi-model RAG with Colpali: - Instead of captioning convert all the data into image, then find the most relevant images and pass them to a vision large language model.

🔁 Iterative and Adaptive Techniques

    Retrieval with Feedback Loops 🔁
        LangChain:
        Runnable Script
    Overview 🔎

    Implementing mechanisms to learn from user interactions and improve future retrievals.
    Implementation 🛠️

    Collect and utilize user feedback on the relevance and quality of retrieved documents and generated responses to fine-tune retrieval and ranking models.

    Adaptive Retrieval 🎯
        LangChain:
        Runnable Script
    Overview 🔎

    Dynamically adjusting retrieval strategies based on query types and user contexts.
    Implementation 🛠️

    Classify queries into different categories and use tailored retrieval strategies for each, considering user context and preferences.

    Iterative Retrieval 🔄
    Overview 🔎

    Performing multiple rounds of retrieval to refine and enhance result quality.
    Implementation 🛠️

    Use the LLM to analyze initial results and generate follow-up queries to fill in gaps or clarify information.

📊 Evaluation

    DeepEval Evaluation: | Comprehensive RAG system evaluation |
    Overview 🔎

    Performing evaluations Retrieval-Augmented Generation systems, by covering several metrics and creating test cases.
    Implementation 🛠️

    Use the deepeval library to conduct test cases on correctness, faithfulness and contextual relevancy of RAG systems.

    GroUSE Evaluation: | Contextually-grounded LLM evaluation |
    Overview 🔎

    Evaluate the final stage of Retrieval-Augmented Generation using metrics of the GroUSE framework and meta-evaluate your custom LLM judge on GroUSE unit tests.
    Implementation 🛠️

    Use the grouse package to evaluate contextually-grounded LLM generations with GPT-4 on the 6 metrics of the GroUSE framework and use unit tests to evaluate a custom Llama 3.1 405B evaluator.

🔬 Explainability and Transparency

    Explainable Retrieval 🔍
        LangChain:
        Runnable Script
    Overview 🔎

    Providing transparency in the retrieval process to enhance user trust and system refinement.
    Implementation 🛠️

    Explain why certain pieces of information were retrieved and how they relate to the query.

🏗️ Advanced Architectures

    Agentic RAG with Contextual AI 🤖
        Agentic RAG:
    Overview 🔎

    Building production-ready agentic RAG pipelines for financial document analysis with Contextual AI's managed platform. This comprehensive tutorial demonstrates how to leverage agentic RAG to solve complex queries through intelligent query reformulation, document parsing, reranking, and grounded language models.
    Implementation 🛠️
        Document Parser: Enterprise-grade parsing with vision models for complex tables, charts, and multi-page documents
        Instruction-Following Reranker: SOTA reranker with instruction-following capabilities for handling conflicting information
        Grounded Language Model (GLM): World's most grounded LLM specifically engineered to minimize hallucinations for RAG use cases
        LMUnit: Natural language unit testing framework for evaluating and optimizing RAG system performance

    Graph RAG with Milvus Vector Database 🔍
        Graph RAG with Milvus:
    Overview 🔎

    A simple yet powerful approach to implement Graph RAG using Milvus vector databases. This technique significantly improves performance on complex multi-hop questions by combining relationship-based retrieval with vector search and reranking.
    Implementation 🛠️
        Store both text passages and relationship triplets (subject-predicate-object) in separate Milvus collections
        Perform multi-way retrieval by querying both collections
        Use an LLM to rerank retrieved relationships based on their relevance to the query
        Retrieve the final passages based on the most relevant relationships

    Knowledge Graph Integration (Graph RAG) 🕸️
        LangChain:
        Runnable Script
    Overview 🔎

    Incorporating structured data from knowledge graphs to enrich context and improve retrieval.
    Implementation 🛠️

    Retrieve entities and their relationships from a knowledge graph relevant to the query, combining this structured data with unstructured text for more informative responses.

    GraphRag (Microsoft) 🎯
        GraphRag:
    Overview 🔎

    Microsoft GraphRAG (Open Source) is an advanced RAG system that integrates knowledge graphs to improve the performance of LLMs
    Implementation 🛠️

    • Analyze an input corpus by extracting entities, relationships from text units. generates summaries of each community and its constituents from the bottom-up.

    RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval 🌳
        LangChain:
        Runnable Script
    Overview 🔎

    Implementing a recursive approach to process and organize retrieved information in a tree structure.
    Implementation 🛠️

    Use abstractive summarization to recursively process and summarize retrieved documents, organizing the information in a tree structure for hierarchical context.

    Self RAG 🔁
        LangChain:
        Runnable Script
    Overview 🔎

    A dynamic approach that combines retrieval-based and generation-based methods, adaptively deciding whether to use retrieved information and how to best utilize it in generating responses.
    Implementation 🛠️

    • Implement a multi-step process including retrieval decision, document retrieval, relevance evaluation, response generation, support assessment, and utility evaluation to produce accurate, relevant, and useful outputs.

    Corrective RAG 🔧
        LangChain:
        Runnable Script
    Overview 🔎

    A sophisticated RAG approach that dynamically evaluates and corrects the retrieval process, combining vector databases, web search, and language models for highly accurate and context-aware responses.
    Implementation 🛠️

    • Integrate Retrieval Evaluator, Knowledge Refinement, Web Search Query Rewriter, and Response Generator components to create a system that adapts its information sourcing strategy based on relevance scores and combines multiple sources when necessary.

🌟 Special Advanced Technique 🌟

    Sophisticated Controllable Agent for Complex RAG Tasks 🤖
    Overview 🔎

    An advanced RAG solution designed to tackle complex questions that simple semantic similarity-based retrieval cannot solve. This approach uses a sophisticated deterministic graph as the "brain" 🧠 of a highly controllable autonomous agent, capable of answering non-trivial questions from your own data.
    Implementation 🛠️

    • Implement a multi-step process involving question anonymization, high-level planning, task breakdown, adaptive information retrieval and question answering, continuous re-planning, and rigorous answer verification to ensure grounded and accurate responses.

Getting Started

To begin implementing these advanced RAG techniques in your projects:

    Clone this repository:

    git clone https://github.com/NirDiamant/RAG_Techniques.git

    Navigate to the technique you're interested in:

    cd all_rag_techniques/technique-name

    Follow the detailed implementation guide in each technique's directory.

Contributing

We welcome contributions from the community! If you have a new technique or improvement to suggest:

    Fork the repository
    Create your feature branch: git checkout -b feature/AmazingFeature
    Commit your changes: git commit -m 'Add some AmazingFeature'
    Push to the branch: git push origin feature/AmazingFeature
    Open a pull request
