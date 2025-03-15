import { test, expect } from '@playwright/test';

// use firefox on macos as test UA
test.use({ userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:136.0) Gecko/20100101 Firefox/136.0"})

test('example.com test', async ({ page }) => {
  await page.goto('http://example.com/');

  await page.getByRole('link', { name: 'More information...' }).click();
  await page.getByRole('link', { name: 'RFC 2606' }).click();

  await expect(page.locator('body')).toContainText('Reserved Top Level DNS Names');
});
