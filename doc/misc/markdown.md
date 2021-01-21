# Markdown

Ce document est écrit en Markdown.

## Directives

Pour mettre un paragraphe en évidence il y a ces directives:

- note
- tip
- caution
- attentino
- warning
- danger
- error

Le code Markdown pour une directive est:

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
![](../logo.png)

## Math
$$\frac{a + b}{1+x^2}$$


## Sidebar
Vous pouvez intégrer un texte dans le coté gauche du texte. 
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


## inclure un document

Inclure le fichier **hello.py**

``` {literalinclude} txtllo.py
txt`

Inclure à partir de la ligne 2.

``` {literalinclude} hello.py
:lines: 2-
```

## Télécharger un document

{download}`hello.py <hello.py>`

{download}`download <hello.py>`

{download}`demo.txt <demo.txt>`

{download}`download <demo.txt>`
