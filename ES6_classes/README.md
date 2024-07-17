# ES6 Classes Project

## Overview
This project involves learning and implementing various concepts of ES6 classes, including class definitions, methods, static methods, inheritance, and metaprogramming. The tasks are designed to help you understand how to define classes, extend them, and use different types of methods in a class.

## Learning Objectives
By the end of this project, you should be able to explain:
- How to define a class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Requirements
- All files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All files should end with a new line
- A README.md file at the root of the project folder is mandatory
- Code should use the `.js` extension
- Code will be tested using Jest with the command `npm run test`
- Code will be verified against lint using ESLint
- Code needs to pass all tests and lint checks using the command `npm run full-test`

## Setup
### Install NodeJS 12.11.x
```sh
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v
npm -v
```

### Install Jest, Babel, and ESLint
```sh
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

### Configuration Files
#### `package.json`
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
    "@babel/preset-env": "^7.6.0",
    "@babel/node": "^7.8.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```

#### `babel.config.js`
```js
module.exports = {
  presets: ['@babel/preset-env'],
};
```

#### `.eslintrc.js`
```js
module.exports = {
  extends: 'airbnb-base',
  plugins: ['jest'],
  env: {
    'jest/globals': true,
  },
};
```

### Run `npm install`
Don't forget to run `npm install` to install the dependencies listed in `package.json`.

## Tasks

### Task 0: You used to attend a place like this at some point
- **File:** `0-classroom.js`
- Implement a class named `ClassRoom` with an attribute `maxStudentsSize` (Number) and assign it to `_maxStudentsSize`.

```js
export default class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }
}
```

### Task 1: Let's make some classrooms
- **File:** `1-make_classrooms.js`
- Implement a function `initializeRooms` that returns an array of 3 `ClassRoom` objects with sizes 19, 20, and 34.

```js
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  return [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)];
}
```

### Task 2: A Course, Getters, and Setters
- **File:** `2-hbtn_course.js`
- Implement a class `HolbertonCourse` with attributes `name` (String), `length` (Number), and `students` (Array of Strings). Implement getters and setters for each attribute.

```js
export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.validateString(name, 'Name');
    this._length = this.validateNumber(length, 'Length');
    this._students = this.validateArray(students, 'Students');
  }

  validateString(value, attribute) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attribute} must be a string`);
    }
    return value;
  }

  validateNumber(value, attribute) {
    if (typeof value !== 'number') {
      throw new TypeError(`${attribute} must be a number`);
    }
    return value;
  }

  validateArray(value, attribute) {
    if (!Array.isArray(value)) {
      throw new TypeError(`${attribute} must be an array`);
    }
    return value;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this.validateString(value, 'Name');
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this._length = this.validateNumber(value, 'Length');
  }

  get students() {
    return this._students;
  }

  set students(value) {
    this._students = this.validateArray(value, 'Students');
  }
}
```

### Task 3: Methods, static methods, computed methods names..... MONEY
- **File:** `3-currency.js`
- Implement a class `Currency` with attributes `code` (String) and `name` (String). Implement getters and setters for each attribute and a method `displayFullCurrency` that returns the attributes in the format `name (code)`.

```js
export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    this._code = value;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = value;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
```

### Task 4: Pricing
- **File:** `4-pricing.js`
- Implement a class `Pricing` with attributes `amount` (Number) and `currency` (Currency). Implement getters and setters for each attribute, a method `displayFullPrice` that returns `amount currency_name (currency_code)`, and a static method `convertPrice` that returns the amount multiplied by the conversion rate.

```js
import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = value;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
```

### Task 5: A Building
- **File:** `5-building.js`
- Implement a class `Building` with an attribute `sqft` (Number). Make it an abstract class with an abstract method `evacuationWarningMessage`.

```js
export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new TypeError('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
```

### Task 6: Inheritance
- **File:** `6-sky_high.js`
- Implement a class `SkyHighBuilding` that extends `Building` with attributes `sqft` (Number) and `floors` (Number). Override `evacuationWarningMessage` to return `Evacuate slowly the NUMBER_OF_FLOORS floors`.

```js
import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
```

### Task 7: Airport
- **File:** `7-airport.js`
- Implement a class `Airport` with attributes `name` (String) and `code` (String). The default string description should return the airport code.

```js
export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
```

### Task 8: Primitive - Holberton Class
- **File:** `8-hbtn_class.js`
- Implement a class `HolbertonClass` with attributes `size` (Number) and `location` (String). When cast into a Number, it

 should return the size. When cast into a String, it should return the location.

```js
export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
```

### Task 9: Hoisting
- **File:** `9-hoisting.js`
- Fix the provided code so that it works correctly with class hoisting.

```js
export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this._holbertonClass;
  }

  get fullStudentDescription() {
    return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}

const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export const listOfStudents = [student1, student2, student3, student4, student5];
```

### Task 10: Vroom
- **File:** `10-car.js`
- Implement a class `Car` with attributes `brand` (String), `motor` (String), and `color` (String). Add a method `cloneCar` that returns a new object of the class.

```js
const carSymbol = Symbol('car');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    this[carSymbol] = function () {
      return new this.constructor(this._brand, this._motor, this._color);
    };
  }

  cloneCar() {
    return this[carSymbol]();
  }
}
```

