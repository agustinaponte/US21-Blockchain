import requests


RPC_URL = "http://public.test2.bfa.ar:8545"


BLOCKS_TO_SHOW = 5


def rpc_call(method, params=[]):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(RPC_URL, json=payload)
    return response.json().get("result")


def hex_to_int(hex_value):
    return int(hex_value, 16)


def get_latest_block_number():
    return hex_to_int(rpc_call("eth_blockNumber"))


def get_block(block_number):
    return rpc_call("eth_getBlockByNumber", [hex(block_number), True])


def main():
    latest_block = get_latest_block_number()
    print(f"Último bloque: {latest_block}\n")


    for i in range(BLOCKS_TO_SHOW):
        block_number = latest_block - i
        block = get_block(block_number)


        if not block:
            continue


        print("\n==============================")
        print(f"Bloque: {block_number}")
        print("==============================")


        print("Block Hash:      ", block["hash"])
        print("Parent Hash:     ", block["parentHash"])
        print("State Root:      ", block["stateRoot"])
        print("Tx Root:         ", block["transactionsRoot"])
        print("Receipts Root:   ", block["receiptsRoot"])
        print("Miner:           ", block["miner"])
        print("Gas Used:        ", int(block["gasUsed"], 16))
        print("Gas Limit:       ", int(block["gasLimit"], 16))
        print("Timestamp:       ", int(block["timestamp"], 16))
        print("Tx count:        ", len(block["transactions"]))


        # Si hay transacciones, mostrar hashes
        if block["transactions"]:
            print("\nTransacciones:")
            for tx in block["transactions"]:
                print(" -", tx["hash"])
        else:
            print("\n(No hay transacciones en este bloque)")


if __name__ == "__main__":
    main()
