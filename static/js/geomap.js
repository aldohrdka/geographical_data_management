var map = L.map('map').setView([20, 0], 2); // Pusatkan peta di sekitar ekuator

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Fungsi untuk menetapkan warna berdasarkan direktorat
function getColor(direktorat) {
    var colors = {
        1: '#FF5733', // Warna untuk Direktur 1
        2: '#33FF57', // Warna untuk Direktur 2
        // Tambahkan sesuai kebutuhan
    };
    return colors[direktorat] || '#3388ff'; // Default color jika tidak ditemukan
}

// Ambil data negara dari API
fetch('/api/negara')
    .then(response => response.json())
    .then(data => {
        data.forEach(function(d) {
            var latLng = getLatLngForCountry(d.nama_negara);
            if (latLng) {
                var marker = L.circleMarker(latLng, {
                    radius: 10,
                    fillColor: getColor(d.id_direktorat),
                    color: "#000",
                    weight: 1,
                    opacity: 1,
                    fillOpacity: 0.8
                }).addTo(map);

                var flagUrl = `https://flagcdn.com/w320/${d.kode_negara.toLowerCase()}.png`; // Gunakan kode negara untuk mengambil bendera
                
                marker.bindPopup(`
                    <b>${d.nama_negara}</b><br>
                    Kawasan: ${d.nama_kawasan}<br>
                    Direktorat: ${d.nama_direktorat}<br>
                    <img src="${flagUrl}" alt="Flag of ${d.nama_negara}" width="50px">
                `);
            }
        });
    });

// Fungsi untuk mendapatkan lat, lng berdasarkan nama negara
function getLatLngForCountry(countryName) {
    var countriesLatLng = {
        'Indonesia': [-2.5489, 118.0149],
        'Malaysia': [4.2105, 101.9758],
        'India': [20.5937, 78.9629],
        'China': [35.8617, 104.1954],
        'United States': [37.0902, -95.7129],
        'Netherlands': [52.1326, 5.2913],
        'Germany': [51.1657, 10.4515],
        'Argentina': [-38.4161, -63.6167]
    };

    return countriesLatLng[countryName] || [0, 0]; // Kembalikan [0, 0] jika tidak ditemukan
}
