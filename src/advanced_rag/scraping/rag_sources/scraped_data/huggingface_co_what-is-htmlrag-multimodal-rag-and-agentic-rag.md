# Source: https://huggingface.co/blog/Kseniase/html-multimodal-agentic-rag
Number of words: 2620

# What is HtmlRAG, Multimodal RAG and Agentic RAG?



What is HtmlRAG, Multimodal RAG and Agentic RAG?
Community Article
Published January 9, 2025
Ksenia Se's avatar
Ksenia Se
Kseniase
Alyona Vert's avatar
Alyona Vert
alyona0l
🔳 We explore in details three RAG methods that address limitations of original RAG and meet the upcoming trends of the new year

Retrieval-Augmented Generation (RAG) is a topic that never gets old and continues expanding more to enhance LLMs functionality. For those, who are not so familiar with RAG: this method empowers models with external knowledge, retrieving the information you actually need from external resources. Today, we’ll dive into three approaches that go further than traditional RAG, overcoming its issues such as retrieved data quality, accuracy of the answers and low performance in specific domains. As multimodality and agentic systems are among the main focuses of 2025 in AI, we’ll explore the following types of RAG: 1) HtmlRAG which works directly with HTML version of text; 2) Multimodal RAG that can retrieve image information; and 3) Agentic RAG which incorporates agentic capabilities in RAG technique. So let’s explore!

📨 Click follow! If you want to receive our articles straight to your inbox, please subscribe here

In today’s episode, we will cover:

    Traditional RAG limitations
    What is HtmlRAG?
        The core idea behind HtmlRAG
        How does HtmlRAG work?
        Limitations
    What is Multimodal RAG?
        The main idea of Multimodal RAG
        How does Multimodal RAG work?
        What about Multimodal RAG performance?
    What is Agentic RAG?
        What does Agentic RAG address?
        How does Agentic RAG work?
        What is good about Agentic RAG?
        Limitations
    Conclusion
    Resources to dive deeper (you can find all mentioned papers here)

Traditional RAG limitations

RAG systems combine a retrieval mechanism with a generative AI model to provide more accurate or contextually relevant responses. However, as any technique, it has several limitations, such as:

    Dependency on the quality of retrieved information: The effectiveness of the response relies heavily on the quality, relevance and bias of the documents retrieved. If the retrieval step fails, the generated output could be incorrect.
    Standard RAG can’t retrieve various types of information, such as HTML texts, images and videos.
    Mismatch between retrieval and query: The system may fail to align the user's query with the right context in the retrieved documents.
    Standard RAG have difficulties with searching across and retrieving multiple sources, or working with complex structures in documents.
    Scalability latency issues: Searching through a large knowledge base can introduce latency, especially if the retrieval system isn't optimized.
    RAG systems might underperform in highly specialized domains where context and nuance are critical.
    Computational resources: Handling large datasets for retrieval can be computationally expensive, requiring significant storage and processing power.

Researchers create different upgraded RAG systems and methods to overcome these issues. Types of RAG we are going to talk about mostly address the limitation of quality and diversity of retrieval information and mismatch between the query and the retrieval. Ladies and Gentlemen, meet HtmlRAG, Multimodal RAG and Agentic RAG.
What is HtmlRAG?
The core idea behind HtmlRAG

Many RAG systems, including those used by tools like ChatGPT and Perplexity, rely on the web as a key source of external information.

Here’s how it usually works: These systems search the web, gather webpage results, strip the content down to plain text, and feed that into the LLM to help it generate better answers. However, this plain text might lose a lot of useful details from webpages, like headings, tables, and other structural information.

To fix this, researchers from Baichuan Intelligent Technology and Renmin University of China introduced HtmlRAG, which uses the original HTML format instead of just plain text.

What’s good about this approach?

    Modern LLMs can understand HTML well, that’s why we can effectively implement this type of RAG.
    HTML preserves the structure and meaning of the content better. Many document formats (like PDFs or Word files) can also be easily turned into HTML, making it a flexible choice.

However, there’s a catch. HTML is full of extra stuff like tags, JavaScript, and styles with unnecessary data and could be too long. That’s why researchers also presented special techniques for these issues. Let’s break down how all of the aspects work together.
How does HtmlRAG work?

HtmlRAG works directly with HTML to keep more of the structure and meaning of the original content, missing the step of converting the data into the plain text. The main parts of HtmlRAG’s working process are HTML Cleaning and Pruning techniques:

image/png
HTML Cleaning

This step removes irrelevant content, simplifies the structure, and reduces the document size to just 6% of its original length. Its steps include:

    Striping out CSS styles, JavaScript, and comments that don’t add value.
    Simplifying the HTML structure by merging redundant tags (for example, combining nested < div > tags).
    Removing empty or irrelevant tags.

HtmlRAG's cleaning reduces tokens by 94.07% compared to 96.71% for plain text and 90.32% for Markdown.
HTML Pruning

This step further reduces the size of the cleaned HTML while keeping only the most relevant parts based on the user's query. This step is more complex, including two different pruning steps and using “block tree” approach to group and rank parts of the HTML.

How is the block tree built?

All the retrieved HTML documents are combined into one for processing. This combined document is converted into a DOM tree using a tool like Beautiful Soup. Child nodes are then merged into their parent nodes to form blocks. The size of each block is controlled by a setting, such as maximum words per block. The tree's granularity (level of detail) can be adjusted depending on the pruning needs to ensure the tree is neither too detailed nor too coarse. For efficient measure of data relevance, the block tree is converted into a token tree, where HTML tags and tokens are color-coded. Block scores are then derived by combining token probabilities.

image/png

The pruning process happens in two steps, both using this block tree structure:

Step 1: Pruning with an embedding model

This step uses a lightweight embedding model to identify and remove less relevant parts of the HTML document. Here’s how it works:

    Each HTML block's text is compared to the user's query using similarity scores from the embedding model.
    Blocks with lower relevance scores are deleted until the document fits the LLM’s input limit.
    After pruning, the remaining HTML structure is cleaned up to remove redundant tags or empty elements.

While this method is fast and effective at reducing the document size, it doesn’t consider the overall document structure, as it evaluates each block in isolation. It also struggles with very small blocks, where there isn’t enough text to determine relevance accurately. So here comes the second step.

Step 2: Fine-grained pruning with a generative model

It is used to refine the HTML further by taking the document’s full structure into account, using a generative model. In general, generative models can process the entire document context at once, unlike embedding models. They are better at identifying nuanced relationships between blocks and their content. So how does it work?

    The process starts with the cleaned HTML from Step 1, expanding the blocks into finer-grained parts.
    A generative model scores each smaller blocks of the document on how well it aligns with the user’s query. The score is calculated by analyzing the "path" of tags leading to each block. (For example: < html >< div >< p >.
    Blocks with lower scores are removed, ensuring the remaining HTML is both compact and meaningful.

To optimize this process HtmlRAG uses token skipping method, where the model skips over repetitive or predictable parts of the HTML structure to save computational resources, and depth-first traversal technique to reuse previously calculated data for reducing redundancy and speedup.

HTML pruning reduces average token counts from 1.6M to 4K while retaining relevance. It also skips 45% of nodes, minimizing cost increases while maintaining effectiveness.
Limitations

While techniques used in HtmlRAG shows good results, several limitations still exist:

    HtmlRAG relies heavily on well-structured HTML input, which means its performance can degrade when processing incomplete or poorly structured pages.
    Multiple sources challenge: The system might struggle with understanding or appropriately weighting context when synthesizing information from multiple sources.
    Domain-specific constraints: HtmlRAG might perform suboptimally for niche or highly specialized domains where the HTML pages do not align with typical structures.

However, despite these limitations HtmlRAG effectively improves retrieval accuracy by working with more complex text format. But if we add image information, will it improve RAG even more?
What is Multimodal RAG?
The main idea of Multimodal RAG

In evolving age of multimodal models it’s obvious that we need RAG techniques that can handle multimodal data. The ideas of Multimodal RAG were explored by Google Research in 2022 with MuRAG approach (as a reminder, you can find all links in the section Resources below). One of the latest research on this type of RAG was conducted by Center for Information and Language Processing and Siemens AG. They tested two ways of processing and retrieving image information from technical and industrial documents. The main question is: Does the multimodal RAG approach work better than RAG using just text?
How does Multimodal RAG work?

Firstly, we need to define how to process and retrieve image information from documents like PDFs. Researchers proposed two variants:

    Multimodal embeddings: This approach directly links the visual content of images with textual queries. Here’s how it works:
        Both images and the question are turned into embeddings using the CLIP tool.
        Similarities are calculated to find the images most relevant to the question.
        Retrieved images are then used by the AI model for answer generation.
    Text summaries from images: Converting images to text allows for better integration with text-based RAG pipelines and reduces the risk of losing information during retrieval. Here’s the working process:
        Summaries of the images are embedded as text and stored in a vector database.
        When a question is asked, the system retrieves the most relevant text summaries and passes them to the AI model along with the original images.

For now, let’s explore how to combined both text and image information to create Multimodal RAG. Two configurations of this RAG type were tested:

image/png

    Separate vector stores:

Text chunks are stored in one vector database, while image embeddings are stored in another vector database. The system performs a similarity search in both databases. Retrieved text and image data are combined and passed to the AI model for answer generation.

This approach keeps text and image data separate, allowing for independent optimization of each modality.

    Combined vector store:

Converted images into text summaries are combined with text chunks from documents (PDFs). Both are embedded as text and stored in a single vector database. Then a single similarity search is performed in the combined database, retrieving both text and image-derived summaries. The AI model retrieves this combined information for answering the question.

Storing everything in one database simplifies the retrieval process and ensures consistent treatment of text and image information.
What about Multimodal RAG performance?

Experiments showed that combining text and images led to better performance compared to using text or images alone. Text summaries from images are proved to be more flexible and effective than multimodal embeddings.

image/png

However, Multimodal RAG has some limitations:

    Reliance on LLMs introduces typical LLM issues such as inaccuracies, hallucinations, and challenges with complex multimodal inputs.
    A lack of publicly available, domain-specific datasets limits the reproducibility and generalizability of the findings and developing such datasets is crucial for future improvements. Now this approach is not domain-specific but it could be extended to other fields.

Overall results prove that empowering RAG with multimodal capabilities has a good impact on the effectiveness of RAG systems.

But what about agentic capabilities that are just as important as multimodal ones?
What is Agentic RAG?

Agentic systems are on the rise and they need all of its element to be more agentic, as well. That’s why many AI researchers are exploring the concepts of agentic RAG to build more efficient systems. Today we want to explore Hugging Face’s variant of Agentic RAG to clarify how such system works.
What does Agentic RAG address?

Earlier in this episode, we highlighted the limitations of standard RAG, and now we will revisit some of them, which are related to query and retrieval mismatch and the quality of retrieval data. What can we say more about these limitations?

    User queries are often written as questions, but documents in the knowledge base may phrase the same information differently, and this mismatch can lower the retrieval quality.
    If the initial retrieval misses the mark, the generated response is likely inaccurate or incomplete.

Here’s where Agentic RAG comes. It enhances RAG by equipping the system with agent-like capabilities, meaning it can:

    Reformulate queries: Turn user questions into retrieval-friendly statements that better match the structure of relevant documents.
    Critique and retry retrieval: Assess the retrieved results, recognize gaps or irrelevance, and retry with adjusted queries.

How does Agentic RAG work?

As traditional RAG system, a RAG Agent queries the vector database using semantic similarity. Here’s how it works:

    The agent starts by transforming the user’s query into a retrieval-friendly statement. It accepts queries in an affirmative form rather than as questions to improve document alignment. For example:

    User query: "How can I upload a model to the Hub?"

    Reformulated query: "Upload a model to the Hub."

    Using the initial query, Agentic RAG searches the database for top-k relevant documents based on embedding similarity.

    Returns the retrieved content for further analysis. If the retrieved results are insufficient or irrelevant, the agent critiques them and generates a new query. This process repeats until sufficient information is retrieved or a pre-set limit is reached.

    Once the agent is satisfied with the retrieved context, it combines the information with the user query and passes it to the LLM to generate a final response.

What is good about Agentic RAG?

It is more autonomous and can retry retrieval with semantically different queries, increasing the chances of finding the right information. This significantly improves accuracy and completeness, especially for complex, domain-specific questions. The agent setup improved performance of standard RAG by 14%, demonstrating the value of query reformulation and iterative retrieval.
Limitations

Building an agentic RAG system, while beneficial, introduces some issues, such as:

    Additional complexity in setup and execution compared to standard RAG systems.
    Increasing computational overhead by adding query reformulation and iterative retrieval steps.
    Dependency on LLM performance: The quality of the system heavily relies on the language model’s ability to generate accurate and contextually relevant reformulated queries and answers.
    Evaluation limitations: Automated evaluations rely on LLM-based judgments, which may introduce biases. That’s why human evaluations are still essential for a more reliable assessment.

Conclusion

We explored three RAG systems which enhance standard RAG in terms of quality of retrieval information and overall efficiency and accuracy. When you need to work with documents with complex structures – HtmlRAG is here to keep all the crucial structure of the text, saving recourses. In the age of multimodality we can’t imagine AI field without working with images, and Multimodal RAG is an essential tool in this case. Agentic RAG is an another level of system which could take RAG on the novel level of autonomy and accuracy. As AI models evolve, RAG technique evolves together with them, and we’ll keep an eye on the new breakthroughs.

