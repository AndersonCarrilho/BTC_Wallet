# BTC_Wallet
Criador de Address Bitcoin

Script de criação de wallets Bitcoin de todos os formatos.
Utililizando a biblioteca Blockthon do grande programador PyMmdrza, utilização de alta performance da biblioteca python Multiprocessing, ele cria em instantes centenas de wallets de todos os padrões BTC oficiais que existem.

Para utilizar este script, precisa instalar as bibliotecas python:
    pip install blockthon  |  
    pip install mnemonic

Com uma boa manipulação do código, ele pode ser facilmente adaptado para sistemas de Puzzle BTC!
Neste script atualizado:

    multiprocessing.cpu_count() é usado para determinar o número de processos a serem criados no pool, aproveitando todos os núcleos da CPU disponíveis.
    Não há pausa time.sleep(1) dentro do loop principal, permitindo que o próprio multiprocessing se encarregue de distribuir e executar as tarefas de forma eficiente.
    A estrutura do loop while True permite que o script continue gerando carteiras indefinidamente até que o usuário interrompa com Ctrl+C.

# Observação
O uso deste script para qualquer forma ilegal ou tentativa de Hacker Wallet, e de inteira responsábilidade do usuário.

Qualquer sugestão ou modificações fique a vontade para pedir aqui.
