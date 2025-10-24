import asyncio
import os
import re
from urllib.parse import urlparse

from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext


OUTPUT_DIRECTORY = "rag_sources/scraped_data"


def sanitize_filename(url):
    """Create a safe filename from a URL"""
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    path = parsed.path.strip('/').replace('/', '_')
    
    if path:
        filename = f"{domain}_{path}"
    else:
        filename = domain
    
    # Remove invalid characters and limit length
    filename = re.sub(r'[^\w\-_]', '_', filename)
    filename = filename[:100]
    
    return filename + ".md"


def extract_urls_from_markdown(md_file_path):
    """Extract URLs from a markdown file"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        url_pattern = r'https?://[^\s\)\]<>]+'
        return re.findall(url_pattern, content)


async def main():
    # Create output directory
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    
    # Extract URLs from readme file (now in rag_sources folder)
    readme_path = os.path.join(os.path.dirname(__file__), "rag_sources", "readme.md")
    readme_path = os.path.normpath(readme_path)
    
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found")
        return
    
    print(f"Extracting URLs from {readme_path}...")
    urls = extract_urls_from_markdown(readme_path)
    
    if not urls:
        print("No URLs found in readme file")
        return
    
    print(f"Found {len(urls)} URLs to scrape\n")
    
    # Track results
    results = {"success": 0, "failed": 0}
    
    # Create crawler with Playwright for JavaScript support
    crawler = PlaywrightCrawler(
        max_requests_per_crawl=len(urls),
        max_request_retries=2,
        max_crawl_depth=0,  # Don't follow links, only scrape provided URLs
        headless=True,  # Run without visible browser window
        browser_type='chromium',
    )
    
    @crawler.router.default_handler
    async def request_handler(context: PlaywrightCrawlingContext) -> None:
        """Handle each scraped page"""
        url = context.request.url
        
        try:
            context.log.info(f'Processing {url}...')
            
            # Wait for page to load (important for JavaScript-heavy sites)
            try:
                await context.page.wait_for_load_state('networkidle', timeout=60000)
            except:
                # If networkidle times out, wait for domcontentloaded instead
                await context.page.wait_for_load_state('domcontentloaded')
            
            # Get page content
            content = await context.page.content()
            
            # Parse with BeautifulSoup
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            
            # Remove unwanted elements
            for selector in [
                'script', 'style', 'nav', 'header', 'footer', 'aside',
                'iframe', '.navigation', '.nav', '.menu', '.sidebar',
                '.advertisement', '.ad', '.banner', '.cookie', '.social-share'
            ]:
                for elem in soup.select(selector):
                    elem.decompose()
            
            # Try to find main content
            main_content = None
            for selector in ['main', 'article', '[role="main"]', '.content', '#content', '.main', '#main']:
                main_content = soup.select_one(selector)
                if main_content:
                    break
            
            if not main_content:
                main_content = soup.find('body') or soup
            
            # Build content
            content_parts = [f"# Source: {url}\n\n"]
            
            # Add title
            title = await context.page.title()
            if title:
                content_parts.append(f"# {title}\n\n")
            
            # Extract text content
            for tag in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'pre', 'code', 'span', 'div']):
                text = tag.get_text(strip=True)
                if text and len(text) > 20:
                    if tag.name.startswith('h'):
                        level = int(tag.name[1])
                        content_parts.append(f"{'#' * level} {text}\n\n")
                    elif tag.name in ['pre', 'code']:
                        content_parts.append(f"```\n{text}\n```\n\n")
                    else:
                        content_parts.append(f"{text}\n\n")
            
            full_content = ''.join(content_parts)
            full_content = re.sub(r'\n{3,}', '\n\n', full_content)
            
            # Save to file
            filename = sanitize_filename(url)
            file_path = os.path.join(OUTPUT_DIRECTORY, filename)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            results["success"] += 1
            print(f"✓ Scraped: {url} -> {filename}")
            
        except Exception as e:
            results["failed"] += 1
            print(f"✗ Failed: {url} - {str(e)}")
    
    # Run the crawler
    await crawler.run(urls)
    
    print(f"\n{'='*60}")
    print(f"Scraping complete!")
    print(f"Success: {results['success']}, Failed: {results['failed']}")
    print(f"Files saved to: {OUTPUT_DIRECTORY}/")
    print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(main())
