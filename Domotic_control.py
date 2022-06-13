#------------------------------ [IMPORT]------------------------------------
import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
from dht import DHT11
import utime

TOKEN = '5031163680:AAG45iFduorhunFrZs6GsGGBc7QUaegYGhE'

#--------------------------- [OBJETOS]---------------------------------------

bot = Bot(TOKEN)

sensorDHT= DHT11(Pin(4))

gas =   ADC(Pin(39))
gas.width(ADC.WIDTH_10BIT) 
gas.atten(ADC.ATTN_11DB)

luz = ADC(Pin(36))
luz.width(ADC.WIDTH_10BIT) 
luz.atten(ADC.ATTN_11DB)

lluvia = ADC(Pin(34))
lluvia.width(ADC.WIDTH_10BIT) 
lluvia.atten(ADC.ATTN_11DB)

ventilador = Pin(19, Pin.OUT)
bombillo  = Pin(5, Pin.OUT)

puerta = PWM(Pin(12), freq=50)

magnetico = Pin(15,Pin.IN,Pin.PULL_UP) # conectado al negativo (1)  oprimir (0)


#----------------------[ SERVO-MOTOR ]---------------------------------------------------------#

def map(x):
        return int((x - 0) * (130- 34) / (180 - 0) + 34)
    
    
#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#

def conectaWifi (red, password):
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

 
#------------------------------------[BOT]---------------------------------------------------------------------#

if conectaWifi ("INFORMATICA2", "Adminredp2017"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    while True:
            
        @bot.add_message_handler("Hola")
        def help(update):
            update.reply('''¡Bienvenido!
                         \n Menu Principal                                        
                         \n Domotic Control House
                         \n Estado de tu Hogar...... 
                         \n Elije una opción:
                         
                         Temperatura : Temp
                         Gas: Gas
                         Luz Dia: Luz
                         Lluvia y Humedad: Clima
                         Activar Aire A: Airea
                         Deasactivar Aire A:Aired
                         Encender Iluminacion : On
                         apagar Iluminacion : Off 
                         Abrir Puerta: Open
                         Cerrar Puerta : Close
                         Estado Puerta: Estado
                                                
                         \n No olvides que estoy para tu seguridad y confort
                         \n garcias''')
              
        
        @bot.add_message_handler("Temp")
        def sensor_temperatura(update):
            
            sensorDHT.measure()
            temp = sensorDHT.temperature()
            hum = sensorDHT.humidity()       
            update.reply("Temperatura: "+ str(temp) + "°C  " + "Humedad: " + str(hum) + "%")
            
        
        @bot.add_message_handler("Gas")
        def sensor_gas(update):
            
            lectura_gas = gas.read()
            if lectura_gas > 600:
                update.reply("Gas: "+ str(lectura_gas) + " Nivel Alto")
            else:
                update.reply("Gas: "+ str(lectura_gas) + " Nivel Normal")
                
        @bot.add_message_handler("Luz")
        def sensor_luz(update):
            
            lectura_luz = luz.read()
            if lectura_luz < 600:
                update.reply("Nivel Luminosidad: "+ str(lectura_luz) + " Dia")
            else:
                update.reply("Nivel Luminosidad: "+ str(lectura_luz) + " Noche")
                
        @bot.add_message_handler("Clima")
        def sensor_lluvia(update):
            
            lectura_lluvia = lluvia.read()
            if lectura_lluvia > 100:
                update.reply("Clima: "+ str(lectura_lluvia) + " Clima lluviosos")
            else:
                update.reply("Clima "+ str(lectura_lluvia) + " clima Seco")
        
        @bot.add_message_handler("Airea")
        def activar_aire(update):
            ventilador.off()
            update.reply("Aire Acondicionado Encendido")
            
        @bot.add_message_handler("Aired")
        def desactivar_aire(update):
            ventilador.on()
            update.reply("Aire Acondicionado apagado")
            
        @bot.add_message_handler("On")
        def activar_iluminacion(update):
            bombillo.off()
            update.reply("Iluminación Encendido")
            
        @bot.add_message_handler("Off")
        def desactivar_ilumunacion(update):
            bombillo.on()
            update.reply("Iluminación apagado")
            
        @bot.add_message_handler("Open")
        def abrir_puerta(update):
            m = map(180)
            puerta.duty(m)
            update.reply("Puerta Abierta")
            
        @bot.add_message_handler("Close")
        def cerrar_puerta(update):
            m = map(90)
            puerta.duty(m)
            update.reply("Puerta Cerrada")
            
           
        @bot.add_message_handler("Estado")
        def estado_puerta(update):
                        
            estado = magnetico.value()
            utime.sleep(0.2)
            
            if estado == 1:
                update.reply("Estado de la puerta: 'Cerrada' ")
            else:
                update.reply("Estado de la puerta: 'Abierta' ")
                
                
        bot.start_loop()
    
else:
       print ("Imposible conectar")
       miRed.active (False)