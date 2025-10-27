from application.app import init_app

tapp = init_app()

if __name__ == "__main__":
    tapp.run(debug="True")