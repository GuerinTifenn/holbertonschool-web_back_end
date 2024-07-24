# JavaScript DOM Manipulation

## Description

This project involves JavaScript DOM manipulation tasks designed to improve understanding and skills in selecting, modifying, and interacting with HTML elements using JavaScript. The tasks cover a range of actions, from simple text color updates to making API requests and dynamically updating the DOM.

## Learning Objectives

By the end of this project, you should be able to:

- Select HTML elements using JavaScript
- Differentiate between ID, class, and tag name selectors
- Modify HTML element styles
- Retrieve and update HTML element content
- Modify the DOM
- Make requests using XmlHTTPRequest and Fetch API
- Bind to DOM events and user events

## Requirements

- **Editors:** All editors are allowed.
- **Browser Compatibility:** All scripts will be interpreted in Chrome browser (version 57.0 or later).
- **File Format:** All files should end with a new line.
- **README:** A mandatory `README.md` file with meaningful information about the project content must be included at the root of the project folder.
- **Code Style:** Your code should be semistandard compliant.
- **Restrictions:** Do not use `var`. HTML should not reload for each action.

## Resources

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [CSS Diner Play with Selectors](https://flukeout.github.io/)
- [Client-side Web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- [Introduction to web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
- [Manipulating documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [Fetching data from the server](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

## Tasks

### 0. Color Me
**File:** [`0-script.js`](./0-script.js)

Write a JavaScript script that updates the text color of the header element to red (`#FF0000`).

- Use `document.querySelector` to select the HTML tag.
- Test with the provided HTML file.

### 1. Click and Turn Red
**File:** [`1-script.js`](./1-script.js)

Write a JavaScript script that updates the text color of the header element to red (`#FF0000`) when the user clicks on the tag with id `red_header`.

- Test with the provided HTML file.

### 2. Add `.red` Class
**File:** [`2-script.js`](./2-script.js)

Write a JavaScript script that adds the class `red` to the header element when the user clicks on the tag with id `red_header`.

- Test with the provided HTML file.

### 3. Toggle Classes
**File:** [`3-script.js`](./3-script.js)

Write a JavaScript script that toggles the class of the header element when the user clicks on the tag with id `toggle_header`.

- The header element must always have one class: `red` or `green`.
- If the current class is `red`, update to `green`, and vice versa.
- Test with the provided HTML file.

### 4. List of Elements
**File:** [`4-script.js`](./4-script.js)

Write a JavaScript script that adds a `li` element to a list when the user clicks on the element with id `add_item`.

- The new element must be: `<li>Item</li>`
- The new element must be added to the `ul` element with class `my_list`.
- Test with the provided HTML file.

### 5. Change the Text
**File:** [`5-script.js`](./5-script.js)

Write a JavaScript script that updates the text of the header element to `New Header!!!` when the user clicks on the element with id `update_header`.

- Test with the provided HTML file.

### 6. Star Wars Character
**File:** [`6-script.js`](./6-script.js)

Write a JavaScript script that fetches the character name from this URL: [https://swapi-api.hbtn.io/api/people/5/?format=json](https://swapi-api.hbtn.io/api/people/5/?format=json)

- The name must be displayed in the HTML tag with id `character`.
- Use the Fetch API.
- Test with the provided HTML file.

### 7. Star Wars Movies
**File:** [`7-script.js`](./7-script.js)

Write a JavaScript script that fetches and lists the title for all movies using this URL: [https://swapi-api.hbtn.io/api/films/?format=json](https://swapi-api.hbtn.io/api/films/?format=json)

- All movie titles must be listed in the HTML `ul` element with id `list_movies`.
- Use the Fetch API.
- Test with the provided HTML file.

### 8. Say Hello!
**File:** [`8-script.js`](./8-script.js)

Write a JavaScript script that fetches from [https://hellosalut.stefanbohacek.dev/?lang=fr](https://hellosalut.stefanbohacek.dev/?lang=fr) and displays the value of `hello` from that fetch in the HTML element with id `hello`.

- The translation of “hello” must be displayed in the HTML element with id `hello`.
- Your script must work when it is imported from the `<head>` tag.
- Test with the provided HTML file.
