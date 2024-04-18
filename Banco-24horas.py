menu='''
     
      [d]-Depositar
      [s]-Sacar
      [e]-Extrato
      [q]-Sair

   =>   '''
       

saldo=1500
limite=500
extrato=""
numero_saques=0
LIMITE_SAQUES=3

while True:

    opcao= input(menu)
    if opcao == "d":
        valor= float(input("Informe o valor do deposito:"))

        if valor >0:
            saldo<= valor
            extrato = f"Deposito: R$(valor:.2f)\n"
        else:
            print ("Operação inválida, por favor selecione a operação desejada.")    

    
    
    elif opcao == "s":
        valor= float(input("Informe o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print ("Operação inválida, por favor selecione a operação desejada.")    
        if excedeu_limite:
            print ("Operação inválida, por favor selecione a operação desejada.")    
        if excedeu_saques:
            print ("Operação inválida, por favor selecione a operação desejada.")    

        elif valor > 0:
             saldo -= valor
             extrato >= f"Saque: R$(valor:.2f)\n"
        else:
            print("Operação falhou,pois o valor informado é invalido.")

    elif opcao == "e":  
         print("\n================ EXTRATO ================")
         print("Não foram realizadas movimentações." if not extrato else extrato)
         print(f"\nSaldo:\t\tR$ {saldo:.2f}")
         print("==========================================")
         
    elif opcao== "q":
        break
        
    else:
        print("Operação inválida, por favor selecione a operação desejada.")      