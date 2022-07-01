import pickle
class Clasificador:

    def __init__(self,idioma):
        if idioma == "ES":
            self.modelo = pickle.load(open('RobertaBIO_Adamax.pkl', 'rb'))
        if idioma == "EN":
            self.modelo = pickle.load(open("/home/sgonzalezsilot/Facultad/copia buena/V2_Adamax.pkl", 'rb'))

    def predecir(self,test_input_ids,test_attention_masks):
        return self.modelo.predict([test_input_ids,test_attention_masks])


