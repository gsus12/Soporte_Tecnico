from Principal.models import Persona,Cliente,Tecnico,orden_servicio
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django  import http
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
import json
from django.utils import simplejson
from django.core import serializers
from datetime import datetime,date,time
import reportlab
import getpass
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm,mm,inch

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4

def inicio(request):
	return render_to_response('inicio.html',context_instance=RequestContext(request))
def listar_cliente(request):
	clientes=Cliente.objects.all().order_by()[:10]
	armario=[]
	for x in clientes:
		cajon={}
		cajon['identificacion']=x.identificacion
		cajon['nombre']=x.Nombre
		cajon['apellido']=x.Apellido
		armario.append(cajon)

	data=json.dumps(armario)
	return HttpResponse(data,mimetype='application/json')

def listar_empleado(request):
	tecnico=Tecnico.objects.all().order_by()[:10]
	armario=[]
	for x in tecnico:
		cajon={}
		cajon['identificacion']=x.identificacion
		cajon['nombre']=x.Nombre
		cajon['apellido']=x.Apellido
		cajon['tipo']=x.tipo_tecnico
		armario.append(cajon)

	data=json.dumps(armario)
	return HttpResponse(data,mimetype='application/json')

def listar_os(request):
	os=orden_servicio.objects.all().order_by()[:10]
	armario=[]
	for x in os:
		cajon={}
		cajon['numero_orden']=x.numero_orden
		cajon['cliente']=x.id_cliente.Nombre
		armario.append(cajon)
	data=json.dumps(armario)
	return HttpResponse(data,mimetype='application/json')

def guardar_cliente(request):
	if request.is_ajax and request.method=='POST':
		tipo=request.POST.get('tipo')		
		if tipo=='persona':
			apellido=request.POST.get('ape')
		else:
			apellido=''
		identificacion=request.POST.get('id')
		telefono=request.POST.get('tel')
		direccion=request.POST.get('dir')
		nombre=request.POST.get('nom')
		ciudad=request.POST.get('ciu')

		print '%s -  %s - %s - %s '%(identificacion,telefono,direccion,nombre)
		
		cliente=Cliente(identificacion=identificacion,Nombre=nombre,Apellido=apellido,tipo_cliente=tipo,telefono=telefono,direccion=direccion,ciudad=ciudad)
		cliente.save()
		#id_persona,tipo_cliente,telefono,direccion
	response={'exito':'exito'}

	return HttpResponse(json.dumps(response),mimetype='application/json')
def actualizar_cliente(request):
	print '-_-'
	if request.is_ajax and request.method=='POST':
		tipo=request.POST.get('tipo')		
		if tipo=='persona':
			apellido=request.POST.get('ape')
		else:
			apellido=''
		identificacion=request.POST.get('id')
		telefono=request.POST.get('tel')
		direccion=request.POST.get('dir')
		nombre=request.POST.get('nom')
		ciudad=request.POST.get('ciu')

		print '%s'%(identificacion)
		cliente=get_object_or_404(Cliente,pk=identificacion)
		cliente.Nombre=nombre
		cliente.Apellido=apellido
		cliente.tipo_cliente=tipo
		cliente.telefono=telefono
		cliente.direccion=direccion
		cliente.ciudad=ciudad
		cliente.save()
		#id_persona,tipo_cliente,telefono,direccion
	response={'exito':'exito'}

	return HttpResponse(json.dumps(response),mimetype='application/json')

def actualizar_tecnico(request):
	if request.is_ajax and request.method=='POST':
		tipo=request.POST.get('tipo')		
		apellido=request.POST.get('ape')
		identificacion=request.POST.get('id')
		telefono=request.POST.get('tel')
		direccion=request.POST.get('dir')
		nombre=request.POST.get('nom')
		
		tecnico=get_object_or_404(Tecnico,pk=identificacion)
		tecnico.Nombre=nombre
		tecnico.Apellido=apellido
		tecnico.tipo_tecnico=tipo
		tecnico.telefono=telefono
		tecnico.direccion=direccion
		tecnico.save()
		
	response={'exito':'exito'}
	return HttpResponse(json.dumps(response),mimetype='application/json')

def guardar_tecnico(request):
	if request.is_ajax and request.method=='POST':
		tipo=request.POST.get('tipo')		
		apellido=request.POST.get('ape')
		identificacion=request.POST.get('id')

		telefono=request.POST.get('tel')

		direccion=request.POST.get('dir')
		nombre=request.POST.get('nom')
		print '%s -  %s - %s - %s%s%s '%(identificacion,telefono,direccion,nombre,apellido,tipo)
		tecnico=Tecnico(identificacion=identificacion,Nombre=nombre,Apellido=apellido,tipo_tecnico=tipo,telefono=telefono,direccion=direccion)
		tecnico.save()
		#id_persona,tipo_cliente,telefono,direccion
	response={'exito':'exito'}
	return HttpResponse(json.dumps(response),mimetype='application/json')
def guardar_os(request):
	if request.is_ajax and request.method=='POST':
		orden=request.POST.get('orden')
		nombre=request.POST.get('nombre')
		telefono=request.POST.get('telefono')
		direccion=request.POST.get('direccion')
		ciudad=request.POST.get('ciudad')
		cc=request.POST.get('cc')
		fecha=request.POST.get('fecha')
		tipo=request.POST.get('tipo')
		motivo=request.POST.get('motivo')
		problema=request.POST.get('problema')
		actividad=request.POST.get('actividad')
		garantiasi=request.POST.get('garantiasi')
		garantiano=request.POST.get('garantiano')
		factusi=request.POST.get('factusi')
		factuno=request.POST.get('factuno')
		pendientesi=request.POST.get('pendientesi')
		pendienteno=request.POST.get('pendienteno')
		observaciones_t=request.POST.get('observaciones_t')
		observaciones_c=request.POST.get('observaciones_c')
		hora_e=request.POST.get('hora_e')
		hora_s=request.POST.get('hora_s')
		garantia=''
		pendiente=''
		facturado=''
		
		if garantiasi=='false' and garantiano=='false':
			garantia=''
		elif garantiasi=='true' and garantiano=='false':
			garantia='si'
		elif garantiasi=='false' and garantiano=='true':
			garantia='no'

		if pendientesi=='false' and pendienteno=='false':
			pendiente=''
		elif pendientesi=='true' and pendienteno=='false':
			pendiente='si'
		elif pendientesi=='false' and pendienteno=='true':
			pendiente='no'

		if factusi=='false' and factuno=='false':
			facturado=''
		elif factusi=='true' and factuno=='false': 
			facturado='si'
		elif factusi=='false' and factuno=='true':
			facturado='no'
		
		if hora_e=='':
			hora_e='00:00:00'
		if hora_s=='':
			hora_s='00:00:00'
		print '%s,%s,%s'%(facturado,pendiente,garantia)

		print '%s,%s'%(hora_s,hora_e)
		cliente=Cliente.objects.get(identificacion=cc)
		orden=orden_servicio(numero_orden=orden,id_cliente=cliente,fecha=fecha,tipo=tipo,motivo=motivo,problema=problema,actividad=actividad,estado='pendiente',facturable=facturado,pendiente=pendiente,garantia=garantia,observacion_tecnico=observaciones_t,observacion_cliente=observaciones_c,hora_entrada=hora_e,hora_salida=hora_s)
		orden.save()
	response={'exito':'exito'}
	return HttpResponse(json.dumps(response),mimetype='application/json')
def actualizar_os(request):
	if request.is_ajax and request.method=='POST':
		orden=request.POST.get('orden')
		nombre=request.POST.get('nombre')
		telefono=request.POST.get('telefono')
		direccion=request.POST.get('direccion')
		ciudad=request.POST.get('ciudad')
		cc=request.POST.get('cc')
		fecha=request.POST.get('fecha')
		tipo=request.POST.get('tipo')
		motivo=request.POST.get('motivo')
		problema=request.POST.get('problema')
		actividad=request.POST.get('actividad')
		garantiasi=request.POST.get('garantiasi')
		garantiano=request.POST.get('garantiano')
		factusi=request.POST.get('factusi')
		factuno=request.POST.get('factuno')
		pendientesi=request.POST.get('pendientesi')
		pendienteno=request.POST.get('pendienteno')
		observaciones_t=request.POST.get('observaciones_t')
		observaciones_c=request.POST.get('observaciones_c')
		hora_e=request.POST.get('hora_e')
		hora_s=request.POST.get('hora_s')

		garantia=''
		pendiente=''
		facturado=''
		
		if garantiasi=='false' and garantiano=='false':
			garantia=''
		elif garantiasi=='true' and garantiano=='false':
			garantia='si'
		elif garantiasi=='false' and garantiano=='true':
			garantia='no'

		if pendientesi=='false' and pendienteno=='false':
			pendiente=''
		elif pendientesi=='true' and pendienteno=='false':
			pendiente='si'
		elif pendientesi=='false' and pendienteno=='true':
			pendiente='no'

		if factusi=='false' and factuno=='false':
			facturado=''
		elif factusi=='true' and factuno=='false': 
			facturado='si'
		elif factusi=='false' and factuno=='true':
			facturado='no'
		# cliente=Cliente.objects.get(identificacion=cc)
		orden=get_object_or_404(orden_servicio,pk=orden)
		orden.tipo=tipo
		orden.motivo=motivo
		orden.problema=problema
		orden.actividad=actividad
		orden.estado='realizado'
		orden.observacion_cliente=observaciones_c
		orden.observacion_tecnico=observaciones_t
		orden.hora_entrada=hora_e
		orden.hora_salida=hora_s
		orden.facturable=facturado
		orden.pendiente=pendiente
		orden.garantia=garantia
		
		orden.save()
	response={'exito':'exito'}
	return HttpResponse(json.dumps(response),mimetype='application/json')
def autocom(request):
	consulta=Cliente.objects.filter(Nombre__istartswith=request.POST['start']).order_by('Nombre')
	print request.POST['start']
	armario=[]
	for x in consulta:
		cajon={}
		cajon['Nombre']=x.Nombre
		armario.append(cajon)
	data=json.dumps(armario)
	print armario
	return HttpResponse(data,mimetype='application/json')
def autobusqueda(request):
	consulta=orden_servicio.objects.filter(numero_orden__istartswith=request.POST['start']).order_by('numero_orden')
	armario=[]
	for x in consulta:
		cajon={}
		cajon['numero_orden']=x.numero_orden
		cajon['nombre']=x.id_cliente.Nombre
		armario.append(cajon)
	data=json.dumps(armario)
	print armario
	return HttpResponse(data,mimetype='application/json')
def autobusqueda_c(request):
	consulta=Cliente.objects.filter(identificacion__istartswith=request.POST['start']) | Cliente.objects.filter(Nombre__istartswith=request.POST['start']).order_by('identificacion')
	armario=[]
	for x in consulta:
		cajon={}
		cajon['identificacion']=x.identificacion
		cajon['nombre']=x.Nombre
		cajon['apellido']=x.Apellido
		armario.append(cajon)
	data=json.dumps(armario)
	print armario
	return HttpResponse(data,mimetype='application/json')
def autobusqueda_e(request):
	consulta=Tecnico.objects.filter(identificacion__istartswith=request.POST['start']) | Tecnico.objects.filter(Nombre__istartswith=request.POST['start']).order_by('identificacion')
	armario=[]
	for x in consulta:
		cajon={}
		cajon['identificacion']=x.identificacion
		cajon['nombre']=x.Nombre
		cajon['apellido']=x.Apellido
		armario.append(cajon)
	data=json.dumps(armario)
	print armario
	return HttpResponse(data,mimetype='application/json')
def busca_os(request):
	if request.is_ajax and request.method=='POST':
		bos=request.POST.get('numero')
		busca_orden=orden_servicio.objects.all().filter(numero_orden=bos)
		armario=[]
		for x in busca_orden:
			cajon={}
			cajon['numero_orden']=x.numero_orden
			cajon['id_cliente']=x.id_cliente.identificacion
			cajon['nombre']=x.id_cliente.Nombre
			cajon['fecha']=str(x.fecha)
			cajon['direccion']=x.id_cliente.direccion
			cajon['telefono']=x.id_cliente.telefono
			cajon['ciudad']=x.id_cliente.ciudad
			cajon['tipo']=x.tipo
			cajon['motivo']=x.motivo
			cajon['actividad']=x.actividad
			cajon['problema']=x.problema
			cajon['observacion_cliente']=x.observacion_cliente
			cajon['observacion_tecnico']=x.observacion_tecnico
			cajon['pendiente']=x.pendiente
			cajon['garantia']=x.garantia
			cajon['facturable']=x.facturable
			cajon['hora_salida']=str(x.hora_salida)
			cajon['hora_entrada']=str(x.hora_entrada)
			armario.append(cajon)
		data=json.dumps(armario)
	return HttpResponse(data,mimetype='application/json')

def busca_cliente(request):
	if request.is_ajax and request.method=='POST':
		identificacion=request.POST.get('numero')
		buscar_cliente=Cliente.objects.all().filter(identificacion=identificacion)
		armario=[]
		for x in buscar_cliente:
			cajon={}
			cajon['identificacion']=x.identificacion
			cajon['Nombre']=x.Nombre
			cajon['Apellido']=x.Apellido
			cajon['tipo_cliente']=x.tipo_cliente
			cajon['telefono']=x.telefono
			cajon['direccion']=x.direccion
			cajon['ciudad']=x.ciudad

			armario.append(cajon)
		data=json.dumps(armario)
	return HttpResponse(data,mimetype='application/json')
def busca_tecnico(request):
	if request.is_ajax and request.method=='POST':
		identificacion=request.POST.get('numero')
		buscar_tecnico=Tecnico.objects.all().filter(identificacion=identificacion)
		armario=[]
		for x in buscar_tecnico:
			cajon={}
			cajon['identificacion']=x.identificacion
			cajon['Nombre']=x.Nombre
			cajon['Apellido']=x.Apellido
			cajon['tipo_tecnico']=x.tipo_tecnico
			cajon['telefono']=x.telefono
			cajon['direccion']=x.direccion
			armario.append(cajon)
		data=json.dumps(armario)
	return HttpResponse(data,mimetype='application/json')


def rellena_campo(request):
	if request.is_ajax and request.method=='POST':
		nombre=request.POST.get('nombre')
		direccion=request.POST.get('dir')
		print nombre
		print '----'
		cliente=Cliente.objects.all().filter(Nombre=nombre)
		armario=[]
		for x in cliente:
			cajon={}
			cajon['nombre']=x.Nombre
			cajon['apellido']=x.Apellido
			cajon['identificacion']=x.identificacion
			cajon['telefono']=x.telefono
			cajon['ciudad']=x.ciudad
			cajon['direccion']=x.direccion
			print '%s, %s, %s, %s, %s,'%(x.Nombre,x.Apellido,x.identificacion,x.telefono,x.direccion)
			armario.append(cajon)
		data=json.dumps(armario)
		print armario
	#response={'exito':'exito'}	

	return HttpResponse(data,mimetype='application/json')
def imprimir_os(request):
	if request.is_ajax and request.method=='POST':
		numero=request.POST.get('numero')
		os=orden_servicio.objects.all().filter(numero_orden=numero)
		a=[]
		a.append(0)
		a[0]=612
		a.append(0)
		a[1]=792
		fechaactual=datetime.now()
		dia=str(fechaactual).split('-')[2]
		dial=str(dia).split(' ')[0]
		mes=str(fechaactual).split('-')[1]
		ano=str(fechaactual).split('-')[0]
		hora=str(fechaactual).split(' ')[1]
		horal=str(hora).split('.')[0]
		print numero
		print dia
		print dial
		print mes
		print ano
		print hora
		print horal
		print 'Orden%s%s%s%s%s.pdf'%(numero,dial,mes,ano,horal)
		erco = canvas.Canvas('Orden%s%s%s%s.pdf'%(numero,dial,mes,ano), pagesize=a)
		erco.setFont('Helvetica',12)	
		erco.drawString(223.151,742.219,'ALTEC TECHNOLOGY SAS.')
		erco.setFont('Helvetica',9.3)
		erco.drawString(260.835,730.867,'NIT.900.340.064-4')
		erco.setFont('Helvetica',7.5)
		erco.drawString(260.38,715.985,'IVA REGIMEN COMUN')
		erco.drawString(216.566,705.762,'Calle 33 N 65C - 17 Oficina 202  PBX: 444 33 65')
		erco.setFont('Helvetica',8.7)
		erco.setFillColorRGB(1,0.0,0.0)
		erco.drawString(201.25,690.874,'Autorizado por la SUPERINTENDENCIA DE VIGILANCIA')
		erco.drawString(234.125,682.34,'Resolucion 3931 del 23 de Junio 2010')
		erco.setFont('Helvetica',8.3)
		erco.drawString(186.471,674.438,'Registro de MINTIC RTIC96000189 del 26 Noviembre de 2010')
		erco.setFont('Helvetica',12)
		for x in os:
			print x.id_cliente.Nombre
			marcai=''
			marcamp=''
			marcamc=''
			marcao=''
			marcaps=''
			marcapn=''
			marcags=''
			marcagn=''
			marcafs=''
			marcafn=''
			erco.setFillColorRGB(0.0,0.0,0.0)
			erco.drawString(36.045,649.286,'Cliente:')
			erco.drawString(82.755,649.286,'%s %s'%(x.id_cliente.Nombre,x.id_cliente.Apellido))
			erco.drawString(36.045,631.074,'Direccion:')
			erco.drawString(90.572,631.074,'%s'%(x.id_cliente.direccion))
			erco.drawString(36.045,612.862,'Responsable:')
			#erco.drawString(110.755,612.862,'Responsable:'%(x))
			erco.drawString(393.22,649.286,'Tel(s):')
			erco.drawString(428.689,649.286,'%s'%(x.id_cliente.telefono))
			erco.drawString(393.22,631.074,'Ciudad:')
			erco.drawString(437.848,631.074,'%s'%(x.id_cliente.ciudad))
			erco.drawString(270.565,612.862,'Nit /CC:')
			erco.drawString(313.565,612.862,'%s'%(x.id_cliente.identificacion))
			erco.setFillColorRGB(0.8,0.8,0.8)
			erco.drawString(489.595,612.862,'D')
			erco.drawString(521.451,612.862,'M')
			erco.drawString(553.444,612.862,'A')
			erco.setFillColorRGB(0.0,0.0,0.0)
			erco.drawString(434.69,612.862,'Fecha:')
			erco.drawString(489.595,612.862,'%s'%(str(x.fecha).split('-')[2]))
			erco.drawString(521.451,612.862,'%s'%(str(x.fecha).split('-')[1]))
			erco.drawString(553.444,612.862,'%s'%(str(x.fecha).split('-')[0]))			
			erco.setFillColorRGB(1,0.0,0.0)
			erco.setFont('Helvetica',15.3)
			erco.drawString(424.549,732.108,'ORDEN DE SERVICIO:')
			erco.drawString(480.459,688.826,'%s'%(x.numero_orden))
			erco.setFillColorRGB(0.0,0.0,0.0)
			erco.setFont('Helvetica',10)
			erco.drawString(44.319,580,'INSTALACION')
			erco.drawString(149.319,580,'MANTENIMIENTO PREVENTIVO')
			erco.drawString(338.997,580,'MANTENIMIENTO CORRECTIVO')
			erco.drawString(525.878,580,'OTRO')
			erco.drawString(44.319,580,'%s'%(marcai))
			erco.drawString(149.319,580,'%s'%(marcamp))
			erco.drawString(338.997,580,'%s'%(marcamc))
			erco.drawString(525.878,580,'%s'%(marcao))
			erco.setFont('Helvetica',8.5)
			erco.drawString(44.319,556.161,'MOTIVO DEL SERVICIO')
			erco.drawString(44.319,556.161,'%s'%(x.motivo))
			erco.drawString(44.319,511.096,'PROBLEMA ENCONTRADO')
			erco.drawString(44.319,511.096,'%s'%(x.problema))
			erco.drawString(44.319,464.887,'ACTIVIDAD REALIZADA')
			erco.drawString(44.319,464.887,'%s'%(x.actividad))
			erco.drawString(44.319,419.096,'PENDIENTES')
			erco.drawString(103.867,419.096,'SI')
			erco.drawString(103.867,419.096,'%s'%(marcaps))
			erco.drawString(135.155,419.096,'NO')
			erco.drawString(135.155,419.096,'%s'%(marcapn))
			erco.drawString(229.037,419.096,'GARANTIA')
			erco.drawString(288.98,419.096,'SI')
			erco.drawString(288.98,419.096,'%s'%(marcags))
			erco.drawString(319.508,419.096,'NO')
			erco.drawString(319.508,419.096,'%s'%(marcagn))
			erco.drawString(426.176,419.096,'FACTURABLE')
			erco.drawString(496.515,419.096,'SI')
			erco.drawString(496.515,419.096,'%s'%(marcafs))
			erco.drawString(526.938,419.096,'NO')
			erco.drawString(526.938,419.096,'%s'%(marcafn))
			erco.drawString(44.319,397.104,'OBSERVACIONES TECNICO')
			erco.drawString(44.319,397.104,'%s'%(x.observacion_tecnico))
			erco.drawString(44.319,352.068,'OBSERVACIONES CLIENTE')
			erco.drawString(44.319,352.068,'%s'%(x.observacion_cliente))
			erco.setFont('Helvetica',13)
			erco.setFillColorRGB(1,0.0,0.0)
			erco.drawString(184.374,286.871,'MATERIALES Y/O EQUIPOS UTILIADOSS')
			erco.setFont('Helvetica',9)
			erco.setFillColorRGB(0.0,0.0,0.0)
			erco.drawString(41.409,266.799,'ITEM')
			erco.drawString(87.365,266.799,'REFERENCIA')
			erco.drawString(277.34,266.799,'DESCRIPCION')
			erco.drawString(445.535,266.799,'CANTIDAD')
			erco.drawString(517.93,266.799,'SERIALES')
			erco.drawString(97.662,96.007,'HORA DE ENTRADA')
			erco.drawString(97.662,96.007,'%s'%(x.hora_entrada))
			erco.drawString(318.18,96.007,'HORA DE SALIDA')
			erco.drawString(318.18,96.007,'%s'%(x.hora_salida))
			erco.drawString(105.181,25.353,'Firma y Nombre del Cliente')
			erco.drawString(398.784,25.353,'Firma y Nombre del Tecnico')
		erco.line(77.733,646.431,388.689,646.431)
		erco.line(427.886,646.431,583.619,646.431)
		erco.line(91.572,629.213,389.489,629.213)
		erco.line(436.342,629.213,583.619,629.213)
		erco.line(109.755,610.485,266.673,610.485)
		erco.line(312.565,610.485,431.269,610.485)
		erco.line(148.899,555.518,572.093,555.518)
		erco.line(44.319,533.189,572.093,533.189)
		erco.line(163.428,509.417,572.093,509.417)
		erco.line(44.319,487.807,572.093,487.807)
		erco.line(159.588,463.676,572.093,463.676)
		erco.line(44.319,443.507,572.093,443.507)
		erco.line(158.665,395.605,572.093,395.605)
		erco.line(44.319,373.995,572.093,373.995)
		erco.line(158.983,350.224,572.093,350.224)
		erco.line(44.319,327.894,572.093,327.894)
		erco.line(44.091,39.761,276.037,39.761)
		erco.line(338.706,39.761,571.373,39.761)
		erco.roundRect(33.757,306.15,547.462,296.064,10,stroke=1,fill=0)
		erco.roundRect(33.757,112.453,547.462,171.64,10,stroke=1,fill=0)
		erco.line(33.757,259.846,580.581,259.846)
		erco.line(33.757,242.618,580.581,242.618)
		erco.line(33.757,224.715,580.581,224.715)
		erco.line(33.757,207.561,580.581,207.561)
		erco.line(33.757,189.627,580.581,189.627)
		erco.line(33.757,171.693,580.581,171.693)
		erco.line(33.757,154.149,580.581,154.149)
		erco.line(33.757,136.411,580.581,136.411)
		erco.line(69.68,284.093,69.68,112.453)
		erco.line(163.689,284.093,163.689,112.453)
		erco.line(439.686,284.093,439.686,112.453)
		erco.line(496.446,284.093,496.446,112.453)
		erco.setFillColorRGB(0.8,0.8,0.8)
		erco.roundRect(114.379,578.551,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(303.816,578.551,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(495.028,578.551,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(557.819,578.551,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(116.153,416.784,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(151.273,416.784,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(301.333,416.784,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(335.39,416.784,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(509.573,416.784,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(542.919,416.784,13.481,9.933,0,stroke=0,fill=1)
		erco.roundRect(188.266,89.349,119.906,19.157,0,stroke=0,fill=1)
		erco.roundRect(396.407,89.349,119.906,19.157,0,stroke=0,fill=1)
		erco.drawImage('altec.png',38.517,672.3,width=82.952,height=86.867)
		erco.showPage()
		erco.save()
		data={'ruta':'Orden%s%s%s%s.pdf'%(numero,dial,mes,ano)}

	return HttpResponse(json.dumps(data),mimetype='application/json')

def descargarpdf(request,nombre):
	print nombre
	fnombre='%s'%(nombre)
	response=HttpResponse(file(fnombre).read())
	response['Content-Type']='application/pdf'
	response['Content-Disposition']='attachment'
	return response