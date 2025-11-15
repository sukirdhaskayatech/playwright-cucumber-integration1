const { Given, Then } = require('@cucumber/cucumber');
const { chromium, expect } = require('@playwright/test');

let browser, context, page;

// Step 1: Launch the Kayatech Admin Portal
Given('I launch the Kayatech Admin Portal', function () {
console.log("Given")
});


// Step 2: Verify the application is displayed
Then('the application should be displayed',  function () {
  // Optional: Check that the page title or logo is visible

  console.log("Title");

});
