from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Kawasan(db.Model):
    __tablename__ = 'kawasan'
    
    id_kawasan = db.Column(db.Integer, primary_key=True)
    nama_kawasan = db.Column(db.String(100), nullable=False)

    # Relasi ke Negara
    negara = relationship('Negara', back_populates='kawasan')


class Direktorat(db.Model):
    __tablename__ = 'direktorat'
    
    id_direktorat = db.Column(db.Integer, primary_key=True)
    nama_direktorat = db.Column(db.String(100), nullable=False)

    # Relasi ke Negara
    negara = relationship('Negara', back_populates='direktorat')


class Negara(db.Model):
    __tablename__ = 'negara'
    
    id_negara = db.Column(db.Integer, primary_key=True)
    nama_negara = db.Column(db.String(100), nullable=False)
    kode_negara = db.Column(db.String(3), nullable=False)
    id_kawasan = db.Column(db.Integer, db.ForeignKey('kawasan.id_kawasan'), nullable=False)
    id_direktorat = db.Column(db.Integer, db.ForeignKey('direktorat.id_direktorat'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Relasi ke Kawasan
    kawasan = relationship('Kawasan', back_populates='negara')

    # Relasi ke Direktorat
    direktorat = relationship('Direktorat', back_populates='negara')
