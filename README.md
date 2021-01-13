# Education numérique

Ce site présente une introduction à l'informatique.
Elle vise l'éducation numérique et utilise le langage **Python** pour illustrer les concepts.

Les sources sont écrit dans le format **Jupyter notebook** et compilé avec **jupyter-book**.

Pour compiler :

  cd doc
  jupyter-book build .

Le résultat se trouvera dans **_build/html**
Pour transférer les pages HTML sur GitHub pages: 

  ghp-import -n -p -f _build/html
  
