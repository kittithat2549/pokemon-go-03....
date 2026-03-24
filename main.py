from pokemon import create_app

app = create_app()

print("RUNNING APP")

if __name__ == "__main__":
    app.run(debug=True)