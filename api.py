from flask import (
    Flask,
    render_template
)
import connexion

# criando instancia da aplicacao
app = connexion.App(__name__,specification_dir='/')

#le swagger.yml para configurar os enpoints
# app.add_api('swagger.yml')

#cria a rota da URL / padrao
@app.route('/')
def home():
    """
    Apenas para bater na localhost:5000/
    
    """
    return render_template('home.html')

# Se estivermos executando no modo autônomo, execute o aplicativo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)