import requests


RPC_URL = "http://public.test2.bfa.ar:8545"


# Simulación de documentos conocidos


DOCUMENTS = [
    {
        "name": "Documento A",
        "doc_hash": "abc123fakehash",
        "block_number": 37313737,
        "expected_block_hash": "0xeee93e0993dee36a3a99b36af8b685c450e3f65c90558fdca385dfa91b295491"
    },
    {
        "name": "Documento B",
        "doc_hash": "otrohashfake",
        "block_number": 37313736,
        "expected_block_hash": "0x27f1733bbc179a0176546af634e8a33f119bc953de540a06d8e9aeec3001fe89"
    }
]


def rpc_call(method, params=[]):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(RPC_URL, json=payload)
    return response.json().get("result")


def get_block(block_number):
    return rpc_call("eth_getBlockByNumber", [hex(block_number), False])


def verify_document(doc):
    print(f"\n🔎 Verificando: {doc['name']}")


    block = get_block(doc["block_number"])


    if not block:
        print("❌ Bloque no encontrado")
        return False


    real_block_hash = block["hash"]


    print("Block esperado: ", doc["expected_block_hash"])
    print("Block real:     ", real_block_hash)


    # 1. Verificar hash del bloque
    if real_block_hash != doc["expected_block_hash"]:
        print("❌ El bloque fue alterado o no coincide")
        return False


    # 2. Verificar que tenga parent (integridad básica)
    if not block["parentHash"]:
        print("❌ Bloque inválido (sin parent)")
        return False


    # 3. Simulación de validación de documento
    print(f"📄 Hash documento: {doc['doc_hash']}")
    print(f"⛓ Anclado en bloque: {doc['block_number']}")


    print("✅ Documento VALIDADO (integridad blockchain confirmada)")
    return True


def main():
    for doc in DOCUMENTS:
        verify_document(doc)


if __name__ == "__main__":
    main()
