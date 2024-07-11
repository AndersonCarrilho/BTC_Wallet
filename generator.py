from Blockthon import Wallet, Bitcoin
from mnemonic import Mnemonic

# Função para gerar endereços Bitcoin e chaves privadas a partir de mnemônicos
def generate_wallet_info(mnemonics):
    seed_bytes = Wallet.Mnemonic_To_Bytes(mnemonics)
    privatekey = Wallet.Bytes_To_PrivateKey(seed_bytes)
    
    p2pkhAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2PKH')
    p2shAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2SH')
    p2wpkhAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WPKH')
    p2wshAddress = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WSH')
    p2wpkhSegwit = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WPKHinP2SH')
    p2wshSegwit = Bitcoin.Address_From_PrivateKey(privatekey, Type='P2WSHinP2SH')
    
    return {
        "PrivateKey": privatekey,
        "P2PKH": p2pkhAddress,
        "P2SH": p2shAddress,
        "P2WPKH": p2wpkhAddress,
        "P2WSH": p2wshAddress,
        "P2WPKHinP2SH": p2wpkhSegwit,
        "P2WSHinP2SH": p2wshSegwit
    }

# Lista de línguas
languages = [
    "english", "chinese_simplified", "chinese_traditional", "french",
    "italian", "japanese", "korean", "spanish", "turkish", "czech", "portuguese"
]

# Gerar mnemônicos em todas as línguas disponíveis e diferentes tamanhos
for language in languages:
    mnemo = Mnemonic(language)
    mnemonics_12 = mnemo.generate(128)
    mnemonics_18 = mnemo.generate(192)
    mnemonics_24 = mnemo.generate(256)

    # Gerar informações da wallet para cada conjunto de mnemônicos
    wallet_info_12 = generate_wallet_info(mnemonics_12)
    wallet_info_18 = generate_wallet_info(mnemonics_18)
    wallet_info_24 = generate_wallet_info(mnemonics_24)

    # Exibir os resultados
    print(f"""
Language: {language}
Mnemonic (12 words): {mnemonics_12}
PrivateKey [Hex]: {wallet_info_12["PrivateKey"]}
{'-' * 22} Bitcoin Addresses {'-' * 22}
Bitcoin P2PKH: {wallet_info_12["P2PKH"]}
Bitcoin P2SH: {wallet_info_12["P2SH"]}
Bitcoin P2WPKH: {wallet_info_12["P2WPKH"]}
Bitcoin P2WSH: {wallet_info_12["P2WSH"]}
Bitcoin P2WPKH in Segwit: {wallet_info_12["P2WPKHinP2SH"]}
Bitcoin P2WSH in Segwit: {wallet_info_12["P2WSHinP2SH"]}

Mnemonic (18 words): {mnemonics_18}
PrivateKey [Hex]: {wallet_info_18["PrivateKey"]}
{'-' * 22} Bitcoin Addresses {'-' * 22}
Bitcoin P2PKH: {wallet_info_18["P2PKH"]}
Bitcoin P2SH: {wallet_info_18["P2SH"]}
Bitcoin P2WPKH: {wallet_info_18["P2WPKH"]}
Bitcoin P2WSH: {wallet_info_18["P2WSH"]}
Bitcoin P2WPKH in Segwit: {wallet_info_18["P2WPKHinP2SH"]}
Bitcoin P2WSH in Segwit: {wallet_info_18["P2WSHinP2SH"]}

Mnemonic (24 words): {mnemonics_24}
PrivateKey [Hex]: {wallet_info_24["PrivateKey"]}
{'-' * 22} Bitcoin Addresses {'-' * 22}
Bitcoin P2PKH: {wallet_info_24["P2PKH"]}
Bitcoin P2SH: {wallet_info_24["P2SH"]}
Bitcoin P2WPKH: {wallet_info_24["P2WPKH"]}
Bitcoin P2WSH: {wallet_info_24["P2WSH"]}
Bitcoin P2WPKH in Segwit: {wallet_info_24["P2WPKHinP2SH"]}
Bitcoin P2WSH in Segwit: {wallet_info_24["P2WSHinP2SH"]}
""")
