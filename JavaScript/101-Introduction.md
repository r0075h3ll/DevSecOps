## How does JavaScript run?

JavaScript is a scripting language popularly known for its use case in Web/Mobile App. development. To run JavaScript code one needs to have a JavaScript Runtime Environment(JSRE) in their machine, that comprises of
1. JavaScript Engine
2. Callback Queue
3. APIs

The browser, in which you're most probably viewing this page, is a runtime environment that has all the listed components - the most important of which is a JavaScript Engine(JSE). Here's a bunch of prevalent JavaScript Engines
- V8; used by Google Chrome
- SpiderMonkey; used by Firefox
- Chakra; used by Safari, etc.

JavaScript Engine is the required component for running any piece of JavaScript code, however, different JSEs work more or less the same. It is the APIs that the RE has access to, introduces different features, functionalities, etc. into a JSRE, making the respective JSRE distinct.

For instance, this code snippet cannot run in Nodejs
```js
<script>
    alert(1);
</script>
```

There could be numerous explanations for why this would fail to execute, but the main reason would be the JSRE. The way browsers handle JS code is by translating it into a tree representation first, whereas Nodejs directly transforms it into machine code and executes it. Browsers depend on the DOM API in order to do most of the work - it is this DOM API that defines the `Window` object, of which `alert()` method is a part - thus allowing you to generate alert popups. Nodejs, being a different JSRE, does not have the DOM API loaded into it, and therefore cannot do the same.

See you in the next one with a brief on JavaScript internals to demonstrate the cause and exploitation of Race Conditions.

### Coming up

- Race Conditions in JavaScript 