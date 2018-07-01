from flask import render_template, url_for, redirect
from toko import app, db
from toko.forms import TambahPegawai, Login
from toko.models import Pegawai

@app.route('/')
def index():
	return render_template('index.html')

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

		return redirect(url_for('index'))
	return render_template('tambah-pegawai.html',form=form_pegawai)


@app.route('/login',methods=['GET','POST'])
def login():
	login = Login()

	if login.validate_on_submit():
		pegawai = Pegawai.query.filter_by(username=login.username.data).first()

		if pegawai is None or not pegawai.check_password(password=login.password.data):
			return redirect(url_for('login'))
		return redirect(url_for('index'))
	return render_template('login.html',form=login)