### PLD Questions - JavaScript DOM manipulation

1. **JavaScript est-il interprété ou compilé ?**
   JavaScript est un langage interprété. Cela signifie que le code est exécuté directement par l'interpréteur (le moteur JavaScript du navigateur) sans nécessiter une phase de compilation préalable.

2. **Quand est-il apparu pour la première fois et pourquoi a-t-il été développé ?**
   JavaScript est apparu pour la première fois en 1995. Il a été développé par Brendan Eich chez Netscape pour permettre des interactions dynamiques et des fonctionnalités avancées dans les pages web.

3. **Que signifie DOM en développement web ?**
   DOM signifie Document Object Model (Modèle Objet de Document).

4. **Qu'est-ce que le DOM ?**
   Le DOM est une interface de programmation pour les documents HTML et XML. Il représente la page de manière structurée, permettant aux langages de script de manipuler le contenu, la structure et le style du document.

5. **Quelles sont les différentes façons de cibler / obtenir des éléments en JS ?**
   On peut cibler / obtenir des éléments en JS de différentes manières :
   - `document.getElementById('id')`
   - `document.getElementsByClassName('className')`
   - `document.getElementsByTagName('tagName')`
   - `document.querySelector('selector')`
   - `document.querySelectorAll('selector')`

6. **Qu'est-ce qu'une pseudo-classe CSS ?**
   Une pseudo-classe CSS est un mot-clé ajouté à un sélecteur qui spécifie un état spécial de l'élément sélectionné.

7. **Donnez un ou plusieurs exemples de pseudo-classes CSS.**
   - `:hover` (pour le survol d'un élément)
   - `:first-child` (pour le premier enfant d'un élément)
   - `:nth-child(n)` (pour le n-ième enfant d'un élément)

8. **Quelle est l'utilisation principale de l'API fetch en JavaScript ?**
   L'API fetch est principalement utilisée pour effectuer des requêtes réseau pour récupérer des ressources via HTTP.

9. **Fetch envoie-t-il des requêtes de manière synchrone ou asynchrone ? Et pourquoi ?**
   Fetch envoie des requêtes de manière asynchrone. Cela permet à la page de continuer à fonctionner sans être bloquée en attendant la réponse du serveur, améliorant ainsi l'expérience utilisateur.

### PLD Questions - ES6 Promises

1. **De manière abstraite et simple, qu'est-ce que les opérations asynchrones ?**
    Les opérations asynchrones sont des opérations qui permettent à un programme de continuer à s'exécuter pendant qu'une tâche se déroule en arrière-plan.

2. **En une phrase simple et courte, qu'est-ce qu'une promesse ?**
    Une promesse est un objet représentant l'achèvement ou l'échec éventuel d'une opération asynchrone.

3. **Quels sont les états d'une promesse ?**
    - En attente (`pending`)
    - Réussie (`fulfilled`)
    - Rejetée (`rejected`)

4. **Pouvons-nous avoir une chaîne de promesses ?**
    Oui, nous pouvons enchaîner des promesses.

5. **Dans quel cas utilisons-nous une chaîne de promesses ?**
    Nous utilisons une chaîne de promesses lorsque nous avons plusieurs opérations asynchrones qui doivent être exécutées en séquence.

6. **Comment et quand utilisons-nous try / catch en JavaScript ?**
    Nous utilisons `try / catch` pour gérer les erreurs lors de l'exécution de blocs de code, particulièrement dans les opérations asynchrones ou les fonctions qui peuvent générer des exceptions.

7. **Dans quels scénarios pouvons-nous utiliser async / await (il y en a plusieurs, citez-en au moins un) ?**
    Nous utilisons `async / await` pour simplifier l'écriture et la gestion des opérations asynchrones, par exemple lors de la récupération de données depuis une API.

### PLD Questions - ES6 data manipulation

1. **Quand et comment utiliser la méthode map() en JavaScript ?**
    Nous utilisons `map()` pour créer un nouveau tableau en appliquant une fonction à chaque élément d'un tableau existant. Exemple :
    ```javascript
    const numbers = [1, 2, 3];
    const doubled = numbers.map(n => n * 2);
    ```

2. **Quand et comment utiliser la méthode filter() en JavaScript ?**
    Nous utilisons `filter()` pour créer un nouveau tableau avec les éléments qui passent un test spécifique. Exemple :
    ```javascript
    const numbers = [1, 2, 3, 4];
    const evens = numbers.filter(n => n % 2 === 0);
    ```

3. **Quand et comment utiliser la méthode reduce() en JavaScript ?**
    Nous utilisons `reduce()` pour appliquer une fonction à un accumulateur et chaque valeur du tableau (de gauche à droite) afin de réduire à une seule valeur. Exemple :
    ```javascript
    const numbers = [1, 2, 3, 4];
    const sum = numbers.reduce((acc, n) => acc + n, 0);
    ```

4. **Qu'est-ce que les tableaux typés en JavaScript ?**
    Les tableaux typés (Typed Arrays) sont des objets semblables à des tableaux qui fournissent un mécanisme pour accéder aux données binaires brutes.

5. **Quand utiliser les tableaux typés ?**
    Nous utilisons les tableaux typés lorsque nous avons besoin de manipuler des données binaires brutes, par exemple pour le traitement de fichiers ou la manipulation de données issues de WebGL.

6. **Quelles sont certaines des caractéristiques d'un tableau typé en JS ?**
    - Taille fixe
    - Stockage contigu en mémoire
    - Types de données homogènes

7. **Qu'est-ce qu'un set en JS et quelles sont ses principales caractéristiques ?**
    Un `Set` en JavaScript est une collection d'éléments uniques. Les principales caractéristiques sont :
    - Unicité des valeurs
    - Pas d'indexation
    - Les éléments peuvent être de tout type

8. **Pouvez-vous donner un exemple d'utilisation des ensembles en JS ?**
    ```javascript
    const set = new Set([1, 2, 3, 3, 4]);
    console.log(set); // Output: Set(4) { 1, 2, 3, 4 }
    ```

9. **Qu'est-ce qu'une map en JS et quelles sont ses principales caractéristiques ?**
    Une `Map` en JavaScript est une collection de paires clé-valeur. Les principales caractéristiques sont :
    - Les clés peuvent être de tout type
    - Les éléments sont stockés dans l'ordre d'insertion
    - La taille d'une `Map` peut être obtenue avec `size`
