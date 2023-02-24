pop_a = 80000
taxa_a = 1.03
pop_b = 200000
taxa_b = 1.015
anos = 0

while pop_a < pop_b:
    pop_a = pop_a * taxa_a
    pop_b = pop_b * taxa_b
    anos = anos + 1

print("A população A ultrapassou B após "+str(anos)+" anos")