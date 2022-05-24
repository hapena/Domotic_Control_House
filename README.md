# Domotic_Control_House


Descripción del proyecto:
El proyecto Docmotic-Contrtol-House se plantea en el contexto de la revolución industrial 4.0 y el uso de las TI en el ámbito urbano; debido a la constante necesidad del uso adecuado de los recursos naturales y en la búsqueda de incrementar y mejorar nuestra calidad de vida el proyecto nos ayuda a aprovechar al máximo todos los recursos que tenemos a nuestro servicio. Esto porque se puede programar y automatizar; abrir, cerrar, apagar, encender y regular los electrodomésticos, la climatización, la ventilación o la iluminación artificial. También se puede regular el funcionamiento de las persianas, puertas, cortinas, riego, suministro de agua o gas y en general casi todos los aparatos electrónicos y una muy buena cantidad de dispositivos en el hogar.
Según Triana W. (2020). El cambio climático y el agotamiento de los recursos convierten la eficiencia energética en un asunto social clave. Con ahorros en el consumo energético, la Domótica nos permite contribuir a la preservación del planeta sin renunciar al máximo de confort. Por otro lado Endesa(2021) ,indica que  Estudios del Instituto para la Diversificación y Ahorro de la Energía (IDAE) apuntan que la domótica puede llegar a ahorrar un 39% en calefacción, un 27% de agua caliente, un 12% en electrodomésticos, un 9% en iluminación y un 2% en aire acondicionado.

El proyecto Docmotic-Contrtol-House nos permite aplicar una gestión eficiente en el consumo de energía, seguridad y confort; que mejoran  la habitabilidad, aumentan la  seguridad y potencian a largo plazo el ahorro de agua, energía y dinero. Este proyecto utiliza sensores, sistemas motorizados, tecnologías inalámbricas y la integración directa con teléfonos celulares para establecer comunicación entre el sistema y el usuario a través de un Telegram Bot API; aplicaciones de software programadas para interactuar con el usuario de Docmotic-Contrtol-House a través del chat. Sus acciones y respuestas han sido creado con el objetivo de tener control total de la vivienda que realiza tareas repetitivas, predefinidas y automatizadas; está diseñado para sustituir el accionar humano por lo que pueden trabajar de una manera eficiente en la administración de recursos en el hogar.

El proyecto Docmotic-Contrtol-House busca crear una solución utilizando que ayude a alcanzar 4 de los 17 Objetivos de Desarrollo Sostenible (ODS), los cuales buscan obtener de manera equilibrada tres dimensiones del desarrollo sostenible: el ámbito económico, social y ambiental. Estos Objetivos son:

3. Salud y Bienestar
7. Energía asequible y no Contaminante
11. Ciudades y Comunidades Sostenibles
13. Acción por el Clima

La Academia Cisco del colegio Jorge Gaitán Cortés utilizará cómo herramientas mediadoras la programación en Python, los conceptos de Internet de las Cosas y Devnet. En el proyecto participarán estudiantes de grado undécimo de la academia CISCO, quienes generarán prototipos del sistema de control Docmotic-Contrtol-House. Debido a todo lo anterior el sistema creado se podrá ir mejorando y actualizando según las tecnologías que vayan saliendo en el mercado. El proyecto será asesorado por los instructores de la Academia SED-CISCO Jorge Gaitán Cortes IED.
Los estudiantes están en proceso de certificación CISCO en Partner: PCAP - Programming Essentials in Python, IoT Fundamentals: Connecting Things, Linux y Devnet.
Se cuenta con el material de laboratorio ofrecido por la institución educativa; entre ellos las plataformas de desarrollo basadas en hardware Libre, (Raspberry Pi 4 Modelo B 4gb Kit, Esp32 Wifi + Bluetooth 4.2 Ble Nodemcu Esp32s), sensores y actuadores; además en la parte del software se trabaja, Python 3, Micropython v1.17, Editores como VsCode,  Thonny IDE, y las plataformas de desarrollo de Cisco Webex Teams.

Ambiente de desarrollo:

![image](https://user-images.githubusercontent.com/71275875/170074475-f96274cc-76bf-45bf-b8d6-2569f34bd6c7.png)![image](https://user-images.githubusercontent.com/71275875/170074507-639a38ba-6905-4b01-a8db-62da84406ce4.png)

Problema:
Estudios Preliminares: Agua y energía

Según Ruiz, L.(2020) el desperdicio de agua en Colombia es del 43 %; indica que  si a eso le sumamos la contaminación que recibe el Río Bogotá a diario, la cifra aumenta. Agrega que Colombia está entre los 20 países con mayor cantidad de agua en el mundo, pero las altas temperaturas, debido al calentamiento global y al desperdicio de los recursos, podrían causar que en los próximos años el 75 % del país sufra de desabastecimiento.  Por eso diferentes entidades trabajan para generar consciencia debido a las malas prácticas en empresas y hogares.
Por otro lado Riaño, N. (2017).  Afirma que las malas prácticas de la población frente al agua también contribuyen a su despilfarro. Desde usuarios que realizan un uso indebido de este líquido hasta errores en la medición, la facturación o condiciones fraudulentas de los clientes.

 ![image](https://user-images.githubusercontent.com/71275875/170075187-e220db87-5d97-4bdb-9031-699da9a6d1ba.png)
Tomado de: La Republica. https://www.larepublica.co/responsabilidad-social/cuatro-de-cada-10-litros-de-agua-potable-se-malgastan-en-colombia-2530612 

Según Enersinc(2017).Los consumos de energía en este sector residencial Urbano se dan básicamente por la refrigeración, iluminación y cocción, siendo esta última la que ocupa el mayor porcentaje (46%), en relación con todos los factores identificados (climatización, calentamiento de agua, iluminación, entre otros).
Teniendo en cuenta lo anterior y con el objetivo de mejorar el uso de la energía y lograr la meta de ahorro en 0,79%8 entre el 2016 y el 2021 afirma  Enersinc(2017),  diferentes entidades han desarrollado en los últimos años estrategias para que todas las zonas del país sean cada vez más eficientes en el uso de la energía, a través de nuevos equipos. 
VARGAS P. (2016) sostiene que según estudios el país malgasta el 10 por ciento de toda la energía que produce, unos 6.000 gigavatios hora año en todos los sectores: industrial, residencial, comercial, salud y público. Añade que Discriminado por tipo de consumidor, en la residencial y pequeños negocios se presentó un crecimiento de 6,72 %.

![image](https://user-images.githubusercontent.com/71275875/170075230-d56ef8ca-a7e8-4497-afe3-126850b44cab.png)
Tomado de: Departamento Nacional de planeación. https://www.dnp.gov.co/Crecimiento-Verde/Documents/ejes-tematicos/Energia/MCV%20-%20Energy%20Demand%20Situation%20VF.pdf 

Pregunta problema y objetivo. 

¿Es posible aplicar las TI y el Internet de las Cosas para  una gestión eficiente en el consumo de energía, seguridad y confort que mejoren la habitabilidad, aumente la seguridad y potencie a largo plazo el ahorro de agua,  energía y dinero en viviendas residenciales de la localidad de Engativá en Bogotá?

Objetivo General y objetivos específicos

General:
Diseñar e implementar un Sistema Domótico a través del uso del IoT que permita la integración directa con teléfonos celulares para establecer comunicación entre el sistema y el usuario a través de un Telegram Bot API para tener control total de la vivienda con tareas predefinidas y automatizadas permitiendo gestionar de manera individual e inteligente nuestro consumo diario de recursos.


Específicos:

Diseñar el prototipo domótico con el uso de sensores, actuadores, sistemas motorizados, y tecnologías inalámbricas para el control de los aparatos y dispositivos electrónicos.

Programar en el sistema las tareas repetitivas, predefinidas y automatizadas a través de la implementación de Python en microcontroladores (Micropython) para sustituir el accionar humano. 

Programar el sistema de comunicación utilizando las tecnologías de Telegram Bot API para permitir la interacción a través del chat con el usuario de Docmotic-Contrtol-House. 

Realizar pruebas y analizar los datos en la aportación del sistema domótico, enfocados en la mejora de la eficiencia en el consumo diario de recursos.

Desarrollo del proyecto:

En este apartado se procederá a explicar el contenido el cual es la base para que el programa funcione de la manera establecida, se abordarán aspectos del código y se profundizará en el circuito conformado para este proyecto.

Circuito:

![image](https://user-images.githubusercontent.com/71275875/170072150-8377aa7a-e0cf-472f-aac1-030138589676.png)


Distribución de Pines:

![image](https://user-images.githubusercontent.com/71275875/170083737-4cc8ffcb-1d6f-42dc-936a-bb0273f79118.png)


Prototipo:

![image](https://user-images.githubusercontent.com/71275875/170077576-26505e47-db25-43a6-a25f-74164466492d.png)


Recursos:

Modulo ESP32 – 30 Pines:

![image](https://user-images.githubusercontent.com/71275875/170076014-dbb65d90-1ad4-49d7-bde2-f7ae562ea7f8.png)


Creado y desarrollado por Espressif Systems, ESP32, una serie de microcontroladores de bajo costo y de bajo consumo con sistema en chip con Wi-Fi y Bluetooth de modo dual integrados. Este dispositivo tomaría los datos de nuestro sensor y así mismo enviando estos registros de temperatura a la nube.

Sensor de temperatura y humedad DTH11:

![image](https://user-images.githubusercontent.com/71275875/170076085-115dc2d2-e87c-4d17-8813-c2aad2888fbe.png)


El DHT11 es un sensor digital de bajo costo de temperatura y humedad. El sensor de humedad utiliza un principio capacitivo mientras que el de temperatura utiliza un termistor. El sensor se integra fácilmente con un Arduino dado que contiene librerías desarrolladas específicamente para el mismo. Las lecturas del sensor sólo pueden realizarse cada dos segundos. El sensor Cuenta con 3 pines (Vcc, GND, OUT) conectados que se conectan a los pines de la tarjeta en el mismo orden a (3.3v, GND, Pin15).



Sensor de humedad suelo:

![image](https://user-images.githubusercontent.com/71275875/170076116-1d0c5182-33d1-4c63-9c38-99d814bbc00d.png)


El módulo sensor de humedad de suelo resulta ser otro módulo que utiliza la conductividad entre dos terminales para determinar ciertos parámetros relacionados a agua, líquidos y humedad. El sensor Cuenta con 3 pines ( + , - , s) conectados que se conectan a los pines de la tarjeta en el mismo orden a (3.3v, GND, Pin39).

Thonny IDE:

![image](https://user-images.githubusercontent.com/71275875/170076660-9dbb78f1-6616-423a-b8fc-5eb13d6cd22d.png)

 
Thonny es un IDE de Python para principiantes, desarrollado en la Universidad de Tartu, Estonia, que tiene un enfoque diferente ya que su depurador está diseñado específicamente para el aprendizaje y la programación de enseñanza. ... Instalación sencilla; viene integrado con python 3.6

Lenguaje de programación Python Vers. 3.9

![image](https://user-images.githubusercontent.com/71275875/170076727-fcdc90fb-8887-4855-934b-84e7d9abddd0.png)

Python es un lenguaje de escritura rápido, escalable, robusta y de código abierto, ventajas que hacen de Python un aliado perfecto para la Inteligencia Artificial. Permite plasmar ideas complejas con unas pocas líneas de código, lo que no es posible con otros lenguajes.



El codigo:

El código ha sido escrito en el lenguaje de programación Python con un enfoque orientado a objetos, haciendo uso de una de las diferentes modalidades que nos brinda este lenguaje, en este caso se construyó en MicroPython y se hicieron uso de librerías enfocadas al funcionamiento del sensor DHT11 y sensor de Agua.

1.(Líneas 1 a 3) En primer lugar, se importan los módulos “machine, time, urequests, network, DHT11”, para usar los pines de la tarjeta, leer los diferentes sensores y establecer comunicación Wifi para envío de datos a internet a través del uso de diferentes Apis.

import network, time, urequests
from dht import DHT11
from machine import Pin, ADC

2.(Líneas 5 a 10) Creamos los diferentes objetos que me permitirán realizar la lectura de los diferentes sesnores; entre ellos el objeto “sensor_Hs” que utiliza el pin 36 de la tarjeta para medir la humedad del suelo; El “bojeto sensorDHT” que utiliza el pin 15 de la tarjeta y permitirá leer temperatura y humedad ambiente. Los Objetos “rojo y Verde” que utilizan los pines 2y 4 y que serán los indicadores de niveles altos o adecuados de las diferentes variables.

sensor_Hs = ADC(Pin(36))  # Creamis el objeto para realizar la lectura de humedad de suelo
sensor_Hs.width(ADC.WIDTH_12BIT)  # permite regular la precisión de lectura
sensor_Hs.atten(ADC.ATTN_11DB) # permite trabajar con 3.3v
sensorDHT = DHT11 (Pin(15))  # Creamos el objeto DHT11 y asignamos el pin apara leer temperatura
rojo = Pin(2, Pin.OUT)  # Creamos el objeto rojo y asignamos el pin
verde= Pin(4, Pin.OUT)  # Creamos el objeto verde y asignamos el pin

3.(Líneas 14 a 25) Seguido al paso anterior procedemos a crear una nueva función que va a permitir la conexión Wifi de la tarjeta ESP32 a la red especificada en el fragmento de código "conectaWifi".

def conectaWifi(red, password):
     global miRed
     miRed = network.WLAN(network.STA_IF)     
     if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
     return True
     
4.(Líneas 30 a 36) Luego procedemos a realizar el llamado a la función conectaWifi con las credenciales del usuario. Imprimimos los datos de conexión y creamos las variables url_1 y url_2 que nos va a permitir hacer uso de los applets creados en la página IFTTT:
url_1: Utiliza el applet que envía datos de los sensores a una hoja de cálculo de Google. url_2: Utiliza el applet que envía datos de los sensores a un correo electrónico de Google.

      if conectaWifi("red", "password"):

          print("Conexión exitosa!")
          print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

          url_1 = "https://maker.ifttt.com/trigger/sensor_dth/with/key/XXXXXXXXXXXXXXXX?"  #  Applet IFTTT
          url_2 = "https://maker.ifttt.com/trigger/correo_emergencia/with/key/XXXXXXXXXXXXXXXX?" # Applet IFTTT
          
          
5.(Líneas 40 a 51) Creamos la función While True; el ciclo infinito que inicia los sensores realiza la lactura de las variables y envia los datos a la url_1.
  while (True):

          time.sleep (4)
          sensorDHT.measure()
          temp=sensorDHT.temperature()
          hum=sensorDHT.humidity()
          hum_suelo =  int(sensor_Hs.read())
          print ("T={:02d} ºC, H={:02d}, Hs={:02d} = %".format (temp,hum, hum_suelo))
          respuesta_1 = urequests.get(url_1+"&value1="+str(temp)+"&value2="+str(hum)+ "&value3="+str(hum_suelo))      
          print(respuesta_1.text)
          print (respuesta_1.status_code)
          respuesta_1.close ()
          
6.(Líneas 53 a 83) Creamos las condicionales “if y else” que de acuerdo a los valores de las variables enviaran alertas a los correos electrónicos haciendo uso de la url_2 y encenderán o apagaran los leds indicadores.

  if hum_suelo < 300 :

              respuesta_2 = urequests.get(url_2+"&value1="+str(hum_suelo))      
              print(respuesta_2.text)
              print (respuesta_2.status_code)
              respuesta_2.close ()
              time.sleep(10)
              rojo.value(1)
              verde.value(0)

          elif temp> 25 :

              respuesta_2 = urequests.get(url_2+"&value1="+str(temp))      
              print(respuesta_2.text)
              print (respuesta_2.status_code)
              respuesta_2.close ()
              time.sleep(10)
              rojo.value(1)
              verde.value(0)

          else:

              rojo.value(0)
              verde.value(1)

