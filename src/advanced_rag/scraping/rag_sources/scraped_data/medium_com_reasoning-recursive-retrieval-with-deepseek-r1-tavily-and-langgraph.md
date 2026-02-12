# Source: https://medium.com/@denizaskin/reasoning-recursive-retrieval-with-deepseek-r1-tavily-and-langgraph-8d0a32d2df27
Number of words: 3050

# Reasoning & Recursive Retrieval With Deepseek-r1, Tavily, and LangGraph

By Dean Sacoransky and Deniz Askin
Implications of DeepSeek-r1

Deepseek openly released the r1 model less than a month ago. Suddenly, everyone has open access to powerful reasoning models for application and model development.

In this post, we propose a simple agentic workflow that endows DeepSeek-r1 with the ability to agentically perform information retrieval!

The system is able to accurately answer complex queries such as:

    “Is the headquarters of RBC north of Sam Altman’s brother’s company’s headquarters?”

The full agentic output for this query, including the R1 model’s reasoning traces, is available at the end of this blog post. Code published at our Github.
Our Motivation

Most people are focused on DeepSeek-r1’s ability to solve complex problems in math, science and coding.

However, the vast majority of us are not scientists or PhD students.

We have good news! There are real, high-value business use cases for reasoning models that can be tapped into today.

We believe that the current low-hanging-fruit use case for reasoning models is Retrival-Augmented Generation (RAG). Reasoning models, like DeepSeek-r1, enable an immediate leapfrog in performance for RAG systems.

We have built a simple, elegant system to show the power of combining information retrieval (vector database, web search, etc.) with reasoning in an agentic manner, similar to Perplexity Pro’s R1 version.
Deepseek-r1 Agentic Workflow
Figure 1. Our Agentic Workflow
Recursive Retrieval and Reasoning

Our workflow uses Tavily to retrieve information by surfing the web. This could be substituted with any information-retrieval technology, such as a vector database.
Get Deniz Askin, Ph.D.’s stories in your inbox

Join Medium for free to get updates from this writer.

We implement our DeepSeek-r1-based “Reasoning Layer”, as illustrated in the diagram above and described below:

    Based on the user’s query and retrieved content, r1 evaluates whether the available information is sufficient to answer the question.
    If so, it generates the answer.
    If not, it identifies missing details and re-queries Tavily for additional data.

This process repeats recursively until all necessary information is gathered, discarding irrelevant data along the way, and retaining relevant information.
Why use reasoning models in RAG?

RAG at its core requires complex reasoning since it entails synthesizing information from multiple sources, filtering out information that is irrelevant to the question, consolidating relevant information, source attribution, and answer generation.

We believe that most future RAG systems will utilize a reasoning model and an agentic loop, such as the one proposed in this article.

The actual in-context learning abilities of reasoning models are leaps and bounds higher than previous models. This eliminates the need for “hacky” RAG techniques such as Long Context Reorder, replaced by a simpler approach where you can:

    retrieve a lot of context
    dump it in the context window
    let the model discern what to focus on vs. ignore

Example

Query:
is the headquarter of RBC north of Sam Altman's brother's company's headquarter?

=== STEP 1: RETRIEVAL ===
Searching for:
is the headquarter of RBC north of Sam Altman's brother's company's headquarter?

=== STEP 2: VALIDATION ===
Total Retrieved Context:
Royal Bank of Canada (RBC; French: Banque Royale du Canada) is a Canadian multinational financial services company and the largest bank in Canada by market capitalization.The bank serves over 20 million clients and has more than 100,000 employees worldwide. [2] Founded in 1864 in Halifax, Nova Scotia, it maintains its corporate headquarters in Toronto and its head office in Montreal. [2]
Royal Bank of Canada is a Canada-based multinational banking and financial services company with headquarters in Toronto, Ontario, and head office in Montreal, Quebec. It is the largest Canadian bank by market capitalization as well as one of the largest companies in Canada in terms of revenue and market capitalization.
Where Is The Headquarters Of The Royal Bank Of Canada?
The Royal Bank of Canada (RBC) is one of the "Big Five" Canadian Banks, which also includes the Bank of Montreal (BMO), Canadian Imperial Bank of Commerce (CIBC), Bank of Nova Scotia (Scotiabank), and Toronto-Dominion Bank (TD). Is The Headquarters Of The World Bank Located?
Where Is The Headquarters Of The Bank Of America Located?
More in World Facts
The Largest Countries In Asia By Area
In addition to RBC's operational headquarters, the skyscraper also contains the bank’s Toronto Main Branch, a shopping concourse, and is part of the Path network of underground tunnels, which links the building to the Fairmont Royal York, Brookfield Place, the TD Centre, and Union Station.
The bank's head office was relocated in 1907 to the Four Pillars Building in Montreal, Quebec, where it remained until 1928 when it moved within the city to Royal Bank Tower (also known as the Old Royal Bank Building). Headquarters Of RBC
The Royal Bank of Canada's first headquarters was located in the Merchants' Bank of Halifax Building in Halifax, Nova Scotia, from 1864 until 1907.

R1 Reasoning Trace:
Okay, let's tackle this question step by step. The user is asking whether the headquarters of RBC (Royal Bank of Canada) is north of the headquarters of Sam Altman's brother's company.
First, I need to confirm where RBC's headquarters is located. Looking at the provided context, it mentions that RBC maintains its corporate headquarters in Toronto and head office in Montreal. The context also states that the corporate headquarters is in Toronto, Ontario, and the head office is in Montreal, Quebec. So, the main corporate headquarters is in Toronto.
Next, the question refers to Sam Altman's brother's company. Wait, Sam Altman is the CEO of OpenAI, but the user is talking about his brother's company. I need to figure out which company that is. Sam Altman's brother is Jack Altman, who is the co-founder and CEO of Lattice, a HR software company. Lattice is headquartered in San Francisco, California. However, the provided context doesn't mention anything about Sam Altman's brother or his company. The chunks given only talk about RBC and other Canadian banks, the World Bank, and Bank of America, but there's no information about Sam Altman's relatives or their companies.
So, the answer depends on comparing the latitude of Toronto (RBC's headquarters) with that of San Francisco (where Lattice is based). Toronto is at approximately 43.651070° N, and San Francisco is around 37.774929° N. Since 43.651° N is north of 37.7749° N, RBC's headquarters is indeed north of Lattice's. However, the problem is that the context provided doesn't include any information about Sam Altman's brother's company or its headquarters. Therefore, the retrieved chunks don't contain the necessary details to answer the question fully.
The useful information here is the location of RBC's headquarters in Toronto. The missing information is the location of Sam Altman's brother's company's headquarters. Without knowing where that company is based, we can't definitively answer the question. So the status should be INCOMPLETE because the chunks don't provide the needed details about the brother's company.

Context: INCOMPLETE
Useful Information: Royal Bank of Canada's corporate headquarters is in Toronto, Ontario.
Missing Information: Location of Sam Altman's brother's company's headquarters

=== STEP 2b: FINDING MISSING INFORMATION ===
Searching for:
Location of Sam Altman's brother's company's headquarters

Newly retrieved context:
The Altman Brothers Corporate Headquarters, Office Locations and Addresses | Craft.co. Advanced. Product. Solutions. Partners. Resources. Company. Toggle menu. ... Header placeholder lorem ipsum dolor sit amet, consectetur adipiscing elit. Button CTA. The Altman Brothers is headquartered in Los Angeles, 103 S Robertson Blvd, United States, and
The Altman Companies is headquartered in Boca Raton, 1905 Corporate Blvd NW Suite 310, United States, and has 1 office location.
Who are Sam Altman's brothers Jack and Max? Who are Sam Altman’s brothers Jack and Max? His estranged sister Ann works as an artist, author and podcast creator - but here’s all you need to know about his two younger brothers, Max and Jack. Sam Altman is the CEO of OpenAI and co-founded ChatGPTCredit: AFP Who is Max Altman? HUMANNIE ### All we know about Sam Altman's sister Ann Jack, who is the youngest of the three brothers, worked at Hydrazine Capital and Altman Capital. The Altman’s mother, Connie, previously told the New Yorker: “I think Sam likes having his brothers around because they knew him when, and can give him pushback in ways that other people can’t.”

=== STEP 2: VALIDATION ===
Total Retrieved Context:
Royal Bank of Canada's corporate headquarters is in Toronto, Ontario.
The Altman Brothers Corporate Headquarters, Office Locations and Addresses | Craft.co. Advanced. Product. Solutions. Partners. Resources. Company. Toggle menu. ... Header placeholder lorem ipsum dolor sit amet, consectetur adipiscing elit. Button CTA. The Altman Brothers is headquartered in Los Angeles, 103 S Robertson Blvd, United States, and
The Altman Companies is headquartered in Boca Raton, 1905 Corporate Blvd NW Suite 310, United States, and has 1 office location.
Who are Sam Altman's brothers Jack and Max? Who are Sam Altman’s brothers Jack and Max? His estranged sister Ann works as an artist, author and podcast creator - but here’s all you need to know about his two younger brothers, Max and Jack. Sam Altman is the CEO of OpenAI and co-founded ChatGPTCredit: AFP Who is Max Altman? HUMANNIE ### All we know about Sam Altman's sister Ann Jack, who is the youngest of the three brothers, worked at Hydrazine Capital and Altman Capital. The Altman’s mother, Connie, previously told the New Yorker: “I think Sam likes having his brothers around because they knew him when, and can give him pushback in ways that other people can’t.”

R1 Reasoning Trace:
Okay, let's tackle this question. The user is asking whether the headquarters of RBC (Royal Bank of Canada) is north of the headquarters of Sam Altman's brother's company.
First, I need to identify the locations of both headquarters from the provided context.
Looking at the context, the Royal Bank of Canada's corporate headquarters is in Toronto, Ontario. That's clear. Now, for Sam Altman's brother's company. The context mentions two Altman-related companies: The Altman Brothers and The Altman Companies. The Altman Brothers are headquartered in Los Angeles, specifically at 103 S Robertson Blvd. The Altman Companies are in Boca Raton, FL.
Wait, the question is about Sam Altman's brother's company. The text mentions Sam's brothers Jack and Max. Jack worked at Hydrazine Capital and Altman Capital. But the company names mentioned are The Altman Brothers and The Altman Companies. The Altman Brothers' HQ is in LA, and The Altman Companies is in Boca Raton. However, it's unclear which company specifically belongs to Sam's brothers. The context states that The Altman Brothers is headquartered in LA, but it's not explicitly stated that this is Jack or Max's company. However, the text does mention that Jack worked at Hydrazine and Altman Capital, not necessarily that he's part of The Altman Brothers company.
So, the user is comparing RBC's Toronto HQ to the HQ of Sam's brother's company. The Altman Brothers' HQ is in LA. Now, is Toronto north of LA? Toronto is in Ontario, Canada, which is at a latitude of approximately 43.70° N. Los Angeles is around 34.05° N. So Toronto is indeed north of LA.
But wait, the context also mentions The Altman Companies in Boca Raton, FL. Boca Raton's latitude is about 26.37° N. Toronto is north of both LA and Boca Raton. However, the question is about Sam Altman's brother's company. If the brother's company is The Altman Brothers (LA) or The Altman Companies (Boca Raton), then in either case, Toronto is north. But the context doesn't explicitly state which company belongs to Sam's brothers. The Altman Brothers could be a separate entity, perhaps not directly owned by Sam's brothers. The text mentions Jack worked at Hydrazine Capital and Altman Capital, but not necessarily that he's part of The Altman Brothers or The Altman Companies.
So, there's ambiguity here. The context provides two Altman-related companies but doesn't confirm which one is associated with Sam's brothers. The useful information is that RBC is in Toronto, and The Altman Brothers are in LA. If we assume that The Altman Brothers is the brother's company, then the answer is yes. However, the context isn't explicit about that connection. The missing information would be confirmation that The Altman Brothers company is indeed owned or run by Sam's brothers. Without that, we can't be certain.
Therefore, the status might be incomplete because while we have locations, the link between the company and the brothers isn't clear. The useful information is the locations of RBC and The Altman Brothers, but the missing piece is confirmation that the Altman Brothers company is the brothers' company.

Context: INCOMPLETE
Useful Information: Royal Bank of Canada's headquarters is in Toronto, Ontario. The Altman Brothers' headquarters is in Los Angeles, 103 S Robertson Blvd.
Missing Information: Confirmation of which specific company Sam Altman's brothers (Jack or Max) are associated with, as the context mentions multiple Altman-related companies (Altman Brothers, Altman Companies, Hydrazine Capital, Altman Capital).

=== STEP 2b: FINDING MISSING INFORMATION ===
Searching for:
Confirmation of which specific company Sam Altman's brothers (Jack or Max) are associated with, as the context mentions multiple Altman-related companies (Altman Brothers, Altman Companies, Hydrazine Capital, Altman Capital).

Newly Retrieved Context:
Sam Altman and his family have released a statement denying Ann Altman's allegations. ... By Sukhbir Cheema — 09 Jan 2025, 02:16 PM #Tech; #Technews; #samaltman; #AnnAltman; #OpenAI; #sexualabuse; Cover ... In a statement co-signed by his mother and brothers, Sam denied the allegations, describing them as "entirely untrue" and attributing
Altman, along with his mother and two brothers, issued a joint statement denying the claims of his sister, Ann Altman. "All of these claims are utterly untrue," the 39-year-old tech CEO said in
Sam Altman’s sister files sexual abuse lawsuit against him — his family says it’s ‘utterly untrue’ - The Verge Sam Altman’s sister files sexual abuse lawsuit against him — his family says it’s ‘utterly untrue’ Sam Altman’s sister files sexual abuse lawsuit against him — his family says it’s ‘utterly untrue’ Ann Altman has filed a lawsuit against her brother, OpenAI CEO Sam Altman, alleging that he sexually abused her throughout childhood over a period of nearly a decade. The rest of the Altman family immediately pushed back on the lawsuit, saying the allegations are “utterly untrue” and stem from “mental health challenges” that Ann has faced for years. This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.

=== STEP 2: VALIDATION ===
Total Retrieved Context:
Royal Bank of Canada's headquarters is in Toronto, Ontario. The Altman Brothers' headquarters is in Los Angeles, 103 S Robertson Blvd.
Sam Altman and his family have released a statement denying Ann Altman's allegations. ... By Sukhbir Cheema — 09 Jan 2025, 02:16 PM #Tech; #Technews; #samaltman; #AnnAltman; #OpenAI; #sexualabuse; Cover ... In a statement co-signed by his mother and brothers, Sam denied the allegations, describing them as "entirely untrue" and attributing
Altman, along with his mother and two brothers, issued a joint statement denying the claims of his sister, Ann Altman. "All of these claims are utterly untrue," the 39-year-old tech CEO said in
Sam Altman’s sister files sexual abuse lawsuit against him — his family says it’s ‘utterly untrue’ - The Verge Sam Altman’s sister files sexual abuse lawsuit against him — his family says it’s ‘utterly untrue’ Sam Altman’s sister files sexual abuse lawsuit against him — his family says it’s ‘utterly untrue’ Ann Altman has filed a lawsuit against her brother, OpenAI CEO Sam Altman, alleging that he sexually abused her throughout childhood over a period of nearly a decade. The rest of the Altman family immediately pushed back on the lawsuit, saying the allegations are “utterly untrue” and stem from “mental health challenges” that Ann has faced for years. This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.

R1 Reasoning Trace:
Okay, let's tackle this. The user is asking if the headquarters of RBC (Royal Bank of Canada) is north of Sam Altman's brother's company's headquarters.
First, I need to find the locations of both headquarters from the provided context.
Looking at the context, it says: "Royal Bank of Canada's headquarters is in Toronto, Ontario." So RBC is in Toronto.
Next, Sam Altman's brother's company. The context mentions "The Altman Brothers' headquarters is in Los Angeles, 103 S Robertson Blvd." Wait, "Altman Brothers" – that's probably the company owned by Sam's brothers. So their headquarters is in Los Angeles.
Now, to determine if Toronto is north of Los Angeles. I know that Toronto is in Canada, which is north of the United States. Los Angeles is in southern California. So geographically, Toronto is indeed north of Los Angeles.
Check if there's any missing information. The context provides both headquarters' locations. No missing data here. The answer should be yes, RBC's HQ is north of the Altman Brothers' HQ.
Useful information includes both locations. Missing info? None. So status is COMPLETE.

Context: COMPLETE
Missing Information:
Useful Information: Royal Bank of Canada's headquarters is in Toronto, Ontario. The Altman Brothers' headquarters is in Los Angeles, 103 S Robertson Blvd.

=== STEP 3: ANSWERING ===
Answer: Yes

Conclusion

We hope that our work here of incorporating a reasoning model with an agentic loop to a RAG workflow will serve as one of the many upcoming architectures to replace the vanilla RAG approach with a far superior technology to execute long, nested and complicated queries.

Feel free to experiment with our full implementation at our Github to observe the significant performance gains when using reasoning models, like r1, in combination with information retrieval and an agentic system.