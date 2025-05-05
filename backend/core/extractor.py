"""
Module for extracting and processing Terms & Conditions content from URLs.
"""
import requests
from bs4 import BeautifulSoup
import re


class TextExtractor:
    """A class to extract text content from web pages."""
    
    def extract_from_url(self, url: str) -> str:
        """Extract text content from a URL."""
        try:
            # Request with a realistic user agent
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            
            # Check if request was successful
            if response.status_code >= 400:
                print(f"[ERROR] Failed to load URL: {url} - Status code: {response.status_code}")
                return ""
                
            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove unwanted elements
            for tag in ['script', 'style', 'nav', 'footer', 'header', 'aside', 'iframe', 'noscript']:
                for element in soup.find_all(tag):
                    element.decompose()
            
            # Extract all paragraphs and headings
            content = []
            
            # Process headings (more important text)
            for i in range(1, 7):
                for heading in soup.find_all(f'h{i}'):
                    text = heading.get_text(strip=True)
                    if text:
                        content.append(f"\n\n{text}\n")
            
            # Process paragraphs (most of the readable content)
            for p in soup.find_all('p'):
                text = p.get_text(strip=True)
                if text:
                    content.append(text)
            
            # Process list items
            for li in soup.find_all('li'):
                text = li.get_text(strip=True)
                if text:
                    content.append(f"• {text}")
            
            # If we didn't get much content, try getting text from divs
            if len(''.join(content)) < 200:
                for div in soup.find_all('div'):
                    # Only get text from divs that look like content (not tiny UI elements)
                    if not div.find_all('div') and len(div.get_text(strip=True)) > 40:
                        content.append(div.get_text(strip=True))
            
            # If still very little content, get body text as a last resort
            if len(''.join(content)) < 200 and soup.body:
                body_text = soup.body.get_text(separator=' ', strip=True)
                # Try to break into logical paragraphs
                paragraphs = re.split(r'(?<=\.)\s+(?=[A-Z])', body_text)
                content = [p.strip() for p in paragraphs if len(p.strip()) > 30]
            
            # Combine all content with proper spacing
            result = '\n\n'.join(content)
            
            # Clean up the result
            result = re.sub(r'\s+', ' ', result)  # Normalize spaces
            result = re.sub(r'\n\s*\n', '\n\n', result)  # Fix multiple newlines
            result = re.sub(r'\s+([.,;:!?])', r'\1', result)  # Fix spacing before punctuation
            
            return result.strip()
            
        except Exception as e:
            print(f"[ERROR] Failed to process URL: {url}\n{e}")
            return "Error extracting text from URL"

