from price_getter import service, __app_name__

def main():
    while True:
        service.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()