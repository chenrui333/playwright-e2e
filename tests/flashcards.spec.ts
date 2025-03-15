import { test, expect } from '@playwright/test';

// use firefox on macos as test UA
test.use({ userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:136.0) Gecko/20100101 Firefox/136.0"})

test('example.com test', async ({ page }) => {
  await page.goto('http://localhost:3000/');
  await expect(page.locator('body')).toContainText('Save and see your changes instantly');
});
