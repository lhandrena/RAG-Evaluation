# Source: https://www.modular.com/blog/use-max-with-open-webui-for-rag-and-web-search?utm_campaign=community&utm_medium=email&_hsmi=344518782&utm_content=344408490&utm_source=hs_email

# GitHub - modular/max-agentic-cookbook: MAX Agentic Cookbook

modular/max-agentic-cookbookPublicNotificationsYou must be signed in to change notification settingsFork12Star38MAX Agentic Cookbookdocs.modular.com/LicenseView license38stars12forksBranchesTagsActivityStarNotificationsYou must be signed in to change notification settings

modular/max-agentic-cookbookPublicNotificationsYou must be signed in to change notification settingsFork12Star38

modular/max-agentic-cookbookPublic

modular/max-agentic-cookbookPublic

NotificationsYou must be signed in to change notification settingsFork12Star38

NotificationsYou must be signed in to change notification settings

MAX Agentic Cookbookdocs.modular.com/LicenseView license38stars12forksBranchesTagsActivityStarNotificationsYou must be signed in to change notification settings

MAX Agentic Cookbookdocs.modular.com/LicenseView license38stars12forksBranchesTagsActivityStarNotificationsYou must be signed in to change notification settings

38stars12forksBranchesTagsActivity

StarNotificationsYou must be signed in to change notification settings

NotificationsYou must be signed in to change notification settings

modular/max-agentic-cookbookmain5Branches8TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all filesRepository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:DiscordAboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repositoryUh oh!There was an error while loading.Please reload this page.Contributors14LanguagesPython62.5%TypeScript27.3%Mojo7.0%JavaScript1.2%Shell0.7%Dockerfile0.6%Other0.7%

# modular/max-agentic-cookbook

main5Branches8TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all filesRepository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:DiscordAboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repositoryUh oh!There was an error while loading.Please reload this page.Contributors14LanguagesPython62.5%TypeScript27.3%Mojo7.0%JavaScript1.2%Shell0.7%Dockerfile0.6%Other0.7%

main5Branches8TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all filesRepository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:DiscordAboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repositoryUh oh!There was an error while loading.Please reload this page.Contributors14LanguagesPython62.5%TypeScript27.3%Mojo7.0%JavaScript1.2%Shell0.7%Dockerfile0.6%Other0.7%

main5Branches8TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all filesRepository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:DiscordAboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repositoryUh oh!There was an error while loading.Please reload this page.Contributors14LanguagesPython62.5%TypeScript27.3%Mojo7.0%JavaScript1.2%Shell0.7%Dockerfile0.6%Other0.7%

main5Branches8TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all filesRepository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:Discord

main5Branches8TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all filesRepository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:Discord

main5Branches8TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all filesRepository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:Discord

main5Branches8TagsGo to fileCodeOpen more actions menu

Go to fileCodeOpen more actions menu

Open more actions menu

Open more actions menu

Folders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all filesRepository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:Discord

Folders and filesNameNameLast commit messageLast commit dateLatest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details.vscode.vscode[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025apps/cookbookapps/cookbookAdd placeholder chapter navigation (#96)Oct 17, 2025archivearchive[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025docsdocsAdd placeholder chapter navigation (#96)Oct 17, 2025packages/recipespackages/recipes[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.dockerignore.dockerignore[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025.gitignore.gitignoreAdd placeholder chapter navigation (#96)Oct 17, 2025.prettierrc.prettierrc[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025CODE_OF_CONDUCT.mdCODE_OF_CONDUCT.mdAdd code of conductFeb 12, 2025LICENSELICENSEAdd LICENSEFeb 12, 2025README.mdREADME.mdUpdate figcaption style to be hiddenOct 17, 2025package.jsonpackage.json[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-lock.yamlpnpm-lock.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025pnpm-workspace.yamlpnpm-workspace.yaml[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)Oct 17, 2025View all files

Latest commitwilliamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025c5c158f·Oct 17, 2025History202 CommitsOpen commit details

williamwUpdate figcaption style to be hiddenOpen commit detailsOct 17, 2025

Update figcaption style to be hiddenOpen commit details

Update figcaption style to be hidden

Update figcaption style to be hidden

c5c158f·Oct 17, 2025History202 CommitsOpen commit details

History202 CommitsOpen commit details

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

Add placeholder chapter navigation (#96)

Add placeholder chapter navigation (#96)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

Add placeholder chapter navigation (#96)

Add placeholder chapter navigation (#96)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

Add placeholder chapter navigation (#96)

Add placeholder chapter navigation (#96)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

Update figcaption style to be hidden

Update figcaption style to be hidden

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

[cookbook] Restructure repo, rename to max-agentic-cookbook (#95)

Repository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:Discord

Repository files navigationModular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:Discord

Repository files navigation

## Repository files navigation

Modular Agentic CookbookA collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.Example conversation: User asks for a joke about Mojo, the smiling fireball who makes GPUs go brrr. The assistant responds: "Why did Mojo the smiling fireball get a job optimizing GPUs? Because he said, 'I'm here to bring the heat! Watch these GPUs go brrr... with a smile, of course! Hope you enjoyed it!'"RequirementsNode.js22.x or higherpnpmpackage managerMAXserver running locally or remotely—see theMAX quickstartQuick StartClone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm installConfigure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'Start developingpnpm devOpenhttp://localhost:3000in your browserFeatured Recipes1.Multi-turn ChatBuild a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:Real-time token streaming using the Vercel AI SDKMarkdown rendering with syntax-highlighted code blocks using StreamdownAuto-scrolling message display with smart scroll detectionSeamless compatibility with Modular MAX and OpenAI-compatible endpoints2.Image CaptioningCreate an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generatedParallel processing: Multiple images processed simultaneously for maximum speedPerformance metrics: TTFT (time to first token) and duration trackingDrag-and-drop image upload with Mantine DropzoneCustomizable prompt for caption generationGallery view with loading states and real-time updatesArchitectureThe cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/For a deep dive into the architecture, see theArchitecture Guide.Adding New RecipesCreate a directory underpackages/recipes/src/your-recipe-name/with:ui.tsx- Frontend React component with inline documentationapi.ts- Backend API handler using Vercel AI SDKEach recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.For detailed instructions, see theContributing Guide.Using with MAXStart MAX model serving (see quickstart):max serve --model google/gemma-3-27b-itConfigure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.Docker DeploymentThe cookbook can run entirely in Docker with MAX model serving included. Build with:docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.Run with GPU support (NVIDIA example):docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latestThe container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.Available Scriptspnpm dev- Start development server with hot reloading (uses Turbopack)pnpm build- Build production-optimized bundlepnpm start- Run production serverpnpm lint- Run ESLint checkspnpm format- Format code with Prettierpnpm format:check- Check code formattingLearning ResourcesThe best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.Documentation:Modular MAXVercel AI SDKNext.jsMantine UIContributingContributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.SupportIssues:GitHub IssuesDiscussions:Modular ForumCommunity:Discord

Modular Agentic Cookbook

# Modular Agentic Cookbook

A collection of recipes demonstrating how to build modern fullstack web apps using Modular MAX, Next.js, and the Vercel AI SDK. Each recipe demonstrates an end-to-end workflow with both frontend and backend implementations, including detailed code comments.

📦 Looking for legacy recipes?Older standalone recipes have been moved to thearchive/folder. These are provided as-is for historical reference only and are no longer maintained.

Node.js22.x or higher

MAXserver running locally or remotely—see theMAX quickstart

Clone and installgit clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm install

git clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm install

```
git clone https://github.com/modular/max-agentic-cookbook.gitcdmax-agentic-cookbook
pnpm install
```

Configure endpointscp .sample.env .env.localEdit.env.localto add your MAX endpoint (or any OpenAI-compatible server):COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'

cp .sample.env .env.local

```
cp .sample.env .env.local
```

Edit.env.localto add your MAX endpoint (or any OpenAI-compatible server):

COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'

```
COOKBOOK_ENDPOINTS='[{"id": "max-local","baseUrl": "http://127.0.0.1:8000/v1","apiKey": "EMPTY"}]'
```

"baseUrl": "http://127.0.0.1:8000/v1",

Start developingpnpm devOpenhttp://localhost:3000in your browser

Openhttp://localhost:3000in your browser

Build a streaming chat interface that maintains conversation context across multiple exchanges. This recipe demonstrates:

Real-time token streaming using the Vercel AI SDK

Markdown rendering with syntax-highlighted code blocks using Streamdown

Auto-scrolling message display with smart scroll detection

Seamless compatibility with Modular MAX and OpenAI-compatible endpoints

Create an intelligent image captioning system that generates natural language descriptions for uploaded images with progressive streaming and performance tracking. Features include:

NDJSON streaming: Custom useNDJSON hook for progressive results—captions appear as they're generated

Parallel processing: Multiple images processed simultaneously for maximum speed

Performance metrics: TTFT (time to first token) and duration tracking

Drag-and-drop image upload with Mantine Dropzone

Customizable prompt for caption generation

Gallery view with loading states and real-time updates

The cookbook is organized as a pnpm workspace monorepo with a clean separation between the Next.js app and shared recipe implementations:

├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/

```
├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/
```

```
├── apps/cookbook/           # Next.js 14 App
│   ├── app/                 # App Router pages & API routes
│   ├── components/          # UI components
│   └── context/             # React context
│
└── packages/recipes/        # Shared recipe implementations
    └── src/
        ├── multiturn-chat/  # Each recipe has:
        │   ├── api.ts       # - Backend API logic
        │   └── ui.tsx       # - Frontend UI component
        └── image-captioning/
```

For a deep dive into the architecture, see theArchitecture Guide.

Create a directory underpackages/recipes/src/your-recipe-name/with:

```
packages/recipes/src/your-recipe-name/
```

ui.tsx- Frontend React component with inline documentation

api.ts- Backend API handler using Vercel AI SDK

Each recipe follows consistent patterns: React hooks for state management, Mantine UI components, and detailed inline comments explaining architecture decisions and data flow.

For detailed instructions, see theContributing Guide.

Start MAX model serving (see quickstart):

max serve --model google/gemma-3-27b-it

```
max serve --model google/gemma-3-27b-it
```

Configure the endpoint in.env.localand select it in the cookbook UI. The cookbook works with MAX or any OpenAI-compatible API.

The cookbook can run entirely in Docker with MAX model serving included. Build with:

docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.

```
docker build --ulimit nofile=65535:65535 -t max-cookbook:latest.
```

Run with GPU support (NVIDIA example):

docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latest

```
docker run --gpus all \
    -v~/.cache/huggingface:/root/.cache/huggingface \
    -e"HF_TOKEN=your-token"\
    -e"MAX_MODEL=mistral-community/pixtral-12b"\
    -p 8000:8000 -p 3000:3000 \
    max-cookbook:latest
```

"HF_TOKEN=your-token"

"MAX_MODEL=mistral-community/pixtral-12b"

The container supports both NVIDIA and AMD GPUs. For detailed instructions including AMD setup, build arguments, and troubleshooting, see theDocker Guide.

pnpm dev- Start development server with hot reloading (uses Turbopack)

pnpm build- Build production-optimized bundle

pnpm start- Run production server

pnpm lint- Run ESLint checks

pnpm format- Format code with Prettier

pnpm format:check- Check code formatting

The best way to learn is by running the cookbook and exploring the recipes. Toggle "Show Code" in the UI to see implementations alongside demos. Each recipe contains extensive inline documentation explaining architecture decisions and integration patterns.

Contributions welcome! Fork the repo, create a feature branch, follow established patterns, and submit a pull request. Ensure proper TypeScript types and comprehensive inline documentation.

See theContributing Guidefor detailed instructions on adding recipes, code standards, and the PR process.

Discussions:Modular Forum

AboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repositoryUh oh!There was an error while loading.Please reload this page.Contributors14LanguagesPython62.5%TypeScript27.3%Mojo7.0%JavaScript1.2%Shell0.7%Dockerfile0.6%Other0.7%

AboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repositoryUh oh!There was an error while loading.Please reload this page.Contributors14LanguagesPython62.5%TypeScript27.3%Mojo7.0%JavaScript1.2%Shell0.7%Dockerfile0.6%Other0.7%

AboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repository

AboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repository

AboutMAX Agentic Cookbookdocs.modular.com/TopicsrecipesmodularmaxgenaiResourcesReadmeLicenseView licenseCode of conductCode of conductContributingContributingUh oh!There was an error while loading.Please reload this page.ActivityCustom propertiesStars38starsWatchers8watchingForks12forksReport repository

recipesmodularmaxgenai

recipesmodularmaxgenai

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

Uh oh!There was an error while loading.Please reload this page.

There was an error while loading.Please reload this page.

LanguagesPython62.5%TypeScript27.3%Mojo7.0%JavaScript1.2%Shell0.7%Dockerfile0.6%Other0.7%

LanguagesPython62.5%TypeScript27.3%Mojo7.0%JavaScript1.2%Shell0.7%Dockerfile0.6%Other0.7%

