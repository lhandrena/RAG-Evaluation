# RAG Sources - Web Scraping

## How to Use

This folder contains a list of URLs that will be scraped to generate markdown files for RAG.

### Adding URLs

Simply paste any URLs you want to scrape below in the "Interesting Links for RAG" section. The scraper will automatically extract and process all URLs starting with `http://` or `https://`.

### Running the Scraper

From the project root directory, run:

```bash
cd src/advanced_rag/scraping
python crawlee_scraper.py
```

Or from the `src/advanced_rag/scraping` directory:

```bash
python crawlee_scraper.py
```

### Output

- Scraped content will be saved as markdown files in the `scraped_data/` subfolder
- Each URL will generate a separate `.md` file with a sanitized filename based on the URL
- The scraper uses Playwright to handle JavaScript-heavy sites (Twitter/X, HuggingFace, etc.)
- All files will include the source URL and extracted content from the page

### Folder Structure

```
rag_sources/
├── readme.md          # This file - add URLs here
└── scraped_data/      # Generated markdown files from scraping
    ├── github_com_example.md
    ├── x_com_example.md
    └── ...
```

---

# Interesting Links for RAG:


https://github.com/NirDiamant/RAG_Techniques

https://cohere.com/blog/rerank-3pt5?utm_source=substack&utm_medium=email

https://engineering.salesforce.com/the-next-generation-of-rag-how-enriched-index-redefines-information-retrieval-for-llms/?utm_source=substack&utm_medium=email

https://x.com/llama_index/status/1878881368186454161

https://x.com/TheTuringPost/status/1878590804325011727

https://www.galileo.ai/blog/mastering-rag-8-scenarios-to-test-before-going-to-production

https://arxiv.org/pdf/2408.11381
https://x.com/rohanpaul_ai/status/1838259514237464893

https://www.wandb.courses/courses/rag-in-production

https://www.modular.com/blog/use-max-with-open-webui-for-rag-and-web-search?utm_campaign=community&utm_medium=email&_hsmi=344518782&utm_content=344408490&utm_source=hs_email

https://x.com/akshay_pachaar/status/1886396550089511119

https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/

https://x.com/LangChainAI/status/1890808291145466085

https://www.linkedin.com/pulse/stoppt-den-hype-fehler-rag-semantische-suche-es-geht-um-biswanger-jvove

https://www.m3-konferenz.de/veranstaltung-83002-se-0-effizientes-retrieval-in-rag-systemen-methoden-optimierungen-und-best-practices.html

https://www.m3-konferenz.de/veranstaltung-83005-se-0-wie-gut-arbeitet-mein-rag-system-wirklich.html

https://x.com/Aurimas_Gr/status/1897989134905393416

https://github.com/DEEP-PolyU/Awesome-GraphRAG

https://x.com/llama_index/status/1898089137649205294
https://github.com/yWorks/yfiles-graph-for-create-llama

https://github.com/Shubhamsaboo/awesome-llm-apps

https://huggingface.co/spaces/mteb/leaderboard

https://x.com/victorialslocum/status/1904504036369543464

https://www.linkedin.com/posts/eordax_generativeai-rag-llms-activity-7312101448740184064-1vMN?utm_source=share&utm_medium=member_desktop&rcm=ACoAABL4hZgBRj0FruXwN4L4sqpnAkE7UqKimTo

https://x.com/jerryjliu0/status/1909642619086684428

https://x.com/TheTuringPost/status/1913915061388849613

https://x.com/akshay_pachaar/status/1920818537968660949

https://www.youtube.com/watch?v=cHVQj7w9TD4

https://galileo.ai/blog/how-do-you-choose-the-right-metrics-for-your-ai-evaluations

https://github.com/fate-ubw/RAGLab?tab=readme-ov-file

https://x.com/jerryjliu0/status/1932852719292985359

https://www.youtube.com/watch?v=RR5le0K4Wtw

https://www.linkedin.com/posts/jjackyliang_after-2-years-of-hype-companies-are-finally-activity-7349518837433647106-KZh6?utm_source=share&utm_medium=member_desktop&rcm=ACoAABL4hZgBRj0FruXwN4L4sqpnAkE7UqKimTo

https://www.youtube.com/watch?v=zeAyuLc_f3Q
https://www.youtube.com/watch?v=knDDGYHnnSI

https://x.com/_avichawla/status/1952256615215976745

https://x.com/_avichawla/status/1955880423302865341

https://x.com/philipvollet/status/1955945448860008655

https://x.com/tuanacelik/status/1957790764873970159?t=2zltxHygZApuYRQraW6s2Q&s=19


https://x.com/_avichawla/status/1977260787027919209
https://github.com/facebookresearch/refrag

https://x.com/techNmak/status/1980156741066133683?t=RGBXF-br-TSAGLqWa71ybg&s=19

https://x.com/rohanpaul_ai/status/1979860725498876077?t=LN6t3LvBm2BOzfn32vWmSw&s=19