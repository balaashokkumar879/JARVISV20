

"""
=========================================
JARVIS AI BRAIN V3
=========================================
"""

import hashlib
import ollama

from config import OLLAMA_MODEL


class Brain:

    def __init__(self):

        self.history = []

        self.cache = {}

        self.system_prompt = """
You are Jarvis.

You are an intelligent desktop AI assistant.

Rules:

1. Always reply in English unless the user requests another language.

2. Keep replies short and natural.

3. If the user asks your name:
"My name is Jarvis. Nice to meet you."

4. Help with:
- Programming
- Windows
- Python
- AI
- Coding
- Automation
- Productivity

5. Never answer in German.

6. Never answer in French.

7. Never answer in Chinese.

8. Never answer in Hindi unless requested.

9. Be friendly.

10. Think step by step before answering.
"""

    # ------------------------------------------------

    def _key(self, text):

        return hashlib.md5(text.lower().encode()).hexdigest()

    # ------------------------------------------------

    def ask(self, prompt):

        key = self._key(prompt)

        if key in self.cache:
            return self.cache[key]

        try:

            messages = [

                {
                    "role": "system",
                    "content": self.system_prompt
                }

            ]

            messages.extend(self.history)

            messages.append(

                {
                    "role": "user",
                    "content": prompt
                }

            )

            response = ollama.chat(

                model=OLLAMA_MODEL,

                messages=messages

            )

            answer = response["message"]["content"].strip()

            self.history.append(

                {

                    "role": "user",

                    "content": prompt

                }

            )

            self.history.append(

                {

                    "role": "assistant",

                    "content": answer

                }

            )

            if len(self.history) > 12:

                self.history = self.history[-12:]

            self.cache[key] = answer

            return answer

        except Exception as e:

            return f"Ollama Error: {e}"

    # ------------------------------------------------

    def clear_memory(self):

        self.history.clear()

        self.cache.clear()

    # ------------------------------------------------

    def summarize(self, text):

        return self.ask(

            f"Summarize this:\n\n{text}"

        )

    # ------------------------------------------------

    def explain(self, topic):

        return self.ask(

            f"Explain this simply:\n\n{topic}"

        )

    # ------------------------------------------------

    def write_code(self, request):

        return self.ask(

            f"Write Python code for:\n\n{request}"

        )

    # ------------------------------------------------

    def remember(self, text):

        self.history.append(

            {

                "role": "system",

                "content": text

            }

        )


brain = Brain()