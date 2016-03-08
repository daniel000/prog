import math

##import matplotlib.pylab as plt


__author__ = ''
class onda_seno: ## Primera opcion para generar la onda sinosoidal
    arregloseno=[]
    def _init_(self,frecuencia,sampleo,tiempo,bits):
        self.frecuenciaonda = frecuencia
        self.sampler = sampleo
        self.time = tiempo
        self.Bit = bits
        self.tam =sampleo * tiempo

    def generar(self): ## funcion para generar la onda
        for i in range (0, self.tam):
            wave = ((2**self.Bit)/2)*math.sin((2*math.pi*self.frecuenciaonda*i)/self.sampler)
            onda_seno.arregloseno.append(wave)
    def imprimir(self):
        plt.plot(onda_seno.arregloseno)
		plt.show()

class onda_cuadrada:
    arregloseno=[]
    def _init_(self,frecuencia,sampleo,tiempo,bits):
        self.frecuenciaonda = frecuencia
        self.sampler = sampleo
        self.time = tiempo
        self.Bit = bits
        self.tamaño =sampleo * tiempo

    def generar(self):
            for i in range(0, self.tam):
                    wave = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)
        if datos<0:
                wave=(-(2**self.NumeroBit)/2)

        if datos>0:
                wave=((2**self.NumeroBit)/2)
                onda_cuadrada.arregloseno.append(wave)

    def graficar(self):
        plt.plot(onda_seno.arregloseno)
		plt.show()

class triangular:
    arregloseno=[]
    def _init_(self,frecuencia,sampleo,tiempo,bits):
        self.frecuenciaonda = frecuencia
        self.sampler = sampleo
        self.time = tiempo
        self.Bit = bits
        self.tamaño =sampleo * tiempo
    def generar(self):
        t1=2*self.Frecuencia*(2**self.NumeroBit)
	    t2=((2**self.NumeroBit)/2)
	    t3=0
            for i in range(0, self.tam):
                wave = ((2**self.NumeroBit)/2)*math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)
        t3=t3+t1
        triangular.arregloseno.append(s)
        if (abs(wave)==t2):
                t1=-1*t1

    def graficar(self):
        plt.plot(triangular.arregloseno)
		plt.show()



def main():
    print("tipo de onda a generar")
    print ("1  Sinusoidal")
	print ("2  Cuadrada")
	print ("3  Triangular")
    menu = input ("ingrese opcion")
    frec = input("Digite la frecuencia del tono a generar: ")
    samp = input("Digite la frecuencia de sampleo: ")
    B = input("Digite el numero de bits: ")
    tim = input("Ingrese el tiempo de audio en segundos: ")
    if menu ==  1:
		graf = onda_seno(frec, samp, B, tim)
            graf.generar()
		    graf.imprimir()
    if menu == 2:
        graf = onda_cuadrada(frec, samp, B, tim)
            graf.generar()
		    graf.imprimir()

    if menu == 3:
        graf = triangular(frec, samp, B, tim)
            graf.generar()
		    graf.imprimir()





if __name__ == "__main__":
    main()

