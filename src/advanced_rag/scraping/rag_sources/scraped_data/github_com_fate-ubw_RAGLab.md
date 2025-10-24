# Source: https://github.com/fate-ubw/RAGLab?tab=readme-ov-file

# GitHub - fate-ubw/RAGLAB: [EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation

fate-ubw/RAGLABPublicNotificationsYou must be signed in to change notification settingsFork35Star309[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381LicenseMIT license309stars35forksBranchesTagsActivityStarNotificationsYou must be signed in to change notification settings

fate-ubw/RAGLABPublicNotificationsYou must be signed in to change notification settingsFork35Star309

fate-ubw/RAGLABPublic

fate-ubw/RAGLABPublic

NotificationsYou must be signed in to change notification settingsFork35Star309

NotificationsYou must be signed in to change notification settings

[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381LicenseMIT license309stars35forksBranchesTagsActivityStarNotificationsYou must be signed in to change notification settings

[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381LicenseMIT license309stars35forksBranchesTagsActivityStarNotificationsYou must be signed in to change notification settings

[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation

arxiv.org/abs/2408.11381

arxiv.org/abs/2408.11381

309stars35forksBranchesTagsActivity

StarNotificationsYou must be signed in to change notification settings

NotificationsYou must be signed in to change notification settings

fate-ubw/RAGLABmain1Branch0TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all filesRepository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repositoryReleasesNo releases publishedPackages0No packages publishedContributors3fate-ubwjim zhangYunzeSongYun-Ze SongjeremiahbuckleyLanguagesPython86.5%Shell13.5%

main1Branch0TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all filesRepository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repositoryReleasesNo releases publishedPackages0No packages publishedContributors3fate-ubwjim zhangYunzeSongYun-Ze SongjeremiahbuckleyLanguagesPython86.5%Shell13.5%

main1Branch0TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all filesRepository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repositoryReleasesNo releases publishedPackages0No packages publishedContributors3fate-ubwjim zhangYunzeSongYun-Ze SongjeremiahbuckleyLanguagesPython86.5%Shell13.5%

main1Branch0TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all filesRepository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repositoryReleasesNo releases publishedPackages0No packages publishedContributors3fate-ubwjim zhangYunzeSongYun-Ze SongjeremiahbuckleyLanguagesPython86.5%Shell13.5%

main1Branch0TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all filesRepository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.

main1Branch0TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all filesRepository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.

main1Branch0TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all filesRepository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.

main1Branch0TagsGo to fileCodeOpen more actions menu

Go to fileCodeOpen more actions menu

Open more actions menu

Open more actions menu

Folders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all filesRepository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.

Folders and filesNameNameLast commit messageLast commit dateLatest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit detailsALCEALCE[feat] update all code to a new repoAug 6, 2024FActScoreFActScore[feat] update all code to a new repoAug 6, 2024auto_gpu_scheduling_scriptsauto_gpu_scheduling_scripts[docs] update readmeAug 23, 2024configconfig[docs] update colbert server for automatic embedding functionAug 22, 2024datadata[docs] update colbert server for automatic embedding functionAug 22, 2024docsdocs[docs] update license & upload Reply_for_Issue1Aug 26, 2024figuresfigures[docs] update readmeAug 22, 2024preprocesspreprocess[docs] update readmeAug 24, 2024raglabraglab[docs] update colbert server for automatic embedding functionAug 22, 2024runrun[docs] update readme and path of wiki2023 for factscoreAug 24, 2024.gitignore.gitignore[docs] update colbert server for automatic embedding functionAug 22, 2024LICENSELICENSE[docs] update readmeOct 6, 2024api_keys.txtapi_keys.txt[feat] update all code to a new repoAug 6, 2024environment.ymlenvironment.ymlenvironment.yml - removed flash-attnOct 16, 2024main-evaluation.pymain-evaluation.py[feat] update all code to a new repoAug 6, 2024main-interact.pymain-interact.py[feat] update all code to a new repoAug 6, 2024main_data_collector.pymain_data_collector.py[feat] update all code to a new repoAug 6, 2024readme.mdreadme.md[docs] update readmeOct 6, 2024utils.pyutils.py[feat] update all code to a new repoAug 6, 2024View all files

Latest commitfate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024a1b655e·Oct 18, 2024History36 CommitsOpen commit details

fate-ubwMerge pull request#8from jeremiahbuckley/mainOpen commit detailsOct 18, 2024

Merge pull request#8from jeremiahbuckley/mainOpen commit details

Merge pull request#8from jeremiahbuckley/main

Merge pull request#8from jeremiahbuckley/main

a1b655e·Oct 18, 2024History36 CommitsOpen commit details

History36 CommitsOpen commit details

[feat] update all code to a new repo

[feat] update all code to a new repo

[feat] update all code to a new repo

[feat] update all code to a new repo

auto_gpu_scheduling_scripts

auto_gpu_scheduling_scripts

auto_gpu_scheduling_scripts

auto_gpu_scheduling_scripts

auto_gpu_scheduling_scripts

auto_gpu_scheduling_scripts

auto_gpu_scheduling_scripts

auto_gpu_scheduling_scripts

[docs] update colbert server for automatic embedding function

[docs] update colbert server for automatic embedding function

[docs] update colbert server for automatic embedding function

[docs] update colbert server for automatic embedding function

[docs] update license & upload Reply_for_Issue1

[docs] update license & upload Reply_for_Issue1

[docs] update colbert server for automatic embedding function

[docs] update colbert server for automatic embedding function

[docs] update readme and path of wiki2023 for factscore

[docs] update readme and path of wiki2023 for factscore

[docs] update colbert server for automatic embedding function

[docs] update colbert server for automatic embedding function

[feat] update all code to a new repo

[feat] update all code to a new repo

environment.yml - removed flash-attn

environment.yml - removed flash-attn

[feat] update all code to a new repo

[feat] update all code to a new repo

[feat] update all code to a new repo

[feat] update all code to a new repo

main_data_collector.py

main_data_collector.py

main_data_collector.py

main_data_collector.py

main_data_collector.py

main_data_collector.py

main_data_collector.py

main_data_collector.py

[feat] update all code to a new repo

[feat] update all code to a new repo

[feat] update all code to a new repo

[feat] update all code to a new repo

Repository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.

Repository files navigationRAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.

Repository files navigation

## Repository files navigation

RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented GenerationRAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.News2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor2024.8.6: RAGLAB is released🌈.🌟FeaturesComprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.📎Related worksInteresting RAG applicationsAutosurvey🔨Install environmentdev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04install minicondagit clone RAGLABhttps://github.com/fate-ubw/RAGLAB.gitcreate environment from yml filecdRAGLAB
conda env create -f environment.ymlinstall flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt🤗 Modelsraglab need several models please download themcdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface🤗 Whole DataIf you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type datasetRun Raglab in Interact ModeInteract Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.Setup colbert serverAll algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsvrun colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.shNoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.shCongratulations！！！Now you have already know how to run raglab 🌈In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarksReproduce paper resultsNoteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper resultsRetrieval server & apiDue to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.shopen another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.shColBERT server started successfully!!! 🌈Automatic GPU Schedulerinference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.installsimple_gpu_schedulerpip install simple_gpu_schedulerrun hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same methodhow to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.shEvaluation for ALCE & FactscoreRAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txtThe evaluation results will be in the same directory as the input file, with the file name suffix.scoreFactscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txtThe evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.jsonNoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscoreProcess knowledge database from sourceIf you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Facedocument:process_wiki.md🤖 Train modelsThis section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.All dataprovides all data necessary for finetuning.document:train_docs.mdCitationIf you find this repository useful, please cite our work.@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}🔖 LicenseRAGLAB is licensed under theMIT License.

RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation

# RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation

RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation

RAGLAB is a modular, research-oriented open-source framework for Retrieval-Augmented Generation (RAG) algorithms. It offers reproductions of 6 existing RAG algorithms and a comprehensive evaluation system with 10 benchmark datasets, enabling fair comparisons between RAG algorithms and easy expansion for efficient development of new algorithms, datasets, and evaluation metrics.

2024.10.6: Our paper has been accepted by EMNLP 2024 System Demonstration.🎉 You can find our paper inRAGLAB.

2024.9.9: RAGLAB has open-sourced all log files and evaluation files inevaluation results📌

2024.8.20: RAGLAB has open-sourced 4 models🤗:llama3-8B-baselineselfrag-llama3-8bllama3-70B-adaptorselfrag-llama3-70B-adaptor

2024.8.6: RAGLAB is released🌈.

Comprehensive RAG Ecosystem:Supports the entire RAG pipeline from data collection and training to auto-evaluation.

Advanced Algorithm Implementations:Reproduces 6 state-of-the-art RAG algorithms, with an easy-to-extend framework for developing new algorithms.

Interact Mode & Evaluation Mode:Interact Mode is specifically designed for quickly understanding algorithms. Evaluation Mode is specifically designed for reproducing paper results and scientific research.

Fair Comparison Platform:Provides benchmark results for 6 algorithms across 5 task types and 10 datasets.

Efficient Retriever Client:Offers local API for parallel access and caching, with average latency under 1 second.

Versatile Generator Support:Compatible with 70B+ models, VLLM, and quantization techniques.

Flexible Instruction Lab:Customizable instruction templates for various RAG scenarios.

Interesting RAG applicationsAutosurvey

dev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04

dev environment：pytorch:2.0.1-py3.10-cuda11.8.0-devel-ubuntu22.04

git clone RAGLABhttps://github.com/fate-ubw/RAGLAB.git

https://github.com/fate-ubw/RAGLAB.git

```
https://github.com/fate-ubw/RAGLAB.git
```

create environment from yml filecdRAGLAB
conda env create -f environment.yml

create environment from yml file

cdRAGLAB
conda env create -f environment.yml

```
cdRAGLAB
conda env create -f environment.yml
```

install flash-attn, en_core_web_sm, punkt manuallypip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt

install flash-attn, en_core_web_sm, punkt manually

pip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt

```
pip install flash-attn==2.2
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt
```

cdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface

```
cdRAGLAB
mkdir modelcdmodel
mkdir output_models#retriever modelmkdir colbertv2.0
huggingface-cli download colbert-ir/colbertv2.0 --local-dir colbertv2.0/ --local-dir-use-symlinks False
mkdir contriever-msmarco
huggingface-cli download facebook/contriever-msmarco --local-dir contriever-msmarco/ --local-dir-use-symlinks False#finetuned generator#8B modelmkdir Llama3-8B-baseline
huggingface-cli download RAGLAB/Llama3-8B-baseline --local-dir Llama3-8B-baseline/ --local-dir-use-symlinks False
mkdir selfrag_llama3_8b-epoch_0_1
huggingface-cli download RAGLAB/selfrag_llama3-8B --local-dir selfrag_llama3_8b-epoch_0_1/ --local-dir-use-symlinks False#70B modelmkdir Llama3-70B-baseline-adapter
huggingface-cli download RAGLAB/Llama3-70B-baseline-adapter --local-dir Llama3-70B-baseline-adapter/ --local-dir-use-symlinks False
mkdir selfrag_llama3_70B-adapter
huggingface-cli download RAGLAB/selfrag_llama3-70B-adapter --local-dir selfrag_llama3_70B-adapter/ --local-dir-use-symlinks False
mkdir Meta-Llama-3-70B
huggingface-cli download meta-llama/Meta-Llama-3-70B --local-dir Meta-Llama-3-70B/ --local-dir-use-symlinks False#base model for finetune and LoRAmkdir Meta-Llama-3-8B
huggingface-cli download meta-llama/Meta-Llama-3-8B --local-dir Meta-Llama-3-8B/ --local-dir-use-symlinks False#ALCE Metric Modelsmkdir gpt2-large
huggingface-cli download openai-community/gpt2-large --local-dir gpt2-large/ --local-dir-use-symlinks False
mkdir roberta-large-squad
huggingface-cli download gaotianyu1350/roberta-large-squad --local-dir roberta-large-squad/ --local-dir-use-symlinks False
mkdir t5_xxl_true_nli_mixture
huggingface-cli download google/t5_xxl_true_nli_mixture --local-dir t5_xxl_true_nli_mixture/ --local-dir-use-symlinks False#factscore model we use gpt3.5 for evaluation, so no need to download local models#models from official selfrag repomkdir selfrag_llama2_7b
huggingface-cli download selfrag/selfrag_llama2_7b --local-dir selfrag_llama2_7b/ --local-dir-use-symlinks False#you can download other model as generator from huggingface
```

#base model for finetune and LoRA

#factscore model we use gpt3.5 for evaluation, so no need to download local models

#models from official selfrag repo

#you can download other model as generator from huggingface

If you only need to understand how different algorithms work, the interact mode developed by RAGLAB can meet your needs.

If you want to reproduce the results from the papers, you need to download all the required data from Hugging Face, including training data, knowledge data, and evaluation data. We have packaged all the data for you, so you just need to download it and it's ready to use.cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type dataset

cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type dataset

```
cdRAGLAB
huggingface-cli download RAGLAB/data --local-dir data --repo-type dataset
```

Run Raglab in Interact Mode

# Run Raglab in Interact Mode

Interact Mode is specifically designed for quickly understanding algorithms. In interact mode, you can run various algorithms very quickly, understand the reasoning process of different algorithms, without needing to download any additional data.

All algorithms integrated in raglab include two modes:interactandevaluation. The test stage demonstrates ininteractmode, just for demostration and eduction 🤗.

NoteDue to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.

Due to colbert's requirement for absolute paths, you need to modify the index_dbPath and text_dbPath in the config file to use absolute paths.

Modify theindex_dbPathandtext_dbPathin config file:colbert_server-10samples.yamlindex_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsv

index_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsv

```
index_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2023-10samples
text_dbPath: /your_root_path/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2023-10samples/enwiki-20230401-10samples.tsv
```

run colbert servercdRAGLAB
sh run/colbert_server/colbert_server-10samples.sh

cdRAGLAB
sh run/colbert_server/colbert_server-10samples.sh

```
cdRAGLAB
sh run/colbert_server/colbert_server-10samples.sh
```

NoteAt this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.

At this point, colbert embedding will prompt that due to path errors, colbert embedding needs to be reprocessed. Please enteryesand then raglab will automatically help you process the embedding and start the colbert server.

Now please open another terminal and try to request the colbert servercdRAGLAB
sh run/colbert_server/ask_api.shIf a result is returned, it means the colbert server has started successfully! 🌈

cdRAGLAB
sh run/colbert_server/ask_api.sh

```
cdRAGLAB
sh run/colbert_server/ask_api.sh
```

If a result is returned, it means the colbert server has started successfully! 🌈

runselfrag(short form & adaptive retrieval) interact mode test 10-samples embeddingcdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.sh

cdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.sh

```
cdRAGLAB
sh run/rag_inference/3-selfrag_reproduction-interact-short_form-adaptive_retrieval.sh
```

Congratulations！！！Now you have already know how to run raglab 🌈

In raglab, each algorithm has 10 queries built-in in interact mode which are sampled from different benchmarks

Reproduce paper results

# Reproduce paper results

Noteremember downloadwiki2018 konwledge databaseandmodelbefore runing paper results

remember downloadwiki2018 konwledge databaseandmodelbefore runing paper results

Retrieval server & api

## Retrieval server & api

Due to colbert's requirement for absolute paths, you need to modify theindex_dbPathandtext_dbPathin config file and process the wiki2018 embedding databaseModify the paths in the config filecdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsvModify the absolute paths bound in the wiki2018 embedding source filevim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",

Modify the paths in the config file

cdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv

```
cdRAGLAB/config/colbert_server
vim colbert_server.yaml
index_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018
text_dbPath: {your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv
```

Modify the absolute paths bound in the wiki2018 embedding source file

vim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",

```
vim /data/retrieval/colbertv2.0_embedding/wiki2018/indexes/wiki2018/metadata.json#change root path, other parameters do not need to be modified"collection":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv","experiment":"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018",
```

#change root path, other parameters do not need to be modified

"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_passages/wiki2018/wiki2018.tsv"

"/{your_root_path}/RAGLAB/data/retrieval/colbertv2.0_embedding/wiki2018"

Attention: colbert_server need atleast 60GB ramcdRAGLAB
sh run/colbert_server/colbert_server.sh

cdRAGLAB
sh run/colbert_server/colbert_server.sh

```
cdRAGLAB
sh run/colbert_server/colbert_server.sh
```

open another terminal test your ColBERT servercdRAGLAB
sh run/colbert_server/ask_api.sh

cdRAGLAB
sh run/colbert_server/ask_api.sh

```
cdRAGLAB
sh run/colbert_server/ask_api.sh
```

ColBERT server started successfully!!! 🌈

Automatic GPU Scheduler

## Automatic GPU Scheduler

inference experiments require running hundreds of scripts in parallel, theautomatic gpu schedulerneeds to be used to automatically allocate GPUs for different bash scripts in Parallel.

installsimple_gpu_schedulerpip install simple_gpu_scheduler

pip install simple_gpu_scheduler

```
pip install simple_gpu_scheduler
```

run hundreds of experiments in one line 😎cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same method

cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same method

```
cdRAGLAB
simple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_run-llama3_8b-baseline-scripts.txt#Other scripts can be run using the same method
```

#Other scripts can be run using the same method

how to write your_script.txt?here is an example#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.sh

#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.sh

```
#auto_inference_selfreg-7b.txtsh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-adaptive_retrieval-pregiven_passages.sh
sh run/rag_inference/selfrag_reproduction/selfrag_reproduction-evaluation-short_form-PubHealth-always_retrieval-pregiven_passages.sh
```

#auto_inference_selfreg-7b.txt

Evaluation for ALCE & Factscore

## Evaluation for ALCE & Factscore

RAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.

RAGLAB includes 3 classic evaluation methods: accuracy, F1, and EM (Exact Match). These 3 methods are simple to calculate, so they can be computed dynamically during the inference process. However, ALCE and Factscore, two advanced metrics, require the completion of the inference process before evaluation.

ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txt

ALCE: RAGLAB has integrated the ALCE repository into RAGLAB. You only need to set the path for the inference results in the config file.

cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txt

```
cdRAGLABcdrun/ALCE/#Change the path in each sh file for the inference generated files#For example:#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \#--mauve \#--qasimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_ALCE.txt
```

#Change the path in each sh file for the inference generated files

#python  ./ALCE/eval.py --f './data/eval_results/ASQA/{your_input_file_path}.jsonl' \

The evaluation results will be in the same directory as the input file, with the file name suffix.score

The evaluation results will be in the same directory as the input file, with the file name suffix.score

Factscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.

Factscore: The Factscore environment requires installation oftorch 1.13.1, which conflicts with the flash-attn version needed in RAGLAB's training and inference modules. Therefore, RAGLAB currently cannot integrate the Factscore environment, so users need to install theFactscoreenvironment separately for evaluation.

After installing the Factscore environment, please modify the path of the inference results in the bash filecdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txt

After installing the Factscore environment, please modify the path of the inference results in the bash file

cdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txt

```
cdRAGLAB/run/Factscore/#change the path in each sh file for the inference generated files#For example:#python  ./FActScore/factscore/factscorer.py  \#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \#--model_name "retrieval+ChatGPT"\#--openai_key ./api_keys.txt \#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \#--verbosesimple_gpu_scheduler --gpus 0,1,2,3,4,5,6,7<auto_gpu_scheduling_scripts/auto_eval_Factscore.txt
```

#change the path in each sh file for the inference generated files

#python  ./FActScore/factscore/factscorer.py  \

#--input_path './data/eval_results/Factscore/{your_input_file_path}.jsonl' \

#--model_name "retrieval+ChatGPT"\

#--openai_key ./api_keys.txt \

#--data_dir ./data/retrieval/colbertv2.0_passages/wiki2023 \

The evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.json

The evaluation results will be in the same directory as the input file, with the file name suffix_factscore_output.json

```
_factscore_output.json
```

NoteDuring the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscore

During the Factscore evaluation process, we used GPT-3.5 as the evaluation model, so there's no need to download a local model. If you need to use a local model to evaluate Factscore, please refer toFactscore

Process knowledge database from source

# Process knowledge database from source

If you wish to process the knowledge database yourself, please refer to the following steps. RAGLAB has already uploaded the processed knowledge database toHugging Face

document:process_wiki.md

This section covers the process of training models in RAGLAB. You can either download all pre-trained models from HuggingFace🤗, or use the tutorial below to train from scratch📝.

All dataprovides all data necessary for finetuning.

document:train_docs.md

If you find this repository useful, please cite our work.

@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}

```
@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}
```

```
@inproceedings{zhang-etal-2024-raglab,
    title = "{RAGLAB}: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation",
    author = "Zhang, Xuanwang and
      Song, Yunze and
      Wang, Yidong and
      Tang, Shuyun and
      others",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2024",
    publisher = "Association for Computational Linguistics",
}
```

RAGLAB is licensed under theMIT License.

About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repositoryReleasesNo releases publishedPackages0No packages publishedContributors3fate-ubwjim zhangYunzeSongYun-Ze SongjeremiahbuckleyLanguagesPython86.5%Shell13.5%

About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repositoryReleasesNo releases publishedPackages0No packages publishedContributors3fate-ubwjim zhangYunzeSongYun-Ze SongjeremiahbuckleyLanguagesPython86.5%Shell13.5%

About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repository

About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repository

About[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generationarxiv.org/abs/2408.11381Topicsragllmretrieval-augmented-generationfair-comparisonResourcesReadmeLicenseMIT licenseUh oh!There was an error while loading.Please reload this page.ActivityStars309starsWatchers1watchingForks35forksReport repository

[EMNLP 2024: Demo Oral] RAGLAB: A Modular and Research-Oriented Unified Framework for Retrieval-Augmented Generation

arxiv.org/abs/2408.11381

arxiv.org/abs/2408.11381

ragllmretrieval-augmented-generationfair-comparison

ragllmretrieval-augmented-generationfair-comparison

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

There was an error while loading.Please reload this page.

ReleasesNo releases published

ReleasesNo releases published

No releases published

Packages0No packages published

Packages0No packages published

No packages published

Contributors3fate-ubwjim zhangYunzeSongYun-Ze Songjeremiahbuckley

Contributors3fate-ubwjim zhangYunzeSongYun-Ze Songjeremiahbuckley

LanguagesPython86.5%Shell13.5%

LanguagesPython86.5%Shell13.5%

