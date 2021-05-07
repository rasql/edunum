# Markdown

Ce document est écrit en Markdown.

## Directives

Pour mettre un paragraphe en évidence, voici quelques directives:

- note
- tip
- caution
- attention
- warning
- danger
- error

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

```{caution}
This is a warning.
```

```{attention}
This is attention info.
```

```{warning}
This is a warning.
```

```{danger}
This is danger info.
```

```{error}
This is error info.
```

## Insert an image
![](../img/logo.png)

## Math
$$\frac{a + b}{1+x^2}$$


## Sidebar
Vous pouvez intégrer un texte dans le côté gauche du texte. 
Les deux textes sont séparés par une barre verticale.

```{sidebar} My sidebar title
My sidebar content
```

## Margin content
Vous pouvez placer un texte dans la marge.

```{margin} An optional title
My margin content
```

## Full-width

````{div} full-width
```{note}
Here's a note that will take the full width
```
````

--- 
## Notebook Statistics
Voici les statistiques des Jupyter notebooks.

```{nb-exec-table}
```


## Inclure un document

Inclure le fichier **hello.py**

``` {literalinclude} hello.py
```

Inclure à partir de la ligne 2.

``` {literalinclude} hello.py
:lines: 2-
```

## Télécharger un document

    {download}`hello.py <hello.py>`

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