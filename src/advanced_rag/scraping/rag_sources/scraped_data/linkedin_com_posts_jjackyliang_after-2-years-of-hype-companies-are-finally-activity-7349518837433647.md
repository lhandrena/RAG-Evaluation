# Source: https://www.linkedin.com/posts/jjackyliang_after-2-years-of-hype-companies-are-finally-activity-7349518837433647106-KZh6?utm_source=share&utm_medium=member_desktop&rcm=ACoAABL4hZgBRj0FruXwN4L4sqpnAkE7UqKimTo

# Vector search hype is over: Claude Code beats Cursor | 🤖 Jacky Liang posted on the topic | LinkedIn

Vector search hype is over: Claude Code beats CursorThis title was summarized by AI from the post below.🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3moReport this postAfter 2 years of hype, companies are finally realizing vector search doesn't solve everything. The 2023 investment peak is over, and the downturn is brutal.

The core problem: similarity != relevance

When you search for getUserById(), you need that exact function. Not findUserByEmail() or updateUserProfile(). Vector search gives you "semantically similar" - which is completely useless for code.

Same with part numbers, SKUs, or any identifier. "P/N 4B0-959-855-A" isn't meaningful text - it's a reference. Vector search returning "4B0-959-855-B" will cost you real money.

Case in point: Claude Code is eating Cursor's lunch

While Cursor forces you to manually tag files with @ symbols, Claude Code finds the right context automatically using good old grep - a 50-year-old utility that actually works. 

Biggest tell that Cursor is feeling the heat? Cursor just hired two Claude Code leads (Boris and Cat). They see the writing on the wall.

Things to takeaway from this: 
- AI isn't about fancy vector databases. It's just search. And sometimes the oldest tools are still the best.
- Stop defaulting to "AI = vector database." Choose the right tool for the job:
Code search? Lexical matching
- Intent understanding? Semantic similarity
- E-commerce? Both

The industry is finally growing up. One-size-fits-all solutions are dead. 

Full blog in comments.86980 CommentsLikeComment🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3moReport this commentWhy Claude Code is eating Cursor's lunch:https://www.tigerdata.com/blog/why-cursor-is-about-to-ditch-vector-search-and-you-should-tooLikeReply6 Reactions7 ReactionsDaniel SvonavaBuild better AI Search with Superlinked | xYouTube3moReport this commentYou are doing vector search wrong :-)LikeReply24 Reactions25 ReactionsChidhambararajan R (a.k.a Chidha)Software Engineer II - AI at JP Morgan | The Tech Buddha Podcast Host3moReport this commentVector search should not be used for lexical similarity, it's extremely inefficient and not recommended for lexical similarity

It should be used for semantic similarity

Eg: in vector similarity 
Sentence A: boat has sailed the river
Sentence B: ship is crossing the river
Sentence C: I am shipping the goods to you

A and B similarity is higher than B, C

VECTOR SEARCH IS REQUIRED IN SCENARIOS where semantic search is prefered over lexical search

And rag is not search, it's summarisation over your search
"Retrieval (any search here) Augmented Generation)"LikeReply7 Reactions8 ReactionsVilhelm von EhrenheimCo-Founder & Chief AI Officer @ QA.tech | ex EQT Motherbrain, Klarna3moReport this commentI think this post shows a lack of understanding what vectors are and how you should use them. Why would anyone use vector search to find exact match on identifiers? That makes no sense. 
However if you do need to search in a vector space vector databases are amazing. I have used them for a multitude of production usecases since long before any of this hype. There is a lot of usecases where similarity is a great approximation of relevance. If not you need to learn another representation. 
And there is no such thing as “Just search”. Search is a hard, multifaceted problem that usually needs more thought than just using off the shelf similarity or hard coded matches. Call me a midwit for all I care.LikeReply40 Reactions41 ReactionsQdrant3moReport this comment1️⃣ Vector Databases are, actually, Search Engines. ➡️  Thanks toGreg Koganfor the cool trend name, which introduced this mega confusion. 🤓   
2️⃣ You compare apples to oranges:  ➡️ "Forget about fancy boats, you cannot drive them on the roads." 🤷
3️⃣ See 1️⃣ 🤗LikeReply16 Reactions17 ReactionsBora Celik3moReport this commentgotta choose the right tool for the job innit? same way as awesome as my timescale db is it cannot answer the "give me the best matching influencer for this brand" question that pinecone is answering like a champion ;)LikeReply5 Reactions6 ReactionsLeo (Leonid) Boytsov3moReport this commentAgree on the failure of one size fits all solutions. Now try to use lexical search to find a function by its somewhat abstract description. Lexical search without query or document expansion fails here. Regarding grepping stuff: you need to know when a query is navigational. It's not so simple as: use vector or lexical search for everything.LikeReply9 Reactions10 ReactionsHenry WellerSenior Product Manager, Vector Search at MongoDB3moReport this commentInteresting read! Despite the title I think at the end of your article you position vectors + lexical/grep as a yes/and situation. the same things you might fail to find with keyword search might turn up with vector search, grep or otherwise.

Framing of ai apps = vector isn’t helpful (any db not providing hybrid search in 2025 is foolish) but this critique also applies to the framing of codeRAG is dead/ grep is all you need. Wish someone would put out some hard NDCG numbers around this but until then that’s my take on the other sideLikeReply4 Reactions5 ReactionsReisel González PérezSr. Solution Engineer @Microsoft | Cloud & AI3moReport this commentLaw of the instrument: "...if all you have is a hammer, everything looks like a nail". It's more about the use cases' nature understanding than the technology capabilities. Plus, a lot of misunderstanding around what is a deterministic, or a non deterministic problem.LikeReply3 Reactions4 ReactionsDevansh DevanshChocolate Milk Cult Leader| Machine Learning Engineer| Writer | AI Researcher| | Computational Math, Data Science, Software Engineering, Computer Science3moReport this commentThere’s a reason Claude Code is nibbling at Cursor’s market share, so much that they literally hired the Claude Code team—it’s all in its search. - is there any validation for that? 

When I did my Deep dive on cursor and the various security issues it had for Enterprise development, one of the key issues that we identified in our analysis was that cursor mismanaged context very inappropriately when compared to augment or Claude Code. 

My speculation for why that was the case was that cursor's team fundamentally is not very very knowledgeable about AI which was something I based on things I knew and also again the issues they were having. Which is why they were using very naive techniques.LikeReply2 Reactions3 ReactionsSee more commentsTo view or add a comment,sign in

# Vector search hype is over: Claude Code beats Cursor

This title was summarized by AI from the post below.

This title was summarized by AI from the post below.

🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3moReport this post

🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3mo

🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3mo

🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3mo

✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)

After 2 years of hype, companies are finally realizing vector search doesn't solve everything. The 2023 investment peak is over, and the downturn is brutal.

The core problem: similarity != relevance

When you search for getUserById(), you need that exact function. Not findUserByEmail() or updateUserProfile(). Vector search gives you "semantically similar" - which is completely useless for code.

Same with part numbers, SKUs, or any identifier. "P/N 4B0-959-855-A" isn't meaningful text - it's a reference. Vector search returning "4B0-959-855-B" will cost you real money.

Case in point: Claude Code is eating Cursor's lunch

While Cursor forces you to manually tag files with @ symbols, Claude Code finds the right context automatically using good old grep - a 50-year-old utility that actually works. 

Biggest tell that Cursor is feeling the heat? Cursor just hired two Claude Code leads (Boris and Cat). They see the writing on the wall.

Things to takeaway from this: 
- AI isn't about fancy vector databases. It's just search. And sometimes the oldest tools are still the best.
- Stop defaulting to "AI = vector database." Choose the right tool for the job:
Code search? Lexical matching
- Intent understanding? Semantic similarity
- E-commerce? Both

The industry is finally growing up. One-size-fits-all solutions are dead. 

Full blog in comments.

After 2 years of hype, companies are finally realizing vector search doesn't solve everything. The 2023 investment peak is over, and the downturn is brutal.

The core problem: similarity != relevance

When you search for getUserById(), you need that exact function. Not findUserByEmail() or updateUserProfile(). Vector search gives you "semantically similar" - which is completely useless for code.

Same with part numbers, SKUs, or any identifier. "P/N 4B0-959-855-A" isn't meaningful text - it's a reference. Vector search returning "4B0-959-855-B" will cost you real money.

Case in point: Claude Code is eating Cursor's lunch

While Cursor forces you to manually tag files with @ symbols, Claude Code finds the right context automatically using good old grep - a 50-year-old utility that actually works. 

Biggest tell that Cursor is feeling the heat? Cursor just hired two Claude Code leads (Boris and Cat). They see the writing on the wall.

Things to takeaway from this: 
- AI isn't about fancy vector databases. It's just search. And sometimes the oldest tools are still the best.
- Stop defaulting to "AI = vector database." Choose the right tool for the job:
Code search? Lexical matching
- Intent understanding? Semantic similarity
- E-commerce? Both

The industry is finally growing up. One-size-fits-all solutions are dead. 

Full blog in comments.

🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3moReport this commentWhy Claude Code is eating Cursor's lunch:https://www.tigerdata.com/blog/why-cursor-is-about-to-ditch-vector-search-and-you-should-tooLikeReply6 Reactions7 Reactions

🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3moReport this commentWhy Claude Code is eating Cursor's lunch:https://www.tigerdata.com/blog/why-cursor-is-about-to-ditch-vector-search-and-you-should-too

🤖 Jacky Liang✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)3moReport this comment

✍🏻 always learning // ai @ tigerdata && founder answerhq.co // pinecone, oracle cloud, singlestore, looker (acq. google)

Why Claude Code is eating Cursor's lunch:https://www.tigerdata.com/blog/why-cursor-is-about-to-ditch-vector-search-and-you-should-too

Why Claude Code is eating Cursor's lunch:https://www.tigerdata.com/blog/why-cursor-is-about-to-ditch-vector-search-and-you-should-too

LikeReply6 Reactions7 Reactions

Daniel SvonavaBuild better AI Search with Superlinked | xYouTube3moReport this commentYou are doing vector search wrong :-)LikeReply24 Reactions25 Reactions

Daniel SvonavaBuild better AI Search with Superlinked | xYouTube3moReport this commentYou are doing vector search wrong :-)

Daniel SvonavaBuild better AI Search with Superlinked | xYouTube3moReport this comment

Build better AI Search with Superlinked | xYouTube

You are doing vector search wrong :-)

You are doing vector search wrong :-)

LikeReply24 Reactions25 Reactions

Chidhambararajan R (a.k.a Chidha)Software Engineer II - AI at JP Morgan | The Tech Buddha Podcast Host3moReport this commentVector search should not be used for lexical similarity, it's extremely inefficient and not recommended for lexical similarity

It should be used for semantic similarity

Eg: in vector similarity 
Sentence A: boat has sailed the river
Sentence B: ship is crossing the river
Sentence C: I am shipping the goods to you

A and B similarity is higher than B, C

VECTOR SEARCH IS REQUIRED IN SCENARIOS where semantic search is prefered over lexical search

And rag is not search, it's summarisation over your search
"Retrieval (any search here) Augmented Generation)"LikeReply7 Reactions8 Reactions

Chidhambararajan R (a.k.a Chidha)Software Engineer II - AI at JP Morgan | The Tech Buddha Podcast Host3moReport this commentVector search should not be used for lexical similarity, it's extremely inefficient and not recommended for lexical similarity

It should be used for semantic similarity

Eg: in vector similarity 
Sentence A: boat has sailed the river
Sentence B: ship is crossing the river
Sentence C: I am shipping the goods to you

A and B similarity is higher than B, C

VECTOR SEARCH IS REQUIRED IN SCENARIOS where semantic search is prefered over lexical search

And rag is not search, it's summarisation over your search
"Retrieval (any search here) Augmented Generation)"

Chidhambararajan R (a.k.a Chidha)Software Engineer II - AI at JP Morgan | The Tech Buddha Podcast Host3moReport this comment

Software Engineer II - AI at JP Morgan | The Tech Buddha Podcast Host

Vector search should not be used for lexical similarity, it's extremely inefficient and not recommended for lexical similarity

It should be used for semantic similarity

Eg: in vector similarity 
Sentence A: boat has sailed the river
Sentence B: ship is crossing the river
Sentence C: I am shipping the goods to you

A and B similarity is higher than B, C

VECTOR SEARCH IS REQUIRED IN SCENARIOS where semantic search is prefered over lexical search

And rag is not search, it's summarisation over your search
"Retrieval (any search here) Augmented Generation)"

Vector search should not be used for lexical similarity, it's extremely inefficient and not recommended for lexical similarity

It should be used for semantic similarity

Eg: in vector similarity 
Sentence A: boat has sailed the river
Sentence B: ship is crossing the river
Sentence C: I am shipping the goods to you

A and B similarity is higher than B, C

VECTOR SEARCH IS REQUIRED IN SCENARIOS where semantic search is prefered over lexical search

And rag is not search, it's summarisation over your search
"Retrieval (any search here) Augmented Generation)"

LikeReply7 Reactions8 Reactions

Vilhelm von EhrenheimCo-Founder & Chief AI Officer @ QA.tech | ex EQT Motherbrain, Klarna3moReport this commentI think this post shows a lack of understanding what vectors are and how you should use them. Why would anyone use vector search to find exact match on identifiers? That makes no sense. 
However if you do need to search in a vector space vector databases are amazing. I have used them for a multitude of production usecases since long before any of this hype. There is a lot of usecases where similarity is a great approximation of relevance. If not you need to learn another representation. 
And there is no such thing as “Just search”. Search is a hard, multifaceted problem that usually needs more thought than just using off the shelf similarity or hard coded matches. Call me a midwit for all I care.LikeReply40 Reactions41 Reactions

Vilhelm von EhrenheimCo-Founder & Chief AI Officer @ QA.tech | ex EQT Motherbrain, Klarna3moReport this commentI think this post shows a lack of understanding what vectors are and how you should use them. Why would anyone use vector search to find exact match on identifiers? That makes no sense. 
However if you do need to search in a vector space vector databases are amazing. I have used them for a multitude of production usecases since long before any of this hype. There is a lot of usecases where similarity is a great approximation of relevance. If not you need to learn another representation. 
And there is no such thing as “Just search”. Search is a hard, multifaceted problem that usually needs more thought than just using off the shelf similarity or hard coded matches. Call me a midwit for all I care.

Vilhelm von EhrenheimCo-Founder & Chief AI Officer @ QA.tech | ex EQT Motherbrain, Klarna3moReport this comment

Co-Founder & Chief AI Officer @ QA.tech | ex EQT Motherbrain, Klarna

I think this post shows a lack of understanding what vectors are and how you should use them. Why would anyone use vector search to find exact match on identifiers? That makes no sense. 
However if you do need to search in a vector space vector databases are amazing. I have used them for a multitude of production usecases since long before any of this hype. There is a lot of usecases where similarity is a great approximation of relevance. If not you need to learn another representation. 
And there is no such thing as “Just search”. Search is a hard, multifaceted problem that usually needs more thought than just using off the shelf similarity or hard coded matches. Call me a midwit for all I care.

I think this post shows a lack of understanding what vectors are and how you should use them. Why would anyone use vector search to find exact match on identifiers? That makes no sense. 
However if you do need to search in a vector space vector databases are amazing. I have used them for a multitude of production usecases since long before any of this hype. There is a lot of usecases where similarity is a great approximation of relevance. If not you need to learn another representation. 
And there is no such thing as “Just search”. Search is a hard, multifaceted problem that usually needs more thought than just using off the shelf similarity or hard coded matches. Call me a midwit for all I care.

LikeReply40 Reactions41 Reactions

Qdrant3moReport this comment1️⃣ Vector Databases are, actually, Search Engines. ➡️  Thanks toGreg Koganfor the cool trend name, which introduced this mega confusion. 🤓   
2️⃣ You compare apples to oranges:  ➡️ "Forget about fancy boats, you cannot drive them on the roads." 🤷
3️⃣ See 1️⃣ 🤗LikeReply16 Reactions17 Reactions

Qdrant3moReport this comment1️⃣ Vector Databases are, actually, Search Engines. ➡️  Thanks toGreg Koganfor the cool trend name, which introduced this mega confusion. 🤓   
2️⃣ You compare apples to oranges:  ➡️ "Forget about fancy boats, you cannot drive them on the roads." 🤷
3️⃣ See 1️⃣ 🤗

Qdrant3moReport this comment

1️⃣ Vector Databases are, actually, Search Engines. ➡️  Thanks toGreg Koganfor the cool trend name, which introduced this mega confusion. 🤓   
2️⃣ You compare apples to oranges:  ➡️ "Forget about fancy boats, you cannot drive them on the roads." 🤷
3️⃣ See 1️⃣ 🤗

1️⃣ Vector Databases are, actually, Search Engines. ➡️  Thanks toGreg Koganfor the cool trend name, which introduced this mega confusion. 🤓   
2️⃣ You compare apples to oranges:  ➡️ "Forget about fancy boats, you cannot drive them on the roads." 🤷
3️⃣ See 1️⃣ 🤗

LikeReply16 Reactions17 Reactions

Bora Celik3moReport this commentgotta choose the right tool for the job innit? same way as awesome as my timescale db is it cannot answer the "give me the best matching influencer for this brand" question that pinecone is answering like a champion ;)LikeReply5 Reactions6 Reactions

Bora Celik3moReport this commentgotta choose the right tool for the job innit? same way as awesome as my timescale db is it cannot answer the "give me the best matching influencer for this brand" question that pinecone is answering like a champion ;)

Bora Celik3moReport this comment

gotta choose the right tool for the job innit? same way as awesome as my timescale db is it cannot answer the "give me the best matching influencer for this brand" question that pinecone is answering like a champion ;)

gotta choose the right tool for the job innit? same way as awesome as my timescale db is it cannot answer the "give me the best matching influencer for this brand" question that pinecone is answering like a champion ;)

LikeReply5 Reactions6 Reactions

Leo (Leonid) Boytsov3moReport this commentAgree on the failure of one size fits all solutions. Now try to use lexical search to find a function by its somewhat abstract description. Lexical search without query or document expansion fails here. Regarding grepping stuff: you need to know when a query is navigational. It's not so simple as: use vector or lexical search for everything.LikeReply9 Reactions10 Reactions

Leo (Leonid) Boytsov3moReport this commentAgree on the failure of one size fits all solutions. Now try to use lexical search to find a function by its somewhat abstract description. Lexical search without query or document expansion fails here. Regarding grepping stuff: you need to know when a query is navigational. It's not so simple as: use vector or lexical search for everything.

Leo (Leonid) Boytsov3moReport this comment

Agree on the failure of one size fits all solutions. Now try to use lexical search to find a function by its somewhat abstract description. Lexical search without query or document expansion fails here. Regarding grepping stuff: you need to know when a query is navigational. It's not so simple as: use vector or lexical search for everything.

Agree on the failure of one size fits all solutions. Now try to use lexical search to find a function by its somewhat abstract description. Lexical search without query or document expansion fails here. Regarding grepping stuff: you need to know when a query is navigational. It's not so simple as: use vector or lexical search for everything.

LikeReply9 Reactions10 Reactions

Henry WellerSenior Product Manager, Vector Search at MongoDB3moReport this commentInteresting read! Despite the title I think at the end of your article you position vectors + lexical/grep as a yes/and situation. the same things you might fail to find with keyword search might turn up with vector search, grep or otherwise.

Framing of ai apps = vector isn’t helpful (any db not providing hybrid search in 2025 is foolish) but this critique also applies to the framing of codeRAG is dead/ grep is all you need. Wish someone would put out some hard NDCG numbers around this but until then that’s my take on the other sideLikeReply4 Reactions5 Reactions

Henry WellerSenior Product Manager, Vector Search at MongoDB3moReport this commentInteresting read! Despite the title I think at the end of your article you position vectors + lexical/grep as a yes/and situation. the same things you might fail to find with keyword search might turn up with vector search, grep or otherwise.

Framing of ai apps = vector isn’t helpful (any db not providing hybrid search in 2025 is foolish) but this critique also applies to the framing of codeRAG is dead/ grep is all you need. Wish someone would put out some hard NDCG numbers around this but until then that’s my take on the other side

Henry WellerSenior Product Manager, Vector Search at MongoDB3moReport this comment

Senior Product Manager, Vector Search at MongoDB

Interesting read! Despite the title I think at the end of your article you position vectors + lexical/grep as a yes/and situation. the same things you might fail to find with keyword search might turn up with vector search, grep or otherwise.

Framing of ai apps = vector isn’t helpful (any db not providing hybrid search in 2025 is foolish) but this critique also applies to the framing of codeRAG is dead/ grep is all you need. Wish someone would put out some hard NDCG numbers around this but until then that’s my take on the other side

Interesting read! Despite the title I think at the end of your article you position vectors + lexical/grep as a yes/and situation. the same things you might fail to find with keyword search might turn up with vector search, grep or otherwise.

Framing of ai apps = vector isn’t helpful (any db not providing hybrid search in 2025 is foolish) but this critique also applies to the framing of codeRAG is dead/ grep is all you need. Wish someone would put out some hard NDCG numbers around this but until then that’s my take on the other side

LikeReply4 Reactions5 Reactions

Reisel González PérezSr. Solution Engineer @Microsoft | Cloud & AI3moReport this commentLaw of the instrument: "...if all you have is a hammer, everything looks like a nail". It's more about the use cases' nature understanding than the technology capabilities. Plus, a lot of misunderstanding around what is a deterministic, or a non deterministic problem.LikeReply3 Reactions4 Reactions

Reisel González PérezSr. Solution Engineer @Microsoft | Cloud & AI3moReport this commentLaw of the instrument: "...if all you have is a hammer, everything looks like a nail". It's more about the use cases' nature understanding than the technology capabilities. Plus, a lot of misunderstanding around what is a deterministic, or a non deterministic problem.

Reisel González PérezSr. Solution Engineer @Microsoft | Cloud & AI3moReport this comment

Sr. Solution Engineer @Microsoft | Cloud & AI

Law of the instrument: "...if all you have is a hammer, everything looks like a nail". It's more about the use cases' nature understanding than the technology capabilities. Plus, a lot of misunderstanding around what is a deterministic, or a non deterministic problem.

Law of the instrument: "...if all you have is a hammer, everything looks like a nail". It's more about the use cases' nature understanding than the technology capabilities. Plus, a lot of misunderstanding around what is a deterministic, or a non deterministic problem.

LikeReply3 Reactions4 Reactions

Devansh DevanshChocolate Milk Cult Leader| Machine Learning Engineer| Writer | AI Researcher| | Computational Math, Data Science, Software Engineering, Computer Science3moReport this commentThere’s a reason Claude Code is nibbling at Cursor’s market share, so much that they literally hired the Claude Code team—it’s all in its search. - is there any validation for that? 

When I did my Deep dive on cursor and the various security issues it had for Enterprise development, one of the key issues that we identified in our analysis was that cursor mismanaged context very inappropriately when compared to augment or Claude Code. 

My speculation for why that was the case was that cursor's team fundamentally is not very very knowledgeable about AI which was something I based on things I knew and also again the issues they were having. Which is why they were using very naive techniques.LikeReply2 Reactions3 Reactions

Devansh DevanshChocolate Milk Cult Leader| Machine Learning Engineer| Writer | AI Researcher| | Computational Math, Data Science, Software Engineering, Computer Science3moReport this commentThere’s a reason Claude Code is nibbling at Cursor’s market share, so much that they literally hired the Claude Code team—it’s all in its search. - is there any validation for that? 

When I did my Deep dive on cursor and the various security issues it had for Enterprise development, one of the key issues that we identified in our analysis was that cursor mismanaged context very inappropriately when compared to augment or Claude Code. 

My speculation for why that was the case was that cursor's team fundamentally is not very very knowledgeable about AI which was something I based on things I knew and also again the issues they were having. Which is why they were using very naive techniques.

Devansh DevanshChocolate Milk Cult Leader| Machine Learning Engineer| Writer | AI Researcher| | Computational Math, Data Science, Software Engineering, Computer Science3moReport this comment

Chocolate Milk Cult Leader| Machine Learning Engineer| Writer | AI Researcher| | Computational Math, Data Science, Software Engineering, Computer Science

There’s a reason Claude Code is nibbling at Cursor’s market share, so much that they literally hired the Claude Code team—it’s all in its search. - is there any validation for that? 

When I did my Deep dive on cursor and the various security issues it had for Enterprise development, one of the key issues that we identified in our analysis was that cursor mismanaged context very inappropriately when compared to augment or Claude Code. 

My speculation for why that was the case was that cursor's team fundamentally is not very very knowledgeable about AI which was something I based on things I knew and also again the issues they were having. Which is why they were using very naive techniques.

There’s a reason Claude Code is nibbling at Cursor’s market share, so much that they literally hired the Claude Code team—it’s all in its search. - is there any validation for that? 

When I did my Deep dive on cursor and the various security issues it had for Enterprise development, one of the key issues that we identified in our analysis was that cursor mismanaged context very inappropriately when compared to augment or Claude Code. 

My speculation for why that was the case was that cursor's team fundamentally is not very very knowledgeable about AI which was something I based on things I knew and also again the issues they were having. Which is why they were using very naive techniques.

LikeReply2 Reactions3 Reactions

To view or add a comment,sign in

4,462 followers937 Posts4 ArticlesView ProfileConnect

4,462 followers937 Posts4 ArticlesView ProfileConnect

## More from this author

Unpopular opinion: Prompt engineering is surprisingly similar to software development.🤖 Jacky Liang2yOn Open Sourcing the Drexel Schedulizer🤖 Jacky Liang7ySome short tips to finding referrals to companies you want to work for🤖 Jacky Liang8y

Unpopular opinion: Prompt engineering is surprisingly similar to software development.🤖 Jacky Liang2y

Unpopular opinion: Prompt engineering is surprisingly similar to software development.🤖 Jacky Liang2y

### Unpopular opinion: Prompt engineering is surprisingly similar to software development.

On Open Sourcing the Drexel Schedulizer🤖 Jacky Liang7y

On Open Sourcing the Drexel Schedulizer🤖 Jacky Liang7y

### On Open Sourcing the Drexel Schedulizer

Some short tips to finding referrals to companies you want to work for🤖 Jacky Liang8y

Some short tips to finding referrals to companies you want to work for🤖 Jacky Liang8y

### Some short tips to finding referrals to companies you want to work for

## Explore related topics

What Makes Vector Search Work WellInnovations Driving Vector Search TechnologyReasons for the Rising Popularity of Vector DatabasesAI's Impact on Coding ProductivityImpact of AI on Human ProgrammersReasons for Developers to Embrace AI ToolsHow AI Is Changing Programmer RolesTips to Avoid Generic AI ContentHow AI Impacts the Role of Human DevelopersReasons AI Cannot Replace Human WritersShow moreShow less

What Makes Vector Search Work WellInnovations Driving Vector Search TechnologyReasons for the Rising Popularity of Vector DatabasesAI's Impact on Coding ProductivityImpact of AI on Human ProgrammersReasons for Developers to Embrace AI ToolsHow AI Is Changing Programmer RolesTips to Avoid Generic AI ContentHow AI Impacts the Role of Human DevelopersReasons AI Cannot Replace Human WritersShow moreShow less

What Makes Vector Search Work Well

What Makes Vector Search Work Well

Innovations Driving Vector Search Technology

Innovations Driving Vector Search Technology

Reasons for the Rising Popularity of Vector Databases

Reasons for the Rising Popularity of Vector Databases

AI's Impact on Coding Productivity

AI's Impact on Coding Productivity

Impact of AI on Human Programmers

Impact of AI on Human Programmers

Reasons for Developers to Embrace AI Tools

Reasons for Developers to Embrace AI Tools

How AI Is Changing Programmer Roles

How AI Is Changing Programmer Roles

Tips to Avoid Generic AI Content

Tips to Avoid Generic AI Content

How AI Impacts the Role of Human Developers

How AI Impacts the Role of Human Developers

Reasons AI Cannot Replace Human Writers

Reasons AI Cannot Replace Human Writers

## Explore content categories

CareerProductivityFinanceSoft Skills & Emotional IntelligenceProject ManagementEducationTechnologyLeadershipEcommerceUser ExperienceShow moreShow less

CareerProductivityFinanceSoft Skills & Emotional IntelligenceProject ManagementEducationTechnologyLeadershipEcommerceUser ExperienceShow moreShow less

Soft Skills & Emotional Intelligence

