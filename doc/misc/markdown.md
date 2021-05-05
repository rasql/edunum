# Markdown

Markdown est un **langage de balisage léger**, avec une syntaxe facile à lire et facile à écrire. Un document balisé par Markdown peut être transformé en HTML ou en PDF. Les fichiers Markdown ont une extension `.md`.


Markdown est utilisé pour formatter les fichiers README sur GitHub.


## Emphase

Les caractères `_` ou `*` sont utilisés pour entourer les mots à mettre en **emphase**.

    _mot_ en *italique*. 
    
_mot_ en *italique*. 

Les caractères  `__` ou `**` sont utilisés pour mettre des mots en **grande emphase**. 

    __mot__ en **gras**. 
    
__mot__ en **gras**. 


## Espaces

Les **espaces multiples** ou des simples retours à la lignes sont tous remplacés par une seule espace.

    Des            grands                espaces
    et
    des
    retours.

    
Des            grands                espaces
et
des
retours.


## Paragraphe

Une **ligne vide** crée un paragraphe.

    Ceci est le premier paragraphe.

    Ceci est le paragraphe suivant.


Ceci est le premier paragraphe.

Ceci est le paragraphe suivant.


## Retour à la ligne forcé

Ajouter **deux espaces** en fin de ligne insère un retour à la ligne forcé.

    Les deux espaces en fin de cette ligne  
    forcent un retour à la ligne.

Les deux espaces en fin de cette ligne  
forcent un retour à la ligne.

## Code

Le caractère ` (backquote) indique des éléments de code.

    La fonction `print(x)` imprime la valeur de la variable `x`. 
    
La fonction `print(x)` imprime la valeur de la variable `x`. 

    

## Directives

Pour mettre un paragraphe en évidence, voici quelques directives:

- note
- tip
- warning

Le code Markdown pour utiliser une directive est:

    ```{note}
    This is a note.
    ```

```{note}
This is a note.
```

```{tip}
This is a tip.
```

```{warning}
This is a warning.
```

## Insérer une image

Le code suivant insère une image.

    ![](../img/logo.png)

![](../img/logo.png)

## Math

Le code suivant insère une formule mathématique en LaTeX.

    $$\frac{a + b}{1+x^2}$$


$$\frac{a + b}{1+x^2}$$


## Sidebar
Vous pouvez intégrer un texte dans le côté gauche du texte. 
Les deux textes sont séparés par une barre verticale.
Ceci est à éviter si le document est destiné pour smartphone.

```{sidebar} My sidebar title
My sidebar content
```

## Margin content
Vous pouvez placer un texte dans la marge.
Ceci est à éviter si le document est destiné pour smartphone.

```{margin} An optional title
My margin content
```

--- 
## Notebook Statistics

Le code

    ```{nb-exec-table}
    ```
    
affiche les statistiques des Jupyter notebooks.

```{nb-exec-table}
```


## Inclure un document

Le code

    ``` {literalinclude} hello.py
    ```

inclut le fichier **hello.py**

``` {literalinclude} hello.py
```

Le code

    ``` {literalinclude} hello.py
    :lines: 2-
    ```
    
inclut le fichier à partir de la ligne 2.

``` {literalinclude} hello.py
:lines: 2-
```

## Télécharger un document

Le code

    {download}`hello.py <hello.py>`

permet de télécharger un fichier.  
{download}`download <hello.py>`

    {download}`demo.txt <demo.txt>`

{download}`download <demo.txt>`


## Questions à choix multiples

Il est possible d'intégrer des questions à choix multiples au fil des pages via la directive `question`.
Dans le corps de la directive, les bonnes et mauvaises réponses sont indiquées via les rôles `{v}` et `{f}` pour *vrai* et *faux*.

`````{tabbed} Aperçu
```{question}
Combien y a-t-il de bits dans un octet ?
Je pense qu'il y en a {f}`2`, {f}`4`, {v}`8` ou {f}`64`.
```
`````

`````{tabbed} Code
````{code-block} markdown
```{question}
Combien y a t'il de bits dans un octet ?
Je pense qu'il y en a {f}`2`, {f}`4`, {v}`8` ou {f}`64`.
```
````
`````

Il est possible de changer le titre affiché au-dessus de la question.
Le contenu de la question peut lui-même être structuré en Markdown.
Dans l'exemple ci-dessous, les réponses sont affichées dans une liste.

`````{tabbed} Aperçu
```{question} Question avec un titre personnalisé
Parmi les informaticiens et informaticiennes suivants, qui a reçu le prix Turing ?
* {v}`Barbara Liskov`
* {v}`Niklaus Wirth`
* {f}`Alan Turing`
* {v}`Tim Berners-Lee`
```
`````

`````{tabbed} Code
````{code-block} markdown
```{question} Question avec un titre personnalisé
Parmi les informaticiens et informaticiennes suivants, qui a reçu le prix Turing ?
* {v}`Barbara Liskov`
* {v}`Niklaus Wirth`
* {f}`Alan Turing`
* {v}`Tim Berners-Lee`
```
````
`````


## Blancs

Pour ajouter des *blancs* dans le texte, il suffit d'utiliser le rôle `bl`.
Dans le texte du rôle, les différentes options de réponses sont séparées par un caractère `|`.
Une réponse valable est précédée d'un caractère `>`.

`````{tabbed} Aperçu
Dans le texte suivant, certains {bl}`>mots|trucs|machins` sont laissés {bl}`pour compte|>blancs|verts|seuls`.
`````

`````{tabbed} Code
```{code-block} markdown
Dans le texte suivant, certains {bl}`>mots|trucs|machins` sont laissés {bl}`pour compte|>blancs|verts|seuls`.
```
`````