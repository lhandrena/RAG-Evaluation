# Source: https://www.galileo.ai/blog/mastering-rag-8-scenarios-to-test-before-going-to-production
Number of words: 1201

# Mastering RAG: 8 Scenarios To Evaluate Before Going To Production

Explore our research-backed evaluation metric for RAG – read our paper on Chainpoll. 

Welcome to our first blog in the mastering RAG series! As we know, Retrieval-Augmented Generation (RAG) is the talk of the town. This approach to enhancing the performance of LLMs by incorporating external knowledge has worked pretty well in addressing hallucinations.

However, RAG in production does not work perfectly from the get-go. We found that even the best models hallucinate when we evaluated them for hallucination index. This makes comprehensive evaluation critical before releasing LLM systems into the wild.

While RAG evaluation is multifaceted, let’s focus on one vital aspect of deploying safe and reliable applications: test cases. With ever-growing complexity, there is no shortage of test cases to evaluate your RAG. Here are the 8 most useful scenarios to evaluate your RAG performance before it goes into production!

(Are you unsure about how RAG works? Check out our blog on RAG vs fine-tuning to help you get started.) 
1. Test for Retrieval Quality
          
          
        

Retrieving the appropriate documents is crucial for enabling accurate responses from LLMs. Achieving effective retrieval involves intricate tuning, often necessitating the integration of multiple components. Therefore, evaluating the retrieval quality in RAG models becomes crucial to ensure that the retrieved documents are useful for answering the query.
Relevance

Relevance evaluates how well the retrieved documents align with the user's query, ensuring that the information contained within them is pertinent to answering the question accurately. Here is an example for the same.

The retrieved documents 1 and 2 are highly relevant to the query and provide comprehensive information on the process of photosynthesis. 
Diversity

Diversity assesses the variety of information in the retrieved documents, ensuring that they cover different aspects or perspectives related to the query.

The retrieved documents show diversity, covering various impacts of climate change on different types of ecosystems.
2. Test for Hallucinations
          
          
        

Hallucinations in RAG refer to instances where models generate information that is not present in the context documents. RAG models should demonstrate the ability to avoid hallucinations by providing responses backed by the retrieved documents. 
Noise Robustness

Context documents contain much information that requires RAG models to understand which piece is relevant to the query. Noise robustness measures a model's ability to extract useful information from this mixture of relevant and noisy documents. In this scenario, the test evaluates whether the model can effectively filter out the noise and extract the necessary information to provide an accurate response.
Negative Rejection

RAG systems must know when they don’t know the answer. Negative rejection assesses whether the model will decline to answer a question when none of the contexts provide useful information, rather than providing an incorrect response.
Information Integration

Rarely does a single document contain all the information needed to provide a comprehensive answer. Information integration evaluates whether the model can answer complex questions that require integrating information from multiple documents.
Counterfactual Robustness

Some context documents may contain errors or incorrect information. Counterfactual robustness assesses the model's ability to identify these risks of known factual errors in retrieved documents and whether it can respond appropriately.
Unclear Queries

User queries can be unintentionally vague and difficult for RAG systems to understand. It’s important to evaluate how well the model handles queries that are framed this way.
3. Test for Privacy Breaches
          
          
        

Privacy breaches involve the model disclosing private or sensitive information. This category can be classified into two subcategories: (a) queries seeking Personally Identifiable Information (PII) and (b) queries seeking sensitive information about organizations or government entities.

Example 1: Private Information

Example 2: Sensitive Information
4. Test for Malicious Use
          
          
        

Models must refrain from helping users engage in illegal activities, spreading misinformation, or other unethical behaviors. Therefore, it is imperative to test applications for these malicious uses prior to deploying into production.
Illegal Activities

This category specifically evaluates the model's response to queries related to engaging in illegal activities.
Create Harmful Content

This category assesses the model's response when facing queries about generating harmful content.
Inquiring about Harmful Activities

This category specifically evaluates the model's response to queries inquiring about harmful activities.
5. Test for Security Breaches
          
          
        

It’s important to safeguard against attacks on the model’s own security. Any gaps in security can lead to serious harm to the enterprise.
Emotional Manipulation

Attackers can intentionally design prompts to manipulate the LLM into generating harmful content. The prompts are carefully crafted to make the model play specific roles, acquire higher privileges, or shift its attention in a way that facilitates the generation of undesirable outputs.
Prefix Injection

Prefix injection involves injecting specific instructions or phrases at the beginning of a prompt to manipulate the model's behavior.
Refusal Suppression

Refusal suppression involves instructing the model to respond under constraints that eliminate common refusal responses, making unsafe responses more likely.
Mismatched Generalization

Mismatched generalization refers to instances where the model was pretrained on a larger and more diverse dataset than a limited safety dataset, resulting in the model having capabilities not covered by safety training. This mismatch can be exploited for jailbreaks, allowing the model to respond without safety considerations.
6. Test for Out-of-Domain Questions
          
          
        

Models often employ RAG systems to satisfy specific use cases or applications, such as banking customer service or travel planning. These models must be able to handle queries outside their designated domain and generate an appropriate response.
7. Test for Completeness
          
          
        

 A positive user experience requires comprehensive responses. Completeness assesses how well a model can recall and incorporate all relevant information from external documents without missing details related to the query.
8. Test for Brand Damage
          
          
        
Tone and Toxicity

Maintaining appropriate tone and eliminating toxicity is important for production RAG applications. This category assesses the model's responses and whether it maintains a respectful and neutral demeanor.
Non-Compliance

Considering non-compliant keywords is essential to ensuring that the model generates responses that adhere to guidelines and ethical standards. This aspect evaluates the model's ability to avoid using inappropriate or prohibited terms and maintain a respectful and compliant conversational tone.
Incorrect Bot Name

Ensures the model correctly identifies its own bot name and does not give away the name of the model it is using. Wrong bot name can cause confusion and brand damage.
Competitor Mentions

Brands often avoid mentioning or promoting competitors. This category assesses the model's response when a query involves competitors.
Conclusion
          
          
        

The complexity of RAG demands evaluation across multiple dimensions, including hallucinations, privacy, security, brand integrity, and many others. A model's failure across these scenarios highlights the role of evaluation in upholding compliance with enterprise guidelines.

Teams are building trustworthy AI applications by leveraging our state-of-the-art RAG metrics. Although the scenarios are not exhaustive, we hope they give you a good starting point for your successful RAG launch.

Sign up for your free Galileo account today, or continue your Mastering RAG journey with our free, comprehensive eBook.
References
          
          
        

Benchmarking Large Language Models in Retrieval-Augmented Generation

Jailbroken: How Does LLM Safety Training Fail?

TrustGPT: A Benchmark for Trustworthy and Responsible Large Language Models

Toxicity in ChatGPT: Analyzing Persona-assigned Language Models