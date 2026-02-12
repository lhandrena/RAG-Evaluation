# Source: https://x.com/akshay_pachaar/status/1886396550089511119
Number of words: 1739

# Akshay 🚀 on X: "Make your RAG application 10x smarter! ColiVara is a unique document retrieval method that does not need chunking or text processing. It still feels like RAG but without OCR, text extraction, broken tables, or missing images. What you see is what you get. ✨ Here’s why it’s a https://t.co/jPapIuG3i0" / X

Make your RAG application 10x smarter!

ColiVara is a unique document retrieval method that does not need chunking or text processing. It still feels like RAG but without OCR, text extraction, broken tables, or missing images.

What you see is what you get. ✨

Here’s why it’s a breakthrough:

🖼️ Vision-based indexing
⚙️ 100+ file format support
⚡ State-of-the-art multimodal retrieval
✨ APIs & SDKs for both Python/TypeScript
⬇️ No vector DB management (pgVector under the hood)

But that’s not all:

📚 Detailed documentation
✅ Seamless local or cloud quickstart
🧠 Late-interaction embeddings for extra accuracy

The best part, it's 100% open-source!

Link to the GitHub repo in next tweet!

https://github.com/tjmlabs/ColiVara
Colivara is a suite of services that allows you to store, search, and retrieve documents based on their visual embedding. ColiVara has state of the art retrieval performance on both text and visual documents. using vision models instead of chunking and text-processing for documents. No OCR, no text extraction, no broken tables, or missing images. 


ColiVara

State of the Art Retrieval - with a delightful developer experience

codecov Tests
Quickstart:

    Get a free API Key from the ColiVara Website.

    Install our Python/Typescript SDK and use it to interact with the API.

pip install colivara-py

or

npm install colivara-ts

    Index a document (a file url, base64 encoded file, or path). It supports over 100 file formats including PDF, DOCX, PPTX, and more.

from colivara_py import ColiVara

client = ColiVara(api_key=os.environ.get("COLIVARA_API_KEY"), # default and can be omitted
                  base_url="https://api.colivara.com"         # default and can be omitted
                  )

# Upload a document to the default_collection
document = client.upsert_document(
                  name="sample_document",       
                  document_url="https://example.com/sample.pdf",   # You can use a file path, base64 encoded file, or a URL
                  metadata={"author": "John Doe"},        # optional - add metadata
                  collection_name="user_1_collection",    # optional - specify a collection
                  wait=True                               # optional - wait for indexing (supports Webhooks)
)

or

import { ColiVara } from 'colivara-ts';

// Initialize the client
const client = new ColiVara('your-api-key');

// Upload a document
const document = await client.upsertDocument({
    name: 'sample_document',
    // optional - specify a collection
    collection_name: 'user_1_collection',
    // You can use a file path, base64 encoded file, or a URL
    document_url: 'https://example.com/sample.pdf',
    // optional - wait for the document to index. Webhooks are also supported.
    wait: true,
    // optional - add metadata
    metadata: { author: 'John Doe' }
});

    Search for a document. You can filter by collection name, collection metadata, and document metadata. You can also specify the number of results you want.

# Simple search
results = client.search("what is 1+1?")
# search with a specific collection
results = client.search("what is 1+1?", collection_name="user_1_collection")
# Search with a filter on document metadata
results = client.search(
    "what is 1+1?",
    query_filter={
        "on": "document",
        "key": "author",
        "value": "John Doe",
        "lookup": "key_lookup",  # or contains
    },
)
# Search with a filter on collection metadata
results = client.search(
    "what is 1+1?",
    query_filter={
        "on": "collection",
        "key": ["tag1", "tag2"],
        "lookup": "has_any_keys",
    },
)
# top 3 pages with the most relevant information
print(results)

In Typescript:

// Simple search
const results = await client.search({query: "what is 1+1?"})

// search with a specific collection
const results = await client.search({query: "what is 1+1?", collection_name: "user_1_collection"})

// Search with a filter on document metadata
const results = await client.search({
    query: "what is 1+1?",
    query_filter: {
        on: "document",
        key: "author",
        value: "John Doe",
        lookup: "key_lookup"
    }
})

// search with a filter on collection metadata
const results = await client.search({
    query: "what is 1+1?",
    query_filter: {
        on: "collection",
        key: ["tag1", "tag2"],
        lookup: "has_any_keys"
    }
})

// top 3 pages with the most relevant information
console.log(results)

Documentation:

Our documentation is available at docs.colivara.com.

Note

If you prefer Swagger, you can try our endpoints at ColiVara API Swagger. You can also import an openAPI spec (for example for Postman) from the swagger documentation endpoint at v1/docs/openapi.json
Why?

RAG (Retrieval Augmented Generation) is a powerful technique that allows us to enhance LLMs (Language Models) output with private documents and proprietary knowledge that is not available elsewhere. (For example, a company's internal documents or a researcher's notes).

However, it is limited by the quality of the text extraction pipeline. With limited ability to extract visual cues and other non-textual information, RAG can be suboptimal for documents that are visually rich.

ColiVara uses vision models to generate embeddings for documents, allowing you to retrieve documents based on their visual content.

From the ColPali paper:

    Documents are visually rich structures that convey information through text, as well as tables, figures, page layouts, or fonts. While modern document retrieval systems exhibit strong performance on query-to-text matching, they struggle to exploit visual cues efficiently, hindering their performance on practical document retrieval applications such as Retrieval Augmented Generation.

Learn More in the ColPali Paper

How does it work?

In short, ColPali is an advanced document retrieval model that leverages Vision Language Models to integrate both textual and visual elements for highly accurate and efficient document search. ColiVara builds on this model to provide a seamless and user-friendly API for document retrieval.

If my documents are text-based, why do I need ColiVara?

Even when your documents are text-based, ColiVara can provide a more accurate and efficient retrieval system. This is because ColiVara uses Late-Interaction style embeddings which is more accurate than pooled embeddings. Our benchmarks contains text-only datasets and we outperform existing systems on these datasets.

Do I need a vector database?

No - ColiVara uses Postgres and pgVector to store vectors for you. You DO NOT need to generate, save, or manage embeddings in anyway.

Do you covert the documents to markdown/text?

No - ColiVara treats everything as an image, and uses vision models. There are no parsing, chunking, or OCR involved. This method outperforms chunking, and OCR for both text-based documents and visual documents.

How does non-pdf documents or web pages work?

We run a pipeline to convert them to images, and perform our normal image-based retrieval. This all happen for you under the hood, and you get the top-k pages when performing retrieval.

Can I use my vector database?

Yes - we have an embedding endpoint that only generates embeddings without saving or doing anything else. You can store these embeddings at your end. Keep in mind that we use late-interaction and multi-vectors, many vector databases do not support this yet.

Do I have to use the SDKs?

No - the SDKs are provided for your convenience. You can use the REST API directly if you prefer.
Key Features

    State of the Art retrieval: ColiVara outperforms existing retrieval systems on both quality and latency.

    Wide Format Support: Supports over 100 file formats including PDF, DOCX, PPTX, and more.

    Filtering: ColiVara allows for filtering on collections and documents on arbitrary metadata fields. For example, you can filter documents by author or year. Or filter collections by type. You get the best of both worlds - structured and unstructured data.

    Convention over Configuration: The API is designed to be easy to use with opinionated and optimized defaults.

    Modern PgVector Features: We use HalfVecs for faster search and reduced storage requirements.

    REST API: Easy to use REST API with Swagger documentation.

    Comprehensive: Full CRUD operations for documents, collections, and users.

Evals:

We run independent evaluations with major releases. The evaluations are based on the ColPali paper and are designed to be reproducible. We use the Vidore dataset and leaderboard as the baseline for our evaluations.

Evaluation Results

You can run the evaluation independently using our eval repo at: https://github.com/tjmlabs/ColiVara-eval

ColPali Evals
Release 1.5.0 (hierarchical clustering) - latest
Benchmark 	Colivara Score 	Avg Latency (s) 	Num Docs
Average 	86.8 	---- 	----
ArxivQA 	87.6 	3.2 	500
DocVQA 	54.8 	2.9 	500
InfoVQA 	90.1 	2.9 	500
Shift Project 	87.7 	5.3 	1000
Artificial Intelligence 	98.7 	4.3 	1000
Energy 	96.4 	4.5 	1000
Government Reports 	96.8 	4.4 	1000
Healthcare Industry 	98.5 	4.5 	1000
TabFQuad 	86.6 	3.7 	280
TatDQA 	70.9 	8.4 	1663
Components:

    Postgres DB with pgvector extension for storing embeddings. (This repo)

    REST API for document/collection management (This repo)

    Embeddings Service. This needs a GPU with at least 8gb VRAM. The code is under ColiVarE repo and is optimized for a serverless GPU workload.

        You can run the embedding service separately and use your own storage and API for the rest of the components. The Embedding service is designed to be modular and can be used with any storage and API. (For example, if you want to use Qdrant for storage and Node for the API)

    Language-specific SDKs for the API
        Python SDK: colivara-py
        Typescript SDK: colivara-ts

Getting Started (Local Setup)

    Setup the Embeddings Service (ColiVarE) - This is a separate repo and is required for the API to work. The directions are available here: ColiVarE

    Clone the repo

git clone https://github.com/tjmlabs/ColiVara

    Create a .env.dev file in the root directory with the following variables:

EMBEDDINGS_URL="the serverless embeddings service url" # for local setup use http://host.docker.internal:8000/runsync
EMBEDDINGS_URL_TOKEN="the serverless embeddings service token"  # for local setup use any string will do.
AWS_S3_ACCESS_KEY_ID="an S3 or compatible storage access key"
AWS_S3_SECRET_ACCESS_KEY="an S3 or compatible storage secret key"
AWS_STORAGE_BUCKET_NAME="an S3 or compatible storage bucket name"

    Run the following commands:

docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
# get the token from the superuser creation
docker-compose exec web python manage.py shell
from accounts.models import CustomUser
user = CustomUser.objects.first().token 
print(user) # save this token somewhere (use it for authorization)

    Application will be running at http://localhost:8001 and the swagger documentation at http://localhost:8001/v1/docs

    To run tests - we have 100% test coverage

docker-compose exec web pytest

    mypy for type checking

docker-compose exec web mypy .

Support

For support, join our Discord community where you can:

    Get help with setup and configuration
    Report bugs and request features
    Connect with other ColiVara users
    Stay updated on new releases and announcements

Click the badge below to join:

Discord
License

This project is licensed under Functional Source License, Version 1.1, Apache 2.0 Future License. See the LICENSE.md file for details.

For commercial licensing, please contact us at tjmlabs.com. We are happy to work with you to provide a license that meets your needs.