from logica.CuentaBancaria import CuentaBancaria

if __name__ == '__main__':
    saldoInicial = float(input("Ingrese el saldo inicial: "))
    cuentaBancaria = CuentaBancaria(saldoInicial)
    cuentaBancaria.interes()
    cuentaBancaria.imprimirSaldo()
