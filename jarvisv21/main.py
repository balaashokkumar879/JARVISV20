"""
=========================================
JARVIS V21
MAIN
=========================================
"""

from core.assistant import Assistant


def main():

    jarvis = Assistant()

    jarvis.start()


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nJarvis Stopped.")
        