# ES6 Basics

## Overview
This project covers the fundamental features and concepts introduced in ECMAScript 6 (ES6). By the end of this project, you will be able to understand and utilize the new syntax and features of ES6 effectively.

## Learning Objectives
By the end of this project, you should be able to explain:

- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops

## Requirements
- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `.js` extension
- Your code will be tested using the Jest Testing Framework
- Your code will be analyzed using the linter ESLint with specific rules provided
- All of your functions must be exported

## Setup
### Install NodeJS 12.11.x
```sh
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v
# v12.11.1
npm -v
# 6.11.3

### Install Jest, Babel, and ESLint
In your project directory:
```sh
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

### Configuration Files
Create the following files with the provided content:

#### package.json
```json
{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.6.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```

#### babel.config.js
```js
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```

#### .eslintrc.js
```js
module.exports = {
  env: {
    es6: true,
    node: true,
    jest: true,
  },
  extends: ['airbnb-base', 'plugin:jest/recommended'],
  rules: {
    'no-console': 'off',
    'no-var': 'error',
    'prefer-const': 'error',
  },
};
```

### Install Dependencies
Run `npm install` from the terminal of your project folder to install all necessary project dependencies.

## Tasks

### 0. Const or let?
Modify `taskFirst` to use `const` and `taskNext` to use `let`.

```js
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();
  return combination;
}
```

### 1. Block Scope
Modify the variables inside `taskBlock` to ensure they are not overwritten inside the conditional block.

```js
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
  }

  return [task, task2];
}
```

### 2. Arrow Functions
Rewrite the function to use ES6’s arrow syntax.

```js
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  this.addNeighborhood = (newNeighborhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}
```

### 3. Parameter Defaults
Condense the internals of the function using default parameter values.

```js
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  return initialNumber + expansion1989 + expansion2019;
}
```

### 4. Rest Parameter Syntax for Functions
Modify the function to return the number of arguments using the rest parameter syntax.

```js
export default function returnHowManyArguments(...args) {
  return args.length;
}
```

### 5. The Wonders of Spread Syntax
Concatenate two arrays and a string using the spread syntax.

```js
export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string];
}
```

### 6. Take Advantage of Template Literals
Rewrite the return statement using a template literal.

```js
export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return `As of ${year}, it was the seventh-highest income county in the United States, with a per capita personal income of ${budget.income}. As of 2015, San Francisco proper had a GDP of ${budget.gdp}, and a GDP per capita of ${budget.capita}.`;
}
```

### 7. Object Property Value Shorthand Syntax
Modify the function’s budget object to use the object property value shorthand syntax.

```js
export default function getBudgetObject(income, gdp, capita) {
  return { income, gdp, capita };
}
```

### 8. Computed Property Names
Rewrite the `getBudgetForCurrentYear` function to use ES6 computed property names.

```js
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  return {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };
}
```

### 9. ES6 Method Properties
Rewrite `getFullBudgetObject` to use ES6 method properties.

```js
import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  return {
    ...budget,
    getIncomeInDollars(income) {
      return `$${income}`;
    },
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };
}
```

### 10. For...of Loops
Rewrite the function `appendToEachArrayValue` to use ES6’s `for...of` operator.

```js
export default function appendToEachArrayValue(array, appendString) {
  for (let value of array) {
    array[array.indexOf(value)] = `${appendString}${value}`;
  }
  return array;
}
```

### 11. Iterator
Write a function `createEmployeesObject` that returns an object with a specified format.

```js
export default function createEmployeesObject(departmentName, employees) {
  return {
    [departmentName]: employees,
  };
}
```

### 12. Report Object
Write a function `createReportObject` that returns an object containing allEmployees and a method property called `getNumberOfDepartments`.

```js
export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    },
  };
}
```
