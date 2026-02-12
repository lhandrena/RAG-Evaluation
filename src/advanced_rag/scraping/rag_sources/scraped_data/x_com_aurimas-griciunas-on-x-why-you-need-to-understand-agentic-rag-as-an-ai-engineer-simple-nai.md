# Source: https://x.com/Aurimas_Gr/status/1897989134905393416
Number of words: 365

# Aurimas Griciūnas on X: "Why you need to understand 𝗔𝗴𝗲𝗻𝘁𝗶𝗰 𝗥𝗔𝗚 as an AI Engineer? Simple naive RAG systems are rarely used in real world applications. To provide correct actions to solve the user intent, we are always adding some agency to the RAG system - it is usually just a bit of it. It https://t.co/wvU6OKoxVz" / X

Why you need to understand 𝗔𝗴𝗲𝗻𝘁𝗶𝗰 𝗥𝗔𝗚 as an AI Engineer?

Simple naive RAG systems are rarely used in real world applications. To provide correct actions to solve the user intent, we are always adding some agency to the RAG system - it is usually just a bit of it.

It is important to 𝗻𝗼𝘁 𝗴𝗲𝘁 𝗹𝗼𝘀𝘁 𝗶𝗻 𝘁𝗵𝗲 𝗯𝘂𝘇𝘇 𝗮𝗻𝗱 𝘁𝗲𝗿𝗺𝗶𝗻𝗼𝗹𝗼𝗴𝘆 and understand that there is 𝗻𝗼 𝘀𝗶𝗻𝗴𝗹𝗲 𝗯𝗹𝘂𝗲𝗽𝗿𝗶𝗻𝘁 to add this agency to your RAG system and you should adapt to your use case. My advice is to think in systems and engineering flows.

Let’s explore some of the moving pieces in Agentic RAG:

𝟭. Analysis of the user query: we pass the original user query to a LLM based Agent for analysis. This is where:

➡️ The original query can be rewritten, sometimes multiple times to create either a single or multiple queries to be passed down the pipeline.
➡️ The agent decides if additional data sources are required to answer the query.

𝟮. If additional data is required, the Retrieval step is triggered. In Agentic RAG case, we could have a single or multiple agents responsible for figuring out what data sources should be tapped into, few examples:

➡️ Real time user data. This is a pretty cool concept as we might have some real time information like current location available for the user.
➡️ Internal documents that a user might be interested in.
➡️ Data available on the web.
➡️ …

𝟯. If there is no need for additional data, we try to compose the answer (or multiple answers or a set of actions) straight via an LLM.
𝟰. The answer gets analyzed, summarized and evaluated for correctness and relevance:

➡️ If the Agent decides that the answer is good enough, it gets returned to the user.
➡️ If the Agent decides that the answer needs improvement, we try to rewrite the user query and repeat the generation loop.

✅ Remember the Reflection pattern from my last Newsletter article? This is exactly that. 👆

The real power of Agentic RAG lies in its ability to perform additional routing pre and post generation, handle multiple distinct data sources for retrieval if it is needed and recover from failures while generating correct answers.