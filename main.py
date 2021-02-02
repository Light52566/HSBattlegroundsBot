from CardLibrary import CardLibrary


def main():
    lib = CardLibrary()
    lib.setPath("cardlib.json")
    lib.loadLibrary()
    cardlib = lib.getLibrary()
    

if __name__ == "__main__":
    main()