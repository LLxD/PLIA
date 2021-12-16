def mundoAspirador():

    objetivo_estado = {'A': '0', 'B': '0'}
    custo = 0

    print("LUGARES DISPONIVEIS: A e B")
    print("ESTADOS DISPONIVEIS: 0 -> Limpo e 1 -> Sujo")
    lugar_input = input("Insira lugar do Aspirador ")

    status_input = input("Insira status do " + lugar_input+" ")
    status_input_outro_comodo = input("Insira status do outro comodo ")
    print("Condição inicial do lugar " + str(objetivo_estado))

    if lugar_input == 'A':
        print("Aspirador foi colocado em lugar A")
        if status_input == '1':
            print("lugar A está sujo.")

            objetivo_estado['A'] = '0'
            custo += 1
            print("custo para limpar A " + str(custo))
            print("lugar A foi limpo.")

            if status_input_outro_comodo == '1':

                print("lugar B está sujo.")
                print("Indo para o lugar B. ")
                custo += 1
                print("custo para mover a direita" + str(custo))

                objetivo_estado['B'] = '0'
                custo += 1
                print("custo para limpar B " + str(custo))
                print("lugar B foi limpo. ")
            else:

                print("lugar B está limpo.")

        if status_input == '0':
            print("lugar A está limpo ")
            if status_input_outro_comodo == '1':
                print("lugar B está sujo.")
                print("Indo para o lugar B. ")
                custo += 1
                print("custo para mover a direita " + str(custo))

                objetivo_estado['B'] = '0'
                custo += 1
                print("custo para limpar B" + str(custo))
                print("lugar B foi limpo. ")
            else:
                print(custo)
                print("lugar B está limpo.")

    else:
        print("Aspirador foi colocado em lugar B")

        if status_input == '1':
            print("lugar B está sujo.")

            objetivo_estado['B'] = '0'
            custo += 1
            print("custo para limpar " + str(custo))
            print("lugar B foi limpo.")

            if status_input_outro_comodo == '1':

                print("lugar A está sujo.")
                print("Movendo para lugar A. ")
                custo += 1
                print("custo para ir para a esquerda" + str(custo))

                objetivo_estado['A'] = '0'
                custo += 1
                print("custo para limpar B " + str(custo))
                print("lugar A foi limpo.")

        else:
            print(custo)

            print("lugar B está limpo.")

            if status_input_outro_comodo == '1':
                print("lugar A está sujo.")
                print("Movendo para lugar A. ")
                custo += 1
                print("custo para ir para a esquerda " + str(custo))

                objetivo_estado['A'] = '0'
                custo += 1
                print("custo para limpar B " + str(custo))
                print("lugar A foi limpo. ")
            else:
                print("lugar A está limpo.")

    print("objetivo estado: ")
    print(objetivo_estado)
    print("Performance: " + str(custo))


mundoAspirador()
