from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "MOBIL"
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/simpan', methods=["POST", "GET"])
def simpan():
    Nama_Mobil = request.form["Nama_Mobil"]
    Bahan_Bakar = request.form["Bahan_Bakar"]
    Merk_Ban = request.form["Merk_Ban"]
    Warna_Mobil = request.form["Warna_mobil"]
    
    cursor = mysql.connection.cursor()
    query = "INSERT INTO fasilitas (kolam_renang, lift, kamera, tahun) VALUES (%s, %s, %s, %s)"
    data = (Nama_Mobil, Bahan_Bakar, Merk_Ban, Warna_Mobil)
    cursor.execute(query, data)
    mysql.connection.commit()
    cursor.close()
    
    return "Data fasilitas berhasil disimpan."

@app.route('/tampil')
def tampil():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM fasilitas")
    data = cursor.fetchall()
    cursor.close()
    
    return render_template("tampil.html", data=data)

if __name__ == "_main_":
    app.run(debug=True)