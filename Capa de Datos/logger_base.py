import logging as log

log.basicConfig(level=log.DEBUG, # Se muestra en pantalla solamente de lo que especificamos en config en adelante
                format='%(asctime)s: %(levelname)s [%(filename)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ]) # Estos son Handlers


if __name__ == '__main__':
    log.debug("Mensaje a nivel de Debug") # Niveles
    log.info("Mensaje a nivel de info")
    log.error("Mensaje a nivel de error")
    log.warning("Mensaje a nivel de warning")
    log.critical("Mensaje a nivel critico")
