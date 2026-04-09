import os

def enviar_notificacao():
    status = os.getenv("STATUS", "desconhecido")

    print("===================================")
    print("NOTIFICAÇÃO DO PIPELINE")
    print(f"Status final: {status}")
    print("Pipeline executado com sucesso!")
    print("===================================")

if __name__ == "__main__":
    enviar_notificacao()