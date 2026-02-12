# Source: https://x.com/victorialslocum/status/1904504036369543464
Number of words: 360

# Victoria Slocum on X: "'Just do RAG' they said. But WHICH RAG? Here’s 7 different RAG Architectures you should know 👇 1️⃣ 𝗡𝗮𝗶𝘃𝗲 𝗥𝗔𝗚: 𝗧𝗵𝗲 𝗖𝗹𝗮𝘀𝘀𝗶𝗰 𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵 Naive RAG is the standard implementation with a relatively straightforward process: • Query comes in from the user • https://t.co/m8J3A3XjEg" / X

'Just do RAG' they said. But WHICH RAG?

Here’s 7 different RAG Architectures you should know 👇

1️⃣ 𝗡𝗮𝗶𝘃𝗲 𝗥𝗔𝗚: 𝗧𝗵𝗲 𝗖𝗹𝗮𝘀𝘀𝗶𝗰 𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵
Naive RAG is the standard implementation with a relatively straightforward process:
• Query comes in from the user
• System retrieves relevant documents from a vector database
• Retrieved documents are combined with the query as context
• LLM generates a response based on both query and context
This works well for many simple applications, like basic Q&A systems or document assistants.

2️⃣ 𝗥𝗲𝘁𝗿𝗶𝗲𝘃𝗲 𝗮𝗻𝗱 𝗥𝗲𝗿𝗮𝗻𝗸 𝗥𝗔𝗚
This one adds a reranking step after the retrieval to improve response quality:
• Initial retrieval returns a larger set of potentially relevant documents
• A reranking model evaluates and scores these documents based on relevance
• Only the highest-scoring documents are sent to the LLM

3️⃣ 𝗠𝘂𝗹𝘁𝗶𝗺𝗼𝗱𝗮𝗹 𝗥𝗔𝗚
The architecture leverages models that can process and retrieve from text, images, audio, video, and other data types. 

4️⃣ 𝗚𝗿𝗮𝗽𝗵 𝗥𝗔𝗚
Graph RAG uses a graph database to incorporate relationship information between documents:
• Documents/chunks are nodes in a graph
• Relationships between documents are edges
• Can follow relationship paths to find contextually relevant information

5️⃣ 𝗛𝘆𝗯𝗿𝗶𝗱 𝗥𝗔𝗚 𝗩𝗲𝗰𝘁𝗼𝗿 𝗗𝗕 𝘄𝗶𝘁𝗵 𝗚𝗿𝗮𝗽𝗵 𝗗𝗕
This architecture combines both vector search and a graph database:
• Vector search identifies semantically similar content
• Graph database provides structured relationship data
• Queries can leverage both similarity and explicit relationships
• Results can include information discovered through relationship traversal

6️⃣ 𝗔𝗴𝗲𝗻𝘁𝗶𝗰 𝗥𝗔𝗚 𝘄𝗶𝘁𝗵 𝗥𝗼𝘂𝘁𝗲𝗿 𝗔𝗴𝗲𝗻𝘁
A single agent makes decisions about retrieval:
• Analyzes the query to determine the best knowledge sources
• Makes strategic decisions about how to retrieve information
• Coordinates the retrieval process based on query understanding
𝘊𝘩𝘦𝘤𝘬 𝘰𝘶𝘵 𝘵𝘩𝘦 𝘘𝘶𝘦𝘳𝘺 𝘈𝘨𝘦𝘯𝘵 𝘪𝘯 𝘞𝘦𝘢𝘷𝘪𝘢𝘵𝘦: https://weaviate.io/blog/query-age
nt?utm_source=linkedin&utm_medium=vs_social&utm_campaign=agents&utm_content=honeypot_post_802941270


7️⃣ 𝗠𝘂𝗹𝘁𝗶-𝗔𝗴𝗲𝗻𝘁 𝗥𝗔𝗚
This one employs multiple specialized agents:
• Master agent coordinates the overall process
• Specialized retrieval agents focus on different tasks
• Agents can communicate and collaborate to solve complex problems
For example, one agent might retrieve from various sources, another might do data transformation, and a third personalizing the results from the user—all coordinated by a master agent that assembles the final response.