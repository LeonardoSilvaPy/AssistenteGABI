import subprocess
import sys

def install_package(package):
    try:
        # Tenta instalar o pacote sem preferência por binário
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Pacote '{package}' instalado com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Falha ao instalar o pacote '{package}', tentando com binário.")
        try:
            # Caso falhe, tenta instalar o pacote com preferência por binário
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--prefer-binary", package])
            print(f"Pacote '{package}' instalado com sucesso (binário).")
        except subprocess.CalledProcessError:
            print(f"Falha ao instalar o pacote '{package}', ignorado.")

def install_requirements():
    with open('requirements.txt') as f:
        for line in f:
            package = line.strip()
            if package:  # Verifica se a linha não está vazia
                install_package(package)

if __name__ == "__main__":
    install_requirements()
