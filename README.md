# holbertonschool-web_back_end

### Questions PLD - Bases d'ES6

1. **Que signifie ES6 ?**
   - ES6 signifie ECMAScript 6, également connu sous le nom d'ECMAScript 2015. C'est la sixième édition du langage ECMAScript.

2. **Qu'est-ce que ES6 ?**
   - ES6 est une mise à jour majeure du langage JavaScript qui introduit de nouvelles fonctionnalités et améliorations pour rendre le code plus lisible, maintenable et performant.

3. **Quelles sont certaines des principales fonctionnalités apparues dans ES6 ?**
   - Quelques-unes des principales fonctionnalités incluent :
     - Les variables `let` et `const`
     - Les classes
     - Les fonctions fléchées
     - Les Template Literals (chaînes de modèles)
     - Les modules (import/export)
     - Les destructurations d'objets et de tableaux
     - Les promesses
     - Les paramètres par défaut
     - Les boucles `for...of`

4. **Quelle est la différence entre une constante et une variable (let et const) en ES6 ?**
   - `let` est utilisé pour déclarer des variables qui peuvent être réassignées. `const` est utilisé pour déclarer des constantes qui ne peuvent pas être réassignées après leur initialisation. Les deux respectent la portée de bloc, contrairement à `var` qui a une portée de fonction.

5. **Qu'est-ce qu'une portée de variable (ou de const) ?**
   - La portée d'une variable détermine où la variable est accessible. Les variables déclarées avec `let` et `const` ont une portée de bloc, ce qui signifie qu'elles ne sont accessibles que dans le bloc où elles sont définies (par exemple, à l'intérieur d'une paire d'accolades `{}`).

6. **Donnez un exemple (code simple) expliquant les portées en ES6.**
   ```javascript
   {
     let a = 10;
     const b = 20;
     var c = 30;
   }
   console.log(c); // 30
   console.log(a); // ReferenceError: a is not defined
   console.log(b); // ReferenceError: b is not defined
   ```

7. **Qu'est-ce que les Template Literals (chaînes de modèles) en ES6 ?**
   - Les Template Literals sont des chaînes de caractères permettant des expressions intégrées. Elles sont délimitées par des backticks (`` ` ``) et peuvent inclure des expressions via la syntaxe `${expression}`.

8. **Donnez un exemple de Template Literals en ES6.**
   ```javascript
   const name = 'John';
   const age = 30;
   const message = `My name is ${name} and I am ${age} years old.`;
   console.log(message); // My name is John and I am 30 years old.
   ```

9. **Transformez cette fonction en une fonction fléchée.**
   - Fonction normale :
     ```javascript
     function add(a, b) {
       return a + b;
     }
     ```
   - Fonction fléchée :
     ```javascript
     const add = (a, b) => a + b;
     ```

### Questions PLD - Classes ES6

1. **Comment définissez-vous une méthode à l'intérieur d'une classe ES6 ?**
   - Une méthode à l'intérieur d'une classe ES6 est définie sans le mot-clé `function`.
     ```javascript
     class MyClass {
       myMethod() {
         console.log('Hello, world!');
       }
     }
     ```

2. **Qu'est-ce qu'une méthode statique ?**
   - Une méthode statique est une méthode définie avec le mot-clé `static` et qui peut être appelée sur la classe elle-même, pas sur une instance de la classe.

3. **Peut-on appeler une méthode statique à partir d'une instance en ES6 ?**
   - Non, les méthodes statiques ne peuvent pas être appelées à partir d'une instance. Elles doivent être appelées sur la classe elle-même.

4. **Comment créer une méthode statique dans une classe ES6 ?**
   - Pour créer une méthode statique, utilisez le mot-clé `static`.
     ```javascript
     class MyClass {
       static myStaticMethod() {
         console.log('This is a static method.');
       }
     }

     MyClass.myStaticMethod(); // This is a static method.
     ```

5. **Quel est l'équivalent de `__init__` (en Python) en JavaScript ?**
   - En JavaScript, l'équivalent de `__init__` est le constructeur, défini avec le mot-clé `constructor`.
     ```javascript
     class MyClass {
       constructor() {
         console.log('This is the constructor.');
       }
     }
     ```

6. **Comment créer une sous-classe (classe dérivée) à partir d'une classe parente en ES6 ?**
   - Pour créer une sous-classe, utilisez le mot-clé `extends`.
     ```javascript
     class ParentClass {
       constructor() {
         console.log('Parent class constructor');
       }
     }

     class ChildClass extends ParentClass {
       constructor() {
         super();
         console.log('Child class constructor');
       }
     }

     const child = new ChildClass(); // Parent class constructor
                                     // Child class constructor
     ```

7. **Qu'est-ce que la méthode constructeur dans une classe ES6 ?**
   - La méthode constructeur est une méthode spéciale d'une classe qui est appelée lors de la création d'une instance de la classe. Elle est définie avec le mot-clé `constructor`.

8. **Peut-on avoir plusieurs méthodes constructeur à l'intérieur d'une classe ?**
   - Non, une classe ne peut avoir qu'une seule méthode constructeur. Si plusieurs constructeurs sont définis, cela entraînera une erreur de syntaxe.
