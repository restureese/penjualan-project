from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length



class TambahPegawai(FlaskForm):
	nama = StringField('Nama Pegawai',validators=[DataRequired(),Length(min=1,max=128)])
	kode = StringField('Kode Pegawai', validators=[DataRequired(),Length(min=3,max=6)])
	username = StringField('Username',validators=[DataRequired(),Length(min=1,max=128)])
	password = PasswordField('Password',validators=[DataRequired()])
	password_cek = PasswordField('Ulangi Password',validators=[DataRequired(),EqualTo('password', message='Passsword Harus Sama!')])
	submit = SubmitField('Tambah Pegawai')

class Login(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	submit = SubmitField('Login')

class TambahBarang(FlaskForm):
