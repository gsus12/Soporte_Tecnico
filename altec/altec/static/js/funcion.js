$(function () 
{
	var state;
	$(document).ready(function () 
	{
		switch (sessionStorage.state){
			case 'ventana_inicio':
				ventana_inicio();
				break;
			;
			case 'ventana_cliente':
				ventana_cliente();
				break;
			;
			case 'ventana_empleado':
				ventana_empleado();
				break;
			;
			case 'ventana_os':
				ventana_os();
				break;
			;
			case 'formulario_os':
				formulario_os();
				break;
			;
			case 'formulario_empleado':
				formulario_empleado();
				break;
			;
			case 'formulario_cliente':
				formulario_cliente();
				break;
			;
		}
		$('#nombre_cliente').autocomplete({
			minLength:1,
			source: function(req, add) {
				$.ajax({
					url:'/autocom/',
					type:'POST',
					data:{
						start: function () { return $('#nombre_cliente').val(); },
					},
					success: function(data) {
						var suggestions= [];
						for(var i in data){
							contener=data[i];
							suggestions.push(contener.Nombre);
						}
						add(suggestions);
					}
				});
			}
		});
		$('#buscar_os').autocomplete({
			minLength:1,
			source: function (req, add) {
				$.ajax({
					url:'/autobusqueda/',
					type:'POST',
					data:{
						start: function () { return $('#buscar_os').val(); },
					},
					success: function(data) {
						var suggestions=[];
						for(var i in data){
							contener=data[i];
							suggestions.push(''+contener.numero_orden+'');
							//contener.numero_orden
						}
						add(suggestions);
					}
				});
			}
		});
		$('#buscar_cliente').autocomplete({
			minLength:1,
			source: function (req, add) {
				$.ajax({
					url:'/autobusqueda_c/',
					type:'POST',
					data:{
						start: function () { return $('#buscar_cliente').val(); },
					},
					success: function(data) {
						var suggestions=[];
						for(var i in data){
							contener=data[i];
							suggestions.push(''+contener.identificacion+'');
							//contener.numero_orden
						}
						add(suggestions);
					}
				});
			}
		});
		$('#buscar_empleado').autocomplete({
			minLength:1,
			source: function (req, add) {
				$.ajax({
					url:'/autobusqueda_e/',
					type:'POST',
					data:{
						start: function () { return $('#buscar_empleado').val(); },
					},
					success: function(data) {
						var suggestions=[];
						for(var i in data){
							contener=data[i];
							suggestions.push(''+contener.identificacion+'');
		
						}
						add(suggestions);
					}
				});
			}
		});
		$('#busca_empleado').click(function () {
			var numero_empleado=$('#buscar_empleado').val();
			formulario_empleado();
			$('#guardar_empleado').css('display','none');
			$('#actualizar_empleado').css('display','inline');
			$.ajax({
				url:'/busca_tecnico/',
				type:'POST',
				data:'numero='+numero_empleado,
				success:function  (data) {
				//por aqui quede
				for(var i in data){
					contener=data[i];
					$("#tipo_tecnico option[value="+ contener.tipo_tecnico +"]").attr("selected",true);
					var tipo=$('#tipo_tecnico').val();
					var identificacion=$('#identificacion_e').val(contener.identificacion);
					var nombre=$('#nombre_e').val(contener.Nombre);
					var apellido=$('#apellido_e').val(contener.Apellido);
					var telefono=$('#telefono_e').val(contener.telefono);
					var direccion=$('#direccion_e').val(contener.direccion);
				}
			}

			})
		});
		$('#busca_cliente').click(function () {
			var numero_cliente=$('#buscar_cliente').val();
			formulario_cliente();
			$('#guardar_cliente').css('display','none');
			$('#actualizar_cliente').css('display','inline');
			$.ajax({
				url:'/busca_cliente/',
				type:'POST',
				data:'numero='+numero_cliente,
				success:function (data) {
					for(var i in data){
						contener=data[i];
						$("#tipo_cliente option[value="+ contener.tipo_cliente +"]").attr("selected",true);
						if (contener.tipo_cliente=='empresa') {
							$('#nombre_c').val(contener.Nombre);
							$('#nombre_empresa').css('display','inline-block');
							$('#nombre_c').css('display','inline');
							$('#nombre_persona').css('display','none');
							$('#apellido_persona').css('display','none');
							$('#nombres_c').css('display','none');
							$('#apellidos_c').css('display','none');
							
						}else{
							$('#nombres_c').val(contener.Nombre);
							$('#apellidos_c').val(contener.Apellido);	
							$('#nombre_empresa').css('display','none');
							$('#nombre_c').css('display','none');
							$('#nombre_persona').css('display','inline-block');
							$('#apellido_persona').css('display','inline-block');
							$('#nombres_c').css('display','inline');
							$('#apellidos_c').css('display','inline');

						}
						$('#identificacion_c').val(contener.identificacion);
						$('#telefono_c').val(contener.telefono);
						$('#direccion_c').val(contener.direccion);
						$('#ciudad_c').val(contener.ciudad);
					}
				}
			})
		})
		$('#busca_os').click(function () {
			var numero_os=$('#buscar_os').val();

			formulario_os();
			$('#guardar_os').css('display','none');
			$('#actualizar_os').css('display','inline');
			$.ajax({
				url:'/busca_os/',
				type:'POST',
				data:'numero='+numero_os,
				success:function(data) {
					for(var i in data){
						contener=data[i];
						$('#numero_orden').val(contener.numero_orden);
						$('#numero_orden').attr('readonly','readonly');
						$('#nombre_cliente').val(contener.nombre);
						$('#telefono_cliente').val(contener.telefono);
						$('#direccion_cliente').val(contener.direccion);
						$('#ciudad_cliente').val(contener.ciudad);
						$('#identificacion_cliente').val(contener.id_cliente);
						$('#fecha_os').val(contener.fecha);
						$('#tipo_servicio').val(contener.tipo);
						$('#motivo_servicio').val(contener.motivo);
						$('#problema_encontrado').val(contener.problema);
						$('#actividad_realizada').val(contener.actividad);
						if (contener.pendiente =='si') {
							$('#pendientesi').prop('checked','true');
						}else{
							if (contener.pendiente =='no') {
								$('#pendienteno').prop('checked','true');
							}
							else{
								$('#pendientesi').prop('checked','false');
								$('#pendienteno').prop('checked','false');

							}
						}
						if (contener.facturable =='si') {
							$('#factusi').prop('checked','true');
						}else{
							if (contener.facturable=='no') {
								$('#factuno').prop('checked','true');
							}else{
								$('#factusi').prop('checked','false');
								$('#factuno').prop('checked','false');

							}
						}
						if (contener.garantia =='si') {
							$('#garantiasi').prop('checked','true');
						}else{
							if (contener.garantia =='no') {
								$('#garantiano').prop('checked','true');

							}else{
								$('#garantiasi').prop('checked','false');
								$('#garantiano').prop('checked','false');
							}
						}
						$('#observacion_tecnico').val(contener.observacion_tecnico);
						$('#observacion_cliente').val(contener.observacion_cliente);
						$('#hora_entrada').val(contener.hora_entrada);
						$('#hora_salida').val(contener.hora_salida);
					
					}
				}
			});
		})
	});

	$('.modificar_empleado').live('click',function () {
		var identificacion_empleado=$(this).attr('id');
		formulario_empleado();
		$('#guardar_empleado').css('display','none');
		$('#actualizar_empleado').css('display','inline');
		$.ajax({
			url:'/busca_tecnico/',
			type:'POST',
			data:'numero='+identificacion_empleado,
			success:function  (data) {
				//por aqui quede
				for(var i in data){
					contener=data[i];
					$("#tipo_tecnico option[value="+ contener.tipo_tecnico +"]").attr("selected",true);
					var tipo=$('#tipo_tecnico').val();
					var identificacion=$('#identificacion_e').val(contener.identificacion);
					var nombre=$('#nombre_e').val(contener.Nombre);
					var apellido=$('#apellido_e').val(contener.Apellido);
					var telefono=$('#telefono_e').val(contener.telefono);
					var direccion=$('#direccion_e').val(contener.direccion);
				}
			}

		});
	});
	$('.modificar_cliente').live('click',function() {
		var identificacion_cliente=$(this).attr('id');
		formulario_cliente();
		$('#guardar_cliente').css('display','none');
		$('#actualizar_cliente').css('display','inline');
		$.ajax({
			url:'/busca_cliente/',
			type:'POST',
			data:'numero='+identificacion_cliente,
			success:function(data) {
				for(var i in data){
					contener=data[i];
					$("#tipo_cliente option[value="+ contener.tipo_cliente +"]").attr("selected",true);
					if (contener.tipo_cliente=='empresa') {
						$('#nombre_c').val(contener.Nombre);
						$('#nombre_empresa').css('display','inline-block');
						$('#nombre_c').css('display','inline');
						$('#nombre_persona').css('display','none');
						$('#apellido_persona').css('display','none');
						$('#nombres_c').css('display','none');
						$('#apellidos_c').css('display','none');
						
					}else{
						$('#nombres_c').val(contener.Nombre);
						$('#apellidos_c').val(contener.Apellido);	
						$('#nombre_empresa').css('display','none');
						$('#nombre_c').css('display','none');
						$('#nombre_persona').css('display','inline-block');
						$('#apellido_persona').css('display','inline-block');
						$('#nombres_c').css('display','inline');
						$('#apellidos_c').css('display','inline');

					}
					$('#identificacion_c').val(contener.identificacion);
					$('#telefono_c').val(contener.telefono);
					$('#direccion_c').val(contener.direccion);
					$('#ciudad_c').val(contener.ciudad);
				}
			}
		});

	})
	$('.imprimir_os').live('click',function () {
		var numero_os=$(this).attr('id');

		$.ajax({
			url:'/imprimir_os/',
			type:'POST',
			data:'numero='+numero_os,
			success:function(data) {
				var algo=data.ruta;
				
				var url=data.ruta;
				$(location).attr('href',url);
			}
		});
	});
	$('.modificar_os').live('click',function() {
		var numero_os=$(this).attr('id');
		formulario_os();
		$('#guardar_os').css('display','none');
		$('#actualizar_os').css('display','inline');
		$.ajax({
			url:'/busca_os/',
			type:'POST',
			data:'numero='+numero_os,
			success:function(data) {
				for(var i in data){
					contener=data[i];
					$('#numero_orden').val(contener.numero_orden);
					$('#numero_orden').attr('readonly','readonly');
					$('#nombre_cliente').val(contener.nombre);
					$('#nombre_cliente')
					$('#telefono_cliente').val(contener.telefono);
					$('#telefono_cliente').attr('readonly','readonly');

					$('#direccion_cliente').val(contener.direccion);
					$('#direccion_cliente').attr('readonly','readonly');
					
					$('#ciudad_cliente').val(contener.ciudad);
					$('#ciudad_cliente').attr('readonly','readonly');

					$('#identificacion_cliente').val(contener.id_cliente);
					$('#identificacion_cliente').attr('readonly','readonly');

					$('#fecha_os').val(contener.fecha);
					$('#fecha_os').attr('readonly','readonly');

					$('#tipo_servicio').val(contener.tipo);
					$('#motivo_servicio').val(contener.motivo);
					$('#problema_encontrado').val(contener.problema);
					$('#actividad_realizada').val(contener.actividad);
					alert(contener.pendiente+' - '+contener.facturable+' - '+contener.garantia);
					if (contener.pendiente =='si') {
						$('#pendientesi').prop('checked','true');
					}else{
						if (contener.pendiente =='no') {
							$('#pendienteno').prop('checked','true');
						}
						else{
							$('#pendientesi').prop('checked','false');
							$('#pendienteno').prop('checked','false');

						}
					}
					if (contener.facturable =='si') {
						$('#factusi').prop('checked','true');
					}else{
						if (contener.facturable=='no') {
							$('#factuno').prop('checked','true');
						}else{
							$('#factusi').prop('checked','false');
							$('#factuno').prop('checked','false');

						}
					}
					if (contener.garantia =='si') {
						$('#garantiasi').prop('checked','true');
					}else{
						if (contener.garantia =='no') {
							$('#garantiano').prop('checked','true');

						}else{
							$('#garantiasi').prop('checked','false');
							$('#garantiano').prop('checked','false');
						}
					}
					$('#observacion_tecnico').val(contener.observacion_tecnico);
					$('#observacion_cliente').val(contener.observacion_cliente);
					$('#hora_entrada').val(contener.hora_entrada);
					$('#hora_salida').val(contener.hora_salida);
				
				}
			}
		});
	});
	$('#nombre_cliente').focusout(function () {
		rellenar_campos();
	})
	function rellenar_campos () {
		var nombre=$('#nombre_cliente').val();
		$('#nombre_cliente').val('');
		$('#telefono_cliente').val('');
		$('#identificacion_cliente').val('');
		$('#ciudad_cliente').val('');
		$('#direccion_cliente').val('');
		
		$.ajax({
			url:'/rellena_campo/',
			type:'POST',
			data:'nombre='+nombre,
			success:function(data) {
				for(var i in data){
					contener=data[i];
					
					$('#nombre_cliente').val(contener.nombre);
					$('#telefono_cliente').val(contener.telefono);
					$('#identificacion_cliente').val(contener.identificacion);
					$('#direccion_cliente').val(contener.direccion);
					$('#ciudad_cliente').val(contener.ciudad);
				}
				
				
			}
		});

	}
	function ventana_inicio () {
		$('#ventana_cliente').css('display','none');
		$('#ventana_inicio').css('display','block');
		$('#ventana_empleado').css('display','none');
		$('#ventana_os').css('display','none');
		$('#formulario_os').css('display','none');
		$('#formulario_empleado').css('display','none');
		$('#formulario_cliente').css('display','none');
		sessionStorage.state='ventana_inicio';
	}
	function ventana_cliente () {
		$('#ventana_cliente').css('display','block');
		$('#ventana_inicio').css('display','none');
		$('#ventana_empleado').css('display','none');
		$('#ventana_os').css('display','none');	
		$('#formulario_os').css('display','none');
		$('#formulario_empleado').css('display','none');
		$('#formulario_cliente').css('display','none');
		sessionStorage.state='ventana_cliente';
		$.ajax({
			url:'/listar_cliente/',
			type:'POST',
			success:function (data) {
				$('#lista_cliente label').remove();
				$('#lista_cliente br').remove();
				$('#lista_cliente a').remove();
				
				for(var i in data){
					contener=data[i];
					$('#lista_cliente').append('<label>'+contener.nombre+' '+contener.apellido+'</label><a class="ver_cliente" id="'+contener.identificacion+'">Ver</a><a class="modificar_cliente" id="'+contener.identificacion+'">Modificar</a><br><br>');
					$('#lista_cliente label').css('color','white');

				}
			},
		});
	}
	function ventana_empleado () {
		$('#ventana_cliente').css('display','none');
		$('#ventana_inicio').css('display','none');
		$('#ventana_empleado').css('display','block');
		$('#ventana_os').css('display','none');
		$('#formulario_os').css('display','none');
		$('#formulario_empleado').css('display','none');
		$('#formulario_cliente').css('display','none');
		sessionStorage.state='ventana_empleado';
		$.ajax({
			url:'/listar_empleado/',
			type:'POST',
			success:function (data) {
				$('#lista_empleado label').remove();
				$('#lista_empleado br').remove();
				$('#lista_empleado a').remove();

				//alert('---');
				for(var i in data){
					contener=data[i];
					$('#lista_empleado').append('<label>'+contener.nombre+' '+contener.apellido+' '+contener.tipo+'</label><a class="ver_empleado" id="'+contener.identificacion+'">Ver</a><a class="modificar_empleado" id="'+contener.identificacion+'">Modificar</a><br><br>');
					$('#lista_empleado label').css('color','white');
				}
			},
		});
	}
	function ventana_os () {
		$('#ventana_cliente').css('display','none');
		$('#ventana_inicio').css('display','none');
		$('#ventana_empleado').css('display','none');
		$('#ventana_os').css('display','block');
		$('#formulario_os').css('display','none');
		$('#formulario_empleado').css('display','none');
		$('#formulario_cliente').css('display','none');
		sessionStorage.state='ventana_os';
		$.ajax({
			url:'/listar_os/',
			type:'POST',
			success:function (data) {
				$('#lista_os label').remove();
				$('#lista_os br').remove();
				$('#lista_os a').remove();

				for(var i in data){
					contener=data[i];
					$('#lista_os').append('<label>'+contener.numero_orden+' - '+contener.cliente+'</label><a class="ver_os" id="'+contener.numero_orden+'">Ver</a><a class="modificar_os" id="'+contener.numero_orden+'">Modificar</a><a class="imprimir_os" id="'+contener.numero_orden+'">Imprimir</a><br><br>');
					$('#lista_os label').css('color','white');
				}
			}
		});
	}
	function formulario_os(){
		$('#ventana_cliente').css('display','none');
		$('#ventana_inicio').css('display','none');
		$('#ventana_empleado').css('display','none');
		$('#ventana_os').css('display','none');
		$('#formulario_os').css('display','block');
		$('#formulario_empleado').css('display','none');
		$('#formulario_cliente').css('display','none');
		sessionStorage.state='formulario_os';
		limpiar_os();
	}
	function formulario_cliente () {
		$('#ventana_cliente').css('display','none');
		$('#ventana_inicio').css('display','none');
		$('#ventana_empleado').css('display','none');
		$('#ventana_os').css('display','none');
		$('#formulario_os').css('display','none');
		$('#formulario_empleado').css('display','none');
		$('#formulario_cliente').css('display','block');
		sessionStorage.state='formulario_cliente';
		limpiar_cliente();
	}
	function formulario_empleado () {
		$('#ventana_cliente').css('display','none');
		$('#ventana_inicio').css('display','none');
		$('#ventana_empleado').css('display','none');
		$('#ventana_os').css('display','none');
		$('#formulario_os').css('display','none');
		$('#formulario_empleado').css('display','block');
		$('#formulario_cliente').css('display','none');
		sessionStorage.state='formulario_empleado';
		limpiar_tecnico();
	}
	function guarda_empresa (id,tel,dir,nom,ciu) {
		var datos='id='+id+'&&tel='+tel+'&&dir='+dir+'&&nom='+nom+'&&tipo=empresa&&ciu='+ciu;
		$.ajax({
			url:'/guardar_cliente/',
			data:datos,
			type:'POST',
			success:function(data) {
				ventana_cliente();
			}
		});
	}

	function guarda_persona (id,tel,dir,nom,ape,ciu) {
		
		var datos='id='+id+'&&tel='+tel+'&&dir='+dir+'&&nom='+nom+'&&tipo=persona&&ape='+ape+'&&ciu='+ciu;
		$.ajax({
			url:'/guardar_cliente/',
			data:datos,
			type:'POST',
			success:function(data) {
				ventana_cliente();
			}
		});
	}
	function guarda_tecnico (id,tel,dir,nom,ape,tipo) {
								
		
		var datos='id='+id+'&&tel='+tel+'&&dir='+dir+'&&nom='+nom+'&&ape='+ape+'&&tipo='+tipo;
		$.ajax({
			url:'/guardar_tecnico/',
			data:datos,
			type:'POST',
			success:function(data) {
				ventana_empleado();
			}
		});
	}
	function guarda_os (orden,nombre,telefono,direccion,ciudad,cc,fecha,tipo,motivo,problema,actividad,garantiasi,garantiano,pendientesi,pendienteno,factusi,factuno,observaciones_c,observaciones_t,hora_s,hora_e) {
		var datos='orden='+orden+'&&nombre='+nombre+'&&telefono='+telefono+'&&direccion='+direccion+'&&ciudad='+ciudad+'&&cc='+cc+'&&fecha='+fecha+'&&tipo='+tipo+'&&motivo='+motivo+'&&problema='+problema+'&&actividad='+actividad+'&&garantiasi='+garantiasi+'&&garantiano='+garantiano+'&&pendientesi='+pendientesi+'&&pendienteno='+pendienteno+'&&factusi='+factusi+'&&factuno='+factuno+'&&observaciones_c='+observaciones_c+'&&observaciones_t='+observaciones_t+'&&hora_s='+hora_s+'&&hora_e='+hora_e;
		$.ajax({
			url:'/guardar_os/',
			data:datos,
			type:'POST',
			success:function(data) {
				ventana_os();
				limpiar_os();
			}
		});
	}
	function limpiar_os () {
		$('#numero_orden').val('');
		$('#nombre_cliente').val('');
		$('#telefono_cliente').val('');
		$('#direccion_cliente').val('');
		$('#ciudad_cliente').val('');
		$('#identificacion_cliente').val('');
		$('#fecha_os').val('');
		$('#tipo_servicio').val('');
		$('#motivo_servicio').val('');
		$('#problema_encontrado').val('');
		$('#actividad_realizada').val('');
		$('#garantiasi').prop('checked',false);
		$('#garantiano').prop('checked',false);
		$('#factusi').prop('checked',false);
		$('#factuno').prop('checked',false);
		$('#pendientesi').prop('checked',false);
		$('#pendienteno').prop('checked',false);
		$('#observacion_tecnico').val('');
		$('#observacion_cliente').val('');
		$('#hora_entrada').val('');
		$('#hora_salida').val('');
	}
	function limpiar_cliente () {
		
		$('#identificacion_c').val('');
		$('#nombre_c').val('');
		$('#nombres_c').val('');
		$('#apellidos_c').val('');
		$('#telefono_c').val('');
		$('#direccion_c').val('');
		$('#ciudad_c').val('');
	}
	function limpiar_tecnico () {
		$('#tipo_tecnico').val('');
		$('#identificacion_e').val('');
		$('#nombre_e').val('');
		$('#apellido_e').val('');
		$('#telefono_e').val('');
		$('#direccion_e').val('');
		
	}
	function actualizar_os (orden,nombre,telefono,direccion,ciudad,cc,fecha,tipo,motivo,problema,actividad,garantiasi,garantiano,pendientesi,pendienteno,factusi,factuno,observaciones_c,observaciones_t,hora_s,hora_e) {
		var datos='orden='+orden+'&&nombre='+nombre+'&&telefono='+telefono+'&&direccion='+direccion+'&&ciudad='+ciudad+'&&cc='+cc+'&&fecha='+fecha+'&&tipo='+tipo+'&&motivo='+motivo+'&&problema='+problema+'&&actividad='+actividad+'&&garantiasi='+garantiasi+'&&garantiano='+garantiano+'&&pendientesi='+pendientesi+'&&pendienteno='+pendienteno+'&&factusi='+factusi+'&&factuno='+factuno+'&&observaciones_c='+observaciones_c+'&&observaciones_t='+observaciones_t+'&&hora_s='+hora_s+'&&hora_e='+hora_e;
		$.ajax({
			url:'/actualizar_os/',
			data:datos,
			type:'POST',
			success:function(data) {
				ventana_os();
				limpiar_os();
			}
		});
	}
	function actualizar_tecnico (id,tel,dir,nom,ape,tipo) {
								
		
		var datos='id='+id+'&&tel='+tel+'&&dir='+dir+'&&nom='+nom+'&&ape='+ape+'&&tipo='+tipo;
		$.ajax({
			url:'/actualizar_tecnico/',
			data:datos,
			type:'POST',
			success:function(data) {
				ventana_empleado();
			}
		});
	}
	
	function actualizar_empresa (id,tel,dir,nom,ciu) {	
		var datos='id='+id+'&&tel='+tel+'&&dir='+dir+'&&nom='+nom+'&&tipo=empresa&&ciu='+ciu;
		$.ajax({
			url:'/actualizar_cliente/',
			data:datos,
			type:'POST',
			success:function  (data) {
				ventana_cliente();
				limpiar_cliente();
			}
		});

	}

	
	function actualizar_persona (id,tel,dir,nom,ape,ciu) {
	
		var datos='id='+id+'&&tel='+tel+'&&dir='+dir+'&&nom='+nom+'&&tipo=persona&&ape='+ape+'&&ciu='+ciu;
		$.ajax({
			url:'/actualizar_cliente/',
			data:datos,
			type:'POST',
			success:function  (data) {
				ventana_cliente();
				limpiar_cliente();
			}
		});
	}

	$('#inicio').click(function () {
		ventana_inicio();
	})
	$('#cliente').click(function () {
		ventana_cliente();
	})
	$('#empleado').click(function () {
		ventana_empleado();
	})
	$('#os').click(function () {
		ventana_os();
	})
	$('#agrega_os').click(function () {
		formulario_os();
	})
	$('#agrega_empleado').click(function () {
		formulario_empleado();
	})
	$('#agrega_cliente').click(function () {
		formulario_cliente();
	})
	$('#cancelar_cliente').click(function () {
		ventana_cliente();
	})
	$('#cancelar_empleado').click(function () {
		ventana_empleado();
	})
	$('#cancelar_os').click(function () {
		ventana_os();
	})
	$('#guardar_os').click(function () {
		var orden=$('#numero_orden').val();
		var nombre=$('#nombre_cliente').val();
		var telefono=$('#telefono_cliente').val();
		var direccion=$('#direccion_cliente').val();
		var ciudad=$('#ciudad_cliente').val();
		var cc=$('#identificacion_cliente').val();
		var fecha=$('#fecha_os').val();
		var tipo=$('#tipo_servicio').val();
		var motivo=$('#motivo_servicio').val();
		var problema=$('#problema_encontrado').val();
		var actividad=$('#actividad_realizada').val();
		var garantiasi=$('#garantiasi').prop('checked');
		var garantiano=$('#garantiano').prop('checked');
		var factusi=$('#factusi').prop('checked');
		var factuno=$('#factuno').prop('checked');
		var pendientesi=$('#pendientesi').prop('checked');
		var pendienteno=$('#pendienteno').prop('checked');
		alert(pendientesi+''+pendienteno+''+garantiasi+''+garantiano+''+factusi+''+factuno);
		var observaciones_t=$('#observacion_tecnico').val();
		var observaciones_c=$('#observacion_cliente').val();
		var hora_e=$('#hora_entrada').val();
		var hora_s=$('#hora_salida').val();
		if(orden==''){
			$('#mensajes_os').html('El campo Numero de orden no debe ir vacio');
			$('#numero_orden').focus();
		}else{
			if(nombre==''){
				$('#mensajes_os').html('El campo Cliente no debe ir vacio');
				$('#nombre_cliente').focus();
			}
			else{
				if (telefono=='') {
					$('#mensajes_os').html('El campo Telefono no debe ir vacio');
					$('#telefono_cliente').focus();
				}
				else{
					if(direccion==''){
						$('#mensajes_os').html('El campo Direccion no debe ir vacio');
						$('direccion_cliente').focus();
					}else{
						if(ciudad==''){
							$('#mensajes_os').html('El campo Ciudad no debe ir vacio');
							$('#ciudad_cliente').focus();
						}else{
							if(cc==''){
								$('#mensajes_os').html('El campo Nit/CC no debe ir vacio');
								$('#identificacion_cliente').focus();
							}else{
								if(fecha==''){
									$('#mensajes_os').html('El campo Fecha no debe ir vacio');
									$('#fecha_os').focus();
								}
								else{
									guarda_os(orden,nombre,telefono,direccion,ciudad,cc,fecha,tipo,motivo,problema,actividad,garantiasi,garantiano,pendientesi,pendienteno,factusi,factuno,observaciones_c,observaciones_t,hora_s,hora_e);
								}
							}
						}
					}
				}
			}
		}

	})
	$('#actualizar_os').click(function () {
		var orden=$('#numero_orden').val();
		var nombre=$('#nombre_cliente').val();
		var telefono=$('#telefono_cliente').val();
		var direccion=$('#direccion_cliente').val();
		var ciudad=$('#ciudad_cliente').val();
		var cc=$('#identificacion_cliente').val();
		var fecha=$('#fecha_os').val();
		var tipo=$('#tipo_servicio').val();
		var motivo=$('#motivo_servicio').val();
		var problema=$('#problema_encontrado').val();
		var actividad=$('#actividad_realizada').val();
		var garantiasi=$('#garantiasi').prop('checked');
		var garantiano=$('#garantiano').prop('checked');
		var factusi=$('#factusi').prop('checked');
		var factuno=$('#factuno').prop('checked');
		var pendientesi=$('#pendientesi').prop('checked');
		var pendienteno=$('#pendienteno').prop('checked');
		alert(pendientesi+''+pendienteno+''+garantiasi+''+garantiano+''+factusi+''+factuno);
		var observaciones_t=$('#observacion_tecnico').val();
		var observaciones_c=$('#observacion_cliente').val();
		var hora_e=$('#hora_entrada').val();
		var hora_s=$('#hora_salida').val();
		if(orden==''){
			$('#mensajes_os').html('El campo Numero de orden no debe ir vacio');
			$('#numero_orden').focus();
		}else{
			if(nombre==''){
				$('#mensajes_os').html('El campo Cliente no debe ir vacio');
				$('#nombre_cliente').focus();
			}
			else{
				if (telefono=='') {
					$('#mensajes_os').html('El campo Telefono no debe ir vacio');
					$('#telefono_cliente').focus();
				}
				else{
					if(direccion==''){
						$('#mensajes_os').html('El campo Direccion no debe ir vacio');
						$('direccion_cliente').focus();
					}else{
						if(ciudad==''){
							$('#mensajes_os').html('El campo Ciudad no debe ir vacio');
							$('#ciudad_cliente').focus();
						}else{
							if(cc==''){
								$('#mensajes_os').html('El campo Nit/CC no debe ir vacio');
								$('#identificacion_cliente').focus();
							}else{
								if(fecha==''){
									$('#mensajes_os').html('El campo Fecha no debe ir vacio');
									$('#fecha_os').focus();
								}
								else{
									actualizar_os(orden,nombre,telefono,direccion,ciudad,cc,fecha,tipo,motivo,problema,actividad,garantiasi,garantiano,pendientesi,pendienteno,factusi,factuno,observaciones_c,observaciones_t,hora_s,hora_e);
								}
							}
						}
					}
				}
			}
		}

	})
	$('#actualizar_empleado').click(function  () {
		var tipo=$('#tipo_tecnico').val();
		var identificacion=$('#identificacion_e').val();
		var nombre=$('#nombre_e').val();
		var apellido=$('#apellido_e').val();
		var telefono=$('#telefono_e').val();
		var direccion=$('#direccion_e').val();
		
		if (nombre=='') {
			$('#nombre_e').focus();
			$('#mensajes_empleado').html('El campo Nombre no debe ir vacio');					
		}else
		{
			if (apellido=='') {
				$('#apellido_e').focus();
				$('#mensajes_empleado').html('El campo Apellido no debe ir vacio');			
			}
			else{
				if(telefono==''){
					$('#telefono_e').focus();
					$('#mensajes_empleado').html('El campo Telefono no debe ir vacio');

				}
				else{
					if(direccion==''){
						$('#direccion_e').focus();
						$('#mensajes_empleado').html('El campo Direccion no debe ir vacio');
					}
					else{
						if(tipo==''){
							$('#tipo_tecnico').focus();
							$('#mensajes_empleado').html('Debe escoger un tipo de tecnico');
						}
						else{
							actualizar_tecnico(identificacion,telefono,direccion,nombre,apellido,tipo);
						}
					}
				}
			}

		}
		
	});
	$('#actualizar_cliente').click(function () {
		var tipo=$('#tipo_cliente').val();
		var identificacion=$('#identificacion_c').val();
		var nombree=$('#nombre_c').val();
		var nombre=$('#nombres_c').val();
		var apellido=$('#apellidos_c').val();
		var telefono=$('#telefono_c').val();
		var direccion=$('#direccion_c').val();
		var ciudad=$('#ciudad_c').val();
		if (tipo=='empresa') {
			if (nombree=='') {
				$('#mensajes_cliente').html('El campo Nombre no debe ir vacio');
				$('#nombre_c').focus();
			}
			else{
				if (telefono=='') {

					$('#mensajes_cliente').html('El campo Telefono no debe ir vacio');
					$('#telefono_c').focus();
				}
				else{
					if (direccion=='') {
						$('#mensajes_cliente').html('El campo Direccion no debe ir vacio');
						$('#direccion_c').focus();
					}
					else{
						if (ciudad=='') {
							$('#mensajes_cliente').html('El campo ciudad no debe ir vacio');
							$('#ciudad_c').focus();
						}
						else{
							actualizar_empresa(identificacion,telefono,direccion,nombree,ciudad);

						}
					}
				}
			}
		}	
		else{
			if (tipo=='persona') {
				if (nombre=='') {
					$('#mensajes_cliente').html('El campo Nombre no debe ir vacio');
					$('#nombres_c').focus();
				}
			
				else{
					if (apellido=='') {
						$('#mensajes_cliente').html('El campo Apellido no debe ir vacio');
						$('#apellidos_c').focus();
					}
					else{
						if (telefono=='') {
							$('#mensajes_cliente').html('El campo Telefono no debe ir vacio');
							$('#telefono_c').focus();
						}
						else{
							if (direccion=='') {
								$('#mensajes_cliente').html('El campo Direccion no debe ir vacio');
								$('#direccion_c').focus();

							}
							else{
								if (ciudad=='') {
									$('#mensajes_cliente').html('El campo ciudad no debe ir vacio');
									$('#ciudad_c').focus();
								}else{
									actualizar_persona(identificacion,telefono,direccion,nombre,apellido,ciudad);
								}
							}
						}
					}
				}
			}
		}


	});
	$('#guardar_cliente').click(function () {
		var tipo=$('#tipo_cliente').val();
		var identificacion=$('#identificacion_c').val();
		var nombree=$('#nombre_c').val();
		var nombre=$('#nombres_c').val();
		var apellido=$('#apellidos_c').val();
		var telefono=$('#telefono_c').val();
		var direccion=$('#direccion_c').val();
		var ciudad=$('#ciudad_c').val();

		
		if (identificacion=='') {
			$('#identificacion_c').focus();
			$('#mensajes_cliente').html('El campo CC/NIT no debe ir vacio');
		}else{
			if (tipo=='empresa') {
				if (nombree=='') {
					$('#mensajes_cliente').html('El campo Nombre no debe ir vacio');
					$('#nombre_c').focus();
				}
				else{
					if (telefono=='') {

						$('#mensajes_cliente').html('El campo Telefono no debe ir vacio');
						$('#telefono_c').focus();
					}
					else{
						if (direccion=='') {
							$('#mensajes_cliente').html('El campo Direccion no debe ir vacio');
							$('#direccion_c').focus();
						}
						else{
							if (ciudad=='') {
								$('#mensajes_cliente').html('El campo ciudad no debe ir vacio');
								$('#ciudad_c').focus();
							}
							else{
								guarda_empresa(identificacion,telefono,direccion,nombree,ciudad);

							}
						}
					}
				}
			}	
			else{
				if (tipo=='persona') {
					if (nombre=='') {
						$('#mensajes_cliente').html('El campo Nombre no debe ir vacio');
						$('#nombres_c').focus();
					}
				
					else{
						if (apellido=='') {
							$('#mensajes_cliente').html('El campo Apellido no debe ir vacio');
							$('#apellidos_c').focus();
						}
						else{
							if (telefono=='') {
								$('#mensajes_cliente').html('El campo Telefono no debe ir vacio');
								$('#telefono_c').focus();
							}
							else{
								if (direccion=='') {
									$('#mensajes_cliente').html('El campo Direccion no debe ir vacio');
									$('#direccion_c').focus();

								}
								else{
									if (ciudad=='') {
										$('#mensajes_cliente').html('El campo ciudad no debe ir vacio');
										$('#ciudad_c').focus();
									}else{
										guarda_persona(identificacion,telefono,direccion,nombre,apellido,ciudad);
									}
								}
							}
						}
					}
				}
			}
		}

		
		
		
	})
	$('#guardar_empleado').click(function () {
		var tipo=$('#tipo_tecnico').val();
		var identificacion=$('#identificacion_e').val();
		var nombre=$('#nombre_e').val();
		var apellido=$('#apellido_e').val();
		var telefono=$('#telefono_e').val();
		var direccion=$('#direccion_e').val();
		
		if (identificacion=='') {
			$('#identificacion_e').focus();
			$('#mensajes_empleado').html('El campo C.C. no debe ir vacio');			
		}else{
			if (nombre=='') {
				$('#nombre_e').focus();
				$('#mensajes_empleado').html('El campo Nombre no debe ir vacio');					
			}else
			{
				if (apellido=='') {
					$('#apellido_e').focus();
					$('#mensajes_empleado').html('El campo Apellido no debe ir vacio');			
				}
				else{
					if(telefono==''){
						$('#telefono_e').focus();
						$('#mensajes_empleado').html('El campo Telefono no debe ir vacio');

					}
					else{
						if(direccion==''){
							$('#direccion_e').focus();
							$('#mensajes_empleado').html('El campo Direccion no debe ir vacio');
						}
						else{
							if(tipo==''){
								$('#tipo_tecnico').focus();
								$('#mensajes_empleado').html('Debe escoger un tipo de tecnico');
							}
							else{
								guarda_tecnico(identificacion,telefono,direccion,nombre,apellido,tipo);
							}
						}
					}
				}

			}
		}
	})
	$('#tipo_cliente').change(function () {
		var tipo_c=$(this).val();
		if (tipo_c=='empresa') {
			$('#nombre_empresa').css('display','inline-block');
			$('#nombre_c').css('display','inline');
			$('#nombre_persona').css('display','none');
			$('#apellido_persona').css('display','none');
			$('#nombres_c').css('display','none');
			$('#apellidos_c').css('display','none');
		}
		if (tipo_c=='persona') {
			$('#nombre_empresa').css('display','none');
			$('#nombre_c').css('display','none');
			$('#nombre_persona').css('display','inline-block');
			$('#apellido_persona').css('display','inline-block');
			$('#nombres_c').css('display','inline');
			$('#apellidos_c').css('display','inline');
		}
	})
	
})