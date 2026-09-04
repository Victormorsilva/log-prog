salario = 1000

desconto = 0
print(f"O desconto inicial é {desconto}")

vt = 6/100 * salario
desconto += vt
print(f"\nO desconto incluindo o VT é {desconto}")

vr = 2/100 * salario
desconto += vr
print(f"\nO desconto incluindo o VT e o VR é {desconto}")