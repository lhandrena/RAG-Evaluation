# Source: https://x.com/philipvollet/status/1955945448860008655
Number of words: 1297

# Philip Vollet on X: "This will retire 90% of RAG systems with dignity (and a sad song playlist). Powered by DSPy: If you're still building "text in, text out" chatbots that only perform blind vector and text searches, you're not gonna make it! My team just dropped Elysia, and it's not just an https://t.co/6FbESB2c0h" / X

This will retire 90% of RAG systems with dignity (and a sad song playlist). Powered by DSPy: If you're still building "text in, text out" chatbots that only perform blind vector and text searches, you're not gonna make it!

My team just dropped Elysia, and it's not just an incremental successor to Verba… It's a whole rethink of how we interact with our data using AI.

𝗪𝗵𝗮𝘁 𝗶𝘀 𝗘𝗹𝘆𝗶𝘀𝗮?
An open-source platform for building agentic RAG architectures. It learns from your preferences, intelligently categorizes, labels, and searches through your data, and provides complete transparency into its decision-making process.

The long & exciting feature list:

• 𝗧𝗿𝗮𝗻𝘀𝗽𝗮𝗿𝗲𝗻𝘁 𝗗𝗲𝗰𝗶𝘀𝗶𝗼𝗻-𝗧𝗿𝗲𝗲 𝗔𝗴𝗲𝗻𝘁𝘀: Elysia’s core is a customizable decision tree, and it visualizes its entire reasoning process, showing you why it chooses a specific tool or path.

It enables advanced error handling, self-healing from failed queries, and prevents infinite loops. You can also add custom tools and branches to build complex, state-aware workflows.

• 𝗗𝗮𝘁𝗮 𝗔𝘄𝗮𝗿𝗲𝗻𝗲𝘀𝘀: Before it even attempts a query, Elysia performs a full analysis of your data collections. This eliminates the blind search problem plaguing most RAG systems and allows for far more complex and accurate query generation.

• 𝗗𝘆𝗻𝗮𝗺𝗶𝗰 𝗗𝗮𝘁𝗮 𝗗𝗶𝘀𝗽𝗹𝗮𝘆𝘀: Your RAG pipeline shouldn't be limited to text, right? That’s why Elysia analyzes each query's results and chooses the best way to display them, from tables and charts to product cards and GitHub tickets. It also features a comprehensive data explorer with search, sorting, and filtering capabilities.

• 𝗛𝘆𝗽𝗲𝗿-𝗣𝗲𝗿𝘀𝗼𝗻𝗮𝗹𝗶𝘇𝗮𝘁𝗶𝗼𝗻 𝘃𝗶𝗮 𝗙𝗲𝗲𝗱𝗯𝗮𝗰𝗸: It uses your positively-rated queries as few-shot examples to improve future responses. This allows you to use smaller, faster models that perform like larger ones over time, cutting costs without sacrificing quality for most use cases.

• 𝗖𝗵𝘂𝗻𝗸-𝗢𝗻-𝗗𝗲𝗺𝗮𝗻𝗱: Elysia chunks documents at query time. It performs initial searches on document-level vectors and only chunks relevant documents on the fly, storing them in a parallel quantized collection with cross references for future use.

𝗧𝗵𝗲 𝗦𝘁𝗮𝗰𝗸
Elysia is built from scratch on Weaviate, using its native features like named vectors, a variety of search types, filters, cross references, quantization, etc. It uses DSPy for LLM interactions and is delivered as a production-ready application via FastAPI, serving a NextJS frontend as static HTML.

Also available as a Python package via pip:

𝗽𝗶𝗽 𝗶𝗻𝘀𝘁𝗮𝗹𝗹 𝗲𝗹𝘆𝘀𝗶𝗮-𝗮𝗶

Type: 𝗲𝗹𝘆𝘀𝗶𝗮 𝘀𝘁𝗮𝗿𝘁

Connect your Weaviate cluster and go explore what’s possible.


https://github.com/weaviate/elysia

Elysia is an agentic platform designed to use tools in a decision tree. A decision agent decides which tools to use dynamically based on its environment and context. You can use custom tools or use the pre-built tools designed to retrieve your data in a Weaviate cluster.

Read the docs!

    💡 Don't forget to check out the Github Repository for the Frontend!

Installation is as simple as:

pip install elysia-ai

Demo of Elysia
Watch our newest Elysia video here:

https://youtu.be/PhCrlpUwEhU?si=rnJVBziKTEdPJiKz
Table of Contents

    Get started (App)
    Get Started (Python)
    Installation
        PyPi (Recommended)
        GitHub
        Configuring Settings
    Architecture
    Open Source Spirit
    FAQ

Get started (App)

Run the app via

elysia start

Then head to localhost:8000 in a browser, navigate to the settings page, add your required API keys, Weaviate cloud cluster details and specify your models. Optionally use --port to specify which port Elysia will be run on.

Alternatively, we have created a demo version of Elysia (rate-limited, fixed datasets) to experiment with. Find it at: https://elysia.weaviate.io/
Get Started (Python)

To use Elysia, you need to either set up your models and API keys in your .env file, or specify them in the config. See the setup page to get started.

Elysia can be used very simply:

from elysia import tool, Tree

tree = Tree()

@tool(tree=tree)
async def add(x: int, y: int) -> int:
    return x + y

tree("What is the sum of 9009 and 6006?")

Elysia is pre-configured to be capable of connecting to and interacting with your Weaviate clusters!

import elysia
tree = elysia.Tree()
response, objects = tree(
    "What are the 10 most expensive items in the Ecommerce collection?",
    collection_names = ["Ecommerce"]
)

This will use the built-in open source query tool or aggregate tool to interact with your Weaviate collections. To get started connecting to Weaviate, see the setting up page in the docs.
Installation (bash) (Linux/MacOS)
PyPi (Recommended)

Elysia requires Python 3.12:

    Installation via brew (macOS)
    Installation via installer (Windows)
    Installation (Ubuntu)

Optionally create a virtual environment via

python3.12 -m venv .venv
source .venv/bin/activate

Then simply run

pip install elysia-ai

to install straight away!
GitHub

To get the latest development version, you can clone the github repo by running

git clone https://github.com/weaviate/elysia

move to the working directory via

cd elysia

Create a virtual environment with Python (version 3.10 - 3.12)

python3.12 -m venv .venv
source .venv/bin/activate

and then install Elysia via pip

pip install -e .

Done! You can now use the Elysia python package
Configuring Settings

Settings page

To use Elysia with Weaviate, i.e. for agentic searching and retrieval, you need to either have a locally running instance of Weaviate, or access to a Weaviate cloud cluster via an api key and URL. This can be specific in the app directly (see above image), or by creating a .env file with

WCD_URL=...
WCD_API_KEY=...
WEAVIATE_IS_LOCAL=... # True or False

Elysia will automatically detect these when running locally, and this will be the default Weaviate cluster for all users logging into the Elysia app. But these can be configured on a user-by-user basis through the config.

Whichever vectoriser you use for your Weaviate collection you will need to specify your corresponding API key, e.g.

OPENAI_API_KEY=...

These will automatically be added to the headers for the Weaviate client.

Same for whichever model you choose for the LLM in Elysia, so if you are using GPT-4o, for example, specify an OPENAI_API_KEY.

Elysia's recommended config is to use OpenRouter to give easy access to a variety of models. So this requires

OPENROUTER_API_KEY=...

Architecture

Elysia is architectured as a modern web application with a full-featured frontend for a responsive, real-time interface and a FastAPI backend serving both the web interface and API. The core logic is written in pure Python – what we call "blood, sweat, and tears" custom logic – with DSPy handling LLM interactions.

Unlike simple agentic platforms which have access to all possible tools at runtime, Elysia has a pre-defined web of possible nodes, each with a corresponding action. Each node in the tree is orchestrated by a decision agent with global context awareness about its environment and its available options. The decision agent evaluates its environment, available actions, past actions and future actions to strategize the best tool to use.

Read more about how we built Elysia in this blog.

Architecture Diagram
Open Source Spirit ✨

Weaviate is proud to offer this open source project for the community. While we strive to address issues as fast as we can, please understand that it may not be maintained with the same rigor as production software. We welcome and encourage community contributions to help keep it running smoothly. Your support in fixing open issues quickly is greatly appreciated.

See the full contributor guidelines to see how you can get started contributing to Elysia!
FAQ
How do I use Elysia with my own data?

Can I run Elysia completely locally? (Locally running Weaviate, local models)

Help! My local model isn't working with Elysia. It's timing out or there are errors.

How do I clear all my Elysia data?

Can I contribute to Elysia?

Where is the best place I can start contributing?

