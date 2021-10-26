from config import os, db, arquivobd

class Cachorros(db.Model):

    #Atributos de Cachorros
    id    = db.Column(db.Integer, primary_key=True)
    Nome  = db.Column(db.String(254))
    Raca  = db.Column(db.String(254))
    Idade = db.Column(db.String(254))
    Dono  = db.Column(db.String(254))

    def __str__(self):
        return str(self.id)+") "+ self.Nome + ", " + self.Raca + ", " + self.Idade + ", " + self.Dono

    def json(self):
        return {
            "id": self.id,
            "Nome": self.Nome,
            "Raca": self.Raca,
            "Idade": self.Idade,
            "Dono": self.Dono
        }
 
if __name__ == "__main__":

    #Apaga arquivo existente
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    #Criando dados para BD
    c1 = Cachorros(Nome = "Cloe", Raca = "FreshPoodle",Idade = "4", Dono = "Juanes")
    c2 = Cachorros(Nome = "Toby", Raca = "Bulldozer",  Idade = "5", Dono = "Jefritto")
    c3 = Cachorros(Nome = "Tito", Raca = "Vira-lata",  Idade = "1", Dono = "Nicolas")
    c4 = Cachorros(Nome = "Mel",  Raca = "Bulldog",    Idade = "3", Dono = "Mariana")

    #Adiciona Cachorros ao BD
    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.add(c4)
    db.session.commit()