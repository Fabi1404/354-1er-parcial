from operator import eq
from kanren import var, eq, run, Relation, facts

a = var()

padre = Relation()
facts(padre, ('juan', 'fabiola'), ('juan', 'daniela'), ('juan', 'tamara'), ('hilarion', 'juan'), ('simon', 'matilde'))

madre = Relation()
facts(madre, ('matilde', 'fabiola'), ('matilde', 'daniela'), ('matilde', 'tamara'), ('petrona', 'matilde'), ('petrona', 'juan'))

hijo = Relation()
facts(hijo, ('fabiola', 'matilde'), ('daniela', 'matilde'), ('tamara', 'matilde'), ('fabiola', 'juan'), ('daniela', 'juan'), ('tamara', 'juan'))

tio = Relation()
facts(tio, ('luis', 'fabiola'), ('luis', 'daniela'), ('luis', 'tamara'))

tia = Relation()
facts(tia, ('berta', 'fabiola'), ('berta', 'daniela'), ('berta', 'tamara'))

abuelo = Relation()
facts(abuelo, ('hilarion', 'fabiola'), ('hilarion', 'daniela'), ('hilarion', 'tamara'), ('simon', 'fabiola'), ('simon', 'daniela'), ('simon', 'tamara'))

abuela = Relation()
facts(abuela, ('petrona', 'fabiola'), ('petrona', 'daniela'), ('petrona', 'tamara'))

print(run(3, a, abuelo(a, 'fabiola')))
print(run(3, a, abuela(a, 'fabiola')))
print(run(3, a, padre(a, 'fabiola')))
print(run(3, a, madre(a, 'fabiola')))
print(run(3, a, tio(a, 'fabiola')))
print(run(3, a, tia(a, 'fabiola')))

