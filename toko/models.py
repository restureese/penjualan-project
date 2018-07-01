from toko import db

from werkzeug.security import generate_password_hash, check_password_hash
import datetime

import random

import barcode

class Pegawai(db.Model):
	__tablename__ = 'pegawai'
	kode = db.Column(db.String(6), primary_key=True)
	nama = db.Column(db.String(128),nullable=False)
	username = db.Column(db.String(128),nullable=False)
	password = db.Column(db.String(128),nullable=False)

	def __init__(self, kode, nama, username, password):
		self.kode = kode.upper()
		self.nama = nama.upper()
		self.username = username
		self.password = generate_password_hash(password)

	def __repr__(self):
		return '<Pegawai bernama %r>' % self.nama

	def check_password(self,password):
		return check_password_hash(self.password,password)


class JenisBarang(db.Model):
	__tablename__ = 'jenis_barang'
	kode = db.Column(db.Integer,primary_key=True,autoincrement=True)
	nama = db.Column(db.String(128),nullable=False)

	def __init__(self, nama):
		self.nama = nama

	def __repr__(self):
		return 'Jenis Barang %r' % self.nama


class Barang(db.Model):
	__tablename__ = 'barang'
	kode = db.Column(db.Integer,primary_key=True)
	nama = db.Column(db.String(128),nullable=False)
	jenis_barang = db.Column(db.Integer,db.ForeignKey('jenis_barang.kode'))
	satuan = db.Column(db.String(32))
	harga_beli = db.Column(db.Integer,nullable=False)
	harga_jual = db.Column(db.Integer,nullable=False)
	stok = db.Column(db.Integer,nullable=False)

	def get_barcode(self):
		EAN = barcode.get_barcode_class('ean13')
		ean = EAN(u'{0}'.format(self.kode))

	def get_kode():
		kode = random.randint(100000000000,999999999999)

	def __init__(self, nama, jenis_barang, satuan, harga_beli, harga_jual, stok):
		self.kode = get_kode()
		self.nama = nama
		self.jenis_barang = jenis_barang
		self.satuan = satuan
		self.harga_beli = harga_beli
		self.harga_jual = harga_jual
		self.stok = stok

	def __repr__(self):
		return '{0} - {1}'.format(self.kode, self.nama)


class Penjualan(db.Model):
	__tablename__ = 'penjualan'
	nota = db.Column(db.String(128),primary_key=True)
	kasir = db.Column(db.String(6),db.ForeignKey('pegawai.kode'))
	tanggal = db.Column(db.DateTime,default=datetime.datetime.utcnow,nullable=False)

	def __init__(self, nota, kasir, tanggal):
		self.nota = nota
		self.kasir = kasir
		self.tanggal = tanggal

	def __repr__(self):
		return 'nota {0} kasir {1}'.format(self.nota,self.kasir)


class DetailPenjualan(db.Model):
	__tablename__ = 'detail_penjualan'
	item = db.Column(db.Integer,primary_key=True,autoincrement=True)
	nota = db.Column(db.String(128),db.ForeignKey('penjualan.nota'))
	barang = db.Column(db.Integer,db.ForeignKey('barang.kode'),nullable=False)
	jumlah = db.Column(db.Integer,nullable=False)
	total = db.Column(db.Integer,nullable=False)

	def update_stok(self):
		barang = Barang.query.filter_by(kode=self.barang).first()
		barang.stok = barang.stok - self.jumlah

	def get_total(self):
		barang = Barang.query.filter_by(kode=self.barang).first()
		return barang.harga_jual * self.jumlah

	def __init__(self, item, nota, barang, jumlah):
		self.item = item
		self.nota = nota
		self.barang = barang
		self.jumlah = jumlah
		self.total = get_total()
		update_stok()

	def __repr__(self):
		return 'nota {0} barang ke {1}'.format(self.nota, self.barang)