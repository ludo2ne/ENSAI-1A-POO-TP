"""Un module avec des fonctions diverses et variées."""


def verifier_nombre_parfait(n):
    """"Vérifie si un nombre est parfait.

    Un nombre parfait est un entier naturel égal à la somme de ses diviseurs
    stricts.

    Parameters
    ----------
    n : int
        L'entier à vérifier.

    Returns
    -------
    bool
        Vrai si l'entier est parfait, faux sinon.

    Examples
    --------
    >>> verifier_nombre_parfait(6)
    True
    >>> verifier_nombre_parfait(8)
    False
    >>> verifier_nombre_parfait(28)
    True
    >>> any(verifier_nombre_parfait(n) for n in range(29, 496))
    False
    >>> verifier_nombre_parfait(496)
    True

    """
    if not (isinstance(n, int) and n > 0):
        raise ValueError("'n' doit être un entier strictement positif")

    # Cas x = 1
    dividers = [1]

    # Cas x > 1
    for x in range(2, n):
        if n%x == 0:
            dividers.append(x)

    return sum(dividers) == n




def verifier_pangramme(text):
    """Vérifie si une chaîne de caractères est un pangramme.

    Un pangramme est une phrase contenant toutes les lettres de l'alphabet.
    Ici, nous considérerons une chaîne de caractères sans se soucier du nombre
    de phrases dans cette chaîne de caractères.

    Parameters
    ----------
    text : str
        Phrase.

    Returns
    -------
    bool
        Vrai si la phrase est un pangramme, faux sinon.

    Examples
    --------
    >>> verifier_pangramme(''.join((chr(n) for n in range(97, 123))))
    True
    >>> verifier_pangramme(''.join((chr(n) for n in range(97, 122))))
    False
    >>> verifier_pangramme(''.join((chr(n) for n in range(65, 91))))
    True
    >>> verifier_pangramme(''.join((chr(n) for n in range(66, 91))))
    False
    >>> verifier_pangramme('The quick brown fox jumps over the lazy dog')
    True
    >>> verifier_pangramme('abcdef')
    False
    """
    # Convert all the characters to lower cases
    text_lower = text.lower()

    # Check, for each letter, if it is present in the lowercase text
    for n in range(97, 123):
        letter = chr(n)
        if not letter in text_lower:
            return False
    return(True)

def trier_liste_trait(text):
    """Trie une chaîne de caractères où les mots sont séparés par des traits.

    Parameters
    ----------
    text : str
        Chaîne de caractères contenant les mots à trier.

    Returns
    -------
    str
        La chaîne de caractères avec les mots triés.

    Examples
    --------
    >>> trier_liste_trait('green-red-yellow-black-white')
    'black-green-red-white-yellow'
    >>> trier_liste_trait('paris-london-madrid-berlin-lisbon-amsterdam')
    'amsterdam-berlin-lisbon-london-madrid-paris'

    """
    # Meilleure version : words = '-'.join(sorted(text.split('-')))

    # Sépare les mots dans une liste
    words=text.split('-')

    # Trie la liste
    words_sorted=sorted(words)

    # Récupère le premier mot
    res=f'{words_sorted[0]}'

    # Ajoute un trait d'union et le mot suivant pour les mots restants
    for word in words_sorted[1:]:
        res+=f'-{word}'
    return res


def position(mots, x, n):
    """Renvoie la liste des mots ayant le caractère x à la n-ième position.

    Parameters
    ----------
    mots : list[str]
        Liste de mots.

    x : str
        Caractère.

    n : int
        Position.

    Returns
    -------
    list[str]
        Sous-liste des mots ayant le caractère x à la n-ième position.

    Examples
    --------
    >>> mots = [
    ...     'Abricot', 'Airelle', 'Ananas', 'Banane', 'Cassis', 'Cerise',
    ...     'Citron', 'Clémentine', 'Coing', 'Datte', 'Fraise', 'Framboise',
    ...     'Grenade', 'Groseille', 'Kaki', 'Kiwi', 'Litchi', 'Mandarine',
    ...     'Mangue', 'Melon', 'Mirabelle', 'Nectarine', 'Orange',
    ...     'Pamplemousse', 'Papaye', 'Pêche', 'Poire', 'Pomme', 'Prune',
    ...     'Raisin'
    ... ]
    >>> position(mots, 'o', 1)
    ['Coing', 'Poire', 'Pomme']
    >>> position(mots, 'a', 42)
    []
    >>> position(mots, 'e', 3)
    ['Airelle']

    """
    return [word for word in mots if word[n : n + 1] == x]


def suites_recurrentes_premier_ordre(u0, v0, fu, fv, n):
    """Calcul les valeurs des deux suites récurrentes du premier ordre.

    On considère deux suites récurrentes (u_k)_k et (v_k)_k définies par :
        - Initialisation : u_0 = u0 et v_0 = v0
        - Relations de recurrence :
            + u_k = fu(u_{k-1}, v_{k-1})
            + v_k = fv(u_{k-1}, v_{k-1})

    Cette fonction renvoie les valeurs u_n et v_n des suites (u_k)_k et (v_k)_k.

    Parameters
    ----------
    u0, v0 : float
        Initialisation des suites

    fu, fv : callable
        Relations de récurrence

    n : int
        Indice des valeurs des suites à renvoyer

    Returns
    -------
    un, vn : float
        Valeurs à l'indice n des suites (u_k)_k et (v_k)_k

    """
    # Initialisation
    u, v = u0, v0

    # Récurrence
    for _ in range(n):
        u,v=fu(u, v),fv(u, v)

    return u, v


def verifier_nombre_palindrome(n):
    """Vérifie si un nombre est un palindrome.

    Un nombre est un palindrome si et seulement s'il se lit de la même façon de la gauche vers la droite ou de la droite vers la gauche.

    Parameters
    ----------
    n : int
        Nombre.

    Returns
    -------
    bool
        Vrai si le nombre est un palindrome, faux sinon.

    Examples
    --------
    >>> verifier_nombre_palindrome(9)
    True
    >>> verifier_nombre_palindrome(12345678987654321)
    True
    >>> verifier_nombre_palindrome(12345678997654321)
    False
    """

    if not (isinstance(n, int) and n > 0):
        raise ValueError("'n' doit être un entier strictement positif")

    # Meilleure solution :
    # n_str = str(n)
    # return n_str == n_str[::-1]

    n_copy     = n
    n_reversed = 0
    while n != 0:
        r          = n%10
        n_reversed = n_reversed*10+r
        n          = n//10

    return n_reversed == n_copy


import datetime


def calculer_nombre_jours_restants_anniversaire(date_naissance):
    """Calcule le nombre de jours restants jusqu'au prochain anniversaire.

    Parameters
    ----------
    date_naissance : datetime.date
        Date de naissance.

    Returns
    -------
    ecart : int
        Nombre de jours jusqu'au prochain anniversaire.

    """
    #Récupère la date d'aujourd'hui
    today = date_naissance.today()

    #Calcule la date d'anniversaire de cette année
    next_birthday = datetime.date(today.year, date_naissance.month, date_naissance.day)

    #Calcule le nombre de jours entre la date d'anniversaire de cette année
    res = (next_birthday - today).days  

    #Si le nombre de jours est négatif
    if res < 0:
        #Le porochain anniversaire est l'année prochaine
        next_birthday = datetime.date(today.year + 1, date_naissance.month, date_naissance.day)
        res = (next_birthday - today).days

    return(res)