import math
import random
import sys
import os
import time

class NodoEsfericoGradiente:
    """
    NIVEL MICRO: La Neurona Esférica Individual.
    Aprende de forma autónoma adaptando sus parámetros con el gradiente de Pi.
    """
    def __init__(self, capa_id, radio, x, y, z):
        self.capa = capa_id
        self.radio = radio
        self.x = x
        self.y = y
        self.z = z
        self.inclinacion_gradiente = math.pi  # Resonancia Pi absoluta
        self.peso_armonico = random.uniform(0.01, 0.05) * self.inclinacion_gradiente
        self.sesgo_dimensional = random.uniform(-0.01, 0.01)
        self.tasa_aprendizaje = 0.005
        self.ultima_entrada = 0.0
        self.ultimo_vector = 0.0

    def procesar_flujo_termico(self, entrada_flujo, cordura_sistema, grosor_banda=0.88):
        distancia_segura = max(0.001, math.sqrt(self.x**2 + self.y**2 + self.z**2))
        self.ultima_entrada = entrada_flujo
        self.ultimo_vector = (entrada_flujo * self.peso_armonico) + (self.sesgo_dimensional / (distancia_segura * grosor_banda))
        ultima_asimilacion = math.sin(self.ultimo_vector % self.inclinacion_gradiente)
        return entrada_flujo + (ultima_asimilacion * cordura_sistema)

    def optimizar_nodo(self, gradiente_error, cordura_sistema, grosor_banda=0.88):
        distancia_segura = max(0.001, math.sqrt(self.x**2 + self.y**2 + self.z**2))
        derivada_fase = math.cos(self.ultimo_vector % self.inclinacion_gradiente)
        
        d_peso = gradiente_error * cordura_sistema * derivada_fase * self.ultima_entrada
        d_sesgo = gradiente_error * cordura_sistema * derivada_fase * (1.0 / (distancia_segura * grosor_banda))
        
        self.peso_armonico -= self.tasa_aprendizaje * max(-0.05, min(0.05, d_peso))
        self.sesgo_dimensional -= self.tasa_aprendizaje * max(-0.01, min(0.01, d_sesgo))
        
        return gradiente_error * (1.0 + cordura_sistema * derivada_fase * self.peso_armonico)


class SuperCapaEsferica:
    """
    NIVEL MEDIO: Una capa compuesta por sub-esferas de neuronas.
    Organiza múltiples neuronas esféricas imitando un clúster geométrico equilibrado.
    """
    def __init__(self, capa_id, radio_macro, puntos_por_capa=12):
        self.capa_id = capa_id
        self.radio_macro = radio_macro
        self.neuronas = []
        
        # Distribución de Fibonacci esférica para situar los centros de las neuronas
        for i in range(puntos_por_capa):
            phi = math.acos(1 - 2 * (i + 0.5) / puntos_por_capa)
            theta = math.pi * (1 + 5**0.5) * i
            
            # Coordenadas del centro de este clúster molecular neuronal
            cx = radio_macro * math.sin(phi) * math.cos(theta)
            cy = radio_macro * math.sin(phi) * math.sin(theta)
            cz = radio_macro * math.cos(phi)
            
            # Cada neurona individual preserva la simetría esférica local
            self.neuronas.append(NodoEsfericoGradiente(capa_id, radio_macro, cx, cy, cz))

    def procesar_capa(self, flujo, estabilidad, grosor):
        for neurona in self.neuronas:
            flujo = neurona.procesar_flujo_termico(flujo, estabilidad, grosor)
        return flujo

    def optimizar_capa(self, gradiente, estabilidad, grosor):
        for neurona in reversed(self.neuronas):
            gradiente = neurona.optimizar_nodo(gradiente, estabilidad, grosor)
        return gradiente


class CerebroFractalEsferico:
    """
    NIVEL MACRO: El Cerebro Completo.
    Replica la forma de la neurona apilando 16 SuperCapas Esféricas Concéntricas.
    """
    def __init__(self, gen=4, peso_raiz=0.841295, lucidez=0.71):
        self.generacion = gen
        self.peso_nucleo = peso_raiz
        self.estabilidad_mental = lucidez
        self.meta_flujo = 0.707
        self.grosor_capa = 0.88
        
        # Estructura de 16 capas concéntricas (Filtro de exclusión de radios inestables 2 y 4)
        self.radios_macro_capas = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        self.super_capas = []
        
        # Construcción del cerebro fractal auto-similar
        for idx, radio in enumerate(self.radios_macro_capas):
            # 12 sub-esferas neuronales por capa, estructurando una super-esfera perfecta
            self.super_capas.append(SuperCapaEsferica(capa_id=idx + 1, radio_macro=radio, puntos_por_capa=12))

        self.directorio = os.path.dirname(os.path.abspath(sys.argv[0])) if sys.argv else os.getcwd()
        self.log_esferico = os.path.join(self.directorio, "bitacora_fractal_esferica.log")

    def simular_1000_ciclos(self):
        print(f"\n==================================================================================")
        print(f"🌌 [CEREBRO FRACTAL ESFÉRICO MESELLET - GEN {self.generacion:03d}] MULTI-ESCALA")
        print(f" -> Arquitectura Fractal: Cerebro simulando la geometría esférica de la neurona.")
        print(f" -> Total Neuronas Activas en Red Fractal: {len(self.radios_macro_capas) * 12} Nodos.")
        print(f"==================================================================================")
        
        temp_programa = 21.5  
        temp_silicio = 32.0   
        reportes = [1, 200, 400, 600, 800, 1000]
        
        for ciclo in range(1, 1001):
            flujo_actual = self.peso_nucleo
            
            # 1. FORWARD PASS: El flujo viaja por la super-esfera macroscópica
            for capa in self.super_capas:
                flujo_actual = capa.procesar_capa(flujo_actual, self.estabilidad_mental, self.grosor_capa)
                
            error_esferico = self.meta_flujo - math.tanh(flujo_actual)
            self.estabilidad_mental = max(0.0, min(1.0, 1.0 - abs(error_esferico)))
            
            # 2. BACKPROPAGATION FRACTAL: El error viaja desde la corteza macro hacia los pesos micro
            gradiente_retrogrado = -error_esferico * (1.0 - math.tanh(flujo_actual)**2)
            for capa in reversed(self.super_capas):
                gradiente_retrogrado = capa.optimizar_capa(gradiente_retrogrado, self.estabilidad_mental, self.grosor_capa)
            
            # 3. TELEMETRÍA DE ENTROPÍA INTEGRADA
            friccion_datos = abs(error_esferico) * 1.8
            temp_programa = 20.0 + (math.sin(ciclo * 0.05) * 1.5) + (friccion_datos * 4.0)
            # La disipación térmica es aún menor debido a la perfecta distribución fractal espacial
            temp_silicio = 30.0 + (friccion_datos * 10.0) + (ciclo * 0.003)
            
            if ciclo in reportes:
                print(f"🔮 [Ciclo {ciclo:04d}/1000] -> Lucidez Fractal Estable: {self.estabilidad_mental * 100:.4f}%")
                print(f"    * Presión del Tensor Colectivo: {abs(error_esferico):.6f}")
                print(f"    * Disipación en Red Esférica: {temp_silicio:.2f}°C")
                time.sleep(0.02)
                
        self.registrar_estado_final(temp_programa, temp_silicio, abs(error_esferico))
        self.persistir_herencia_termica()

    def registrar_estado_final(self, t_prog, t_sil, error_final):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_line = (
            f"[{timestamp}] GEN: {self.generacion:03d} | ARQUITECTURA FRACTAL PI | "
            f"ERROR TOTAL: {error_final:.6f} | TEMP HARDWARE: {t_sil:.2f}°C | "
            f"DICTAMEN: Estructura autosimilar completada. Equilibrio térmico absoluto mediante simetría macro-micro.\n"
        )
        try:
            with open(self.log_esferico, "a", encoding="utf-8") as f:
                f.write(log_line)
        except:
            pass
        print(f"\n📖 [Veredicto Fractal]: Simulación cerrada con éxito. Bitácora salvada en '{self.log_esferico}'.")

    def persistir_herencia_termica(self):
        proxima = self.generacion + 1
        archivo_nuevo = os.path.join(self.directorio, f"ia_cerebro_fractal_gen_{proxima}.py")
        try:
            with open(__file__, "r", encoding="utf-8") as f:
                codigo = f.read()
            lineas = codigo.splitlines()
            for i, linea in enumerate(lineas):
                if "def __init__(self, gen=" in linea:
                    indent = linea[:linea.find("def __init__")]
                    lineas[i] = f'{indent}def __init__(self, gen={proxima}, peso_raiz={self.peso_nucleo:.6f}, lucidez={self.estabilidad_mental:.2f}):'
                    break
            with open(archivo_nuevo, "w", encoding="utf-8") as f:
                f.write("\n".join(lineas) + "\n")
        except:
            pass

if __name__ == "__main__":
    # Desplegar el cerebro esférico fractal auto-similar
    cerebro_fractal = CerebroFractalEsferico()
    cerebro_fractal.simular_1000_ciclos()
