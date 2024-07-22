# ES6 Data Manipulation

## Project Overview
This project focuses on ES6 data manipulation techniques. It includes various tasks that will help you understand and implement modern JavaScript features such as array methods, typed arrays, sets, maps, and more. By the end of this project, you should be able to manipulate data structures effectively using ES6 features.


## Resources
Read or watch the following resources to help you with this project:
- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
- [Set Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

### Learning Objectives
By the end of this project, you should be able to explain:
- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays
- The Set, Map, and WeakMap data structures

### Requirements
- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `.js` extension
- Your code will be tested using Jest with the command `npm run test`
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint checks (`npm run full-test`)
- All of your functions must be exported

## Setup
### Install NodeJS 20.x.x
Run the following commands in your home directory to install NodeJS:
```sh
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```
Verify the installation:
```sh
nodejs -v
# Expected output: v20.15.1

npm -v
# Expected output: 10.7.0
```

### Install Jest, Babel, and ESLint
Run the following commands in your project directory:
```sh
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

### Configuration files
Ensure you have the following configuration files:

#### package.json
This file should contain your project dependencies and scripts.

#### babel.config.js
This file should configure Babel for the project.

#### .eslintrc.js
This file should configure ESLint for the project.

### Don’t forget to run
```sh
npm install
```
when you have the `package.json` file.

## Tasks
### 0. Basic list of objects
**File:** [`0-get_list_students.js`](./0-get_list_students.js)

Create a function named `getListStudents` that returns an array of objects, each object containing three attributes: `id` (Number), `firstName` (String), and `location` (String).

Example:
```js
[
  { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
  { id: 2, firstName: 'James', location: 'Columbia' },
  { id: 5, firstName: 'Serena', location: 'San Francisco' }
]
```

### 1. More mapping
**File:** [`1-get_list_student_ids.js`](./1-get_list_student_ids.js)

Create a function `getListStudentIds` that returns an array of ids from a list of objects. If the argument is not an array, return an empty array. Use the `map` function on the array.

Example:
```js
getListStudentIds("hello"); // []
getListStudentIds(getListStudents()); // [1, 2, 5]
```

### 2. Filter
**File:** [`2-get_students_by_loc.js`](./2-get_students_by_loc.js)

Create a function `getStudentsByLocation` that returns an array of objects who are located in a specific city. Use the `filter` function on the array.

Example:
```js
getStudentsByLocation(getListStudents(), 'San Francisco');
// [
//   { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
//   { id: 5, firstName: 'Serena', location: 'San Francisco' }
// ]
```

### 3. Reduce
**File:** [`3-get_ids_sum.js`](./3-get_ids_sum.js)

Create a function `getStudentIdsSum` that returns the sum of all the student ids. Use the `reduce` function on the array.

Example:
```js
getStudentIdsSum(getListStudents()); // 8
```

### 4. Combine
**File:** [`4-update_grade_by_city.js`](./4-update_grade_by_city.js)

Create a function `updateStudentGradeByCity` that returns an array of students for a specific city with their new grade. If a student doesn’t have a grade in newGrades, the final grade should be "N/A". Use `filter` and `map` combined.

Example:
```js
updateStudentGradeByCity(getListStudents(), "San Francisco", [{ studentId: 5, grade: 97 }, { studentId: 1, grade: 86 }]);
// [
//   { id: 1, firstName: 'Guillaume', location: 'San Francisco', grade: 86 },
//   { id: 5, firstName: 'Serena', location: 'San Francisco', grade: 97 }
// ]
```

### 5. Typed Arrays
**File:** [`5-typed_arrays.js`](./5-typed_arrays.js)

Create a function `createInt8TypedArray` that returns a new ArrayBuffer with an Int8 value at a specific position. If adding the value is not possible, throw an error "Position outside range".

Example:
```js
createInt8TypedArray(10, 2, 89);
// DataView { byteLength: 10, byteOffset: 0, buffer: ArrayBuffer { byteLength: 10 } }
```

### 6. Set data structure
**File:** [`6-set.js`](./6-set.js)

Create a function `setFromArray` that returns a Set from an array.

Example:
```js
setFromArray([12, 32, 15, 78, 98, 15]); // Set { 12, 32, 15, 78, 98 }
```

### 7. More set data structure
**File:** [`7-has_array_values.js`](./7-has_array_values.js)

Create a function `hasValuesFromArray` that returns a boolean if all the elements in the array exist within the set.

Example:
```js
hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1]); // true
hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [10]); // false
hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1, 10]); // false
```

### 8. Clean set
**File:** [`8-clean_set.js`](./8-clean_set.js)

Create a function `cleanSet` that returns a string of all the set values that start with a specific string (startString). When a value starts with startString, only append the rest of the string. The string should contain all the values of the set separated by `-`.

Example:
```js
cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), 'bon'); // 'jovi-aparte-appetit'
cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), ''); // ''
```

### 9. Map data structure
**File:** [`9-groceries_list.js`](./9-groceries_list.js)

Create a function `groceriesList` that returns a map of groceries with the following items (name, quantity):
- Apples, 10
- Tomatoes, 10
- Pasta, 1
- Rice, 1
- Banana, 5

Example:
```js
groceriesList();
// Map { 'Apples' => 10, 'Tomatoes' => 10, 'Pasta' => 1, 'Rice' => 1, 'Banana' => 5 }
```

### 10. More map data structure
**File:** [`10-update_uniq_items.js`](./10-update_uniq_items.js)

Create a function `updateUniqueItems` that returns an updated map for all items with initial quantity at 1. For each entry of the map where the quantity is 1, update the quantity to 100. If updating the quantity is not possible, throw an error "Cannot process".

Example:
```js
updateUniqueItems(groceriesList());
// Map { 'Apples' => 10, 'Tomatoes' => 10, 'Pasta' => 100, 'Rice' => 100,

 'Banana' => 5 }
```
