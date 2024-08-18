from models import db, Negara

class NegaraRepository:

    @staticmethod
    def create_negara(data):
        negara = Negara(
            id_kawasan=data['id_kawasan'],
            id_direktorat=data['id_direktorat'],
            nama_negara=data['nama_negara'],
            kode_negara=data['kode_negara']
        )
        db.session.add(negara)
        db.session.commit()
        return negara

    @staticmethod
    def delete_negara(id):
        negara = Negara.query.get(id)
        if negara:
            db.session.delete(negara)
            db.session.commit()
