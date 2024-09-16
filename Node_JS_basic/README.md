# NodeJS Basics

This project focuses on introducing the basic concepts of NodeJS, including using JavaScript in a NodeJS environment, working with core modules, creating HTTP servers, and using Express to simplify server creation. The goal is to understand how to build a server using both vanilla NodeJS and Express, handle asynchronous operations, and improve development efficiency using tools like Babel and Nodemon.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without referencing external resources:

1. Run JavaScript code using NodeJS.
2. Utilize NodeJS modules.
3. Use NodeJS to read files.
4. Access command-line arguments and environment variables using the `process` object.
5. Create a basic HTTP server using NodeJS.
6. Develop a more advanced HTTP server using ExpressJS.
7. Handle advanced routing with ExpressJS.
8. Integrate ES6 syntax into NodeJS using Babel-node.
9. Use Nodemon for efficient development.

## Resources

- [Node JS Getting Started](https://nodejs.org/en/docs/guides/getting-started-guide/)
- [Process API Documentation](https://nodejs.org/dist/latest-v14.x/docs/api/process.html)
- [Child Process Documentation](https://nodejs.org/api/child_process.html)
- [Express Getting Started](https://expressjs.com/en/starter/installing.html)
- [Mocha Documentation](https://mochajs.org/)
- [Nodemon Documentation](https://www.npmjs.com/package/nodemon)

## Project Requirements

- Use only the following editors: `vi`, `vim`, `emacs`, or `Visual Studio Code`.
- All code will be compiled and run on Ubuntu 20.04 LTS using NodeJS (version 20.x.x).
- Ensure all files end with a new line.
- A `README.md` file at the root of the project is mandatory.
- The code should use the `.js` extension.
- Tests will be conducted using Jest with the command `npm run test`.
- Your code will be linted with ESLint and must pass all lint checks.
- Export all functions and classes using the format: `module.exports = myFunction;`.

## Provided Files

- `database.csv`: Contains sample student data used in various tasks.
- `package.json`: File to manage dependencies.
- `.eslintrc.js`: ESLint configuration.
- `babel.config.js`: Babel configuration.

Run `$ npm install` to install dependencies before starting the project.

## Tasks

### 0. Basic JavaScript Execution with NodeJS

- **File**: `0-console.js`
- Create a function `displayMessage` that prints a string argument to `STDOUT`.

```bash
$ node 0-main.js
Hello NodeJS!
```

### 1. Using Process stdin

- **File**: `1-stdin.js`
- Create a program that prompts for a name, displays it, and closes with a message.

```bash
$ node 1-stdin.js
Welcome to Holberton School, what is your name?
```

### 2. Reading a File Synchronously

- **File**: `2-read_file.js`
- Implement `countStudents` function to read and display student information from a CSV file synchronously.

```bash
$ node 2-main_1.js
Number of students: 10
```

### 3. Reading a File Asynchronously

- **File**: `3-read_file_async.js`
- Implement `countStudents` to read the file asynchronously and return a Promise.

```bash
$ node 3-main_1.js
Number of students: 10
```

### 4. HTTP Server with Node's HTTP Module

- **File**: `4-http.js`
- Create a small HTTP server that responds with "Hello Holberton School!" on any endpoint.

```bash
$ curl localhost:1245
Hello Holberton School!
```

### 5. More Complex HTTP Server

- **File**: `5-http.js`
- Extend the server to handle `/students` and return a list of students.

```bash
$ curl localhost:1245/students
This is the list of our students
```

### 6. HTTP Server with Express

- **File**: `6-http_express.js`
- Create a simple HTTP server using Express that responds to any endpoint with "Hello Holberton School!"

```bash
$ curl localhost:1245
Hello Holberton School!
```

### 7. More Complex HTTP Server with Express

- **File**: `7-http_express.js`
- Extend the Express server to handle `/students` and return student information.

```bash
$ curl localhost:1245/students
This is the list of our students
```

### 8. Organizing a Complex HTTP Server with Express

- **Directory**: `full_server`
- Organize the project into controllers and routes for better structure.
- Create `readDatabase` utility function in `full_server/utils.js` for asynchronous reading of the CSV.
- Add `AppController` and `StudentsController` in `full_server/controllers/`.

```bash
$ npm run dev
```

- Access the server and retrieve student information from `/students` or by major from `/students/:major`.

```bash
$ curl localhost:1245/students/CS
List: Johann, Arielle, ...
```

## Setup Instructions

1. Clone the repository.
2. Install dependencies:

   ```bash
   $ npm install
   ```

3. Run tests:

   ```bash
   $ npm run test
   ```

4. To run the full test (tests + lint):

   ```bash
   $ npm run full-test
   ```

## Linting and Formatting

Make sure to run ESLint before submitting:

```bash
$ npm run lint
```
