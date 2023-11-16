import unittest
from unittest.mock import patch
import ai

class TestAI(unittest.TestCase):
    def test_create_prompt(self):
        title = "titulo"
        content = "contenido"
        expected_prompt = "Vamos a comunicarnos en español (castellano de España). Al final de este mensaje te voy a compartir una noticia. Empleando un tono profesional e informativo quiero que redactes un resumen de esa noticia en español con un límite de 200 caracteres. Es necesario que incluyas 2 emojis que estén relacionados con la noticia. ESTÁ PROHIBIDO USAR HASHTAGS .Respóndeme en español castellano de ESPAÑA. La noticia tiene este título: titulo. Y el cuerpo de la noticia contenido. (El id de la respuesta json debe ser \"tweet\"). MUY IMPORTANTE RESPONDER EN ESPAÑOL. ESTÁ PROHIBIDO RESPONDER EN INGLÉS"
        self.assertEqual(ai.create_prompt(title, content), expected_prompt)

    @patch('requests.post')
    def test_generate_text(self, mock_post):
        prompt = "prompt"
        ai.generate_text(prompt)
        mock_post.assert_called_once_with(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": prompt,
                "format": "json",
                "stream": False
            }
        )

if __name__ == '__main__':
    unittest.main()