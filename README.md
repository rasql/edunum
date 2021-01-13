# Education numérique

Ce site présente une introduction à l'informatique.
Il vise l'éducation numérique en langue française.

Nous avons fait le choix d'utiliser le langage **Python** pour illustrer les concepts d'informatique.

Les fichiers sources sont écrit dans le format **Jupyter notebook** et compilé avec **jupyter-book**.

Le matériel est présenté sous forme de site web statique ou sous forme de notebook dynamique sur Binder.

Pour compiler les fichiers en local utilisez:

```
cd doc
jupyter-book build .
```

Le résultat se trouvera dans **_build/html**
Pour transférer les pages HTML sur GitHub pages utilisez:

```
ghp-import -n -p -f _build/html
```
  
Les pages en ligne se trouvent à l'adresse
https://rasql.github.io/edunum