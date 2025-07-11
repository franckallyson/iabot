import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.inicializado, self.robo = inicializar()

    def testar_00_inicializado(self):
        self.assertTrue(self.inicializado)

    def testar_01_oi_ola(self):
        saudacoes = ["oi", "olá", "oi, tudo bem?", "e aí", "tudo certo?", "oi, como vai?", "como vai"]

        for saudacao in saudacoes:
            print(f"testando a saudação: {saudacao}")

            resposta, confianca = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, CONFIANCA_MINIMA)
            self.assertIn("Olá! Sou o IABot, seu assistente virtual para dúvidas sobre Inteligência Artificial. Quer saber algo sobre IA, machine learning ou outros temas relacionados?", resposta)

    def testar_02_variabilidades(self):
        saudacoes = ["como vai?", "olá, como vai?", "olá, tudo bem?", "tudo bem?"]

        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            resposta, confianca = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, CONFIANCA_MINIMA)
            self.assertIn("Sou o IABot, seu assistente virtual para dúvidas sobre Inteligência Artificial", resposta)

    def testar_03_bom_dia(self):
        saudacoes = ["bom dia", "oi, bom dia", "olá, bom dia"]

        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            resposta, confianca = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, CONFIANCA_MINIMA)
            self.assertIn("Bom dia! Sou o IABot. Posso te ajudar com perguntas sobre Inteligência Artificial. Como posso ajudar você hoje?", resposta)

    def testar_04_boa_tarde(self):
        saudacoes = ["boa tarde", "oi, boa tarde", "olá, boa tarde"]

        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            resposta, confianca = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, CONFIANCA_MINIMA)
            self.assertIn("Boa tarde! Aqui é o IABot. Fique à vontade para perguntar qualquer coisa sobre IA!", resposta)
    
    def testar_05_boa_noite(self):
        saudacoes = ["boa noite", "oi, boa noite", "olá, boa noite"]

        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            resposta, confianca = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, CONFIANCA_MINIMA)
            self.assertIn("Boa noite! Sou o IABot, pronto para tirar suas dúvidas sobre Inteligência Artificial. O que você quer saber?", resposta)


class TesteUtilidades(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.inicializado, self.robo = inicializar()

    def testar_00_inicializado(self):
        self.assertTrue(self.inicializado)

    def testar_01_quem_e(self):

        mensagens = [ "quem é você?",
        "o que você faz?",
        "qual o seu objetivo?",
        "para que você serve?"]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("sou o iabot, um assistente virtual criado para ajudar estudantes e curiosos com informações sobre inteligência artificial. posso responder dúvidas básicas e técnicas sobre o tema", resposta.text.lower())

    def testar_02_e_humano(self):
        mensagens = [ "você é humano?",
        "você é uma pessoa?",
        "você é real?",
        "quem está falando comigo?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)    
            self.assertIn("não sou humano. sou um robô programado para conversar sobre inteligência artificial e compartilhar conhecimento sobre o tema", resposta.text.lower())
    
    def testar_03_pode_ensinar_ia(self):
        mensagens = [ "você pode me ensinar IA?",
        "você ensina inteligência artificial?",
        "como aprender inteligência artificial com você?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)    
            self.assertIn("posso te ajudar a entender conceitos e te orientar com links e dicas de onde estudar ia. se quiser, posso indicar cursos gratuitos", resposta.text.lower())
    
    def testar_04_entende_ia(self):
        mensagens = [ "você entende de IA?",
        "você sabe sobre inteligência artificial?",
        "você é especialista em IA?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)    
            self.assertIn("fui treinado para conversar sobre diversos tópicos ligados à inteligência artificial, como machine learning, redes neurais e aplicações práticas. pode perguntar", resposta.text.lower())
    
    def testar_05_mais_informacoes(self):
        mensagens = [ "onde encontro mais informações?",
        "tem site sobre IA?",
        "onde posso pesquisar mais sobre inteligência artificial?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)    
            self.assertIn("você pode acessar sites como coursera, edx, fast.ai, deeplearning.ai ou buscar no youtube por canais especializados. posso sugerir links se quiser", resposta.text.lower())
     

class TesteInteligenciaArtificial(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.inicializado, self.robo = inicializar()

    def testar_00_inicializado(self):
        self.assertTrue(self.inicializado)

    def testar_01_o_que_e_ia(self):
        mensagens = [ "o que é inteligência artificial?",
        "defina inteligência artificial",
        "qual o conceito de IA?",
        "o que é ia?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("inteligência artificial é um ramo da ciência da computação que busca desenvolver sistemas capazes de simular a inteligência humana, como aprender, raciocinar, resolver problemas e tomar decisões", resposta.text.lower())

    def testar_02_ia_fraca_forte(self):
        mensagens = [ "qual a diferença entre IA fraca e IA forte?",
        "o que é IA fraca?",
        "o que é IA forte?",
        "diferença entre IA fraca e forte" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("a ia fraca é projetada para realizar tarefas específicas, como assistentes virtuais. já a ia forte teria a capacidade de pensar, entender e aprender de forma autônoma, como um ser humano. atualmente, só existe ia fraca", resposta.text.lower())

    def testar_03_machine_learning(self):
        mensagens = [ "o que é machine learning?",
        "defina aprendizado de máquina",
        "como funciona o machine learning?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("machine learning, ou aprendizado de máquina, é uma área da ia que ensina computadores a aprenderem com dados, identificando padrões para tomar decisões sem serem explicitamente programados para cada tarefa", resposta.text.lower())

    def testar_04_rede_neural(self):
        mensagens = [ "o que são redes neurais?",
        "defina rede neural",
        "como funciona uma rede neural?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("redes neurais são modelos computacionais inspirados no cérebro humano. elas são compostas por camadas de 'neurônios' artificiais que processam informações para realizar tarefas como reconhecimento de voz ou imagem", resposta.text.lower())

    def testar_05_linguagens_programacao(self):
        mensagens = [ "quais linguagens de programação são usadas em IA?",
        "linguagens de programação para IA",
        "qual linguagem aprender para IA?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("as linguagens mais usadas em ia são python, r, java, julia e c++. python é a mais popular por sua simplicidade e pelas diversas bibliotecas específicas para ia, como tensorflow, pytorch e scikit-learn", resposta.text.lower())

    def testar_06_industria(self):
        mensagens = [ "como a IA é usada na indústria?",
        "aplicações da IA na indústria",
        "para que serve a IA nas empresas?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("a ia é usada em diversas áreas da indústria, como automação de processos, manutenção preditiva, análise de dados, atendimento ao cliente com chatbots, sistemas de recomendação e muito mais", resposta.text.lower())

    def testar_07_substituir_humanos(self):
        mensagens = [ "a IA vai substituir os humanos?",
        "a inteligência artificial vai tirar empregos?",
        "IA vai roubar empregos?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("a ia pode substituir algumas funções repetitivas, mas também cria novas oportunidades de trabalho. o ideal é que a ia complemente o trabalho humano, tornando-o mais eficiente", resposta.text.lower())

    def testar_08_riscos(self):
        mensagens = [ "quais são os riscos da inteligência artificial?",
        "perigos da IA",
        "a IA é perigosa?" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("os principais riscos da ia incluem o uso indevido da tecnologia, viés nos algoritmos, perda de privacidade, desemprego em massa e falta de regulamentação. é importante desenvolver e usar a ia com responsabilidade", resposta.text.lower())

    def testar_09_estudar_de_graca(self):
        mensagens = [ "onde posso estudar IA gratuitamente?",
        "como aprender IA de graça?",
        "cursos gratuitos de inteligência artificial" ]

        for mensagem in mensagens:
            print(f"testando: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("você pode estudar ia gratuitamente em plataformas como coursera, edx, udacity, khan academy e youtube. algumas instituições como a usp e a fundação bradesco também oferecem cursos online", resposta.text.lower())


if __name__ == "__main__":
    unittest.main()