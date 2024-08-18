from flask import Flask, jsonify, request, render_template
from models import db, Direktorat, Kawasan, Negara
from repository import NegaraRepository

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/geographical'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Flask application is running!", 200

# Create a new Negara
@app.route('/api/negara', methods=['POST'])
def create_negara():
    data = request.json
    negara = NegaraRepository.create_negara(data)
    return jsonify({'message': 'Negara created successfully'}), 201

# Get all Negara
@app.route('/api/negara', methods=['GET'])
def get_all_negara():
    all_negara = Negara.query.all()
    result = []
    for negara in all_negara:
        negara_data = {
            'id_negara': negara.id_negara,
            'nama_negara': negara.nama_negara,
            'kode_negara': negara.kode_negara,
            'id_kawasan': negara.id_kawasan,
            'id_direktorat': negara.id_direktorat,
            'created_at': negara.created_at,
            'updated_at': negara.updated_at,
            'nama_kawasan': negara.kawasan.nama_kawasan,  # Mengambil nama_kawasan dari relasi
            'nama_direktorat': negara.direktorat.nama_direktorat  # Mengambil nama_direktorat dari relasi
        }
        result.append(negara_data)
    return jsonify(result), 200

# Get a specific Negara by ID
@app.route('/api/negara/<int:id>', methods=['GET'])
def get_negara(id):
    negara = Negara.query.get_or_404(id)
    negara_data = {
        'id_negara': negara.id_negara,
        'nama_negara': negara.nama_negara,
        'kode_negara': negara.kode_negara,
        'id_kawasan': negara.id_kawasan,
        'id_direktorat': negara.id_direktorat,
        'created_at': negara.created_at,
        'updated_at': negara.updated_at,
        'nama_kawasan': negara.kawasan.nama_kawasan,
        'nama_direktorat': negara.direktorat.nama_direktorat
    }
    return jsonify(negara_data), 200

# Update a specific Negara by ID
@app.route('/api/negara/<int:id>', methods=['PUT'])
def update_negara(id):
    data = request.json
    negara = Negara.query.get_or_404(id)
    negara.id_kawasan = data['id_kawasan']
    negara.id_direktorat = data['id_direktorat']
    negara.nama_negara = data['nama_negara']
    negara.kode_negara = data['kode_negara']
    db.session.commit()
    return jsonify({'message': 'Negara updated successfully'}), 200

# Delete a specific Negara by ID
@app.route('/api/negara/<int:id>', methods=['DELETE'])
def delete_negara(id):
    NegaraRepository.delete_negara(id)
    return jsonify({'message': 'Negara deleted successfully'}), 200

# Serve the geomap page
@app.route('/geomap')
def geomap():
    return render_template('geomap.html')

# Serve the datatable page
@app.route('/datatable')
def datatable():
    return render_template('datatable.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
