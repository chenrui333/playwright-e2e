default: test

test:
  DEBUG=pw:webserver npx playwright test
