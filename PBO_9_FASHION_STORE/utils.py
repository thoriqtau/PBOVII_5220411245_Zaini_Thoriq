def resetOS():
    import os
    sistem_operasi = os.name
    match sistem_operasi:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')

def header():
    print(f"{'SELAMAT DATANG DI TOKO FASHION':^40}")
    print(f"{'SILAHKAN BELANJA':^40}")
    print('-'*40)