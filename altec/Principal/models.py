from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
	identificacion=models.IntegerField(primary_key=True)
	Nombre=models.CharField(max_length=100,verbose_name='Nombres')	
	Apellido=models.CharField(max_length=100,blank=True,verbose_name='Apellidos')

	def __unicode__(self):
		return '%s %s' % (self.Nombre,self.Apellido)

class Cliente(models.Model):
	identificacion=models.IntegerField(primary_key=True)
	Nombre=models.CharField(max_length=100,verbose_name='Nombres')	
	Apellido=models.CharField(max_length=100,blank=True,verbose_name='Apellidos')	
	tipo_cliente=models.CharField(max_length=100,verbose_name='Tipo Cliente')
	telefono=models.IntegerField(verbose_name='Telefono')
	direccion=models.CharField(max_length=100,verbose_name='Direccion')
	ciudad=models.CharField(max_length=100,verbose_name='Ciudad')
	def __unicode__(self):
		return '%s'%(self.identificacion)

class Tecnico(models.Model):
	identificacion=models.IntegerField(primary_key=True)
	Nombre=models.CharField(max_length=100,verbose_name='Nombres')	
	Apellido=models.CharField(max_length=100,blank=True,verbose_name='Apellidos')
	tipo_tecnico=models.CharField(max_length=100,verbose_name='Tipo')
	telefono=models.IntegerField(verbose_name='Telefono de contacto')
	direccion=models.CharField(verbose_name='Direccion',max_length=100)
	def __unicode__(self):
		return '%s'%(self.identificacion)


class orden_servicio(models.Model):
	estados=(
		(u'realizado',u'Realizado'),
		(u'pendiente',u'Pendiente'),
		(u'cerrado',u'Cerrado'),
	)
	tipos=(
		(u'instalacion',u'Instalacion'),
		(u'mantenimiento_preventivo',u'Mantenimiento Preventivo'),
		(u'mantenimiento_correctivo',u'Mantenimiento Correctivo'),
		(u'otro',u'Otro'),
	)
	numero_orden=models.IntegerField(verbose_name='Orden de Servicio',primary_key=True)
	id_cliente=models.ForeignKey(Cliente)
	fecha=models.DateField(verbose_name='Fecha')
	tipo=models.CharField(max_length=1000,verbose_name='Tipo de servicio',choices=tipos)
	motivo=models.CharField(max_length=1000,verbose_name='Motivo del servicio')
	problema=models.CharField(max_length=1000,verbose_name='Problema encontrado',blank=True)
	actividad=models.CharField(max_length=1000,verbose_name='Actividad realizada',blank=True)
	estado=models.CharField(max_length=100,verbose_name='Estado del servicio',choices=estados)
	observacion_tecnico=models.CharField(max_length=1000,verbose_name='Observaciones del Tecnico',blank=True)
	observacion_cliente=models.CharField(max_length=1000,verbose_name='Observaciones del Cliente',blank=True)
	hora_entrada=models.TimeField(blank=True)
	hora_salida=models.TimeField(blank=True)
	responsable=models.CharField(max_length=100,verbose_name='Responsable',blank=True)
	pendiente=models.CharField(max_length=10,verbose_name='Pendiente',blank=True)
	facturable=models.CharField(max_length=10,verbose_name='Facturable',blank=True)
	garantia=models.CharField(max_length=10,verbose_name='Garantia',blank=True)
	def __unicode__(self):
		return '%s'%(self.numero_orden)