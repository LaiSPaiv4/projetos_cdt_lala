from app import db

class FinancialProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    meta = db.Column(db.String(100)) # "Investir" ou "Organizar"
    renda_mensal = db.Column(db.Float)
    banco_principal = db.Column(db.String(50)) # "Nubank" ou "Inter"

    def calcular_plano_503020(self):
        # A mágica da matemática financeira
        return {
            "essencial": self.renda_mensal * 0.5,
            "estilo_vida": self.renda_mensal * 0.3,
            "reserva_investimento": self.renda_mensal * 0.2
        }


'''from app import db

class FinancialProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    meta = db.Column(db.String(200))
    renda_mensal = db.Column(db.Float, default=0.0)
    gastos_essenciais = db.Column(db.Float, default=0.0)
    estilo_vida = db.Column(db.Float, default=0.0)
    poupanca_investimento = db.Column(db.Float, default=0.0)
    banco_principal = db.Column(db.String(50))#

    def calcular_plano_503020(self):
        plano ={
            "essencial" : self.renda_mensal*0.50,
            "estilo":self.renda_mensal*0.30,
            "reserva": self.renda_mensal*0.20
        }

        return plano'''