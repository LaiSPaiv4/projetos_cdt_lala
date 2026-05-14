from app import create_app

app = create_app()

if __name__ == "__main__":
    # O host 0.0.0.0 permite que você acesse do celular na mesma rede se quiser
    app.run(debug=True)