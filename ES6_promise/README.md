# ES6 Promises

## Overview
This project focuses on understanding and implementing ES6 Promises in JavaScript. By the end of this project, you should be able to explain and use Promises, async/await, and error handling in JavaScript.

## Resources
Read or watch the following materials to understand the concepts:
- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An introduction](https://developers.google.com/web/fundamentals/primers/promises)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

## Learning Objectives
By the end of this project, you should be able to explain:
- What Promises are, why they are used, and how they work
- How to use `then`, `resolve`, and `catch` methods
- How to use every method of the Promise object
- How to handle errors using `Throw / Try`
- How to use the `await` operator
- How to write and use `async` functions

## Requirements
- All files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files should end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- Code should use the `.js` extension
- Code will be tested using Jest with the command `npm run test`
- Code will be verified against lint using ESLint
- All functions must be exported

## Setup
### Install NodeJS 20.x.x
In your home directory, run:
```sh
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```
Verify installation:
```sh
nodejs -v
v20.15.1
npm -v
10.7.0
```

### Install Jest, Babel, and ESLint
In your project directory, run:
```sh
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
npm install --save-dev eslint
```
Don't forget to run `npm install` when you have the `package.json`.

## Files
### [`package.json`](./package.json)
Configuration file for NodeJS and npm.

### [`babel.config.js`](./babel.config.js)
Configuration file for Babel.

### [`utils.js`](./utils.js)
Contains functions for tasks requiring `uploadPhoto` and `createUser`.

### [`.eslintrc.js`](./.eslintrc.js)
Configuration file for ESLint.

## Response Data Format
- `uploadPhoto` returns a response in the format:
  ```json
  {
    "status": 200,
    "body": "photo-profile-1"
  }
  ```
- `createUser` returns a response in the format:
  ```json
  {
    "firstName": "Guillaume",
    "lastName": "Salva"
  }
  ```

## Tasks
### 0. Keep every promise you make and only make promises you can keep
- Create a function `getResponseFromAPI()` that returns a Promise.
- **File:** [`0-promise.js`](./0-promise.js)

### 1. Don't make a promise...if you know you can't keep it
- Create a function `getFullResponseFromAPI(success)` that returns a promise.
- When `success` is true, resolve the promise with `{status: 200, body: 'Success'}`.
- When `success` is false, reject the promise with an error message `"The fake API is not working currently"`.
- **File:** [`1-promise.js`](./1-promise.js)

### 2. Catch me if you can!
- Create a function `handleResponseFromAPI(promise)` that appends three handlers:
  - On resolve, return `{status: 200, body: 'success'}`.
  - On reject, return an empty Error object.
  - Log `"Got a response from the API"` for every resolution.
- **File:** [`2-then.js`](./2-then.js)

### 3. Handle multiple successful promises
- Create a function `handleProfileSignup()` that imports `uploadPhoto` and `createUser` from `utils.js`.
- Resolve all promises and log `body firstName lastName` to the console.
- On error, log `"Signup system offline"`.
- **File:** [`3-all.js`](./3-all.js)

### 4. Simple promise
- Create a function `signUpUser(firstName, lastName)` that returns a resolved promise with `{firstName, lastName}`.
- **File:** [`4-user-promise.js`](./4-user-promise.js)

### 5. Reject the promises
- Create a function `uploadPhoto(filename)` that returns a rejected promise with an error message `"$fileName cannot be processed"`.
- **File:** [`5-photo-reject.js`](./5-photo-reject.js)

### 6. Handle multiple promises
- Import `signUpUser` from `4-user-promise.js` and `uploadPhoto` from `5-photo-reject.js`.
- Create a function `handleProfileSignup(firstName, lastName, fileName)` that calls the two functions and returns an array of results.
- **File:** [`6-final-user.js`](./6-final-user.js)

### 7. Load balancer
- Create a function `loadBalancer(chinaDownload, USDownload)` that returns the value of the first resolved promise.
- **File:** [`7-load_balancer.js`](./7-load_balancer.js)

### 8. Throw an error
- Create a function `divideFunction(numerator, denominator)` that throws an error when `denominator` is 0. Otherwise, it returns the result of the division.
- **File:** [`8-try.js`](./8-try.js)

### 9. Throw error / try catch
- Create a function `guardrail(mathFunction)` that returns an array `queue`.
  - On success, append the function's result to `queue`.
  - On error, append the error message to `queue`.
  - Always append `"Guardrail was processed"` to `queue`.
- **File:** [`9-try.js`](./9-try.js)

