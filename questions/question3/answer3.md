From: Eric
Subject: Error on website

Hi Marc,

It sounds like you're attempting to reference a variable, "searchkit", in your code before having defined it. Make sure you define "searchkit" as a variable or method before the line of code in which you're referencing it in index.js.

If it's defined elsewhere instead of in index.js, make sure that you reference it from index.js as a dependency (either from another file or by installing it via your package manager.)

Javascript's ReferenceError is documented here: [MDN: ReferenceError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)

Other tactics you can use to prevent ReferenceErrors:

- use Javascript's strict mode
- use `let` or `const` instead of `var` - this makes the scope of your variables more predictable
- consider using try-catch blocks to handle the potential for errors gracefully
- consider using ESLint or TypeScript to identify and resolve issues like this while you're developing.

Please let me know if this helps you resolve the issue.

Best,

Eric
