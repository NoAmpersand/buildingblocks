from solcx import compile_standard

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

compiled_sol = compile_standard({
    "language": "Solidity",
    "source": {"SimpleSotrage.sol": {"content": simple_storage_file}},
    "settings" : {
        "outputSelection" : {
            "*" : {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        },
    }
}
)
