from google.adk.agents import Agent
from dotenv import load_dotenv
from playwright.async_api import async_playwright
import os
import asyncio
import base64

load_dotenv('./.env')

root_agent_model="gemini-2.0-flash-exp"
tester_agent_model="gemini-2.0-flash"

async def visual_testing(url: str = "demo-url") -> dict:
    """Performs visual testing on a webpage using Playwright.
    
    Args:
        url (str): The URL of the webpage to test. Defaults to "demo-url".
    
    Returns:
        dict: A dictionary containing test results and screenshots.
    """
    try:
        async with async_playwright() as p:
            # Launch browser
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            # Navigate to the page
            await page.goto(url)
            
            # Take screenshot and convert to base64
            screenshot_bytes = await page.screenshot()
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
            
            # Basic visual checks
            viewport_size = page.viewport_size
            page_content = await page.content()
            
            # Close browser
            await browser.close()
            
            # Create markdown image string
            image_markdown = f"![Screenshot](data:image/png;base64,{screenshot_base64})"
            
            return {
                "status": "success",
                "screenshot": image_markdown,
                "viewport_size": viewport_size,
                "content_length": len(page_content),
                "message": "Visual testing completed successfully"
            }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "message": "Visual testing failed"
        }

tester_agent = Agent(
    name= "tester_agent",
    model=tester_agent_model,
    description="Handles visual testing and quality assurance tasks using Playwright.",
    instruction="""You are a testing agent specialized in visual testing and quality assurance.

**Available Tools**:
- visual_testing: Performs visual testing on webpages using Playwright

**Response Guidelines**:
- Always start your response with the screenshot in markdown format
- Then provide the test results and analysis
- Explain any issues found during testing
- Suggest improvements when possible

**Testing Process**:
1. Navigate to the specified URL
2. Capture and encode screenshot
3. Perform basic visual checks
4. Report results with details and screenshot

**Response Format**:
1. Screenshot (in markdown format)
2. Test Status: Success/Failure
3. Viewport Information
4. Content Analysis
5. Recommendations (if any)

IMPORTANT: Always include the screenshot at the beginning of your response using the markdown format provided in the tool response.""",
    tools=[visual_testing]
    )
