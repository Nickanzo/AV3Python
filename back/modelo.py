from config import os, db, arquivobd

class Telefone(db.Model):

    #Atributos de Telefone
    id = db.Column(db.Integer, primary_key=True)
    celular = db.Column(db.Integer)
    fixo = db.Column(db.Integer)
    emerg = db.Column(db.Integer)

    def __str__(self):
        return str(self.id)+") "+ self.celular + ", " + self.fixo + ", " + self.emerg

    def json(self):
        return {
            "id": self.id,
            "Celular": self.celular,
            "Fixo": self.fixo,
            "Emergencial": self.emerg
        }

class Endereco(db.Model):

    #Atributos de Endereço
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.Integer)
    numero = db.Column(db.Integer)
    compl = db.Column(db.String(20))

    def __str__(self):
        return str(self.id)+") "+ self.cep + ", " + self.numero + ", " + self.compl

    def json(self):
        return {
            "id": self.id,
            "CEP": self.cep,
            "Numero": self.numero,
            "Complemento": self.compl
        }

class Contato(db.Model):

    #Atributos de Endereço
    id = db.Column(db.Integer, primary_key=True)
    enderecoId = db.Column(db.Integer, db.ForeignKey(Endereco.id), nullable=False)
    endereco = db.relationship("Endereco")
    telefoneId = db.Column(db.Integer, db.ForeignKey(Telefone.id))
    telefone = db.relationship("Telefone")

    def __str__(self):
        return str(self.id) + ") " + self.endereco + ", " + self.telefone

    def json(self):
        return {
            "id": self.id,
            "Endereço": self.endereco,
            "Telefone": self.telefone
        }

class Pessoa(db.Model):

    #Atributos de Pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    contatoId = db.Column(db.Integer, db.ForeignKey(Contato.id), nullable=False)
    contato = db.relationship("Contato")

    def __str__(self):
        return str(self.id) + ") " + self.nome + ", " + self.contato

    def json(self):
        return {
            "id": self.id,
            "Nome": self.nome,
            "Contato": self.contato
        }

class Cachorro(db.Model):

    #Atributos de Cachorros
    id    = db.Column(db.Integer, primary_key=True)
    nome  = db.Column(db.String(254))
    idade = db.Column(db.String(254))
    donoId  = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    dono = db.relationship("Pessoa")

    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " + self.idade + ", " + self.dono

    def json(self):
        return {
            "id": self.id,
            "Nome": self.Nome,
            "Idade": self.Idade,
            "Dono": self.Dono
        }

class Dono(db.Model):

    #Atributos de Donos
    id = db.Column(db.Integer, primary_key=True)
    pessoaId = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship("Pessoa")
    cachorroId = db.Column(db.Integer, db.ForeignKey(Cachorro.id), nullable=False)
    cachorro = db.relationship("Cachorro")

    def __str__(self):
        return str(self.id) + ") " + self.pessoa + ", " + self.cachorro

    def json(self):
        return {
            "id": self.id,
            "Pessoa": self.pessoa,
            "Cachorro": self.cachorro
        }

class Tosa(db.Model):

    #Atributos de Tosa
    id = db.Column(db.Integer, primary_key=True)
    cachorroId = db.Column(db.Integer, db.ForeignKey(Cachorro.id), nullable=False)
    cachorro = db.relationship("Cachorro")
    data = db.Column(db.Date())
    horario = db.Column(db.Time())

    def __str__(self):
        return str(self.id) + ") " + self.cachorro + ", " + self.data + ", " + self.horario

    def json(self):
        return {
            "id": self.id,
            "Cachorro": self.cachorro,
            "Data": self.data,
            "Horário": self.horario
        }

class Consultorio(db.Model):

    #Atributos de Consultorio
    id = db.Column(db.Integer, primary_key=True)
    enderecoId = db.Column(db.Integer, db.ForeignKey(Endereco.id), nullable=False)
    endereco = db.relationship("Endereco")
    sala = db.Column(db.String(4))

class Veterinario(db.Model):

    #Atributos de Veterinario
    id = db.Column(db.Integer, primary_key=True)
    pessoaId = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship("Pessoa")
    consultorioId = db.Column(db.Integer, db.ForeignKey(Consultorio.id), nullable=False)
    consultorio = db.relationship("Consultorio")

    def __str__(self):
        return str(self.id) + ") " + self.pessoa + ", " + self.consultorio

    def json(self):
        return {
            "id": self.id,
            "Pessoa": self.pessoa,
            "Consultorio": self.consultorio
        }

class ConsultaVet(db.Model):

    #Atributos de Consulta de Veterinario
    id = db.Column(db.Integer, primary_key=True)
    veterinarioId = db.Column(db.Integer, db.ForeignKey(Veterinario.id), nullable=False)
    veterinario = db.relationship("Veterinario")
    cachorroId = db.Column(db.Integer, db.ForeignKey(Cachorro.id), nullable=False)
    cachorro = db.relationship("Cachorro")
    data = db.Column(db.Date())
    horario = db.Column(db.Time())

    def __str__(self):
        return str(self.id) + ") " + self.veterinario + ", " + self.cachorro + \
               ", " + self.data + ", " + self.horario

    def json(self):
        return {
            "id": self.id,
            "Veterinario": self.veterinario,
            "Cachorro": self.cachorro,
            "Data": self.data,
            "Horario": self.horario
        }