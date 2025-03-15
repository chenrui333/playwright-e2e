# latest tag points to sha256:02810c978d5396bf382ab6015c25ad6bed9e39f4a41c5b9c829e9fea439274e2
# and got updated on 08/16/2024
# while 1.51.0 was updated on 03/06/2025
FROM mcr.microsoft.com/playwright:1.51.0

COPY package.json package-lock.json* ./

RUN npm ci

COPY . .

# Run tests with an HTML reporter that outputs results to /app/playwright-report
CMD ["npx", "playwright", "test", "--reporter=html"]
