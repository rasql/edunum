# Education numérique

Ce site présente une **introduction à l'informatique**.
Il vise l'éducation numérique en langue française. 
Nous avons fait le choix d'utiliser le langage **Python** pour illustrer les concepts d'informatique.

Les fichiers sources sont 
- écrit dans le format **Jupyter notebook** et 
- compilé avec **jupyter-book**.

Le matériel est présenté sous forme de 
- site web statique ou 
- notebook dynamique sur Binder.

Pour compiler les fichiers en local utilisez:

```
cd doc
jupyter-book build .
```

Le résultat se trouvera dans **_build/html**
Pour transférer les pages HTML sur GitHub pages utilisez:

- n - include à **.nojekyll** file
- p - push the branch to origin/{branch}
- f - force the push to the repository

```
ghp-import -n -p -f _build/html
```
  
Les pages en ligne se trouvent à l'adresse
https://rasql.github.io/edunum


## Installation des outils

```
pip install jupyter-book
pip install ghp-import
```
## Extensions

Des extensions Sphinx ont été ajouté avec un dossier `extension`:
- questions
- blanks
`
Un dossier `doc/_static` a été ajouté avec
- reactions

Le fichier `_config.yml` a été modifié:

    sphinx:
    config:
        html_show_copyright: false
        language: fr
        html_theme: sphinx_book_theme
    local_extensions:
        questions: ../extensions/
        blanks: ../extensions/
        
