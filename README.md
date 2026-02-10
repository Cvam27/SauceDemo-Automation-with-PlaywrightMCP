# SauceDemo Automation Testing

This project automates testing for the SauceDemo website using Playwright and Python with Page Object Model. The entire project was created using Playwright MCP.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   playwright install
   ```

2. Run tests:
   ```bash
   pytest
   ```

## Test Cases

- Login tests (valid/invalid scenarios)
- Product management (add, remove, sort)
- Cart functionality
- Checkout process
- Logout

## Features

- Page Object Model structure
- Screenshots and videos on test failures
- Retry mechanism (2 retries)
- GitHub Actions CI/CD
