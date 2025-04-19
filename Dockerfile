# latest tag points to sha256:02810c978d5396bf382ab6015c25ad6bed9e39f4a41c5b9c829e9fea439274e2
# and got updated on 08/16/2024
# while 1.51.0 was updated on 03/06/2025
# Ubuntu 24.04 LTS (Noble Numbat), image tags include noble
# Ubuntu 22.04 LTS (Jammy Jellyfish), image tags include jammy
FROM mcr.microsoft.com/playwright:v1.52.0-noble@sha256:a021500a801bab0611049217ffad6b9697d827205c15babb86a53bc1a61c02d5

ENV CI=true

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm ci

COPY . .

# Run tests with an HTML reporter that outputs results to /app/playwright-report
CMD ["npx", "playwright", "test", "--reporter=html"]
