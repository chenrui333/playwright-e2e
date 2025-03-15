# latest tag points to sha256:02810c978d5396bf382ab6015c25ad6bed9e39f4a41c5b9c829e9fea439274e2
# and got updated on 08/16/2024
# while 1.51.0 was updated on 03/06/2025
# Ubuntu 24.04 LTS (Noble Numbat), image tags include noble
# Ubuntu 22.04 LTS (Jammy Jellyfish), image tags include jammy
FROM mcr.microsoft.com/playwright:v1.51.0-noble@sha256:dcc7a57c035cea22d94ef62edaf4e63b2d84352d990f936424344c6b05a3d9b4

ENV CI=true

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm ci

COPY . .

# Run tests with an HTML reporter that outputs results to /app/playwright-report
CMD ["npx", "playwright", "test", "--reporter=html"]
