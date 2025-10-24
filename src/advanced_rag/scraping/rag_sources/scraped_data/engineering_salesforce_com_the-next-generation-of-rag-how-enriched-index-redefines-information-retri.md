# Source: https://engineering.salesforce.com/the-next-generation-of-rag-how-enriched-index-redefines-information-retrieval-for-llms/?utm_source=substack&utm_medium=email

# Next-Gen RAG: How Enriched Index Redefines Information Retrieval for LLMs

Robert XueJan 09											-
						6 min read

Robert XueJan 09											-
						6 min read

Robert XueJan 09											-
						6 min read

Jan 09											-
						6 min read

Jan 09											-
						6 min read

In our “Engineering Energizers” Q&A series, we explore the stories of engineering innovators transforming the tech landscape. Today, we spotlight Robert Xue, a software engineering architect at Salesforce who is spearheading the development of Enriched Index – an advanced Retrieval-Augmented Generation (RAG) system that improves information retrieval with enhanced precision and scalability.Discover how Robert’s team creates dynamic retrieval systems that balance precision and speed by adjusting query complexity, uses hierarchical indexing and parallel processing to manage growing data demands, and implements strong encryption and compliance measures to ensure trust and security.What is your team’s mission as it relates to Enriched Index?Our mission is to provide scalable, reusable components for Large Language Model (LLM) applications, enabling developers to create adaptable and efficient solutions. By emphasizing modularity, we aim to help organizations address complex challenges without starting from scratch.How Enriched Index Differs from Traditional RAG Index:Multi-round Indexing:Enriches data with contextual metadata to ensure retrieved information is complete and relevant.Dynamic, Context-Aware Retrieval:Transforms static information retrieval into an adaptable, scalable system capable of handling complex queries.These advancements reduce preprocessing requirements and streamline workflows, making Enriched Index ideal for both sophisticated enterprise solutions and general AI-driven applications.Robert dives into Salesforce’s innovation process.What was the most significant technical challenge your team faced while developing Enriched Index?The most significant challenge was balancing feature value with computational efficiency. For example, knowledge graphs offered advanced query resolution but came with substantial infrastructure demands. While valuable for complex use cases, they were often unnecessary for simpler queries, making feature prioritization crucial.To address this, we focused on metadata augmentation and summarization techniques. Features like RAPTOR Summarization improved data organization by creating enriched representations of source material, enhancing retrieval accuracy and efficiency without overburdening system resources.Pilot programs were essential in refining our approach. By testing real-world scenarios with customers, we validated the impact of our solutions and aligned them with user needs. This iterative process ensured that we prioritized practical advancements, delivering balanced performance and laying the groundwork for future innovations.What unexpected technical hurdle did your team encounter with Enriched Index?One unexpected hurdle was latency. Advanced features like query expansion and augmented retrieval algorithms significantly improved accuracy but introduced delays that frustrated users. Balancing precision and responsiveness required innovative solutions.To tackle this, we developed a dual-path system. High-complexity queries were routed through advanced algorithms, while simpler queries used lightweight retrieval algorithm optimized for speed. This ensured quick responses without compromising the quality of results for complex tasks.Operationally, standardizing inputs from diverse data sources was another challenge. Many external systems lacked consistent metadata, complicating preprocessing. We addressed this by implementing intermediary normalization layers that standardized data before indexing. These solutions not only resolved latency and compatibility issues but also enhanced overall system performance, ensuring a seamless user experience across various workloads.How Enriched Index enhanced RAG in Salesforce.How does your team balance the need for rapid deployment with maintaining high standards of trust and security?Balancing speed and security involves a dual approach. For customers who need control, we offer “bring-your-own-model” capabilities, allowing them to integrate LLMs tailored to their compliance needs. For other customers, we provide curated models trained on vetted datasets, ensuring high reliability right out of the box.Our infrastructure uses multi-layered encryption and stringent access controls to protect data during processing. We also maintain transparency by documenting deployment pipelines and security protocols, which empowers developers to audit and customize solutions with confidence.Continuous monitoring and regular audits reinforce this balance, ensuring that new features meet strict security standards.By addressing diverse customer requirements while maintaining robust safety measures, we deliver solutions that meet both rapid deployment goals and trust expectations. This approach is especially critical in regulated industries, where compliance is non-negotiable.What strategies does your team use to address scalability challenges when implementing Enriched Index?Scalability challenges were addressed using a multi-faceted approach to ensure consistent performance across diverse workloads. Key strategies for addressing scalability included:In-House Solutions: We transitioned from relying on external providers to gain greater control over our infrastructure and resources.Hierarchical Indexing: We organized data into clusters, which reduced computational complexity and improved retrieval efficiency.Parallel Processing Pipelines: We enabled simultaneous request handling without performance degradation.Fallback Mechanisms: We maintained system reliability during peak loads by dynamically rerouting processes.Continuous Monitoring:We adapted to evolving customer demands through real-time optimizations and performance tuning.These strategies allowed the team to scale Enriched Index effectively, meeting enterprise-level demands while maintaining reliability and responsiveness.What ongoing research and development efforts are being undertaken to enhance the capabilities of Enriched Index?Our R&D efforts focus on refining CRM-specific use cases while exploring broader AI applications. Collaboration with pilot customers provides valuable insights into real-world challenges, which inform our iterative development process.One key area of innovation is summarization. We are developing efficient summarization algorithm that doesn’t need LLM to function well. Proprietary in house LLM like TextEVAL also streamlined model evaluations, reducing manual oversight and accelerating improvements.Additionally, we are investigating context-aware query expansions that dynamically adjust the retrieval query based on query complexity and the index’s richness. These efforts ensure that Enriched Index remains at the forefront of AI retrieval technologies, delivering practical solutions that evolve with customer needs and industry trends.Robert dives deeper into how Salesforce engineers innovate.What measures are in place to ensure the ethical use of Enriched Index, particularly regarding data privacy and bias mitigation?Ethical considerations are central to our approach. Attribute-Based Access Control (ABAC) ensures that derived data adheres to the visibility permissions of its source materials, safeguarding against unintended data exposure during aggregation.Bias mitigation is another key focus area. We train models using diverse datasets and incorporate fairness algorithms to reduce systemic biases. Regular audits evaluate compliance with ethical guidelines and regulatory standards, ensuring our systems meet customer expectations.To prevent premature risks, features like cross-document summarization are deferred until visibility controls are fully refined. By taking a cautious, deliberate approach, we uphold data privacy and ethical standards while delivering high-quality results.Can you share a case study or example where Enriched Index significantly improved a process or outcome?Enriched index has shown its potential in the banking sector, where legal document processing often involves complex semantic distinctions. Traditional semantic search systems frequently struggled to differentiate between similar legal terms, leading to irrelevant or incomplete results.By leveraging metadata enrichment and chunk-based retrieval, Enriched index accurately distinguished nuanced legal concepts. This capability enhanced the efficiency of information retrieval, reducing the burden on manual processes and enabling faster decision-making. The deployment highlighted the platform’s ability to address domain-specific challenges with precision, making it an invaluable tool for industries that require highly accurate, context-aware information retrieval.Learn moreStay connected — join ourTalent Community!Check out ourTechnology and Productteams to learn how you can get involved.

In our “Engineering Energizers” Q&A series, we explore the stories of engineering innovators transforming the tech landscape. Today, we spotlight Robert Xue, a software engineering architect at Salesforce who is spearheading the development of Enriched Index – an advanced Retrieval-Augmented Generation (RAG) system that improves information retrieval with enhanced precision and scalability.Discover how Robert’s team creates dynamic retrieval systems that balance precision and speed by adjusting query complexity, uses hierarchical indexing and parallel processing to manage growing data demands, and implements strong encryption and compliance measures to ensure trust and security.What is your team’s mission as it relates to Enriched Index?Our mission is to provide scalable, reusable components for Large Language Model (LLM) applications, enabling developers to create adaptable and efficient solutions. By emphasizing modularity, we aim to help organizations address complex challenges without starting from scratch.How Enriched Index Differs from Traditional RAG Index:Multi-round Indexing:Enriches data with contextual metadata to ensure retrieved information is complete and relevant.Dynamic, Context-Aware Retrieval:Transforms static information retrieval into an adaptable, scalable system capable of handling complex queries.These advancements reduce preprocessing requirements and streamline workflows, making Enriched Index ideal for both sophisticated enterprise solutions and general AI-driven applications.Robert dives into Salesforce’s innovation process.What was the most significant technical challenge your team faced while developing Enriched Index?The most significant challenge was balancing feature value with computational efficiency. For example, knowledge graphs offered advanced query resolution but came with substantial infrastructure demands. While valuable for complex use cases, they were often unnecessary for simpler queries, making feature prioritization crucial.To address this, we focused on metadata augmentation and summarization techniques. Features like RAPTOR Summarization improved data organization by creating enriched representations of source material, enhancing retrieval accuracy and efficiency without overburdening system resources.Pilot programs were essential in refining our approach. By testing real-world scenarios with customers, we validated the impact of our solutions and aligned them with user needs. This iterative process ensured that we prioritized practical advancements, delivering balanced performance and laying the groundwork for future innovations.What unexpected technical hurdle did your team encounter with Enriched Index?One unexpected hurdle was latency. Advanced features like query expansion and augmented retrieval algorithms significantly improved accuracy but introduced delays that frustrated users. Balancing precision and responsiveness required innovative solutions.To tackle this, we developed a dual-path system. High-complexity queries were routed through advanced algorithms, while simpler queries used lightweight retrieval algorithm optimized for speed. This ensured quick responses without compromising the quality of results for complex tasks.Operationally, standardizing inputs from diverse data sources was another challenge. Many external systems lacked consistent metadata, complicating preprocessing. We addressed this by implementing intermediary normalization layers that standardized data before indexing. These solutions not only resolved latency and compatibility issues but also enhanced overall system performance, ensuring a seamless user experience across various workloads.How Enriched Index enhanced RAG in Salesforce.How does your team balance the need for rapid deployment with maintaining high standards of trust and security?Balancing speed and security involves a dual approach. For customers who need control, we offer “bring-your-own-model” capabilities, allowing them to integrate LLMs tailored to their compliance needs. For other customers, we provide curated models trained on vetted datasets, ensuring high reliability right out of the box.Our infrastructure uses multi-layered encryption and stringent access controls to protect data during processing. We also maintain transparency by documenting deployment pipelines and security protocols, which empowers developers to audit and customize solutions with confidence.Continuous monitoring and regular audits reinforce this balance, ensuring that new features meet strict security standards.By addressing diverse customer requirements while maintaining robust safety measures, we deliver solutions that meet both rapid deployment goals and trust expectations. This approach is especially critical in regulated industries, where compliance is non-negotiable.What strategies does your team use to address scalability challenges when implementing Enriched Index?Scalability challenges were addressed using a multi-faceted approach to ensure consistent performance across diverse workloads. Key strategies for addressing scalability included:In-House Solutions: We transitioned from relying on external providers to gain greater control over our infrastructure and resources.Hierarchical Indexing: We organized data into clusters, which reduced computational complexity and improved retrieval efficiency.Parallel Processing Pipelines: We enabled simultaneous request handling without performance degradation.Fallback Mechanisms: We maintained system reliability during peak loads by dynamically rerouting processes.Continuous Monitoring:We adapted to evolving customer demands through real-time optimizations and performance tuning.These strategies allowed the team to scale Enriched Index effectively, meeting enterprise-level demands while maintaining reliability and responsiveness.What ongoing research and development efforts are being undertaken to enhance the capabilities of Enriched Index?Our R&D efforts focus on refining CRM-specific use cases while exploring broader AI applications. Collaboration with pilot customers provides valuable insights into real-world challenges, which inform our iterative development process.One key area of innovation is summarization. We are developing efficient summarization algorithm that doesn’t need LLM to function well. Proprietary in house LLM like TextEVAL also streamlined model evaluations, reducing manual oversight and accelerating improvements.Additionally, we are investigating context-aware query expansions that dynamically adjust the retrieval query based on query complexity and the index’s richness. These efforts ensure that Enriched Index remains at the forefront of AI retrieval technologies, delivering practical solutions that evolve with customer needs and industry trends.Robert dives deeper into how Salesforce engineers innovate.What measures are in place to ensure the ethical use of Enriched Index, particularly regarding data privacy and bias mitigation?Ethical considerations are central to our approach. Attribute-Based Access Control (ABAC) ensures that derived data adheres to the visibility permissions of its source materials, safeguarding against unintended data exposure during aggregation.Bias mitigation is another key focus area. We train models using diverse datasets and incorporate fairness algorithms to reduce systemic biases. Regular audits evaluate compliance with ethical guidelines and regulatory standards, ensuring our systems meet customer expectations.To prevent premature risks, features like cross-document summarization are deferred until visibility controls are fully refined. By taking a cautious, deliberate approach, we uphold data privacy and ethical standards while delivering high-quality results.Can you share a case study or example where Enriched Index significantly improved a process or outcome?Enriched index has shown its potential in the banking sector, where legal document processing often involves complex semantic distinctions. Traditional semantic search systems frequently struggled to differentiate between similar legal terms, leading to irrelevant or incomplete results.By leveraging metadata enrichment and chunk-based retrieval, Enriched index accurately distinguished nuanced legal concepts. This capability enhanced the efficiency of information retrieval, reducing the burden on manual processes and enabling faster decision-making. The deployment highlighted the platform’s ability to address domain-specific challenges with precision, making it an invaluable tool for industries that require highly accurate, context-aware information retrieval.Learn moreStay connected — join ourTalent Community!Check out ourTechnology and Productteams to learn how you can get involved.

In our “Engineering Energizers” Q&A series, we explore the stories of engineering innovators transforming the tech landscape. Today, we spotlight Robert Xue, a software engineering architect at Salesforce who is spearheading the development of Enriched Index – an advanced Retrieval-Augmented Generation (RAG) system that improves information retrieval with enhanced precision and scalability.Discover how Robert’s team creates dynamic retrieval systems that balance precision and speed by adjusting query complexity, uses hierarchical indexing and parallel processing to manage growing data demands, and implements strong encryption and compliance measures to ensure trust and security.What is your team’s mission as it relates to Enriched Index?Our mission is to provide scalable, reusable components for Large Language Model (LLM) applications, enabling developers to create adaptable and efficient solutions. By emphasizing modularity, we aim to help organizations address complex challenges without starting from scratch.How Enriched Index Differs from Traditional RAG Index:Multi-round Indexing:Enriches data with contextual metadata to ensure retrieved information is complete and relevant.Dynamic, Context-Aware Retrieval:Transforms static information retrieval into an adaptable, scalable system capable of handling complex queries.These advancements reduce preprocessing requirements and streamline workflows, making Enriched Index ideal for both sophisticated enterprise solutions and general AI-driven applications.Robert dives into Salesforce’s innovation process.What was the most significant technical challenge your team faced while developing Enriched Index?The most significant challenge was balancing feature value with computational efficiency. For example, knowledge graphs offered advanced query resolution but came with substantial infrastructure demands. While valuable for complex use cases, they were often unnecessary for simpler queries, making feature prioritization crucial.To address this, we focused on metadata augmentation and summarization techniques. Features like RAPTOR Summarization improved data organization by creating enriched representations of source material, enhancing retrieval accuracy and efficiency without overburdening system resources.Pilot programs were essential in refining our approach. By testing real-world scenarios with customers, we validated the impact of our solutions and aligned them with user needs. This iterative process ensured that we prioritized practical advancements, delivering balanced performance and laying the groundwork for future innovations.What unexpected technical hurdle did your team encounter with Enriched Index?One unexpected hurdle was latency. Advanced features like query expansion and augmented retrieval algorithms significantly improved accuracy but introduced delays that frustrated users. Balancing precision and responsiveness required innovative solutions.To tackle this, we developed a dual-path system. High-complexity queries were routed through advanced algorithms, while simpler queries used lightweight retrieval algorithm optimized for speed. This ensured quick responses without compromising the quality of results for complex tasks.Operationally, standardizing inputs from diverse data sources was another challenge. Many external systems lacked consistent metadata, complicating preprocessing. We addressed this by implementing intermediary normalization layers that standardized data before indexing. These solutions not only resolved latency and compatibility issues but also enhanced overall system performance, ensuring a seamless user experience across various workloads.How Enriched Index enhanced RAG in Salesforce.How does your team balance the need for rapid deployment with maintaining high standards of trust and security?Balancing speed and security involves a dual approach. For customers who need control, we offer “bring-your-own-model” capabilities, allowing them to integrate LLMs tailored to their compliance needs. For other customers, we provide curated models trained on vetted datasets, ensuring high reliability right out of the box.Our infrastructure uses multi-layered encryption and stringent access controls to protect data during processing. We also maintain transparency by documenting deployment pipelines and security protocols, which empowers developers to audit and customize solutions with confidence.Continuous monitoring and regular audits reinforce this balance, ensuring that new features meet strict security standards.By addressing diverse customer requirements while maintaining robust safety measures, we deliver solutions that meet both rapid deployment goals and trust expectations. This approach is especially critical in regulated industries, where compliance is non-negotiable.What strategies does your team use to address scalability challenges when implementing Enriched Index?Scalability challenges were addressed using a multi-faceted approach to ensure consistent performance across diverse workloads. Key strategies for addressing scalability included:In-House Solutions: We transitioned from relying on external providers to gain greater control over our infrastructure and resources.Hierarchical Indexing: We organized data into clusters, which reduced computational complexity and improved retrieval efficiency.Parallel Processing Pipelines: We enabled simultaneous request handling without performance degradation.Fallback Mechanisms: We maintained system reliability during peak loads by dynamically rerouting processes.Continuous Monitoring:We adapted to evolving customer demands through real-time optimizations and performance tuning.These strategies allowed the team to scale Enriched Index effectively, meeting enterprise-level demands while maintaining reliability and responsiveness.What ongoing research and development efforts are being undertaken to enhance the capabilities of Enriched Index?Our R&D efforts focus on refining CRM-specific use cases while exploring broader AI applications. Collaboration with pilot customers provides valuable insights into real-world challenges, which inform our iterative development process.One key area of innovation is summarization. We are developing efficient summarization algorithm that doesn’t need LLM to function well. Proprietary in house LLM like TextEVAL also streamlined model evaluations, reducing manual oversight and accelerating improvements.Additionally, we are investigating context-aware query expansions that dynamically adjust the retrieval query based on query complexity and the index’s richness. These efforts ensure that Enriched Index remains at the forefront of AI retrieval technologies, delivering practical solutions that evolve with customer needs and industry trends.Robert dives deeper into how Salesforce engineers innovate.What measures are in place to ensure the ethical use of Enriched Index, particularly regarding data privacy and bias mitigation?Ethical considerations are central to our approach. Attribute-Based Access Control (ABAC) ensures that derived data adheres to the visibility permissions of its source materials, safeguarding against unintended data exposure during aggregation.Bias mitigation is another key focus area. We train models using diverse datasets and incorporate fairness algorithms to reduce systemic biases. Regular audits evaluate compliance with ethical guidelines and regulatory standards, ensuring our systems meet customer expectations.To prevent premature risks, features like cross-document summarization are deferred until visibility controls are fully refined. By taking a cautious, deliberate approach, we uphold data privacy and ethical standards while delivering high-quality results.Can you share a case study or example where Enriched Index significantly improved a process or outcome?Enriched index has shown its potential in the banking sector, where legal document processing often involves complex semantic distinctions. Traditional semantic search systems frequently struggled to differentiate between similar legal terms, leading to irrelevant or incomplete results.By leveraging metadata enrichment and chunk-based retrieval, Enriched index accurately distinguished nuanced legal concepts. This capability enhanced the efficiency of information retrieval, reducing the burden on manual processes and enabling faster decision-making. The deployment highlighted the platform’s ability to address domain-specific challenges with precision, making it an invaluable tool for industries that require highly accurate, context-aware information retrieval.Learn moreStay connected — join ourTalent Community!Check out ourTechnology and Productteams to learn how you can get involved.

In our “Engineering Energizers” Q&A series, we explore the stories of engineering innovators transforming the tech landscape. Today, we spotlight Robert Xue, a software engineering architect at Salesforce who is spearheading the development of Enriched Index – an advanced Retrieval-Augmented Generation (RAG) system that improves information retrieval with enhanced precision and scalability.

Discover how Robert’s team creates dynamic retrieval systems that balance precision and speed by adjusting query complexity, uses hierarchical indexing and parallel processing to manage growing data demands, and implements strong encryption and compliance measures to ensure trust and security.

What is your team’s mission as it relates to Enriched Index?

Our mission is to provide scalable, reusable components for Large Language Model (LLM) applications, enabling developers to create adaptable and efficient solutions. By emphasizing modularity, we aim to help organizations address complex challenges without starting from scratch.

How Enriched Index Differs from Traditional RAG Index:Multi-round Indexing:Enriches data with contextual metadata to ensure retrieved information is complete and relevant.Dynamic, Context-Aware Retrieval:Transforms static information retrieval into an adaptable, scalable system capable of handling complex queries.

How Enriched Index Differs from Traditional RAG Index:

Multi-round Indexing:Enriches data with contextual metadata to ensure retrieved information is complete and relevant.

Dynamic, Context-Aware Retrieval:Transforms static information retrieval into an adaptable, scalable system capable of handling complex queries.

These advancements reduce preprocessing requirements and streamline workflows, making Enriched Index ideal for both sophisticated enterprise solutions and general AI-driven applications.

Robert dives into Salesforce’s innovation process.

What was the most significant technical challenge your team faced while developing Enriched Index?

The most significant challenge was balancing feature value with computational efficiency. For example, knowledge graphs offered advanced query resolution but came with substantial infrastructure demands. While valuable for complex use cases, they were often unnecessary for simpler queries, making feature prioritization crucial.

To address this, we focused on metadata augmentation and summarization techniques. Features like RAPTOR Summarization improved data organization by creating enriched representations of source material, enhancing retrieval accuracy and efficiency without overburdening system resources.

Pilot programs were essential in refining our approach. By testing real-world scenarios with customers, we validated the impact of our solutions and aligned them with user needs. This iterative process ensured that we prioritized practical advancements, delivering balanced performance and laying the groundwork for future innovations.

What unexpected technical hurdle did your team encounter with Enriched Index?

One unexpected hurdle was latency. Advanced features like query expansion and augmented retrieval algorithms significantly improved accuracy but introduced delays that frustrated users. Balancing precision and responsiveness required innovative solutions.

To tackle this, we developed a dual-path system. High-complexity queries were routed through advanced algorithms, while simpler queries used lightweight retrieval algorithm optimized for speed. This ensured quick responses without compromising the quality of results for complex tasks.

Operationally, standardizing inputs from diverse data sources was another challenge. Many external systems lacked consistent metadata, complicating preprocessing. We addressed this by implementing intermediary normalization layers that standardized data before indexing. These solutions not only resolved latency and compatibility issues but also enhanced overall system performance, ensuring a seamless user experience across various workloads.

How Enriched Index enhanced RAG in Salesforce.

How does your team balance the need for rapid deployment with maintaining high standards of trust and security?

Balancing speed and security involves a dual approach. For customers who need control, we offer “bring-your-own-model” capabilities, allowing them to integrate LLMs tailored to their compliance needs. For other customers, we provide curated models trained on vetted datasets, ensuring high reliability right out of the box.

Our infrastructure uses multi-layered encryption and stringent access controls to protect data during processing. We also maintain transparency by documenting deployment pipelines and security protocols, which empowers developers to audit and customize solutions with confidence.

Continuous monitoring and regular audits reinforce this balance, ensuring that new features meet strict security standards.By addressing diverse customer requirements while maintaining robust safety measures, we deliver solutions that meet both rapid deployment goals and trust expectations. This approach is especially critical in regulated industries, where compliance is non-negotiable.

What strategies does your team use to address scalability challenges when implementing Enriched Index?

Scalability challenges were addressed using a multi-faceted approach to ensure consistent performance across diverse workloads. Key strategies for addressing scalability included:In-House Solutions: We transitioned from relying on external providers to gain greater control over our infrastructure and resources.Hierarchical Indexing: We organized data into clusters, which reduced computational complexity and improved retrieval efficiency.Parallel Processing Pipelines: We enabled simultaneous request handling without performance degradation.Fallback Mechanisms: We maintained system reliability during peak loads by dynamically rerouting processes.Continuous Monitoring:We adapted to evolving customer demands through real-time optimizations and performance tuning.

Scalability challenges were addressed using a multi-faceted approach to ensure consistent performance across diverse workloads. Key strategies for addressing scalability included:

In-House Solutions: We transitioned from relying on external providers to gain greater control over our infrastructure and resources.

Hierarchical Indexing: We organized data into clusters, which reduced computational complexity and improved retrieval efficiency.

Parallel Processing Pipelines: We enabled simultaneous request handling without performance degradation.

Fallback Mechanisms: We maintained system reliability during peak loads by dynamically rerouting processes.

Continuous Monitoring:We adapted to evolving customer demands through real-time optimizations and performance tuning.

These strategies allowed the team to scale Enriched Index effectively, meeting enterprise-level demands while maintaining reliability and responsiveness.

What ongoing research and development efforts are being undertaken to enhance the capabilities of Enriched Index?

Our R&D efforts focus on refining CRM-specific use cases while exploring broader AI applications. Collaboration with pilot customers provides valuable insights into real-world challenges, which inform our iterative development process.

One key area of innovation is summarization. We are developing efficient summarization algorithm that doesn’t need LLM to function well. Proprietary in house LLM like TextEVAL also streamlined model evaluations, reducing manual oversight and accelerating improvements.

Additionally, we are investigating context-aware query expansions that dynamically adjust the retrieval query based on query complexity and the index’s richness. These efforts ensure that Enriched Index remains at the forefront of AI retrieval technologies, delivering practical solutions that evolve with customer needs and industry trends.

Robert dives deeper into how Salesforce engineers innovate.

What measures are in place to ensure the ethical use of Enriched Index, particularly regarding data privacy and bias mitigation?

Ethical considerations are central to our approach. Attribute-Based Access Control (ABAC) ensures that derived data adheres to the visibility permissions of its source materials, safeguarding against unintended data exposure during aggregation.

Bias mitigation is another key focus area. We train models using diverse datasets and incorporate fairness algorithms to reduce systemic biases. Regular audits evaluate compliance with ethical guidelines and regulatory standards, ensuring our systems meet customer expectations.

To prevent premature risks, features like cross-document summarization are deferred until visibility controls are fully refined. By taking a cautious, deliberate approach, we uphold data privacy and ethical standards while delivering high-quality results.

Can you share a case study or example where Enriched Index significantly improved a process or outcome?

Enriched index has shown its potential in the banking sector, where legal document processing often involves complex semantic distinctions. Traditional semantic search systems frequently struggled to differentiate between similar legal terms, leading to irrelevant or incomplete results.

By leveraging metadata enrichment and chunk-based retrieval, Enriched index accurately distinguished nuanced legal concepts. This capability enhanced the efficiency of information retrieval, reducing the burden on manual processes and enabling faster decision-making. The deployment highlighted the platform’s ability to address domain-specific challenges with precision, making it an invaluable tool for industries that require highly accurate, context-aware information retrieval.

Learn moreStay connected — join ourTalent Community!Check out ourTechnology and Productteams to learn how you can get involved.

Stay connected — join ourTalent Community!

Check out ourTechnology and Productteams to learn how you can get involved.

Artificial IntelligenceUnveiling the AI Architecture Powering 435 Million Monthly Knowledge Articles for Scalable Customer SupportShreya AggarwalDec 18						-
						6 min readArtificial IntelligenceScaling AI Systems: Secrets for Managing 100,000 Training and Metadata Requests Per MinuteRama RamanDec 17						-
						7 min readArtificial IntelligenceEngineering AI-Driven Recommendations: How Real-Time Personalization Powers Smarter, More Meaningful Customer EngagementSneha SinglaDec 16						-
						6 min readArtificial IntelligenceInside the Brain of Agentforce: Revealing the Atlas Reasoning EnginePhil MuiDec 10						-
						7 min read

Artificial IntelligenceUnveiling the AI Architecture Powering 435 Million Monthly Knowledge Articles for Scalable Customer SupportShreya AggarwalDec 18						-
						6 min readArtificial IntelligenceScaling AI Systems: Secrets for Managing 100,000 Training and Metadata Requests Per MinuteRama RamanDec 17						-
						7 min readArtificial IntelligenceEngineering AI-Driven Recommendations: How Real-Time Personalization Powers Smarter, More Meaningful Customer EngagementSneha SinglaDec 16						-
						6 min readArtificial IntelligenceInside the Brain of Agentforce: Revealing the Atlas Reasoning EnginePhil MuiDec 10						-
						7 min read

Artificial IntelligenceUnveiling the AI Architecture Powering 435 Million Monthly Knowledge Articles for Scalable Customer SupportShreya AggarwalDec 18						-
						6 min read

Artificial Intelligence

### Unveiling the AI Architecture Powering 435 Million Monthly Knowledge Articles for Scalable Customer Support

Shreya AggarwalDec 18						-
						6 min read

Shreya AggarwalDec 18						-
						6 min read

Dec 18						-
						6 min read

Dec 18						-
						6 min read

Artificial IntelligenceScaling AI Systems: Secrets for Managing 100,000 Training and Metadata Requests Per MinuteRama RamanDec 17						-
						7 min read

Artificial Intelligence

### Scaling AI Systems: Secrets for Managing 100,000 Training and Metadata Requests Per Minute

Rama RamanDec 17						-
						7 min read

Rama RamanDec 17						-
						7 min read

Dec 17						-
						7 min read

Dec 17						-
						7 min read

Artificial IntelligenceEngineering AI-Driven Recommendations: How Real-Time Personalization Powers Smarter, More Meaningful Customer EngagementSneha SinglaDec 16						-
						6 min read

Artificial Intelligence

### Engineering AI-Driven Recommendations: How Real-Time Personalization Powers Smarter, More Meaningful Customer Engagement

Sneha SinglaDec 16						-
						6 min read

Sneha SinglaDec 16						-
						6 min read

Dec 16						-
						6 min read

Dec 16						-
						6 min read

Artificial IntelligenceInside the Brain of Agentforce: Revealing the Atlas Reasoning EnginePhil MuiDec 10						-
						7 min read

Artificial Intelligence

### Inside the Brain of Agentforce: Revealing the Atlas Reasoning Engine

Phil MuiDec 10						-
						7 min read

Phil MuiDec 10						-
						7 min read

Dec 10						-
						7 min read

Dec 10						-
						7 min read

