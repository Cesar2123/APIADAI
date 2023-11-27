from django.db import models

# Create your models here.

class sesion(models.Model):
    id_user = models.IntegerField(primary_key=True,db_column='idUser')
    name = models.CharField(max_length=100, db_column="Nombre")
    email = models.CharField(max_length=100, db_column="Correo")
    pas = models.CharField(max_length=100, db_column="Pass")
    class Meta:
        db_table = 'Ingreso'
        
    # tabla de respuestas
class formulario(models.Model):
    id_respuesta = models.IntegerField(primary_key=True,db_column='idrespuesta')
    name1 = models.CharField(max_length=100, db_column="Nombres")
    apellidop = models.CharField(max_length=100, db_column="Apellidop")
    apellidom = models.CharField(max_length=100, db_column="Apellidom")
    matricula = models.CharField(max_length=100, db_column="Matricula")
    consideras = models.CharField(max_length=100, db_column="Considerascom")
    compra = models.CharField(max_length=100, db_column="Compraint")
    notificacion = models.CharField(max_length=100, db_column="Notwhats")
    experiencia = models.CharField(max_length=100, db_column="Maneraco")
    productos = models.CharField(max_length=100, db_column="Producnu")
    pago = models.CharField(max_length=100, db_column="pagotarj")
    
    class Meta:
        db_table = 'Formulario'
    