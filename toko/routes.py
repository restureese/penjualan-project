from flask import render_template, url_for, redirect, jsonify, request
from flask_restful import Resource
from toko import app, db, api
from toko.forms import TambahPegawai, Login
from toko.models import Pegawai
import json


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',view='dashboard')

@app.route('/tambah_pegawai',methods=['GET','POST'])
def register():
	form_pegawai = TambahPegawai()

	if form_pegawai.validate_on_submit():
		kode = form_pegawai.kode.data
		nama = form_pegawai.nama.data
		username = form_pegawai.username.data
		password = form_pegawai.password.data

		pegawai = Pegawai(kode,nama,username,password)
		db.session.add(pegawai)
		db.session.commit()

		return redirect(url_for('dashboard'))
	return render_template('tambah-pegawai.html',form=form_pegawai)


@app.route('/login/',methods=['GET','POST'])
def login():
	login = Login()

	if login.validate_on_submit():
		pegawai = Pegawai.query.filter_by(username=login.username.data.upper()).first()

		if pegawai is None or not pegawai.check_password(password=login.password.data):
			return redirect(url_for('login'))
		return redirect(url_for('dashboard'))
	return render_template('login.html',form=login)

@app.route('/dashboard/', methods=['POST','GET'])
def dashboard():
	return render_template('index.html',view='dashboard')

@app.route('/master/',methods=['POST','GET'])
def master():
	return render_template('index.html',view='master')

@app.route('/transaksi/',methods=['POST','GET'])
def transaksi():
	return render_template('index.html',view='transaksi')

@app.route('/akun/',methods=['POST','GET'])
def akun():
	akuns = Pegawai.query.all()

	return render_template('index.html',view='akun',akuns=akuns)

@app.route('/akun/action/',methods=['GET','POST'])
def akunPegawai():
	if request.method == 'POST':
		if request.form['aksi'] == 'tambah':
			kode = str(request.form['kode'])
			nama = str(request.form['nama'])
			username = str(request.form['username'])
			password = str(request.form['password'])

			pegawai = Pegawai(kode, nama, username, password)
			db.session.add(pegawai)
			db.session.commit()
		elif request.form['aksi'] == 'hapus':
			pegawai = Pegawai.query.filter_by(kode=request.form['kode']).first()
			db.session.delete(pegawai)
			db.session.commit()
		else:
			#update akun
			pegawai = Pegawai.query.filter_by(kode=request.form['kode']).first()
			pegawai.nama = request.form['nama']
			pegawai.username = request.form['username']
			pegawai.password = request.form['password']
			db.session.commit()
	
	return jsonify(result='berhasil disimpan')


class PegawaiForm(Resource):
	def post(self):
		pegawai = Pegawai.query.filter_by(kode=request.form['kode']).first()
		return {'kode': pegawai.kode,'nama':pegawai.nama, 'username':pegawai.username, 'password':pegawai.password}

api.add_resource(PegawaiForm, '/pegawai/getdata')