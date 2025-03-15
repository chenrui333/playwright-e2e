FROM mcr.microsoft.com/playwright:latest

COPY package.json package-lock.json* ./

RUN npm ci

COPY . .

# Run tests with an HTML reporter that outputs results to /app/playwright-report
CMD ["npx", "playwright", "test", "--reporter=html"]
