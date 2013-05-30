import random


# n=3600 => 5 horas de busqueda en twitter
def select_random_rows(rows, n=3600):
    """
returns a list of n objects from rows,
chosen randomly
    """
    nrows = []
    for i in range(n):
        r = random.randint(0, n - i - 1)
        nrows.append(rows[r])
        rows.remove(rows[r])
    return nrows
