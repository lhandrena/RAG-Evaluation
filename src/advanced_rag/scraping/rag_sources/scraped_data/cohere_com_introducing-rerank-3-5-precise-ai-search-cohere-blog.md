# Source: https://cohere.com/blog/rerank-3pt5?utm_source=substack&utm_medium=email
Number of words: 831

# Introducing Rerank 3.5: Precise AI Search | Cohere Blog

Rerank 3.5 delivers improved reasoning and multilingual capabilities to search complex enterprise data with greater accuracy. 
Product
Newsroom

Share:

Key Contributors: Daniel Simig, Nabila Abraham, Clifton Poth, Martin Hentschel, Violet Dang, Minghan Li, Michael Peng, Nils Reimers, and Elliott Choi

Rerank 3.5 is our latest AI search foundation model. It enables businesses to significantly improve the relevancy of information surfaced within search and retrieval-augmented generation (RAG) systems.

Rerank 3.5 delivers state-of-the-art features, including:

    Enhanced reasoning skills to enable understanding complex user questions which express various constraints that have traditionally challenged search systems.
    Broad data compatibility to search long documents with rich and relevant metadata (e.g. emails, reports), semi-structured data (e.g. tables, JSON), and code.
    Improved multilingual performance across 100+ languages and industry-leading in global business languages such as Arabic, French, Japanese, and Korean. 

    "Cohere is a key part of what makes Notion AI work. Their reranker gives us both the speed and quality we need, and it’s consistently improving. It’s been essential for getting our AI Connectors out the door quickly." - Simon Last, Cofounder & CTO, Notion

Improve enterprise AI systems in minutes

Rerank 3.5 efficiently finds the most relevant business data to answer a user question. It accomplishes this through a method called “cross-encoding” where the model computes a relevance score for a business document in relation to a user question. This method enables highly accurate information understanding, exceeding traditional keyword and embedding search, and can be applied after an initial dense retrieval stage to ensure the answers surfaced to users are maximally precise.

Rerank 3.5 is compatible with any existing search system, can be implemented with just a few lines of code, and tends to have negligible impact to overall system latency. It is most frequently used within retrieval-augmented generation (RAG) applications to provide generative AI models, such as our Command R series, with real-time business context to inform their outputs.

This offers a means of increasing the reliability of AI systems, helping sophisticated businesses move past experimentation and into production deployments to accelerate data-driven decision making.
Understand complex data across 100+ languages

Search systems often fail to retrieve relevant information when users implicitly or explicitly express constraints on what they would like returned. We identified that this was partially due to traditional systems lacking the ability to reason. Rerank 3.5 shows substantial improvements in this area, understanding complex multifaceted questions that other search systems fail to answer.
Reasoning Datasets are adversarial datasets where the user bounds a semantic search with implicit and explicit criteria. Reasoning dataset is measured as P@1 out of 2.

This capability is particularly helpful for businesses operating within specialized industries such as finance, government, energy, manufacturing, and healthcare. For example, on a financial services dataset we curated to be generally representative for common use cases, Rerank 3.5 performance was +23.4% better than Hybrid Search and +30.8% better than BM25. We expect organizations in these industries to observe similar improvements when evaluating performance on their data.

Rerank 3.5 also offers industry-leading multilingual capabilities. It can search across data in 100+ languages, with state-of-the-art accuracy on the following 10 global business languages: Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, and Spanish.
Cohere’s multilingual evaluation suite consists of external datasets covering 18 different languages in a variety of monolingual and cross-lingual settings. Multilingual performance is measured by nDCG@10

When compared to our previous Rerank 3 model, Rerank 3.5 delivers a +26.4% improvement on cross-lingual search where the user query is in a different language than the documents being searched. This helps large organizations eliminate barriers to accessing information across geographies and teams.
Get started with Rerank 3.5

Rerank 3.5 is available today on Cohere’s platform, Amazon Bedrock, and Amazon SageMaker. Our latest reranker is available for the first time on Amazon Bedrock through the new Rerank API (learn more). It will soon be available across additional cloud platforms.

    “We’re excited to work with Cohere to bring their latest reranker search model to Amazon Bedrock. Cohere Rerank 3.5 delivers state-of-the-art search and retrieval capabilities and enables powerful multilingual RAG applications. Rerank 3.5 enhances search accuracy by reranking keyword and vector results, ensuring only the most relevant content reaches the model—improving both search precision and enterprise efficiency. Whether in finance, hospitality, retail, e-commerce or beyond, Cohere's Rerank 3.5 model in Amazon Bedrock enables organizations to improve how they surface and utilize critical information, delivering better responses while reducing both latency and costs.”
    - Rahul Pathak, VP Data & AI GTM, AWS

Rerank 3.5 can also be deployed into any Virtual Private Cloud (VPC) or on-premise environment. To get started with Rerank 3.5 for your business, and learn more about options for large enterprise deployments, please contact our sales team.