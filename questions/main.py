from app import main


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("error: ", ex)
