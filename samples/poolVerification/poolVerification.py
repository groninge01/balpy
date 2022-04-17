import balpy


def main():
    network = "fantom"
    poolId = "0x1352fd97a1828093bf375f62e088bc196facd1ee000000000000000000000404"
    # On Ethereum and Ethereum testnets, you can pass creationHash=None
    # On Polygon, you must pass the pool creation hash to generate verification params
    creationHash = None
    # creationHash = "0x18c7e1c9235c6e93878e55a87ed249f9d0ceb9d12ee584794e92f80f7645686d";
    verbose = True

    bal = balpy.balpy.balpy(network)
    isVerified = bal.isContractVerified(poolId, verbose=verbose)
    if not isVerified:
        command = bal.balGeneratePoolCreationArguments(
            poolId, verbose=verbose, creationHash=creationHash
        )
    else:
        print("Pool is already verified")
        quit()

    print()
    print(command)
    print()

    print(
        "If you need more complete instructions on what to do with this command, go to:"
    )
    print("\thttps://dev.balancer.fi/resources/pools/verification\n")


if __name__ == "__main__":
    main()
