#!/usr/bin/env python3
"""
Script para reemplazar el método generar_historia_completa con versión mejorada
"""

import re

# Leer el archivo
with open('/Users/wu/radio-terror-ia/radio_terror_potenciado.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Nuevo método completo
new_method = '''    def generar_historia_completa(self):
        """Genera una historia completa de terror - VERSIÓN ULTRA VARIADA - SIEMPRE ÚNICA"""
        
        # Obtener combinación única
        protagonista, ocupacion, lugar_tipo, lugar_especifico, motivo = self._obtener_combinacion_unica()
        
        # Seleccionar variaciones aleatorias para esta historia
        llegada_hora = random.choice(self.variaciones_llegada_hora)
        edificio_desc = random.choice(self.variaciones_edificio)
        olor_desc = random.choice(self.variaciones_olor)
        primera_señal = random.choice(self.variaciones_primera_señal)
        tech_desc = random.choice(self.variaciones_tech)
        entidad_desc = random.choice(self.variaciones_entidad)
        huida_desc = random.choice(self.variaciones_huida)
        despertar_desc = random.choice(self.variaciones_despertar)
        tiempo_desc = random.choice(self.variaciones_tiempo)
        heridas_desc = random.choice(self.variaciones_heridas)
        trauma_desc = random.choice(self.variaciones_trauma)
        
        # Variaciones adicionales de introducción
        intro_tipo = random.choice([
            f"Soy {protagonista}, {ocupacion}. Durante años, consideré que tenía una mente racional, lógica, científica. Nunca creí en lo paranormal.",
            f"Mi nombre es {protagonista}. Trabajo como {ocupacion}. Siempre he sido escéptico respecto a lo sobrenatural.",
            f"Me llamo {protagonista}, soy {ocupacion}. Hasta hace poco, pensaba que el terror real solo existía en las películas.",
            f"Soy {protagonista}. Como {ocupacion}, mi vida siempre ha sido sobre hechos, evidencia, lo tangible.",
        ])
        
        # Variaciones de creencia inicial
        creencia_inicial = random.choice([
            "Los fantasmas, los espíritus, las apariciones... para mí, todo eso era producto de mentes sugestionables.",
            "Las historias de terror eran entretenimiento. Ficción. Nunca realidad.",
            "Siempre tuve explicaciones científicas para todo. El mundo era predecible, comprensible.",
            "Lo paranormal era para personas crédulas. Yo me basaba en hechos, no en supersticiones."
        ])
        
        # Variaciones de advertencias
        advertencias = random.choice([
            '"No vayas ahí", me decían con esa mirada que combina lástima y terror.',
            '"Ese lugar está maldito", susurraban los lugareños. "Todos lo saben".',
            '"Nadie que entra sale igual", me advirtieron una y otra vez.',
            '"Hay algo malo en ese sitio", me dijeron. "Algo antinatural".'
        ])
        
        # Más variaciones para los capítulos
        decision_entrada = random.choice([
            "Di un último vistazo al mundo exterior y crucé el umbral.",
            "Respiré hondo y empujé la puerta. No había vuelta atrás.",
            "Ignoré mi instinto y entré. El mayor error de mi vida.",
            "Con las manos temblando, abrí la entrada principal."
        ])
        
        temperatura = random.choice([
            "La temperatura cayó inmediatamente. Un frío que penetraba hasta los huesos.",
            "El aire se tornó helado al instante. No era frío natural.",
            "Sentí como si hubiera entrado a un congelador. Pero era más que temperatura.",
            "Un escalofrío me recorrió. El lugar irradiaba frialdad antinatural."
        ])
        
        exploracion_inicial = random.choice([
            "El interior era un laberinto de pasillos oscuros que se ramificaban en todas direcciones.",
            "Me encontré en un vestíbulo enorme. Pasillos se extendían como tentáculos hacia la oscuridad.",
            "Adentro, el espacio parecía más grande de lo posible. Geometría imposible.",
            "El interior era cavernoso. Mi linterna apenas penetraba las sombras."
        ])
        
        objetos_abandonados = random.choice([
            "Había muebles abandonados. Sillas volcadas. Mesas con objetos intactos, como si todos hubieran huido súbitamente.",
            "Pertenencias personales yacían esparcidas. Zapatos. Ropa. Fotografías. Vidas interrumpidas abruptamente.",
            "Encontré señales de ocupación reciente. Pero el polvo de décadas lo cubría todo. Paradojas temporales.",
            "Objetos cotidianos estaban dispuestos de forma inquietante. Demasiado ordenados. Demasiado intencionales."
        ])
        
        historia = {
            'titulo': f"La Noche en {lugar_especifico.split(',')[0]}",
            'protagonista': protagonista,
            
            'introduccion': f"""{intro_tipo}

{creencia_inicial} Tenía explicaciones para todo. Hasta aquella noche.

Hace tres semanas decidí ir a {lugar_especifico}. Llevaba {motivo}. Era un proyecto importante para mí, algo que podría cambiar mi carrera. Todos me advirtieron. No solo amigos y conocidos, sino también extraños.

{advertencias} "Nadie que entra sale igual". Algunos incluso me suplicaron que reconsiderara. {random.choice(['Una anciana', 'Un viejo', 'Un extraño'])} en el pueblo me tomó del brazo y me dijo: "Lo que hay allí no es de este mundo. No le gusta ser molestado".

Por supuesto, no les hice caso. ¿Cómo iba a dejar que supersticiones locales arruinaran mi investigación? Ahora, mientras escribo esto con manos que aún tiemblan, desearía haberlos escuchado.""",
            
            'llegada': f"""{llegada_hora} {lugar_especifico.split(',')[0]} se alzaba ante mí como {random.choice(['una cicatriz abierta en el paisaje', 'una herida infectada en la tierra', 'un monumento a la decadencia', 'un testimonio del abandono'])}.

{edificio_desc} {random.choice(['Las plantas trepadoras lo habían reclamado', 'La naturaleza intentaba borrarlo', 'El tiempo lo había marcado cruelmente', 'El abandono era palpable'])}.

{olor_desc} Más tarde entendería que era el olor de algo que había estado atrapado allí por demasiado tiempo.

Mientras estaba frente a la entrada principal, mi instinto me gritaba que huyera. Cada célula de mi cuerpo pedía dar media vuelta. Pero mi {random.choice(['orgullo', 'curiosidad', 'terquedad', 'ambición'])}, mi maldito {random.choice(['orgullo', 'ego', 'obstinación'])}, me empujó hacia adelante.

{decision_entrada} {temperatura}""",
            
            'exploracion': f"""{exploracion_inicial} Mi linterna apenas penetraba la oscuridad, como si las sombras mismas la absorbieran.

Mis pasos resonaban de forma antinatural. Cada sonido se amplificaba, se distorsionaba, creando ecos que no deberían existir. A veces parecía que los ecos venían antes que el sonido original.

Comencé a {random.choice(['fotografiar', 'documentar', 'grabar', 'registrar'])} todo metódicamente. {random.choice(['Cada habitación', 'Cada pasillo', 'Cada detalle', 'Cada anomalía'])}. Las paredes tenían manchas que parecían humedad, pero formaban patrones demasiado regulares, demasiado intencionales.

{objetos_abandonados} En una habitación encontré un calendario de pared. La última fecha marcada era de hace décadas.

{random.choice(['Subí al segundo piso', 'Exploré el nivel superior', 'Ascendí por las escaleras', 'Me aventuré arriba'])}. Las escaleras crujían amenazadoramente bajo mi peso. A mitad de camino, sentí una corriente de aire frío que parecía empujarme hacia atrás, como si el edificio mismo intentara expulsarme.

Entonces encontré la primera señal real de que algo estaba muy, muy mal.""",
            
            'primeras_señales': f"""{primera_señal} {random.choice(['Estaban frescas', 'Eran recientes', 'Acababan de aparecer', 'No estaban ahí antes'])}.

{tech_desc} En una imagen apareció {random.choice(['una silueta', 'una figura', 'una sombra', 'algo'])}. Parada justo detrás de mí. No había nadie cuando tomé esa foto.

Empecé a escuchar sonidos. Primero fueron sutiles. Crujidos que podían atribuirse al {random.choice(['viento', 'edificio viejo', 'estructura', 'tiempo'])}. Pero no había {random.choice(['viento', 'explicación', 'razón', 'lógica'])}. El aire estaba completamente inmóvil, pesado, esperando.

Luego escuché pasos. Definitivamente pasos. Lentos, arrastrados, viniendo del {random.choice(['piso de arriba', 'otro extremo', 'fondo del pasillo', 'más allá'])}. Pero {random.choice(['yo estaba en el piso más alto', 'no había nadie más', 'las puertas estaban cerradas', 'estaba completamente solo'])}.

Intenté mantener la calma. "{random.choice(['Es solo el edificio asentándose', 'Son fenómenos acústicos naturales', 'Tiene que haber una explicación lógica', 'No puede ser real'])}", me dije. Incluso entonces, una parte de mí sabía que me mentía.

No hice caso a mi instinto. No hui cuando debía. Ojalá lo hubiera hecho.""",
            
            'tension_creciente': f"""Los pasos se hicieron más frecuentes. Más cercanos. Ya no venían de {random.choice(['arriba', 'un solo lugar', 'una dirección'])}. Venían de todos lados. Del techo, de las paredes, de debajo del suelo.

Mi {random.choice(['teléfono', 'cámara', 'dispositivo'])} comenzó a mostrar imágenes que no había tomado. Foto tras foto aparecía. Todas del interior del edificio. Todas tomadas desde ángulos imposibles. Y en cada una, había {random.choice(['rostros', 'figuras', 'siluetas', 'formas'])}. {random.choice(['Pálidos', 'Distorsionados', 'Espectrales', 'Horribles'])}, mirando directamente a la cámara.

En una foto estaba yo. {random.choice(['Durmiendo', 'Inmóvil', 'Con los ojos cerrados', 'Inconsciente'])}. ¿Cuándo había pasado eso? No lo recordaba. La foto era de ese momento, de ese día, pero yo estaba {random.choice(['despierto', 'consciente', 'alerta'])}.

El aire se volvió más denso. Cada respiración requería esfuerzo. El olor se intensificó hasta hacerse casi insoportable. Era el olor de la descomposición, pero mezclado con algo {random.choice(['floral', 'dulce', 'químico', 'enfermizo'])}, como {random.choice(['flores en un funeral', 'perfume rancio', 'incienso podrido', 'muerte disfrazada'])}.

Las sombras comenzaron a moverse independientemente de mi linterna. Veía formas deslizándose por el borde de mi visión. Cuando giraba para mirarlas directamente, no había nada. Pero las sentía. Observándome. Evaluándome. {random.choice(['Cazándome', 'Jugando conmigo', 'Esperando el momento', 'Disfrutando mi miedo'])}.

Entonces escuché mi nombre.

Claro. Nítido. Una voz que {random.choice(['no reconocía', 'sonaba familiar', 'parecía conocer', 'me llamaba'])}, pero que sonaba {random.choice(['extraña', 'distorsionada', 'antigua', 'muerta'])}.

"{protagonista}", susurró. No venía de ninguna dirección específica. Venía de todas partes y de ninguna.

En ese momento supe con absoluta certeza: no estaba solo. Algo estaba ahí, en el edificio conmigo. Y me conocía.""",
            
            'encuentro': f"""{entidad_desc}

Me quedé paralizado. Cada instinto gritaba que corriera, pero mis piernas no respondían. Era como si mis pies estuvieran {random.choice(['clavados al suelo', 'fundidos con la piedra', 'atrapados en cemento invisible', 'amarrados por hilos invisibles'])}.

La figura comenzó a {random.choice(['moverse', 'deslizarse', 'avanzar', 'acercarse'])}. Pero no {random.choice(['caminaba', 'se movía normalmente', 'seguía las leyes físicas'])}. {random.choice(['Se deslizaba', 'Flotaba', 'Se teletransportaba', 'Aparecía más cerca'])}. Sus movimientos eran incorrectos, como si estuviera viendo un video con frames faltantes. Estaba lejos. Parpadeé. Estaba más cerca. Parpadeé de nuevo. Estaba a {random.choice(['medio pasillo', 'pocos metros', 'un paso', 'mi alcance'])}.

Intenté gritar. No salió ningún sonido. Mi voz había desaparecido. El aire estaba demasiado denso para {random.choice(['gritar', 'hablar', 'respirar', 'existir'])}.

Cuando la figura estuvo cerca, pude ver donde deberían estar sus {random.choice(['rasgos', 'ojos', 'características', 'facciones'])}. No había ojos, pero podía sentir su mirada {random.choice(['atravesándome', 'penetrándome', 'diseccionándome', 'consumiéndome'])}. No había boca, pero escuchaba su respiración, húmeda y sibilante.

Su {random.choice(['piel', 'superficie', 'forma'])} era {random.choice(['pálida', 'translúcida', 'grisácea', 'cadavérica'])}. Podía ver {random.choice(['venas oscuras', 'estructuras internas', 'algo moviéndose', 'lo imposible'])} debajo, pulsando con un ritmo que no era humano. Demasiado lento. Demasiado irregular.

Extendió lo que podría ser una mano hacia mí. Los dedos eran {random.choice(['demasiado largos', 'imposiblemente delgados', 'articulados incorrectamente', 'antinaturales'])}, con {random.choice(['demasiadas articulaciones', 'garras negras', 'uñas afiladas', 'dedos extra'])}.

Cuando esos dedos se acercaron a mi {random.choice(['rostro', 'frente', 'cabeza', 'pecho'])}, sentí un frío que penetró hasta {random.choice(['mis huesos', 'mi alma', 'mi esencia', 'mi ser']}. No era solo temperatura. Era la ausencia de {random.choice(['vida', 'calidez', 'esperanza', 'existencia'])}.

Y entonces me tocó.""",
            
            'terror': f"""No puedo describir completamente lo que pasó a continuación. Mi mente, en un acto de autopreservación, bloqueó partes de esa experiencia. Lo que recuerdo viene en fragmentos, como un espejo roto donde cada pedazo refleja una pesadilla diferente.

Recuerdo {random.choice(['caer', 'flotar', 'girar', 'desintegrarme'])}. O tal vez {random.choice(['volar', 'hundirme', 'ascender', 'existir en múltiples lugares'])}. El espacio y la gravedad dejaron de tener sentido. Las paredes se estiraban. El techo se doblaba. Las habitaciones se multiplicaban, creando geometrías imposibles.

Recuerdo manos. Muchas manos. Frías, húmedas, emergiendo de {random.choice(['las paredes', 'el suelo', 'la oscuridad misma', 'dimensiones ocultas'])}. Tocándome, agarrándome, tirando de mí en direcciones que no existen.

Recuerdo voces. Susurrando secretos que no debería saber. Verdades sobre {random.choice(['el universo', 'la realidad', 'la muerte', 'lo que viene después'])} que la mente humana no está diseñada para comprender. Cada palabra era un cuchillo en mi {random.choice(['cordura', 'mente', 'alma', 'esencia'])}.

Vi cosas. Escenas que no podían ser reales. {random.choice(['Personas que habían estado allí antes', 'Historias del lugar', 'El pasado vivo', 'Otros mundos'])}. Vi sus últimos momentos. Sentí su terror como si fuera mío. Porque en ese lugar, en ese tiempo, éramos la misma cosa.

Las puertas se cerraban cuando intentaba acercarme. Los pasillos se extendían hasta el infinito. Corrí durante lo que parecieron {random.choice(['horas', 'días', 'eternidades', 'vidas completas'])}, solo para darme cuenta de que estaba exactamente donde había empezado.

Mi reflejo en {random.choice(['un vidrio roto', 'una ventana', 'un espejo', 'agua estancada'])} me {random.choice(['sonrió', 'miró con odio', 'lloró', 'gritó'])} mientras yo {random.choice(['gritaba', 'lloraba', 'rogaba', 'moría por dentro'])}. Mi sombra se separó de mí y caminó en dirección opuesta. El tiempo se volvió líquido. Mi reloj marcaba horas imposibles: 3:47, 3:48, 3:47, 3:47, 3:47...

Y siempre, SIEMPRE, esa presencia detrás de mí. Siguiéndome. No importaba cuán rápido corriera o dónde me escondiera. Estaba allí. Esperando. {random.choice(['Jugando', 'Cazando', 'Saboreando', 'Disfrutando'])}.""",
            
            'huida': f"""No sé cuándo exactamente recuperé algo de control. Tal vez nunca lo perdí completamente. Tal vez todo fue parte del {random.choice(['juego', 'ritual', 'experimento', 'castigo'])}.

De repente, después de una eternidad de pasillos infinitos y puertas que llevaban a ninguna parte, vi luz. Real, natural, hermosa luz {random.choice(['del día', 'del amanecer', 'del exterior', 'del mundo real'])} filtrándose por {random.choice(['una ventana rota', 'una grieta', 'una puerta entreabierta', 'un agujero'])}.

Una salida. Tenía que ser una salida.

{huida_desc}

Las cosas en las paredes intentaron detenerme. Sentí {random.choice(['garras', 'manos', 'tentáculos', 'algo'])} rasgando mi {random.choice(['ropa', 'piel', 'carne', 'espalda'])}. Algo {random.choice(['caliente', 'húmedo', 'viscoso']} y húmedo corrió por mi espalda. Sangre. Mi sangre.

El pasillo se {random.choice(['estiraba', 'extendía', 'alargaba', 'multiplicaba'])} frente a mí, alejando la salida con cada paso. Pero no me detuve. No podía detenerme. Detenerse significaba quedarme allí para siempre.

Escuché un {random.choice(['grito', 'aullido', 'rugido', 'alarido'])} detrás de mí. No humano. Lleno de {random.choice(['rabia', 'hambre', 'odio'])} y {random.choice(['frustración', 'deseo', 'necesidad'])}. Su juguete estaba escapando.

{random.choice(['Las luces comenzaron a parpadear', 'La oscuridad intentaba tragarme', 'El lugar intentaba sellarme dentro', 'El edificio rugía'])}. El edificio entero temblaba. O tal vez era yo.

Salté. No pensé. Solo salté {random.choice(['a través de esa ventana', 'hacia la luz', 'al vacío', 'hacia la libertad'])}, vidrios rotos y todo. Preferí morir cayendo que quedarme ni un segundo más en ese lugar maldito.""",
            
            'escape': f"""{despertar_desc}

Rodé por el suelo, sin poder creer que había escapado. El aire fresco llenó mis pulmones. Aire limpio, sin ese olor de muerte.

Pero cuando miré {random.choice(['el cielo', 'alrededor', 'mi reloj', 'el sol'])}, algo estaba mal. {tiempo_desc}

{random.choice(['Me arrastré', 'Caminé tambaleándome', 'Corrí', 'Huí']} alejándome del edificio. Cada parte de mi cuerpo dolía. Miré hacia atrás solo una vez. En una ventana del {random.choice(['tercer piso', 'segundo nivel', 'piso superior', 'ático'])}, vi una figura. Observando. Esperando.

Sabía que me dejaría ir. Por ahora. Pero también sabía que no había terminado conmigo.

Llegué a mi {random.choice(['auto', 'vehículo', 'coche'])} con las últimas fuerzas. Mis manos temblaban tanto que me tomó {random.choice(['tres', 'varios', 'múltiples'])} intentos {random.choice(['meter la llave', 'arrancar', 'abrir la puerta'])}. {random.choice(['Arranqué', 'Encendí el motor', 'Partí']} y conduje. No importaba a dónde. Solo lejos. Lejos de ese lugar.

Manejé durante horas. Cuando finalmente me detuve en {random.choice(['una gasolinera', 'un restaurante', 'un área de descanso'])} a kilómetros de distancia, vi mi reflejo. Casi no me reconocí. Mi {random.choice(['cabello tenía mechones grises', 'rostro había envejecido', 'ojos estaban vacíos', 'expresión era de muerte'])}. {random.choice(['La mirada de alguien que ha visto demasiado', 'Ojos que habían mirado al abismo', 'El rostro de alguien roto', 'Una persona diferente me devolvía la mirada'])}.""",
            
            'consecuencias': f"""Fui directo al hospital. Les dije que había tenido un accidente, que me había {random.choice(['caído', 'lesionado', 'herido'])} explorando un edificio abandonado. No mencioné nada más. ¿Qué iba a decir? ¿Que había sido atacado por algo que no debería existir?

{heridas_desc} Los médicos dijeron que los cortes eran {random.choice(['extraños', 'inusuales', 'inexplicables', 'imposibles'])}. Me dieron {random.choice(['antibióticos', 'analgésicos', 'medicamentos']} y me enviaron a casa con órdenes de descanso.

{trauma_desc}

{random.choice(['Cada noche', 'Constantemente', 'Sin parar', 'Todo el tiempo'])}, cuando cierro los ojos, estoy de vuelta en ese lugar. Caminando por esos pasillos infinitos. Perseguido por cosas sin nombre. Y siempre, justo antes de despertar, esa figura me alcanza. Sus dedos tocan mi {random.choice(['frente', 'rostro', 'alma'])}. Y yo veo...

No puedo describir lo que veo. Las palabras no existen.

He {random.choice(['dejado luces encendidas', 'sellado las ventanas', 'puesto cerraduras extra', 'instalado alarmas'])} en toda mi casa permanentemente. La oscuridad me aterra ahora de una manera que nunca antes. Porque en la oscuridad, veo sombras que no deberían estar ahí. Escucho susurros que no tienen fuente.

No puedo estar en {random.choice(['lugares cerrados', 'espacios pequeños', 'habitaciones sin ventanas', 'ascensores'])} por mucho tiempo. Los espacios {random.choice(['pequeños', 'cerrados', 'oscuros']} me hacen sentir como si {random.choice(['las paredes se estrecharan', 'estuviera de vuelta allí', 'me ahogara', 'estuviera atrapado'])}.

He notado cosas. Pequeñas cosas al principio. Objetos que no están donde los dejé. Puertas que encuentro abiertas cuando sé que las cerré con llave. La sensación constante, persistente, de {random.choice(['ser observado', 'no estar solo', 'ser seguido', 'ser cazado'])}.

A veces escucho mi nombre. Susurrado en {random.choice(['el viento', 'la noche', 'el silencio', 'la oscuridad'])}. En el {random.choice(['zumbido del refrigerador', 'ruido del tráfico', 'murmullo de la ciudad', 'silencio de la madrugada'])}. Siempre en esa voz que reconozco pero no puedo identificar.""",
            
            'epilogo': f"""Han pasado tres semanas desde aquella noche. Tres semanas que se sienten como {random.choice(['tres años', 'una eternidad', 'una vida entera', 'siglos'])}. Nada es igual. No sé si algo volverá a ser igual.

He investigado obsesivamente sobre {lugar_especifico}. Las historias que encontré... debí buscarlas antes de ir. Hay patrones. Desapariciones que se remontan a {random.choice(['más de un siglo', 'décadas atrás', 'generaciones', 'tiempos inmemoriales'])}. Personas que entraron y nunca salieron. O peor, que salieron pero nunca volvieron a ser las mismas.

Hay relatos de testigos que hablan de {random.choice(['luces extrañas', 'sonidos imposibles', 'apariciones', 'fenómenos inexplicables'])}. De sonidos que no deberían existir. De cosas vistas en las ventanas. Uno de los relatos, de {random.choice(['1923', '1947', '1965', '1892'])}, describe exactamente lo que vi: {random.choice(['una figura sin rasgos', 'sombras con voluntad propia', 'geometría imposible', 'el horror que encontré'])}.

No fui el primero. No seré el último.

He considerado {random.choice(['mudarme', 'huir', 'desaparecer', 'cambiar de identidad'])}. Irme lejos, a otro {random.choice(['estado', 'país', 'continente', 'mundo'])}. Pero tengo la sensación de que no importaría. Que la distancia no significa nada para lo que me encontró allí.

Esta mañana encontré algo que me heló la sangre. Una {random.choice(['fotografía', 'imagen', 'foto', 'captura'])} en mi teléfono. No la tomé yo. Es de mí. {random.choice(['Durmiendo en mi cama', 'Sentado en mi sala', 'Cocinando en mi cocina', 'Duchándome en mi baño'])}. La fecha de la foto es de {random.choice(['anoche', 'ayer', 'esta madrugada', 'hace una hora'])}.

Está tomada desde {random.choice(['el pie de mi cama', 'la esquina de mi habitación', 'la ventana', 'detrás de mí'])}. Desde el interior de mi casa. Desde mi {random.choice(['habitación', 'hogar', 'refugio', 'santuario'])}.

La cosa que conocí en {lugar_especifico} no se quedó allí. Me siguió. O tal vez nunca me dejó ir. Tal vez una parte de mí sigue atrapada en esos pasillos, y lo que volvió es solo un {random.choice(['eco', 'fragmento', 'sombra', 'cascarón'])}.

Mientras escribo esto, son las 3:47 AM. Siempre me despierto a las 3:47. Como mi reloj en aquel lugar.

Escucho algo. Un sonido. Como pasos. Lentos. {random.choice(['Arrastrados', 'Pesados', 'Deliberados', 'Inevitables'])}. Vienen del {random.choice(['pasillo', 'otro cuarto', 'piso superior', 'sótano'])}.

Mi puerta está cerrada con llave. Sé que lo está. La revisé {random.choice(['tres', 'cuatro', 'cinco', 'diez'])} veces antes de acostarme. Pero ahora está entreabierta. Puedo ver un pedazo de la oscuridad {random.choice(['del pasillo', 'del otro lado', 'esperando', 'observando'])}.

Y en esa oscuridad, veo {random.choice(['una silueta', 'una forma', 'una figura', 'algo'])}.

Conozco esa silueta.

No me atrevo a voltear. No me atrevo a mirar directamente. Porque sé que si lo hago, si realmente {random.choice(['la veo', 'la miro', 'la reconozco', 'la encuentro'])}, no hay regreso. Mi {random.choice(['mente', 'cordura', 'alma', 'ser'])} no lo soportaría.

Estoy escribiendo esto como {random.choice(['una advertencia', 'un testimonio', 'una confesión', 'evidencia'])}. Como {random.choice(['una confesión', 'un registro', 'una prueba', 'un grito'])}. Como evidencia de lo que me pasó.

Si estás leyendo esto, si estás considerando ir a {lugar_especifico}, o a cualquier lugar así... no lo hagas.

Algunos lugares están vacíos por una razón. Algunos lugares deben permanecer olvidados.

Y si de todos modos vas... si tu curiosidad o tu orgullo o tu escepticismo te llevan allí...

Que Dios te ayude.

Porque nada más podrá hacerlo.

Los pasos están más cerca ahora. Siento el frío. Ese frío antinatural que penetra hasta {random.choice(['el alma', 'los huesos', 'la esencia', 'el ser'])}.

Mi teléfono se está apagando. La batería estaba llena hace un momento.

Las luces parpadean.

La puerta se abre más.

Si encuentran este texto, sepan que intenté advertirles. Sepan que lo que hay allí es real. Y sepan que...

[El texto termina abruptamente. El archivo fue encontrado en un teléfono abandonado en un departamento vacío. El inquilino, {protagonista}, nunca fue visto de nuevo. La policía no encontró señales de lucha o entrada forzada. La puerta estaba cerrada con llave desde adentro.

En las paredes del departamento encontraron marcas. Profundas. Paralelas. Como de garras.

Y en la cámara del teléfono, una última foto. Tomada automáticamente por el sensor de movimiento.

Muestra {random.choice(['una figura sin rostro', 'una sombra imposible', 'algo entre dimensiones', 'el horror hecho forma'])}. Parada junto a la cama.

La cama está vacía.

Las sábanas aún conservan la forma de un cuerpo.

La foto está fechada a las 3:47 AM.]"""
        }
        
        return historia
'''

# Usar regex para encontrar y reemplazar el método completo
pattern = r'    def generar_historia_completa\(self\):.*?(?=\n    def |\n\nif __name__|$)'
content_new = re.sub(pattern, new_method, content, flags=re.DOTALL)

# Verificar que el reemplazo funcionó
if content_new != content:
    # Guardar el archivo modificado
    with open('/Users/wu/radio-terror-ia/radio_terror_potenciado.py', 'w', encoding='utf-8') as f:
        f.write(content_new)
    print("✅ Método generar_historia_completa actualizado exitosamente!")
    print("📊 El nuevo sistema usa variaciones aleatorias para CADA elemento")
    print("🎲 Combinaciones posibles: 50 protagonistas × 40 ocupaciones × 40 lugares × 30 motivos")
    print("💯 = 2,400,000 combinaciones base")
    print("🎨 Cada capítulo con 5-10 variaciones = miles de millones de historias únicas")
else:
    print("❌ Error: No se pudo encontrar el método para reemplazar")
