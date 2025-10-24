# Source: https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/

# Self-RAG

Self-RAG¶Self-RAG is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents and generations.In thepaper, a few decisions are made:Should I retrieve from retriever,R-Input:x (question)ORx (question),y (generation)Decides when to retrieveDchunks withROutput:yes, no, continueAre the retrieved passagesDrelevant to the questionx-Input: (x (question),d (chunk)) fordinDdprovides useful information to solvexOutput:relevant, irrelevantAre the LLM generation from each chunk inDis relevant to the chunk (hallucinations, etc)  -Input:x (question),d (chunk),y (generation)fordinDAll of the verification-worthy statements iny (generation)are supported bydOutput:{fully supported, partially supported, no supportThe LLM generation from each chunk inDis a useful response tox (question)-Input:x (question),y (generation)fordinDy (generation)is a useful response tox (question).Output:{5, 4, 3, 2, 1}We will implement some of these ideas from scratch usingLangGraph.Setup¶First let's install our required packages and set our API keys%pipinstall-Ulangchain_communitytiktokenlangchain-openailangchainhubchromadblangchainlanggraphimportgetpassimportosdef_set_env(key:str):ifkeynotinos.environ:os.environ[key]=getpass.getpass(f"{key}:")_set_env("OPENAI_API_KEY")Set upLangSmithfor LangGraph developmentSign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get startedhere.Retriever¶Let's index 3 blog posts.API Reference:RecursiveCharacterTextSplitter|WebBaseLoader|Chroma|OpenAIEmbeddingsfromlangchain.text_splitterimportRecursiveCharacterTextSplitterfromlangchain_community.document_loadersimportWebBaseLoaderfromlangchain_community.vectorstoresimportChromafromlangchain_openaiimportOpenAIEmbeddingsurls=["https://lilianweng.github.io/posts/2023-06-23-agent/","https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/","https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",]docs=[WebBaseLoader(url).load()forurlinurls]docs_list=[itemforsublistindocsforiteminsublist]text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=250,chunk_overlap=0)doc_splits=text_splitter.split_documents(docs_list)# Add to vectorDBvectorstore=Chroma.from_documents(documents=doc_splits,collection_name="rag-chroma",embedding=OpenAIEmbeddings(),)retriever=vectorstore.as_retriever()LLMs¶Using Pydantic with LangChainThis notebook uses Pydantic v2BaseModel, which requireslangchain-core >= 0.3. Usinglangchain-core < 0.3will result in errors due to mixing of Pydantic v1 and v2BaseModels.API Reference:ChatPromptTemplate|ChatOpenAI### Retrieval Graderfromlangchain_core.promptsimportChatPromptTemplatefromlangchain_openaiimportChatOpenAIfrompydanticimportBaseModel,Field# Data modelclassGradeDocuments(BaseModel):"""Binary score for relevance check on retrieved documents."""binary_score:str=Field(description="Documents are relevant to the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeDocuments)# Promptsystem="""You are a grader assessing relevance of a retrieved document to a user question.\nIt does not need to be a stringent test. The goal is to filter out erroneous retrievals.\nIf the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.\nGive a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""grade_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Retrieved document:\n\n{document}\n\nUser question:{question}"),])retrieval_grader=grade_prompt|structured_llm_graderquestion="agent memory"docs=retriever.invoke(question)doc_txt=docs[1].page_contentprint(retrieval_grader.invoke({"question":question,"document":doc_txt}))binary_score='no'API Reference:StrOutputParser### Generatefromlangchainimporthubfromlangchain_core.output_parsersimportStrOutputParser# Promptprompt=hub.pull("rlm/rag-prompt")# LLMllm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0)# Post-processingdefformat_docs(docs):return"\n\n".join(doc.page_contentfordocindocs)# Chainrag_chain=prompt|llm|StrOutputParser()# Rungeneration=rag_chain.invoke({"context":docs,"question":question})print(generation)The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.### Hallucination Grader# Data modelclassGradeHallucinations(BaseModel):"""Binary score for hallucination present in generation answer."""binary_score:str=Field(description="Answer is grounded in the facts, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeHallucinations)# Promptsystem="""You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\nGive a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""hallucination_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Set of facts:\n\n{documents}\n\nLLM generation:{generation}"),])hallucination_grader=hallucination_prompt|structured_llm_graderhallucination_grader.invoke({"documents":docs,"generation":generation})GradeHallucinations(binary_score='yes')### Answer Grader# Data modelclassGradeAnswer(BaseModel):"""Binary score to assess answer addresses question."""binary_score:str=Field(description="Answer addresses the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeAnswer)# Promptsystem="""You are a grader assessing whether an answer addresses / resolves a question\nGive a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""answer_prompt=ChatPromptTemplate.from_messages([("system",system),("human","User question:\n\n{question}\n\nLLM generation:{generation}"),])answer_grader=answer_prompt|structured_llm_graderanswer_grader.invoke({"question":question,"generation":generation})GradeAnswer(binary_score='yes')### Question Re-writer# LLMllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)# Promptsystem="""You a question re-writer that converts an input question to a better version that is optimized\nfor vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""re_write_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Here is the initial question:\n\n{question}\nFormulate an improved question.",),])question_rewriter=re_write_prompt|llm|StrOutputParser()question_rewriter.invoke({"question":question})"What is the role of memory in an agent's functioning?"Graph¶Capture the flow in as a graph.Graph state¶fromtypingimportListfromtyping_extensionsimportTypedDictclassGraphState(TypedDict):"""Represents the state of our graph.Attributes:question: questiongeneration: LLM generationdocuments: list of documents"""question:strgeneration:strdocuments:List[str]### Nodesdefretrieve(state):"""Retrieve documentsArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, documents, that contains retrieved documents"""print("---RETRIEVE---")question=state["question"]# Retrievaldocuments=retriever.invoke(question)return{"documents":documents,"question":question}defgenerate(state):"""Generate answerArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, generation, that contains LLM generation"""print("---GENERATE---")question=state["question"]documents=state["documents"]# RAG generationgeneration=rag_chain.invoke({"context":documents,"question":question})return{"documents":documents,"question":question,"generation":generation}defgrade_documents(state):"""Determines whether the retrieved documents are relevant to the question.Args:state (dict): The current graph stateReturns:state (dict): Updates documents key with only filtered relevant documents"""print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")question=state["question"]documents=state["documents"]# Score each docfiltered_docs=[]fordindocuments:score=retrieval_grader.invoke({"question":question,"document":d.page_content})grade=score.binary_scoreifgrade=="yes":print("---GRADE: DOCUMENT RELEVANT---")filtered_docs.append(d)else:print("---GRADE: DOCUMENT NOT RELEVANT---")continuereturn{"documents":filtered_docs,"question":question}deftransform_query(state):"""Transform the query to produce a better question.Args:state (dict): The current graph stateReturns:state (dict): Updates question key with a re-phrased question"""print("---TRANSFORM QUERY---")question=state["question"]documents=state["documents"]# Re-write questionbetter_question=question_rewriter.invoke({"question":question})return{"documents":documents,"question":better_question}### Edgesdefdecide_to_generate(state):"""Determines whether to generate an answer, or re-generate a question.Args:state (dict): The current graph stateReturns:str: Binary decision for next node to call"""print("---ASSESS GRADED DOCUMENTS---")state["question"]filtered_documents=state["documents"]ifnotfiltered_documents:# All documents have been filtered check_relevance# We will re-generate a new queryprint("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---")return"transform_query"else:# We have relevant documents, so generate answerprint("---DECISION: GENERATE---")return"generate"defgrade_generation_v_documents_and_question(state):"""Determines whether the generation is grounded in the document and answers question.Args:state (dict): The current graph stateReturns:str: Decision for next node to call"""print("---CHECK HALLUCINATIONS---")question=state["question"]documents=state["documents"]generation=state["generation"]score=hallucination_grader.invoke({"documents":documents,"generation":generation})grade=score.binary_score# Check hallucinationifgrade=="yes":print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")# Check question-answeringprint("---GRADE GENERATION vs QUESTION---")score=answer_grader.invoke({"question":question,"generation":generation})grade=score.binary_scoreifgrade=="yes":print("---DECISION: GENERATION ADDRESSES QUESTION---")return"useful"else:print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")return"not useful"else:pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")return"not supported"Build Graph¶The just follows the flow we outlined in the figure above.API Reference:END|StateGraph|STARTfromlanggraph.graphimportEND,StateGraph,STARTworkflow=StateGraph(GraphState)# Define the nodesworkflow.add_node("retrieve",retrieve)# retrieveworkflow.add_node("grade_documents",grade_documents)# grade documentsworkflow.add_node("generate",generate)# generateworkflow.add_node("transform_query",transform_query)# transform_query# Build graphworkflow.add_edge(START,"retrieve")workflow.add_edge("retrieve","grade_documents")workflow.add_conditional_edges("grade_documents",decide_to_generate,{"transform_query":"transform_query","generate":"generate",},)workflow.add_edge("transform_query","retrieve")workflow.add_conditional_edges("generate",grade_generation_v_documents_and_question,{"not supported":"generate","useful":END,"not useful":"transform_query",},)# Compileapp=workflow.compile()frompprintimportpprint# Runinputs={"question":"Explain how the different types of agent memory work?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Short-term memory is used for in-context learning in agents, allowing them ''to learn quickly. Long-term memory enables agents to retain and recall vast ''amounts of information over extended periods. Agents can also utilize ''external tools like APIs to access additional information beyond what is ''stored in their memory.')inputs={"question":"Explain how chain of thought prompting works?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Chain of thought prompting works by repeatedly prompting the model to ask ''follow-up questions to construct the thought process iteratively. This ''method can be combined with queries to search for relevant entities and ''content to add back into the context. It extends the thought process by ''exploring multiple reasoning possibilities at each step, creating a tree ''structure of thoughts.')

Self-RAG¶Self-RAG is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents and generations.In thepaper, a few decisions are made:Should I retrieve from retriever,R-Input:x (question)ORx (question),y (generation)Decides when to retrieveDchunks withROutput:yes, no, continueAre the retrieved passagesDrelevant to the questionx-Input: (x (question),d (chunk)) fordinDdprovides useful information to solvexOutput:relevant, irrelevantAre the LLM generation from each chunk inDis relevant to the chunk (hallucinations, etc)  -Input:x (question),d (chunk),y (generation)fordinDAll of the verification-worthy statements iny (generation)are supported bydOutput:{fully supported, partially supported, no supportThe LLM generation from each chunk inDis a useful response tox (question)-Input:x (question),y (generation)fordinDy (generation)is a useful response tox (question).Output:{5, 4, 3, 2, 1}We will implement some of these ideas from scratch usingLangGraph.Setup¶First let's install our required packages and set our API keys%pipinstall-Ulangchain_communitytiktokenlangchain-openailangchainhubchromadblangchainlanggraphimportgetpassimportosdef_set_env(key:str):ifkeynotinos.environ:os.environ[key]=getpass.getpass(f"{key}:")_set_env("OPENAI_API_KEY")Set upLangSmithfor LangGraph developmentSign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get startedhere.Retriever¶Let's index 3 blog posts.API Reference:RecursiveCharacterTextSplitter|WebBaseLoader|Chroma|OpenAIEmbeddingsfromlangchain.text_splitterimportRecursiveCharacterTextSplitterfromlangchain_community.document_loadersimportWebBaseLoaderfromlangchain_community.vectorstoresimportChromafromlangchain_openaiimportOpenAIEmbeddingsurls=["https://lilianweng.github.io/posts/2023-06-23-agent/","https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/","https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",]docs=[WebBaseLoader(url).load()forurlinurls]docs_list=[itemforsublistindocsforiteminsublist]text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=250,chunk_overlap=0)doc_splits=text_splitter.split_documents(docs_list)# Add to vectorDBvectorstore=Chroma.from_documents(documents=doc_splits,collection_name="rag-chroma",embedding=OpenAIEmbeddings(),)retriever=vectorstore.as_retriever()LLMs¶Using Pydantic with LangChainThis notebook uses Pydantic v2BaseModel, which requireslangchain-core >= 0.3. Usinglangchain-core < 0.3will result in errors due to mixing of Pydantic v1 and v2BaseModels.API Reference:ChatPromptTemplate|ChatOpenAI### Retrieval Graderfromlangchain_core.promptsimportChatPromptTemplatefromlangchain_openaiimportChatOpenAIfrompydanticimportBaseModel,Field# Data modelclassGradeDocuments(BaseModel):"""Binary score for relevance check on retrieved documents."""binary_score:str=Field(description="Documents are relevant to the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeDocuments)# Promptsystem="""You are a grader assessing relevance of a retrieved document to a user question.\nIt does not need to be a stringent test. The goal is to filter out erroneous retrievals.\nIf the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.\nGive a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""grade_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Retrieved document:\n\n{document}\n\nUser question:{question}"),])retrieval_grader=grade_prompt|structured_llm_graderquestion="agent memory"docs=retriever.invoke(question)doc_txt=docs[1].page_contentprint(retrieval_grader.invoke({"question":question,"document":doc_txt}))binary_score='no'API Reference:StrOutputParser### Generatefromlangchainimporthubfromlangchain_core.output_parsersimportStrOutputParser# Promptprompt=hub.pull("rlm/rag-prompt")# LLMllm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0)# Post-processingdefformat_docs(docs):return"\n\n".join(doc.page_contentfordocindocs)# Chainrag_chain=prompt|llm|StrOutputParser()# Rungeneration=rag_chain.invoke({"context":docs,"question":question})print(generation)The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.### Hallucination Grader# Data modelclassGradeHallucinations(BaseModel):"""Binary score for hallucination present in generation answer."""binary_score:str=Field(description="Answer is grounded in the facts, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeHallucinations)# Promptsystem="""You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\nGive a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""hallucination_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Set of facts:\n\n{documents}\n\nLLM generation:{generation}"),])hallucination_grader=hallucination_prompt|structured_llm_graderhallucination_grader.invoke({"documents":docs,"generation":generation})GradeHallucinations(binary_score='yes')### Answer Grader# Data modelclassGradeAnswer(BaseModel):"""Binary score to assess answer addresses question."""binary_score:str=Field(description="Answer addresses the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeAnswer)# Promptsystem="""You are a grader assessing whether an answer addresses / resolves a question\nGive a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""answer_prompt=ChatPromptTemplate.from_messages([("system",system),("human","User question:\n\n{question}\n\nLLM generation:{generation}"),])answer_grader=answer_prompt|structured_llm_graderanswer_grader.invoke({"question":question,"generation":generation})GradeAnswer(binary_score='yes')### Question Re-writer# LLMllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)# Promptsystem="""You a question re-writer that converts an input question to a better version that is optimized\nfor vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""re_write_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Here is the initial question:\n\n{question}\nFormulate an improved question.",),])question_rewriter=re_write_prompt|llm|StrOutputParser()question_rewriter.invoke({"question":question})"What is the role of memory in an agent's functioning?"Graph¶Capture the flow in as a graph.Graph state¶fromtypingimportListfromtyping_extensionsimportTypedDictclassGraphState(TypedDict):"""Represents the state of our graph.Attributes:question: questiongeneration: LLM generationdocuments: list of documents"""question:strgeneration:strdocuments:List[str]### Nodesdefretrieve(state):"""Retrieve documentsArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, documents, that contains retrieved documents"""print("---RETRIEVE---")question=state["question"]# Retrievaldocuments=retriever.invoke(question)return{"documents":documents,"question":question}defgenerate(state):"""Generate answerArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, generation, that contains LLM generation"""print("---GENERATE---")question=state["question"]documents=state["documents"]# RAG generationgeneration=rag_chain.invoke({"context":documents,"question":question})return{"documents":documents,"question":question,"generation":generation}defgrade_documents(state):"""Determines whether the retrieved documents are relevant to the question.Args:state (dict): The current graph stateReturns:state (dict): Updates documents key with only filtered relevant documents"""print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")question=state["question"]documents=state["documents"]# Score each docfiltered_docs=[]fordindocuments:score=retrieval_grader.invoke({"question":question,"document":d.page_content})grade=score.binary_scoreifgrade=="yes":print("---GRADE: DOCUMENT RELEVANT---")filtered_docs.append(d)else:print("---GRADE: DOCUMENT NOT RELEVANT---")continuereturn{"documents":filtered_docs,"question":question}deftransform_query(state):"""Transform the query to produce a better question.Args:state (dict): The current graph stateReturns:state (dict): Updates question key with a re-phrased question"""print("---TRANSFORM QUERY---")question=state["question"]documents=state["documents"]# Re-write questionbetter_question=question_rewriter.invoke({"question":question})return{"documents":documents,"question":better_question}### Edgesdefdecide_to_generate(state):"""Determines whether to generate an answer, or re-generate a question.Args:state (dict): The current graph stateReturns:str: Binary decision for next node to call"""print("---ASSESS GRADED DOCUMENTS---")state["question"]filtered_documents=state["documents"]ifnotfiltered_documents:# All documents have been filtered check_relevance# We will re-generate a new queryprint("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---")return"transform_query"else:# We have relevant documents, so generate answerprint("---DECISION: GENERATE---")return"generate"defgrade_generation_v_documents_and_question(state):"""Determines whether the generation is grounded in the document and answers question.Args:state (dict): The current graph stateReturns:str: Decision for next node to call"""print("---CHECK HALLUCINATIONS---")question=state["question"]documents=state["documents"]generation=state["generation"]score=hallucination_grader.invoke({"documents":documents,"generation":generation})grade=score.binary_score# Check hallucinationifgrade=="yes":print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")# Check question-answeringprint("---GRADE GENERATION vs QUESTION---")score=answer_grader.invoke({"question":question,"generation":generation})grade=score.binary_scoreifgrade=="yes":print("---DECISION: GENERATION ADDRESSES QUESTION---")return"useful"else:print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")return"not useful"else:pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")return"not supported"Build Graph¶The just follows the flow we outlined in the figure above.API Reference:END|StateGraph|STARTfromlanggraph.graphimportEND,StateGraph,STARTworkflow=StateGraph(GraphState)# Define the nodesworkflow.add_node("retrieve",retrieve)# retrieveworkflow.add_node("grade_documents",grade_documents)# grade documentsworkflow.add_node("generate",generate)# generateworkflow.add_node("transform_query",transform_query)# transform_query# Build graphworkflow.add_edge(START,"retrieve")workflow.add_edge("retrieve","grade_documents")workflow.add_conditional_edges("grade_documents",decide_to_generate,{"transform_query":"transform_query","generate":"generate",},)workflow.add_edge("transform_query","retrieve")workflow.add_conditional_edges("generate",grade_generation_v_documents_and_question,{"not supported":"generate","useful":END,"not useful":"transform_query",},)# Compileapp=workflow.compile()frompprintimportpprint# Runinputs={"question":"Explain how the different types of agent memory work?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Short-term memory is used for in-context learning in agents, allowing them ''to learn quickly. Long-term memory enables agents to retain and recall vast ''amounts of information over extended periods. Agents can also utilize ''external tools like APIs to access additional information beyond what is ''stored in their memory.')inputs={"question":"Explain how chain of thought prompting works?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Chain of thought prompting works by repeatedly prompting the model to ask ''follow-up questions to construct the thought process iteratively. This ''method can be combined with queries to search for relevant entities and ''content to add back into the context. It extends the thought process by ''exploring multiple reasoning possibilities at each step, creating a tree ''structure of thoughts.')

Self-RAG is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents and generations.

In thepaper, a few decisions are made:

Should I retrieve from retriever,R-

Should I retrieve from retriever,R-

Input:x (question)ORx (question),y (generation)

Input:x (question)ORx (question),y (generation)

Decides when to retrieveDchunks withR

Output:yes, no, continue

Output:yes, no, continue

Are the retrieved passagesDrelevant to the questionx-

Are the retrieved passagesDrelevant to the questionx-

Input: (x (question),d (chunk)) fordinD

Input: (x (question),d (chunk)) fordinD

dprovides useful information to solvex

Output:relevant, irrelevant

Output:relevant, irrelevant

Are the LLM generation from each chunk inDis relevant to the chunk (hallucinations, etc)  -

Are the LLM generation from each chunk inDis relevant to the chunk (hallucinations, etc)  -

Input:x (question),d (chunk),y (generation)fordinD

Input:x (question),d (chunk),y (generation)fordinD

All of the verification-worthy statements iny (generation)are supported byd

Output:{fully supported, partially supported, no support

Output:{fully supported, partially supported, no support

```
{fully supported, partially supported, no support
```

The LLM generation from each chunk inDis a useful response tox (question)-

The LLM generation from each chunk inDis a useful response tox (question)-

Input:x (question),y (generation)fordinD

Input:x (question),y (generation)fordinD

y (generation)is a useful response tox (question).

Output:{5, 4, 3, 2, 1}

We will implement some of these ideas from scratch usingLangGraph.

First let's install our required packages and set our API keys

%pipinstall-Ulangchain_communitytiktokenlangchain-openailangchainhubchromadblangchainlanggraph

```
%pipinstall-Ulangchain_communitytiktokenlangchain-openailangchainhubchromadblangchainlanggraph
```

```
%pipinstall-Ulangchain_communitytiktokenlangchain-openailangchainhubchromadblangchainlanggraph
```

%pipinstall-Ulangchain_communitytiktokenlangchain-openailangchainhubchromadblangchainlanggraph

importgetpassimportosdef_set_env(key:str):ifkeynotinos.environ:os.environ[key]=getpass.getpass(f"{key}:")_set_env("OPENAI_API_KEY")

```
importgetpassimportosdef_set_env(key:str):ifkeynotinos.environ:os.environ[key]=getpass.getpass(f"{key}:")_set_env("OPENAI_API_KEY")
```

```
importgetpassimportosdef_set_env(key:str):ifkeynotinos.environ:os.environ[key]=getpass.getpass(f"{key}:")_set_env("OPENAI_API_KEY")
```

def_set_env(key:str):

ifkeynotinos.environ:

os.environ[key]=getpass.getpass(f"{key}:")

_set_env("OPENAI_API_KEY")

Set upLangSmithfor LangGraph developmentSign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get startedhere.

Set upLangSmithfor LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get startedhere.

Let's index 3 blog posts.

API Reference:RecursiveCharacterTextSplitter|WebBaseLoader|Chroma|OpenAIEmbeddings

fromlangchain.text_splitterimportRecursiveCharacterTextSplitterfromlangchain_community.document_loadersimportWebBaseLoaderfromlangchain_community.vectorstoresimportChromafromlangchain_openaiimportOpenAIEmbeddingsurls=["https://lilianweng.github.io/posts/2023-06-23-agent/","https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/","https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",]docs=[WebBaseLoader(url).load()forurlinurls]docs_list=[itemforsublistindocsforiteminsublist]text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=250,chunk_overlap=0)doc_splits=text_splitter.split_documents(docs_list)# Add to vectorDBvectorstore=Chroma.from_documents(documents=doc_splits,collection_name="rag-chroma",embedding=OpenAIEmbeddings(),)retriever=vectorstore.as_retriever()

```
fromlangchain.text_splitterimportRecursiveCharacterTextSplitterfromlangchain_community.document_loadersimportWebBaseLoaderfromlangchain_community.vectorstoresimportChromafromlangchain_openaiimportOpenAIEmbeddingsurls=["https://lilianweng.github.io/posts/2023-06-23-agent/","https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/","https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",]docs=[WebBaseLoader(url).load()forurlinurls]docs_list=[itemforsublistindocsforiteminsublist]text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=250,chunk_overlap=0)doc_splits=text_splitter.split_documents(docs_list)# Add to vectorDBvectorstore=Chroma.from_documents(documents=doc_splits,collection_name="rag-chroma",embedding=OpenAIEmbeddings(),)retriever=vectorstore.as_retriever()
```

```
fromlangchain.text_splitterimportRecursiveCharacterTextSplitterfromlangchain_community.document_loadersimportWebBaseLoaderfromlangchain_community.vectorstoresimportChromafromlangchain_openaiimportOpenAIEmbeddingsurls=["https://lilianweng.github.io/posts/2023-06-23-agent/","https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/","https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",]docs=[WebBaseLoader(url).load()forurlinurls]docs_list=[itemforsublistindocsforiteminsublist]text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=250,chunk_overlap=0)doc_splits=text_splitter.split_documents(docs_list)# Add to vectorDBvectorstore=Chroma.from_documents(documents=doc_splits,collection_name="rag-chroma",embedding=OpenAIEmbeddings(),)retriever=vectorstore.as_retriever()
```

fromlangchain.text_splitterimportRecursiveCharacterTextSplitter

langchain.text_splitter

RecursiveCharacterTextSplitter

fromlangchain_community.document_loadersimportWebBaseLoader

langchain_community.document_loaders

fromlangchain_community.vectorstoresimportChroma

langchain_community.vectorstores

fromlangchain_openaiimportOpenAIEmbeddings

"https://lilianweng.github.io/posts/2023-06-23-agent/",

"https://lilianweng.github.io/posts/2023-06-23-agent/"

"https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",

"https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/"

"https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",

"https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/"

docs=[WebBaseLoader(url).load()forurlinurls]

docs_list=[itemforsublistindocsforiteminsublist]

text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(

RecursiveCharacterTextSplitter

from_tiktoken_encoder

chunk_size=250,chunk_overlap=0

doc_splits=text_splitter.split_documents(docs_list)

vectorstore=Chroma.from_documents(

documents=doc_splits,

collection_name="rag-chroma",

embedding=OpenAIEmbeddings(),

retriever=vectorstore.as_retriever()

Using Pydantic with LangChainThis notebook uses Pydantic v2BaseModel, which requireslangchain-core >= 0.3. Usinglangchain-core < 0.3will result in errors due to mixing of Pydantic v1 and v2BaseModels.

Using Pydantic with LangChain

This notebook uses Pydantic v2BaseModel, which requireslangchain-core >= 0.3. Usinglangchain-core < 0.3will result in errors due to mixing of Pydantic v1 and v2BaseModels.

```
langchain-core >= 0.3
```

API Reference:ChatPromptTemplate|ChatOpenAI

### Retrieval Graderfromlangchain_core.promptsimportChatPromptTemplatefromlangchain_openaiimportChatOpenAIfrompydanticimportBaseModel,Field# Data modelclassGradeDocuments(BaseModel):"""Binary score for relevance check on retrieved documents."""binary_score:str=Field(description="Documents are relevant to the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeDocuments)# Promptsystem="""You are a grader assessing relevance of a retrieved document to a user question.\nIt does not need to be a stringent test. The goal is to filter out erroneous retrievals.\nIf the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.\nGive a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""grade_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Retrieved document:\n\n{document}\n\nUser question:{question}"),])retrieval_grader=grade_prompt|structured_llm_graderquestion="agent memory"docs=retriever.invoke(question)doc_txt=docs[1].page_contentprint(retrieval_grader.invoke({"question":question,"document":doc_txt}))

```
### Retrieval Graderfromlangchain_core.promptsimportChatPromptTemplatefromlangchain_openaiimportChatOpenAIfrompydanticimportBaseModel,Field# Data modelclassGradeDocuments(BaseModel):"""Binary score for relevance check on retrieved documents."""binary_score:str=Field(description="Documents are relevant to the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeDocuments)# Promptsystem="""You are a grader assessing relevance of a retrieved document to a user question.\nIt does not need to be a stringent test. The goal is to filter out erroneous retrievals.\nIf the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.\nGive a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""grade_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Retrieved document:\n\n{document}\n\nUser question:{question}"),])retrieval_grader=grade_prompt|structured_llm_graderquestion="agent memory"docs=retriever.invoke(question)doc_txt=docs[1].page_contentprint(retrieval_grader.invoke({"question":question,"document":doc_txt}))
```

```
### Retrieval Graderfromlangchain_core.promptsimportChatPromptTemplatefromlangchain_openaiimportChatOpenAIfrompydanticimportBaseModel,Field# Data modelclassGradeDocuments(BaseModel):"""Binary score for relevance check on retrieved documents."""binary_score:str=Field(description="Documents are relevant to the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeDocuments)# Promptsystem="""You are a grader assessing relevance of a retrieved document to a user question.\nIt does not need to be a stringent test. The goal is to filter out erroneous retrievals.\nIf the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.\nGive a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""grade_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Retrieved document:\n\n{document}\n\nUser question:{question}"),])retrieval_grader=grade_prompt|structured_llm_graderquestion="agent memory"docs=retriever.invoke(question)doc_txt=docs[1].page_contentprint(retrieval_grader.invoke({"question":question,"document":doc_txt}))
```

fromlangchain_core.promptsimportChatPromptTemplate

langchain_core.prompts

fromlangchain_openaiimportChatOpenAI

frompydanticimportBaseModel,Field

classGradeDocuments(BaseModel):

"""Binary score for relevance check on retrieved documents."""

"""Binary score for relevance check on retrieved documents."""

binary_score:str=Field(

description="Documents are relevant to the question, 'yes' or 'no'"

"Documents are relevant to the question, 'yes' or 'no'"

# LLM with function call

# LLM with function call

llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

structured_llm_grader=llm.with_structured_output(GradeDocuments)

structured_llm_grader

with_structured_output

system="""You are a grader assessing relevance of a retrieved document to a user question.\n

"""You are a grader assessing relevance of a retrieved document to a user question.

It does not need to be a stringent test. The goal is to filter out erroneous retrievals.\n

It does not need to be a stringent test. The goal is to filter out erroneous retrievals.

If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.\n

If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.

Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""

Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""

grade_prompt=ChatPromptTemplate.from_messages(

("human","Retrieved document:\n\n{document}\n\nUser question:{question}"),

retrieval_grader=grade_prompt|structured_llm_grader

structured_llm_grader

question="agent memory"

docs=retriever.invoke(question)

doc_txt=docs[1].page_content

print(retrieval_grader.invoke({"question":question,"document":doc_txt}))

API Reference:StrOutputParser

### Generatefromlangchainimporthubfromlangchain_core.output_parsersimportStrOutputParser# Promptprompt=hub.pull("rlm/rag-prompt")# LLMllm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0)# Post-processingdefformat_docs(docs):return"\n\n".join(doc.page_contentfordocindocs)# Chainrag_chain=prompt|llm|StrOutputParser()# Rungeneration=rag_chain.invoke({"context":docs,"question":question})print(generation)

```
### Generatefromlangchainimporthubfromlangchain_core.output_parsersimportStrOutputParser# Promptprompt=hub.pull("rlm/rag-prompt")# LLMllm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0)# Post-processingdefformat_docs(docs):return"\n\n".join(doc.page_contentfordocindocs)# Chainrag_chain=prompt|llm|StrOutputParser()# Rungeneration=rag_chain.invoke({"context":docs,"question":question})print(generation)
```

```
### Generatefromlangchainimporthubfromlangchain_core.output_parsersimportStrOutputParser# Promptprompt=hub.pull("rlm/rag-prompt")# LLMllm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0)# Post-processingdefformat_docs(docs):return"\n\n".join(doc.page_contentfordocindocs)# Chainrag_chain=prompt|llm|StrOutputParser()# Rungeneration=rag_chain.invoke({"context":docs,"question":question})print(generation)
```

fromlangchainimporthub

fromlangchain_core.output_parsersimportStrOutputParser

langchain_core.output_parsers

prompt=hub.pull("rlm/rag-prompt")

llm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0)

defformat_docs(docs):

return"\n\n".join(doc.page_contentfordocindocs)

rag_chain=prompt|llm|StrOutputParser()

generation=rag_chain.invoke({"context":docs,"question":question})

The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.

```
The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.
```

```
The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.
```

The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.

The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.

### Hallucination Grader# Data modelclassGradeHallucinations(BaseModel):"""Binary score for hallucination present in generation answer."""binary_score:str=Field(description="Answer is grounded in the facts, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeHallucinations)# Promptsystem="""You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\nGive a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""hallucination_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Set of facts:\n\n{documents}\n\nLLM generation:{generation}"),])hallucination_grader=hallucination_prompt|structured_llm_graderhallucination_grader.invoke({"documents":docs,"generation":generation})

```
### Hallucination Grader# Data modelclassGradeHallucinations(BaseModel):"""Binary score for hallucination present in generation answer."""binary_score:str=Field(description="Answer is grounded in the facts, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeHallucinations)# Promptsystem="""You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\nGive a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""hallucination_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Set of facts:\n\n{documents}\n\nLLM generation:{generation}"),])hallucination_grader=hallucination_prompt|structured_llm_graderhallucination_grader.invoke({"documents":docs,"generation":generation})
```

```
### Hallucination Grader# Data modelclassGradeHallucinations(BaseModel):"""Binary score for hallucination present in generation answer."""binary_score:str=Field(description="Answer is grounded in the facts, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeHallucinations)# Promptsystem="""You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\nGive a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""hallucination_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Set of facts:\n\n{documents}\n\nLLM generation:{generation}"),])hallucination_grader=hallucination_prompt|structured_llm_graderhallucination_grader.invoke({"documents":docs,"generation":generation})
```

### Hallucination Grader

### Hallucination Grader

classGradeHallucinations(BaseModel):

"""Binary score for hallucination present in generation answer."""

"""Binary score for hallucination present in generation answer."""

binary_score:str=Field(

description="Answer is grounded in the facts, 'yes' or 'no'"

"Answer is grounded in the facts, 'yes' or 'no'"

# LLM with function call

# LLM with function call

llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

structured_llm_grader=llm.with_structured_output(GradeHallucinations)

structured_llm_grader

with_structured_output

system="""You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\n

"""You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.

Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""

Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""

hallucination_prompt=ChatPromptTemplate.from_messages(

("human","Set of facts:\n\n{documents}\n\nLLM generation:{generation}"),

hallucination_grader=hallucination_prompt|structured_llm_grader

structured_llm_grader

hallucination_grader.invoke({"documents":docs,"generation":generation})

GradeHallucinations(binary_score='yes')

```
GradeHallucinations(binary_score='yes')
```

```
GradeHallucinations(binary_score='yes')
```

GradeHallucinations(binary_score='yes')

GradeHallucinations(binary_score='yes')

### Answer Grader# Data modelclassGradeAnswer(BaseModel):"""Binary score to assess answer addresses question."""binary_score:str=Field(description="Answer addresses the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeAnswer)# Promptsystem="""You are a grader assessing whether an answer addresses / resolves a question\nGive a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""answer_prompt=ChatPromptTemplate.from_messages([("system",system),("human","User question:\n\n{question}\n\nLLM generation:{generation}"),])answer_grader=answer_prompt|structured_llm_graderanswer_grader.invoke({"question":question,"generation":generation})

```
### Answer Grader# Data modelclassGradeAnswer(BaseModel):"""Binary score to assess answer addresses question."""binary_score:str=Field(description="Answer addresses the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeAnswer)# Promptsystem="""You are a grader assessing whether an answer addresses / resolves a question\nGive a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""answer_prompt=ChatPromptTemplate.from_messages([("system",system),("human","User question:\n\n{question}\n\nLLM generation:{generation}"),])answer_grader=answer_prompt|structured_llm_graderanswer_grader.invoke({"question":question,"generation":generation})
```

```
### Answer Grader# Data modelclassGradeAnswer(BaseModel):"""Binary score to assess answer addresses question."""binary_score:str=Field(description="Answer addresses the question, 'yes' or 'no'")# LLM with function callllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)structured_llm_grader=llm.with_structured_output(GradeAnswer)# Promptsystem="""You are a grader assessing whether an answer addresses / resolves a question\nGive a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""answer_prompt=ChatPromptTemplate.from_messages([("system",system),("human","User question:\n\n{question}\n\nLLM generation:{generation}"),])answer_grader=answer_prompt|structured_llm_graderanswer_grader.invoke({"question":question,"generation":generation})
```

classGradeAnswer(BaseModel):

"""Binary score to assess answer addresses question."""

"""Binary score to assess answer addresses question."""

binary_score:str=Field(

description="Answer addresses the question, 'yes' or 'no'"

"Answer addresses the question, 'yes' or 'no'"

# LLM with function call

# LLM with function call

llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

structured_llm_grader=llm.with_structured_output(GradeAnswer)

structured_llm_grader

with_structured_output

system="""You are a grader assessing whether an answer addresses / resolves a question\n

"""You are a grader assessing whether an answer addresses / resolves a question

Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""

Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""

answer_prompt=ChatPromptTemplate.from_messages(

("human","User question:\n\n{question}\n\nLLM generation:{generation}"),

answer_grader=answer_prompt|structured_llm_grader

structured_llm_grader

answer_grader.invoke({"question":question,"generation":generation})

GradeAnswer(binary_score='yes')

```
GradeAnswer(binary_score='yes')
```

```
GradeAnswer(binary_score='yes')
```

GradeAnswer(binary_score='yes')

GradeAnswer(binary_score='yes')

### Question Re-writer# LLMllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)# Promptsystem="""You a question re-writer that converts an input question to a better version that is optimized\nfor vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""re_write_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Here is the initial question:\n\n{question}\nFormulate an improved question.",),])question_rewriter=re_write_prompt|llm|StrOutputParser()question_rewriter.invoke({"question":question})

```
### Question Re-writer# LLMllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)# Promptsystem="""You a question re-writer that converts an input question to a better version that is optimized\nfor vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""re_write_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Here is the initial question:\n\n{question}\nFormulate an improved question.",),])question_rewriter=re_write_prompt|llm|StrOutputParser()question_rewriter.invoke({"question":question})
```

```
### Question Re-writer# LLMllm=ChatOpenAI(model="gpt-4o-mini",temperature=0)# Promptsystem="""You a question re-writer that converts an input question to a better version that is optimized\nfor vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""re_write_prompt=ChatPromptTemplate.from_messages([("system",system),("human","Here is the initial question:\n\n{question}\nFormulate an improved question.",),])question_rewriter=re_write_prompt|llm|StrOutputParser()question_rewriter.invoke({"question":question})
```

### Question Re-writer

### Question Re-writer

llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

system="""You a question re-writer that converts an input question to a better version that is optimized\n

"""You a question re-writer that converts an input question to a better version that is optimized

for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""

for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""

re_write_prompt=ChatPromptTemplate.from_messages(

"Here is the initial question:\n\n{question}\nFormulate an improved question.",

"Here is the initial question:

Formulate an improved question."

question_rewriter=re_write_prompt|llm|StrOutputParser()

question_rewriter.invoke({"question":question})

"What is the role of memory in an agent's functioning?"

```
"What is the role of memory in an agent's functioning?"
```

```
"What is the role of memory in an agent's functioning?"
```

"What is the role of memory in an agent's functioning?"

"What is the role of memory in an agent's functioning?"

Capture the flow in as a graph.

fromtypingimportListfromtyping_extensionsimportTypedDictclassGraphState(TypedDict):"""Represents the state of our graph.Attributes:question: questiongeneration: LLM generationdocuments: list of documents"""question:strgeneration:strdocuments:List[str]

```
fromtypingimportListfromtyping_extensionsimportTypedDictclassGraphState(TypedDict):"""Represents the state of our graph.Attributes:question: questiongeneration: LLM generationdocuments: list of documents"""question:strgeneration:strdocuments:List[str]
```

```
fromtypingimportListfromtyping_extensionsimportTypedDictclassGraphState(TypedDict):"""Represents the state of our graph.Attributes:question: questiongeneration: LLM generationdocuments: list of documents"""question:strgeneration:strdocuments:List[str]
```

fromtyping_extensionsimportTypedDict

classGraphState(TypedDict):

Represents the state of our graph.

Represents the state of our graph.

generation: LLM generation

generation: LLM generation

documents: list of documents

documents: list of documents

### Nodesdefretrieve(state):"""Retrieve documentsArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, documents, that contains retrieved documents"""print("---RETRIEVE---")question=state["question"]# Retrievaldocuments=retriever.invoke(question)return{"documents":documents,"question":question}defgenerate(state):"""Generate answerArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, generation, that contains LLM generation"""print("---GENERATE---")question=state["question"]documents=state["documents"]# RAG generationgeneration=rag_chain.invoke({"context":documents,"question":question})return{"documents":documents,"question":question,"generation":generation}defgrade_documents(state):"""Determines whether the retrieved documents are relevant to the question.Args:state (dict): The current graph stateReturns:state (dict): Updates documents key with only filtered relevant documents"""print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")question=state["question"]documents=state["documents"]# Score each docfiltered_docs=[]fordindocuments:score=retrieval_grader.invoke({"question":question,"document":d.page_content})grade=score.binary_scoreifgrade=="yes":print("---GRADE: DOCUMENT RELEVANT---")filtered_docs.append(d)else:print("---GRADE: DOCUMENT NOT RELEVANT---")continuereturn{"documents":filtered_docs,"question":question}deftransform_query(state):"""Transform the query to produce a better question.Args:state (dict): The current graph stateReturns:state (dict): Updates question key with a re-phrased question"""print("---TRANSFORM QUERY---")question=state["question"]documents=state["documents"]# Re-write questionbetter_question=question_rewriter.invoke({"question":question})return{"documents":documents,"question":better_question}### Edgesdefdecide_to_generate(state):"""Determines whether to generate an answer, or re-generate a question.Args:state (dict): The current graph stateReturns:str: Binary decision for next node to call"""print("---ASSESS GRADED DOCUMENTS---")state["question"]filtered_documents=state["documents"]ifnotfiltered_documents:# All documents have been filtered check_relevance# We will re-generate a new queryprint("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---")return"transform_query"else:# We have relevant documents, so generate answerprint("---DECISION: GENERATE---")return"generate"defgrade_generation_v_documents_and_question(state):"""Determines whether the generation is grounded in the document and answers question.Args:state (dict): The current graph stateReturns:str: Decision for next node to call"""print("---CHECK HALLUCINATIONS---")question=state["question"]documents=state["documents"]generation=state["generation"]score=hallucination_grader.invoke({"documents":documents,"generation":generation})grade=score.binary_score# Check hallucinationifgrade=="yes":print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")# Check question-answeringprint("---GRADE GENERATION vs QUESTION---")score=answer_grader.invoke({"question":question,"generation":generation})grade=score.binary_scoreifgrade=="yes":print("---DECISION: GENERATION ADDRESSES QUESTION---")return"useful"else:print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")return"not useful"else:pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")return"not supported"

```
### Nodesdefretrieve(state):"""Retrieve documentsArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, documents, that contains retrieved documents"""print("---RETRIEVE---")question=state["question"]# Retrievaldocuments=retriever.invoke(question)return{"documents":documents,"question":question}defgenerate(state):"""Generate answerArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, generation, that contains LLM generation"""print("---GENERATE---")question=state["question"]documents=state["documents"]# RAG generationgeneration=rag_chain.invoke({"context":documents,"question":question})return{"documents":documents,"question":question,"generation":generation}defgrade_documents(state):"""Determines whether the retrieved documents are relevant to the question.Args:state (dict): The current graph stateReturns:state (dict): Updates documents key with only filtered relevant documents"""print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")question=state["question"]documents=state["documents"]# Score each docfiltered_docs=[]fordindocuments:score=retrieval_grader.invoke({"question":question,"document":d.page_content})grade=score.binary_scoreifgrade=="yes":print("---GRADE: DOCUMENT RELEVANT---")filtered_docs.append(d)else:print("---GRADE: DOCUMENT NOT RELEVANT---")continuereturn{"documents":filtered_docs,"question":question}deftransform_query(state):"""Transform the query to produce a better question.Args:state (dict): The current graph stateReturns:state (dict): Updates question key with a re-phrased question"""print("---TRANSFORM QUERY---")question=state["question"]documents=state["documents"]# Re-write questionbetter_question=question_rewriter.invoke({"question":question})return{"documents":documents,"question":better_question}### Edgesdefdecide_to_generate(state):"""Determines whether to generate an answer, or re-generate a question.Args:state (dict): The current graph stateReturns:str: Binary decision for next node to call"""print("---ASSESS GRADED DOCUMENTS---")state["question"]filtered_documents=state["documents"]ifnotfiltered_documents:# All documents have been filtered check_relevance# We will re-generate a new queryprint("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---")return"transform_query"else:# We have relevant documents, so generate answerprint("---DECISION: GENERATE---")return"generate"defgrade_generation_v_documents_and_question(state):"""Determines whether the generation is grounded in the document and answers question.Args:state (dict): The current graph stateReturns:str: Decision for next node to call"""print("---CHECK HALLUCINATIONS---")question=state["question"]documents=state["documents"]generation=state["generation"]score=hallucination_grader.invoke({"documents":documents,"generation":generation})grade=score.binary_score# Check hallucinationifgrade=="yes":print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")# Check question-answeringprint("---GRADE GENERATION vs QUESTION---")score=answer_grader.invoke({"question":question,"generation":generation})grade=score.binary_scoreifgrade=="yes":print("---DECISION: GENERATION ADDRESSES QUESTION---")return"useful"else:print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")return"not useful"else:pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")return"not supported"
```

```
### Nodesdefretrieve(state):"""Retrieve documentsArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, documents, that contains retrieved documents"""print("---RETRIEVE---")question=state["question"]# Retrievaldocuments=retriever.invoke(question)return{"documents":documents,"question":question}defgenerate(state):"""Generate answerArgs:state (dict): The current graph stateReturns:state (dict): New key added to state, generation, that contains LLM generation"""print("---GENERATE---")question=state["question"]documents=state["documents"]# RAG generationgeneration=rag_chain.invoke({"context":documents,"question":question})return{"documents":documents,"question":question,"generation":generation}defgrade_documents(state):"""Determines whether the retrieved documents are relevant to the question.Args:state (dict): The current graph stateReturns:state (dict): Updates documents key with only filtered relevant documents"""print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")question=state["question"]documents=state["documents"]# Score each docfiltered_docs=[]fordindocuments:score=retrieval_grader.invoke({"question":question,"document":d.page_content})grade=score.binary_scoreifgrade=="yes":print("---GRADE: DOCUMENT RELEVANT---")filtered_docs.append(d)else:print("---GRADE: DOCUMENT NOT RELEVANT---")continuereturn{"documents":filtered_docs,"question":question}deftransform_query(state):"""Transform the query to produce a better question.Args:state (dict): The current graph stateReturns:state (dict): Updates question key with a re-phrased question"""print("---TRANSFORM QUERY---")question=state["question"]documents=state["documents"]# Re-write questionbetter_question=question_rewriter.invoke({"question":question})return{"documents":documents,"question":better_question}### Edgesdefdecide_to_generate(state):"""Determines whether to generate an answer, or re-generate a question.Args:state (dict): The current graph stateReturns:str: Binary decision for next node to call"""print("---ASSESS GRADED DOCUMENTS---")state["question"]filtered_documents=state["documents"]ifnotfiltered_documents:# All documents have been filtered check_relevance# We will re-generate a new queryprint("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---")return"transform_query"else:# We have relevant documents, so generate answerprint("---DECISION: GENERATE---")return"generate"defgrade_generation_v_documents_and_question(state):"""Determines whether the generation is grounded in the document and answers question.Args:state (dict): The current graph stateReturns:str: Decision for next node to call"""print("---CHECK HALLUCINATIONS---")question=state["question"]documents=state["documents"]generation=state["generation"]score=hallucination_grader.invoke({"documents":documents,"generation":generation})grade=score.binary_score# Check hallucinationifgrade=="yes":print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")# Check question-answeringprint("---GRADE GENERATION vs QUESTION---")score=answer_grader.invoke({"question":question,"generation":generation})grade=score.binary_scoreifgrade=="yes":print("---DECISION: GENERATION ADDRESSES QUESTION---")return"useful"else:print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")return"not useful"else:pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")return"not supported"
```

state (dict): The current graph state

state (dict): The current graph state

state (dict): New key added to state, documents, that contains retrieved documents

state (dict): New key added to state, documents, that contains retrieved documents

print("---RETRIEVE---")

question=state["question"]

documents=retriever.invoke(question)

return{"documents":documents,"question":question}

state (dict): The current graph state

state (dict): The current graph state

state (dict): New key added to state, generation, that contains LLM generation

state (dict): New key added to state, generation, that contains LLM generation

print("---GENERATE---")

question=state["question"]

documents=state["documents"]

generation=rag_chain.invoke({"context":documents,"question":question})

return{"documents":documents,"question":question,"generation":generation}

defgrade_documents(state):

Determines whether the retrieved documents are relevant to the question.

Determines whether the retrieved documents are relevant to the question.

state (dict): The current graph state

state (dict): The current graph state

state (dict): Updates documents key with only filtered relevant documents

state (dict): Updates documents key with only filtered relevant documents

print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")

"---CHECK DOCUMENT RELEVANCE TO QUESTION---"

question=state["question"]

documents=state["documents"]

score=retrieval_grader.invoke(

{"question":question,"document":d.page_content}

grade=score.binary_score

print("---GRADE: DOCUMENT RELEVANT---")

"---GRADE: DOCUMENT RELEVANT---"

filtered_docs.append(d)

print("---GRADE: DOCUMENT NOT RELEVANT---")

"---GRADE: DOCUMENT NOT RELEVANT---"

return{"documents":filtered_docs,"question":question}

deftransform_query(state):

Transform the query to produce a better question.

Transform the query to produce a better question.

state (dict): The current graph state

state (dict): The current graph state

state (dict): Updates question key with a re-phrased question

state (dict): Updates question key with a re-phrased question

print("---TRANSFORM QUERY---")

"---TRANSFORM QUERY---"

question=state["question"]

documents=state["documents"]

better_question=question_rewriter.invoke({"question":question})

return{"documents":documents,"question":better_question}

defdecide_to_generate(state):

Determines whether to generate an answer, or re-generate a question.

Determines whether to generate an answer, or re-generate a question.

state (dict): The current graph state

state (dict): The current graph state

str: Binary decision for next node to call

str: Binary decision for next node to call

print("---ASSESS GRADED DOCUMENTS---")

"---ASSESS GRADED DOCUMENTS---"

filtered_documents=state["documents"]

ifnotfiltered_documents:

# All documents have been filtered check_relevance

# All documents have been filtered check_relevance

# We will re-generate a new query

# We will re-generate a new query

"---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"

"---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"

return"transform_query"

# We have relevant documents, so generate answer

# We have relevant documents, so generate answer

print("---DECISION: GENERATE---")

"---DECISION: GENERATE---"

defgrade_generation_v_documents_and_question(state):

grade_generation_v_documents_and_question

Determines whether the generation is grounded in the document and answers question.

Determines whether the generation is grounded in the document and answers question.

state (dict): The current graph state

state (dict): The current graph state

str: Decision for next node to call

str: Decision for next node to call

print("---CHECK HALLUCINATIONS---")

"---CHECK HALLUCINATIONS---"

question=state["question"]

documents=state["documents"]

generation=state["generation"]

score=hallucination_grader.invoke(

{"documents":documents,"generation":generation}

grade=score.binary_score

# Check hallucination

# Check hallucination

print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")

"---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---"

# Check question-answering

# Check question-answering

print("---GRADE GENERATION vs QUESTION---")

"---GRADE GENERATION vs QUESTION---"

score=answer_grader.invoke({"question":question,"generation":generation})

grade=score.binary_score

print("---DECISION: GENERATION ADDRESSES QUESTION---")

"---DECISION: GENERATION ADDRESSES QUESTION---"

print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")

"---DECISION: GENERATION DOES NOT ADDRESS QUESTION---"

pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")

"---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---"

return"not supported"

The just follows the flow we outlined in the figure above.

API Reference:END|StateGraph|START

fromlanggraph.graphimportEND,StateGraph,STARTworkflow=StateGraph(GraphState)# Define the nodesworkflow.add_node("retrieve",retrieve)# retrieveworkflow.add_node("grade_documents",grade_documents)# grade documentsworkflow.add_node("generate",generate)# generateworkflow.add_node("transform_query",transform_query)# transform_query# Build graphworkflow.add_edge(START,"retrieve")workflow.add_edge("retrieve","grade_documents")workflow.add_conditional_edges("grade_documents",decide_to_generate,{"transform_query":"transform_query","generate":"generate",},)workflow.add_edge("transform_query","retrieve")workflow.add_conditional_edges("generate",grade_generation_v_documents_and_question,{"not supported":"generate","useful":END,"not useful":"transform_query",},)# Compileapp=workflow.compile()

```
fromlanggraph.graphimportEND,StateGraph,STARTworkflow=StateGraph(GraphState)# Define the nodesworkflow.add_node("retrieve",retrieve)# retrieveworkflow.add_node("grade_documents",grade_documents)# grade documentsworkflow.add_node("generate",generate)# generateworkflow.add_node("transform_query",transform_query)# transform_query# Build graphworkflow.add_edge(START,"retrieve")workflow.add_edge("retrieve","grade_documents")workflow.add_conditional_edges("grade_documents",decide_to_generate,{"transform_query":"transform_query","generate":"generate",},)workflow.add_edge("transform_query","retrieve")workflow.add_conditional_edges("generate",grade_generation_v_documents_and_question,{"not supported":"generate","useful":END,"not useful":"transform_query",},)# Compileapp=workflow.compile()
```

```
fromlanggraph.graphimportEND,StateGraph,STARTworkflow=StateGraph(GraphState)# Define the nodesworkflow.add_node("retrieve",retrieve)# retrieveworkflow.add_node("grade_documents",grade_documents)# grade documentsworkflow.add_node("generate",generate)# generateworkflow.add_node("transform_query",transform_query)# transform_query# Build graphworkflow.add_edge(START,"retrieve")workflow.add_edge("retrieve","grade_documents")workflow.add_conditional_edges("grade_documents",decide_to_generate,{"transform_query":"transform_query","generate":"generate",},)workflow.add_edge("transform_query","retrieve")workflow.add_conditional_edges("generate",grade_generation_v_documents_and_question,{"not supported":"generate","useful":END,"not useful":"transform_query",},)# Compileapp=workflow.compile()
```

fromlanggraph.graphimportEND,StateGraph,START

workflow=StateGraph(GraphState)

workflow.add_node("retrieve",retrieve)# retrieve

workflow.add_node("grade_documents",grade_documents)# grade documents

workflow.add_node("generate",generate)# generate

workflow.add_node("transform_query",transform_query)# transform_query

workflow.add_edge(START,"retrieve")

workflow.add_edge("retrieve","grade_documents")

workflow.add_conditional_edges(

add_conditional_edges

"transform_query":"transform_query",

"generate":"generate",

workflow.add_edge("transform_query","retrieve")

workflow.add_conditional_edges(

add_conditional_edges

grade_generation_v_documents_and_question,

grade_generation_v_documents_and_question

"not supported":"generate",

"not useful":"transform_query",

app=workflow.compile()

frompprintimportpprint# Runinputs={"question":"Explain how the different types of agent memory work?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])

```
frompprintimportpprint# Runinputs={"question":"Explain how the different types of agent memory work?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])
```

```
frompprintimportpprint# Runinputs={"question":"Explain how the different types of agent memory work?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])
```

frompprintimportpprint

inputs={"question":"Explain how the different types of agent memory work?"}

"Explain how the different types of agent memory work?"

foroutputinapp.stream(inputs):

forkey,valueinoutput.items():

pprint(f"Node '{key}':")

# Optional: print full state at each node

# Optional: print full state at each node

# pprint.pprint(value["keys"], indent=2, width=80, depth=None)

# pprint.pprint(value["keys"], indent=2, width=80, depth=None)

pprint(value["generation"])

---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Short-term memory is used for in-context learning in agents, allowing them ''to learn quickly. Long-term memory enables agents to retain and recall vast ''amounts of information over extended periods. Agents can also utilize ''external tools like APIs to access additional information beyond what is ''stored in their memory.')

```
---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Short-term memory is used for in-context learning in agents, allowing them ''to learn quickly. Long-term memory enables agents to retain and recall vast ''amounts of information over extended periods. Agents can also utilize ''external tools like APIs to access additional information beyond what is ''stored in their memory.')
```

```
---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Short-term memory is used for in-context learning in agents, allowing them ''to learn quickly. Long-term memory enables agents to retain and recall vast ''amounts of information over extended periods. Agents can also utilize ''external tools like APIs to access additional information beyond what is ''stored in their memory.')
```

---CHECK DOCUMENT RELEVANCE TO QUESTION---

---CHECK DOCUMENT RELEVANCE TO QUESTION---

---GRADE: DOCUMENT NOT RELEVANT---

---GRADE: DOCUMENT NOT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---GRADE: DOCUMENT NOT RELEVANT---

---GRADE: DOCUMENT NOT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---ASSESS GRADED DOCUMENTS---

---ASSESS GRADED DOCUMENTS---

---DECISION: GENERATE---

---DECISION: GENERATE---

"Node 'grade_documents':"

"Node 'grade_documents':"

---CHECK HALLUCINATIONS---

---CHECK HALLUCINATIONS---

---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---

---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---

---GRADE GENERATION vs QUESTION---

---GRADE GENERATION vs QUESTION---

---DECISION: GENERATION ADDRESSES QUESTION---

---DECISION: GENERATION ADDRESSES QUESTION---

('Short-term memory is used for in-context learning in agents, allowing them '

('Short-term memory is used for in-context learning in agents, allowing them '

'to learn quickly. Long-term memory enables agents to retain and recall vast '

'to learn quickly. Long-term memory enables agents to retain and recall vast '

'amounts of information over extended periods. Agents can also utilize '

'amounts of information over extended periods. Agents can also utilize '

'external tools like APIs to access additional information beyond what is '

'external tools like APIs to access additional information beyond what is '

'stored in their memory.')

'stored in their memory.')

inputs={"question":"Explain how chain of thought prompting works?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])

```
inputs={"question":"Explain how chain of thought prompting works?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])
```

```
inputs={"question":"Explain how chain of thought prompting works?"}foroutputinapp.stream(inputs):forkey,valueinoutput.items():# Nodepprint(f"Node '{key}':")# Optional: print full state at each node# pprint.pprint(value["keys"], indent=2, width=80, depth=None)pprint("\n---\n")# Final generationpprint(value["generation"])
```

inputs={"question":"Explain how chain of thought prompting works?"}

"Explain how chain of thought prompting works?"

foroutputinapp.stream(inputs):

forkey,valueinoutput.items():

pprint(f"Node '{key}':")

# Optional: print full state at each node

# Optional: print full state at each node

# pprint.pprint(value["keys"], indent=2, width=80, depth=None)

# pprint.pprint(value["keys"], indent=2, width=80, depth=None)

pprint(value["generation"])

---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Chain of thought prompting works by repeatedly prompting the model to ask ''follow-up questions to construct the thought process iteratively. This ''method can be combined with queries to search for relevant entities and ''content to add back into the context. It extends the thought process by ''exploring multiple reasoning possibilities at each step, creating a tree ''structure of thoughts.')

```
---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Chain of thought prompting works by repeatedly prompting the model to ask ''follow-up questions to construct the thought process iteratively. This ''method can be combined with queries to search for relevant entities and ''content to add back into the context. It extends the thought process by ''exploring multiple reasoning possibilities at each step, creating a tree ''structure of thoughts.')
```

```
---RETRIEVE---"Node 'retrieve':"'\n---\n'---CHECK DOCUMENT RELEVANCE TO QUESTION------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT NOT RELEVANT------GRADE: DOCUMENT RELEVANT------GRADE: DOCUMENT RELEVANT------ASSESS GRADED DOCUMENTS------DECISION: GENERATE---"Node 'grade_documents':"'\n---\n'---GENERATE------CHECK HALLUCINATIONS------DECISION: GENERATION IS GROUNDED IN DOCUMENTS------GRADE GENERATION vs QUESTION------DECISION: GENERATION ADDRESSES QUESTION---"Node 'generate':"'\n---\n'('Chain of thought prompting works by repeatedly prompting the model to ask ''follow-up questions to construct the thought process iteratively. This ''method can be combined with queries to search for relevant entities and ''content to add back into the context. It extends the thought process by ''exploring multiple reasoning possibilities at each step, creating a tree ''structure of thoughts.')
```

---CHECK DOCUMENT RELEVANCE TO QUESTION---

---CHECK DOCUMENT RELEVANCE TO QUESTION---

---GRADE: DOCUMENT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---GRADE: DOCUMENT NOT RELEVANT---

---GRADE: DOCUMENT NOT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---GRADE: DOCUMENT RELEVANT---

---ASSESS GRADED DOCUMENTS---

---ASSESS GRADED DOCUMENTS---

---DECISION: GENERATE---

---DECISION: GENERATE---

"Node 'grade_documents':"

"Node 'grade_documents':"

---CHECK HALLUCINATIONS---

---CHECK HALLUCINATIONS---

---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---

---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---

---GRADE GENERATION vs QUESTION---

---GRADE GENERATION vs QUESTION---

---DECISION: GENERATION ADDRESSES QUESTION---

---DECISION: GENERATION ADDRESSES QUESTION---

('Chain of thought prompting works by repeatedly prompting the model to ask '

('Chain of thought prompting works by repeatedly prompting the model to ask '

'follow-up questions to construct the thought process iteratively. This '

'follow-up questions to construct the thought process iteratively. This '

'method can be combined with queries to search for relevant entities and '

'method can be combined with queries to search for relevant entities and '

'content to add back into the context. It extends the thought process by '

'content to add back into the context. It extends the thought process by '

'exploring multiple reasoning possibilities at each step, creating a tree '

'exploring multiple reasoning possibilities at each step, creating a tree '

'structure of thoughts.')

'structure of thoughts.')

