import bit_conversor as bc
import adders

if __name__ == "__main__":

    input_a = int(input("Primeiro numero: "))
    input_b = int(input("Segundo numero: "))
    
    a = bc.to_bits(input_a)
    b = bc.to_bits(input_b)

    print(f"Binário: {a} - Decimal: {input_a}")
    print(f"Binário: {b} - Decimal: {input_b}")

    # Transforma em lista pois será necessário iterar sobre os itens
    a = list(map(int, a))
    b = list(map(int, b))

    result = []
    carry_in = 0

    # Faz a iteração de trás pra frente, começando do último bit
    for x in range(len(a) -1, -1, -1):
        sum, carry_out = adders.full_adder(a[x], b[x], carry_in)
        result.append(sum)
        carry_in = carry_out

    # Como salvou de trás pra frente, invertemos a saída para converter em inteiro novamente
    result = ''.join(str(x) for x in reversed(result))

    print(f'Binário: {result} - Decimal: {bc.to_decimal(result)}')
